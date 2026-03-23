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
from mininet.node import Switch, Host, Controller, RemoteController, OVSKernelSwitch
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
        h1 = self.net.addHost( 'h1', mac='26:4F:C9:04:92:44' )
        h2 = self.net.addHost( 'h2', mac='0E:0D:74:EF:56:17' )
        h3 = self.net.addHost( 'h3', mac='6A:77:01:02:B2:FE' )
        h4 = self.net.addHost( 'h4', mac='A2:5C:8F:FC:65:6E' )
        h5 = self.net.addHost( 'h5', mac='22:5B:30:2C:63:46' )
        h6 = self.net.addHost( 'h6', mac='B6:88:33:9D:8C:18' )
        h7 = self.net.addHost( 'h7', mac='12:88:5F:45:9B:05' )
        h8 = self.net.addHost( 'h8', mac='02:8C:05:9E:CF:A7' )
        h9 = self.net.addHost( 'h9', mac='B6:85:9F:91:EF:42' )
        h10 = self.net.addHost( 'h10', mac='42:F9:02:E8:CB:D1' )
        h11 = self.net.addHost( 'h11', mac='EA:70:E9:05:20:9C' )
        h12 = self.net.addHost( 'h12', mac='CA:E1:73:DB:32:33' )
        h13 = self.net.addHost( 'h13', mac='6E:E2:00:DA:E3:69' )
        h14 = self.net.addHost( 'h14', mac='A6:AE:59:8C:DC:79' )
        h15 = self.net.addHost( 'h15', mac='FE:98:3F:F8:1E:79' )
        h16 = self.net.addHost( 'h16', mac='9A:82:53:0E:43:BE' )
        h17 = self.net.addHost( 'h17', mac='1E:8F:48:3A:AE:26' )
        h18 = self.net.addHost( 'h18', mac='26:BD:6D:03:21:F8' )
        h19 = self.net.addHost( 'h19', mac='3A:60:37:44:9E:B7' )
        h20 = self.net.addHost( 'h20', mac='C2:5D:45:EF:BD:3C' )
        h21 = self.net.addHost( 'h21', mac='AE:1D:A7:18:5A:42' )
        h22 = self.net.addHost( 'h22', mac='76:21:06:7B:D9:5A' )
        h23 = self.net.addHost( 'h23', mac='12:72:13:76:D0:4A' )
        h24 = self.net.addHost( 'h24', mac='AA:CE:1D:05:63:FB' )
        h25 = self.net.addHost( 'h25', mac='C2:81:68:A6:B4:75' )
        h26 = self.net.addHost( 'h26', mac='7E:5E:00:36:F4:B1' )
        h27 = self.net.addHost( 'h27', mac='5E:EA:1F:E7:0B:FD' )
        h28 = self.net.addHost( 'h28', mac='3E:45:FB:07:5E:87' )
        h29 = self.net.addHost( 'h29', mac='66:85:06:F1:92:74' )
        h30 = self.net.addHost( 'h30', mac='9E:F0:80:72:DE:C4' )
        h31 = self.net.addHost( 'h31', mac='26:5C:3B:E2:76:CF' )
        h32 = self.net.addHost( 'h32', mac='52:2A:4E:0B:B9:4A' )
        h100 = self.net.addHost( 'h100', mac='6E:E3:41:E2:15:02')
        h200 = self.net.addHost( 'h200', mac='CA:93:C4:1E:F6:B3')
        h300 = self.net.addHost( 'h300', mac='AA:A3:41:2E:94:AB')
        h400 = self.net.addHost( 'h400', mac='82:8D:CC:BA:5B:18')
        s1 = self.net.addSwitch( 's1', protocols='OpenFlow14' )
        s2 = self.net.addSwitch( 's2', protocols='OpenFlow14' )
        s3 = self.net.addSwitch( 's3', protocols='OpenFlow14' )
        s4 = self.net.addSwitch( 's4', protocols='OpenFlow14' )
        s5 = self.net.addSwitch( 's5', protocols='OpenFlow14' )
        s6 = self.net.addSwitch( 's6', protocols='OpenFlow14' )
        s7 = self.net.addSwitch( 's7', protocols='OpenFlow14' )
        s8 = self.net.addSwitch( 's8', protocols='OpenFlow14' )
        s9 = self.net.addSwitch( 's9', protocols='OpenFlow14' )
        s10 = self.net.addSwitch( 's10', protocols='OpenFlow14' )
        s11 = self.net.addSwitch( 's11', protocols='OpenFlow14' )
        s12 = self.net.addSwitch( 's12', protocols='OpenFlow14' )
        s13 = self.net.addSwitch( 's13', protocols='OpenFlow14' )
        s14 = self.net.addSwitch( 's14', protocols='OpenFlow14' )
        s15 = self.net.addSwitch( 's15', protocols='OpenFlow14' )
        s16 = self.net.addSwitch( 's16', protocols='OpenFlow14' )
        s17 = self.net.addSwitch( 's17', protocols='OpenFlow14' )
        s18 = self.net.addSwitch( 's18', protocols='OpenFlow14' )
        s19 = self.net.addSwitch( 's19', protocols='OpenFlow14' )
        s20 = self.net.addSwitch( 's20', protocols='OpenFlow14' )
        s21 = self.net.addSwitch( 's21', protocols='OpenFlow14' )
        s22 = self.net.addSwitch( 's22', protocols='OpenFlow14' )
        s23 = self.net.addSwitch( 's23', protocols='OpenFlow14' )
        s24 = self.net.addSwitch( 's24', protocols='OpenFlow14' )
        s25 = self.net.addSwitch( 's25', protocols='OpenFlow14' )
        s26 = self.net.addSwitch( 's26', protocols='OpenFlow14')
        s27 = self.net.addSwitch( 's27', protocols='OpenFlow14')
        s28 = self.net.addSwitch( 's28', protocols='OpenFlow14' )
        s29 = self.net.addSwitch( 's29', protocols='OpenFlow14' )
        s30 = self.net.addSwitch( 's30', protocols='OpenFlow14' )
        s31 = self.net.addSwitch( 's31', protocols='OpenFlow14' )
        s32 = self.net.addSwitch( 's32', protocols='OpenFlow14' )
        s100 = self.net.addSwitch( 's100', protocols='OpenFlow14' )
        s200 = self.net.addSwitch( 's200', protocols='OpenFlow14' )
        s300 = self.net.addSwitch( 's300', protocols='OpenFlow14' )
        s400 = self.net.addSwitch( 's400', protocols='OpenFlow14' )
        
        for h in self.net.hosts:
          print ("disable ipv6 host: "+h.name)
          h.cmd("sysctl -w net.ipv6.conf.all.disable_ipv6=1")
          h.cmd("sysctl -w net.ipv6.conf.default.disable_ipv6=1")
          h.cmd("sysctl -w net.ipv6.conf.lo.disable_ipv6=1")

        for sw in self.net.switches:
          print ("disable ipv6 switch: "+sw.name)
          sw.cmd("sysctl -w net.ipv6.conf.all.disable_ipv6=1")
          sw.cmd("sysctl -w net.ipv6.conf.default.disable_ipv6=1")
          sw.cmd("sysctl -w net.ipv6.conf.lo.disable_ipv6=1")          

                        
        info("*** Associating hosts e switches\n")
        self.net.addLink( h1, s1, bw=0.5)
        self.net.addLink( h2, s2, bw=0.5)
        self.net.addLink( h3, s3, bw=0.5)
        self.net.addLink( h4, s4, bw=0.5)
        self.net.addLink( h5, s5, bw=0.5)
        self.net.addLink( h6, s6, bw=0.5)
        self.net.addLink( h7, s7, bw=0.5)
        self.net.addLink( h8, s8, bw=0.5)
        self.net.addLink( h9, s9, bw=0.5)
        self.net.addLink( h10, s10, bw=0.5)
        self.net.addLink( h11, s11, bw=0.5)
        self.net.addLink( h12, s12, bw=0.5)
        self.net.addLink( h13, s13, bw=0.5)
        self.net.addLink( h14, s14, bw=0.5)
        self.net.addLink( h15, s15, bw=0.5)
        self.net.addLink( h16, s16, bw=0.5)
        self.net.addLink( h17, s17, bw=0.5)
        self.net.addLink( h18, s18, bw=0.5)
        self.net.addLink( h19, s19, bw=0.5)
        self.net.addLink( h20, s20, bw=0.5)
        self.net.addLink( h21, s21, bw=0.5)
        self.net.addLink( h22, s22, bw=0.5)
        self.net.addLink( h23, s23, bw=0.5)
        self.net.addLink( h24, s24, bw=0.5)
        self.net.addLink( h25, s25, bw=0.5)
        self.net.addLink( h26, s26, bw=0.5)
        self.net.addLink( h27, s27, bw=0.5)
        self.net.addLink( h28, s28, bw=0.5)
        self.net.addLink( h29, s29, bw=0.5)
        self.net.addLink( h30, s30, bw=0.5)
        self.net.addLink( h31, s31, bw=0.5)
        self.net.addLink( h32, s32, bw=0.5)
        self.net.addLink( s1, s2, bw=0.5, delay='10ms')
        self.net.addLink( s1, s12, bw=0.5, delay='10ms')
        self.net.addLink( s2, s3, bw=0.5, delay='10ms')
        self.net.addLink( s2, s11, bw=0.5, delay='10ms')
        self.net.addLink( s3, s4, bw=0.5, delay='10ms')
        self.net.addLink( s3, s10, bw=0.5, delay='10ms')
        self.net.addLink( s4, s5, bw=0.5, delay='10ms')
        self.net.addLink( s5, s6, bw=0.5, delay='10ms')
        self.net.addLink( s5, s8, bw=0.5, delay='10ms')
        self.net.addLink( s5, s10, bw=0.5, delay='10ms')
        self.net.addLink( s6, s7, bw=0.5, delay='10ms')
        self.net.addLink( s7, s8, bw=0.5, delay='10ms')
        self.net.addLink( s7, s20, bw=0.5, delay='10ms')
        self.net.addLink( s8, s9, bw=0.5, delay='10ms')
        self.net.addLink( s8, s19, bw=0.5, delay='10ms')
        self.net.addLink( s9, s10, bw=0.5, delay='10ms')
        self.net.addLink( s9, s18, bw=0.5, delay='10ms')
        self.net.addLink( s9, s16, bw=0.5, delay='10ms')
        self.net.addLink( s10, s11, bw=0.5, delay='10ms')
        self.net.addLink( s11, s12, bw=0.5, delay='10ms')
        self.net.addLink( s11, s16, bw=0.5, delay='10ms')        
        self.net.addLink( s10, s11, bw=0.5, delay='10ms')
        self.net.addLink( s12, s13, bw=0.5, delay='10ms')
        self.net.addLink( s12, s15, bw=0.5, delay='10ms')
        self.net.addLink( s13, s14, bw=0.5, delay='10ms')
        self.net.addLink( s14, s15, bw=0.5, delay='10ms')
        self.net.addLink( s14, s31, bw=0.5, delay='10ms')
        self.net.addLink( s15, s16, bw=0.5, delay='10ms')
        self.net.addLink( s15, s32, bw=0.5, delay='10ms')
        self.net.addLink( s16, s17, bw=0.5, delay='10ms')
        self.net.addLink( s17, s18, bw=0.5, delay='10ms')
        self.net.addLink( s17, s26, bw=0.5, delay='10ms')
        self.net.addLink( s17, s32, bw=0.5, delay='10ms')
        self.net.addLink( s18, s19, bw=0.5, delay='10ms')
        self.net.addLink( s18, s25, bw=0.5, delay='10ms')
        self.net.addLink( s19, s20, bw=0.5, delay='10ms')
        self.net.addLink( s19, s22, bw=0.5, delay='10ms')
        self.net.addLink( s20, s21, bw=0.5, delay='10ms')
        self.net.addLink( s21, s22, bw=0.5, delay='10ms')
        self.net.addLink( s22, s23, bw=0.5, delay='10ms')
        self.net.addLink( s22, s25, bw=0.5, delay='10ms')
        self.net.addLink( s23, s24, bw=0.5, delay='10ms')
        self.net.addLink( s24, s25, bw=0.5, delay='10ms')
        self.net.addLink( s24, s27, bw=0.5, delay='10ms')
        self.net.addLink( s25, s26, bw=0.5, delay='10ms')
        self.net.addLink( s26, s27, bw=0.5, delay='10ms')
        self.net.addLink( s26, s29, bw=0.5, delay='10ms')
        self.net.addLink( s27, s28, bw=0.5, delay='10ms')
        self.net.addLink( s28, s29, bw=0.5, delay='10ms')
        self.net.addLink( s29, s30, bw=0.5, delay='10ms')
        self.net.addLink( s29, s32, bw=0.5, delay='10ms')
        self.net.addLink( s30, s31, bw=0.5, delay='10ms')
        self.net.addLink( s31, s32, bw=0.5, delay='10ms')
        self.net.addLink( s100, h100, bw=0.5)
        self.net.addLink( s100, s1, bw=0.5, delay='10ms')
        self.net.addLink( s200, h200, bw=0.5)
        self.net.addLink( s200, s24, bw=0.5, delay='10ms')
        self.net.addLink( s300, h300, bw=0.5)
        self.net.addLink( s400, s21, bw=0.5, delay='10ms')
        self.net.addLink( s400, h400, bw=0.5)
        self.net.addLink( s300, s6, bw=0.5, delay='10ms')
                                
        #info("*** Starting network\n")
        self.net.build()
                    
        info( '*** Adding controller\n' )
        c0 = self.net.addController('c0', controller=RemoteController, ip='172.17.0.2', port=6653)
        c0.start()
        s1.start([c0])
        s2.start([c0])
        s3.start([c0])
        s4.start([c0])
        s5.start([c0])
        s6.start([c0])
        s7.start([c0]) 
        s8.start([c0])
        s9.start([c0])
        s10.start([c0])
        s11.start([c0])
        s12.start([c0])
        s13.start([c0])
        s14.start([c0])
        s15.start([c0])
        s16.start([c0])
        s17.start([c0]) 
        s18.start([c0])
        s19.start([c0])
        s20.start([c0])
        s21.start([c0])
        s22.start([c0])
        s23.start([c0])
        s24.start([c0])
        s25.start([c0])
        s26.start([c0])
        s27.start([c0]) 
        s28.start([c0])
        s29.start([c0])
        s30.start([c0])
        s31.start([c0])
        s32.start([c0])
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
        '''cmd = "/sbin/ethtool --offload %s %s off" \
                  % (host.defaultIntf(), off)
        host.cmd(cmd)''' 
            
        for host in nodes:
            if 'params' not in host.params:
                host.params['params'] = {}
            host.params['params']['workDir'] = Minindn.workDir
            homeDir = '{}/{}'.format(Minindn.workDir, host.name)
            host.params['params']['homeDir'] = homeDir
            host.cmd('mkdir -p {}'.format(homeDir))
            host.cmd('export HOME={} && cd ~'.format(homeDir))
                      
