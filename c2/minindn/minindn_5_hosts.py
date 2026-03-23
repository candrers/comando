import argparse
import sys
import time
import os
import configparser
from subprocess import call, Popen, PIPE
import shutil
import glob
from traceback import format_exc
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.link import TCLink
from mininet.node import Switch, Controller, RemoteController, OVSKernelSwitch
from mininet.util import ipStr, ipParse
from mininet.log import info, debug, error


class Minindn(object):
    
    ndnSecurityDisabled = False
    workDir = '/tmp/minindn'
    resultDir = None

    def __init__(self, parser=argparse.ArgumentParser(), topo=None, topoFile=None, noTopo=False,
                 workDir=None, **mininetParams):
        
        self.parser = Minindn.parseArgs(parser)
        self.args = self.parser.parse_args()

        if not workDir:
            Minindn.workDir = os.path.abspath(self.args.workDir)
        else:
            Minindn.workDir = os.path.abspath(workDir)

        Minindn.resultDir = self.args.resultDir
        
        self.net=Mininet(link=TCLink, switch=OVSKernelSwitch, **mininetParams)

        info("*** Creating nodes\n")
        h1 = self.net.addHost( 'h1', mac='6E:93:C4:2E:5B:18')
        h100 = self.net.addHost( 'h100', mac='6E:E3:41:E2:15:02')
        h200 = self.net.addHost( 'h200', mac='CA:93:C4:1E:F6:B3')
        h300 = self.net.addHost( 'h300', mac='AA:A3:41:2E:94:AB')
        h400 = self.net.addHost( 'h400', mac='82:8D:CC:BA:5B:18')
        s1 = self.net.addSwitch( 's1', protocols='OpenFlow14' )
        s100 = self.net.addSwitch( 's100', protocols='OpenFlow14' )
        s200 = self.net.addSwitch( 's200', protocols='OpenFlow14' )
        s300 = self.net.addSwitch( 's300', protocols='OpenFlow14' )
        s400 = self.net.addSwitch( 's400', protocols='OpenFlow14' )
                        
        info("*** Associating hosts e switches\n")
        self.net.addLink( s1, h1, bw=1)
        self.net.addLink( s100, h100, bw=1)
        self.net.addLink( s200, h200, bw=1)
        self.net.addLink( s300, h300, bw=1)
        self.net.addLink( s400, h400, bw=1)
        self.net.addLink( s1, s100, bw=1)
        self.net.addLink( s1, s200, bw=1)
        self.net.addLink( s1, s300, bw=1)
        self.net.addLink( s1, s400, bw=1)
                                
        #info("*** Starting network\n")
        self.net.build()
                    
        info( '*** Adding controller\n' )
        c0 = self.net.addController('c0', controller=RemoteController, ip='172.17.0.2', port=6633)
        c0.start()
        s1.start([c0]) 
        s100.start([c0]) 
        s200.start([c0])
        s300.start([c0])
        s400.start([c0])
        
        self.initParams(self.net.hosts)

        self.cleanups = []

        if not self.net.switches:
            self.ethernetPairConnectivity()

        try:
            process = Popen(['ndnsec-get-default', '-k'], stdout=PIPE, stderr=PIPE)
            output, error = process.communicate()
            if process.returncode == 0:
                Minindn.ndnSecurityDisabled = '/dummy/KEY/-%9C%28r%B8%AA%3B%60' in output.decode("utf-8")
                info('Dummy key chain patch is installed in ndn-cxx. Security will be disabled.\n')
            else:
                debug(error)
        except:
            pass

    @staticmethod
    def parseArgs(parent):
        parser = argparse.ArgumentParser(prog='minindn', parents=[parent], add_help=False)

        # nargs='?' required here since optional argument
        parser.add_argument('topoFile', nargs='?', default='/usr/local/etc/mini-ndn/default-topology.conf',
                            help='If no template_file is given, topologies/default-topology.conf will be used.')

        parser.add_argument('--work-dir', action='store', dest='workDir', default='/tmp/minindn',
                            help='Specify the working directory; default is /tmp/minindn')

        parser.add_argument('--result-dir', action='store', dest='resultDir', default=None,
                            help='Specify the full path destination folder where experiment results will be moved')

        return parser

    def ethernetPairConnectivity(self):
        ndnNetBase = '10.0.0.0'
        interfaces = []
        for host in self.net.hosts:
            for intf in host.intfList():
                link = intf.link
                node1, node2 = link.intf1.node, link.intf2.node

                if isinstance(node1, Switch) or isinstance(node2, Switch):
                    continue

                if link.intf1 not in interfaces and link.intf2 not in interfaces:
                    interfaces.append(link.intf1)
                    interfaces.append(link.intf2)
                    node1.setIP(ipStr(ipParse(ndnNetBase) + 1) + '/30', intf=link.intf1)
                    node2.setIP(ipStr(ipParse(ndnNetBase) + 2) + '/30', intf=link.intf2)
                    ndnNetBase = ipStr(ipParse(ndnNetBase) + 4)

    @staticmethod
    def processTopo(topoFile):
        config = configparser.ConfigParser(delimiters=' ', allow_no_value=True)
        config.read(topoFile)
        topo = Topo()

        items = config.items('nodes')
        coordinates = []

        for item in items:
            name = item[0].split(':')[0]
            params = {}
            if item[1]:
                if all (x in item[1] for x in ['radius', 'angle']) and item[1] in coordinates:
                    error("FATAL: Duplicate Coordinate, \'{}\' used by multiple nodes\n" \
                        .format(item[1]))
                    sys.exit(1)
                coordinates.append(item[1])

                for param in item[1].split(' '):
                    if param == '_':
                        continue
                    params[param.split('=')[0]] = param.split('=')[1]

            topo.addHost(name, params=params)

        try:
            items = config.items('switches')
            for item in items:
                name = item[0].split(':')[0]
                topo.addSwitch(name)
        except configparser.NoSectionError:
            # Switches are optional
            pass

        items = config.items('links')
        for item in items:
            link = item[0].split(':')

            params = {}
            for param in item[1].split(' '):
                key = param.split('=')[0]
                value = param.split('=')[1]
                if key in ['bw', 'jitter', 'max_queue_size']:
                    value = int(value)
                if key == 'loss':
                    value = float(value)
                params[key] = value

            topo.addLink(link[0], link[1], **params)

        return topo

    def start(self):
        self.net.start()
        time.sleep(3)

    def stop(self):
        for cleanup in self.cleanups:
            cleanup()
        self.net.stop()

        if Minindn.resultDir is not None:
            info("Moving results to \'{}\'\n".format(Minindn.resultDir))
            os.system("mkdir -p {}".format(Minindn.resultDir))
            for file in glob.glob('{}/*'.format(Minindn.workDir)):
                shutil.move(file, Minindn.resultDir)

    @staticmethod
    def cleanUp():
        devnull = open(os.devnull, 'w')
        call('nfd-stop', stdout=devnull, stderr=devnull)
        call('mn --clean'.split(), stdout=devnull, stderr=devnull)

    @staticmethod
    def verifyDependencies():
        """Prevent MiniNDN from running without necessary dependencies"""
        dependencies = ['nfd', 'nlsr', 'infoedit', 'ndnping', 'ndnpingserver']
        devnull = open(os.devnull, 'w')
        # Checks that each program is in the system path
        for program in dependencies:
            if call(['which', program], stdout=devnull):
                error('{} is missing from the system path! Exiting...\n'.format(program))
                sys.exit(1)
        devnull.close()

    @staticmethod
    def sleep(seconds):
        # sleep is not required if ndn-cxx is using in-memory keychain
        if not Minindn.ndnSecurityDisabled:
            time.sleep(seconds)

    @staticmethod
    def handleException():
        """Utility method to perform cleanup steps and exit after catching exception"""
        Minindn.cleanUp()
        info(format_exc())
        exit(1)

    def initParams(self, nodes):
        """Initialize Mini-NDN parameters for array of nodes"""
        for host in nodes:
            if 'params' not in host.params:
                host.params['params'] = {}
            host.params['params']['workDir'] = Minindn.workDir
            homeDir = '{}/{}'.format(Minindn.workDir, host.name)
            host.params['params']['homeDir'] = homeDir
            host.cmd('mkdir -p {}'.format(homeDir))
            host.cmd('export HOME={} && cd ~'.format(homeDir))
