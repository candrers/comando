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
        h1 = self.net.addHost( 'h1' )
        h2 = self.net.addHost( 'h2' )
        h3 = self.net.addHost( 'h3' )
        h4 = self.net.addHost( 'h4' )
        h5 = self.net.addHost( 'h5' )
        h6 = self.net.addHost( 'h6' )
        h7 = self.net.addHost( 'h7' )
        h8 = self.net.addHost( 'h8' )
        h9 = self.net.addHost( 'h9' )
        h10 = self.net.addHost( 'h10' )
        h11 = self.net.addHost( 'h11' )
        h12 = self.net.addHost( 'h12' )
        h13 = self.net.addHost( 'h13' )
        h14 = self.net.addHost( 'h14' )
        h15 = self.net.addHost( 'h15' )
        h16 = self.net.addHost( 'h16' )
        h17 = self.net.addHost( 'h17' )
        h18 = self.net.addHost( 'h18' )
        h19 = self.net.addHost( 'h19' )
        h20 = self.net.addHost( 'h20' )
        h21 = self.net.addHost( 'h21' )
        h22 = self.net.addHost( 'h22' )
        h23 = self.net.addHost( 'h23' )
        h24 = self.net.addHost( 'h24' )
        h25 = self.net.addHost( 'h25' )
        h26 = self.net.addHost( 'h26' )
        h27 = self.net.addHost( 'h27' )
        h28 = self.net.addHost( 'h28' )
        h29 = self.net.addHost( 'h29' )
        h30 = self.net.addHost( 'h30' )
        h31 = self.net.addHost( 'h31' )
        h32 = self.net.addHost( 'h32' )
        h33 = self.net.addHost( 'h33' )
        h34 = self.net.addHost( 'h34' )
        h35 = self.net.addHost( 'h35' )
        h36 = self.net.addHost( 'h36' )
        h37 = self.net.addHost( 'h37' )
        h38 = self.net.addHost( 'h38' )
        h39 = self.net.addHost( 'h39' )
        h40 = self.net.addHost( 'h40' )
        h41 = self.net.addHost( 'h41' )
        h42 = self.net.addHost( 'h42' )
        h43 = self.net.addHost( 'h43' )
        h44 = self.net.addHost( 'h44' )
        h45 = self.net.addHost( 'h45' )
        h46 = self.net.addHost( 'h46' )
        h47 = self.net.addHost( 'h47' )
        h48 = self.net.addHost( 'h48' )
        h49 = self.net.addHost( 'h49' )
        h50 = self.net.addHost( 'h50' )
        h51 = self.net.addHost( 'h51' )
        h52 = self.net.addHost( 'h52' )
        h53 = self.net.addHost( 'h53' )
        h54 = self.net.addHost( 'h54' )
        h55 = self.net.addHost( 'h55' )
        h56 = self.net.addHost( 'h56' )
        h57 = self.net.addHost( 'h57' )
        h58 = self.net.addHost( 'h58' )
        h59 = self.net.addHost( 'h59' )
        h60 = self.net.addHost( 'h60' )
        h61 = self.net.addHost( 'h61' )
        h62 = self.net.addHost( 'h62' )
        h63 = self.net.addHost( 'h63' )
        h64 = self.net.addHost( 'h64' )
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
        s33 = self.net.addSwitch( 's33', protocols='OpenFlow14' )
        s34 = self.net.addSwitch( 's34', protocols='OpenFlow14' )
        s35 = self.net.addSwitch( 's35', protocols='OpenFlow14' )
        s36 = self.net.addSwitch( 's36', protocols='OpenFlow14' )
        s37 = self.net.addSwitch( 's37', protocols='OpenFlow14' )
        s38 = self.net.addSwitch( 's38', protocols='OpenFlow14' )
        s39 = self.net.addSwitch( 's39', protocols='OpenFlow14' )
        s40 = self.net.addSwitch( 's40', protocols='OpenFlow14' )
        s41 = self.net.addSwitch( 's41', protocols='OpenFlow14' )
        s42 = self.net.addSwitch( 's42', protocols='OpenFlow14' )
        s43 = self.net.addSwitch( 's43', protocols='OpenFlow14' )
        s44 = self.net.addSwitch( 's44', protocols='OpenFlow14' )
        s45 = self.net.addSwitch( 's45', protocols='OpenFlow14' )
        s46 = self.net.addSwitch( 's46', protocols='OpenFlow14' )
        s47 = self.net.addSwitch( 's47', protocols='OpenFlow14' )
        s48 = self.net.addSwitch( 's48', protocols='OpenFlow14' )
        s49 = self.net.addSwitch( 's49', protocols='OpenFlow14' )
        s50 = self.net.addSwitch( 's50', protocols='OpenFlow14' )
        s51 = self.net.addSwitch( 's51', protocols='OpenFlow14' )
        s52 = self.net.addSwitch( 's52', protocols='OpenFlow14' )
        s53 = self.net.addSwitch( 's53', protocols='OpenFlow14' )
        s54 = self.net.addSwitch( 's54', protocols='OpenFlow14' )
        s55 = self.net.addSwitch( 's55', protocols='OpenFlow14' )
        s56 = self.net.addSwitch( 's56', protocols='OpenFlow14' )
        s57 = self.net.addSwitch( 's57', protocols='OpenFlow14' )
        s58 = self.net.addSwitch( 's58', protocols='OpenFlow14' )
        s59 = self.net.addSwitch( 's59', protocols='OpenFlow14' )
        s60 = self.net.addSwitch( 's60', protocols='OpenFlow14' )
        s61 = self.net.addSwitch( 's61', protocols='OpenFlow14' )
        s62 = self.net.addSwitch( 's62', protocols='OpenFlow14' )
        s63 = self.net.addSwitch( 's63', protocols='OpenFlow14' )
        s64 = self.net.addSwitch( 's64', protocols='OpenFlow14' )
        s100 = self.net.addSwitch( 's100', protocols='OpenFlow14' )
        s200 = self.net.addSwitch( 's200', protocols='OpenFlow14' )
        s300 = self.net.addSwitch( 's300', protocols='OpenFlow14' )
        s400 = self.net.addSwitch( 's400', protocols='OpenFlow14' )
                        
        info("*** Associating hosts e switches\n")
        self.net.addLink( h1, s1, bw=1)
        self.net.addLink( h2, s2, bw=1)
        self.net.addLink( h3, s3, bw=1)
        self.net.addLink( h4, s4, bw=1)
        self.net.addLink( h5, s5, bw=1)
        self.net.addLink( h6, s6, bw=1)
        self.net.addLink( h7, s7, bw=1)
        self.net.addLink( h8, s8, bw=1)
        self.net.addLink( h9, s9, bw=1)
        self.net.addLink( h10, s10, bw=1)
        self.net.addLink( h11, s11, bw=1)
        self.net.addLink( h12, s12, bw=1)
        self.net.addLink( h13, s13, bw=1)
        self.net.addLink( h14, s14, bw=1)
        self.net.addLink( h15, s15, bw=1)
        self.net.addLink( h16, s16, bw=1)
        self.net.addLink( h17, s17, bw=1)
        self.net.addLink( h18, s18, bw=1)
        self.net.addLink( h19, s19, bw=1)
        self.net.addLink( h20, s20, bw=1)
        self.net.addLink( h21, s21, bw=1)
        self.net.addLink( h22, s22, bw=1)
        self.net.addLink( h23, s23, bw=1)
        self.net.addLink( h24, s24, bw=1)
        self.net.addLink( h25, s25, bw=1)
        self.net.addLink( h26, s26, bw=1)
        self.net.addLink( h27, s27, bw=1)
        self.net.addLink( h28, s28, bw=1)
        self.net.addLink( h29, s29, bw=1)
        self.net.addLink( h30, s30, bw=1)
        self.net.addLink( h31, s31, bw=1)
        self.net.addLink( h32, s32, bw=1)
        self.net.addLink( h33, s33, bw=1)
        self.net.addLink( h34, s34, bw=1)
        self.net.addLink( h35, s35, bw=1)
        self.net.addLink( h36, s36, bw=1)
        self.net.addLink( h37, s37, bw=1)
        self.net.addLink( h38, s38, bw=1)
        self.net.addLink( h39, s39, bw=1)
        self.net.addLink( h40, s40, bw=1)
        self.net.addLink( h41, s41, bw=1)
        self.net.addLink( h42, s42, bw=1)
        self.net.addLink( h43, s43, bw=1)
        self.net.addLink( h44, s44, bw=1)
        self.net.addLink( h45, s45, bw=1)
        self.net.addLink( h46, s46, bw=1)
        self.net.addLink( h47, s47, bw=1)
        self.net.addLink( h48, s48, bw=1)
        self.net.addLink( h49, s49, bw=1)
        self.net.addLink( h50, s50, bw=1)
        self.net.addLink( h51, s51, bw=1)
        self.net.addLink( h52, s52, bw=1)
        self.net.addLink( h53, s53, bw=1)
        self.net.addLink( h54, s54, bw=1)
        self.net.addLink( h55, s55, bw=1)
        self.net.addLink( h56, s56, bw=1)
        self.net.addLink( h57, s57, bw=1)
        self.net.addLink( h58, s58, bw=1)
        self.net.addLink( h59, s59, bw=1)
        self.net.addLink( h60, s60, bw=1)
        self.net.addLink( h61, s61, bw=1)
        self.net.addLink( h62, s62, bw=1)
        self.net.addLink( h63, s63, bw=1)
        self.net.addLink( h64, s64, bw=1)
        self.net.addLink( s1, s2, bw=1, delay='5ms')
        self.net.addLink( s1, s12, bw=1, delay='5ms')
        self.net.addLink( s1, s16, bw=1, delay='5ms')
        self.net.addLink( s1, s22, bw=1, delay='5ms')
        self.net.addLink( s2, s3, bw=1, delay='5ms')
        self.net.addLink( s2, s11, bw=1, delay='5ms')
        self.net.addLink( s2, s23, bw=1, delay='5ms')
        self.net.addLink( s3, s4, bw=1, delay='5ms')
        self.net.addLink( s3, s10, bw=1, delay='5ms')
        self.net.addLink( s3, s24, bw=1, delay='5ms')
        self.net.addLink( s4, s5, bw=1, delay='5ms')
        self.net.addLink( s4, s9, bw=1, delay='5ms')
        self.net.addLink( s4, s25, bw=1, delay='5ms')
        self.net.addLink( s5, s6, bw=1, delay='5ms')
        self.net.addLink( s5, s8, bw=1, delay='5ms')
        self.net.addLink( s5, s26, bw=1, delay='5ms')
        self.net.addLink( s6, s7, bw=1, delay='5ms')
        self.net.addLink( s6, s27, bw=1, delay='5ms')
        self.net.addLink( s7, s8, bw=1, delay='5ms')
        self.net.addLink( s8, s9, bw=1, delay='5ms')
        self.net.addLink( s9, s10, bw=1, delay='5ms')        
        self.net.addLink( s10, s11, bw=1, delay='5ms')
        self.net.addLink( s11, s12, bw=1, delay='5ms')
        self.net.addLink( s12, s13, bw=1, delay='5ms')
        self.net.addLink( s13, s16, bw=1, delay='5ms')
        self.net.addLink( s13, s14, bw=1, delay='5ms')
        self.net.addLink( s14, s15, bw=1, delay='5ms')
        self.net.addLink( s15, s16, bw=1, delay='5ms')
        self.net.addLink( s15, s18, bw=1, delay='5ms')
        self.net.addLink( s16, s17, bw=1, delay='5ms')
        self.net.addLink( s17, s20, bw=1, delay='5ms')
        self.net.addLink( s17, s18, bw=1, delay='5ms')
        self.net.addLink( s17, s22, bw=1, delay='5ms')
        self.net.addLink( s18, s19, bw=1, delay='5ms')
        self.net.addLink( s19, s42, bw=1, delay='5ms')
        self.net.addLink( s19, s20, bw=1, delay='5ms')
        self.net.addLink( s20, s21, bw=1, delay='5ms')
        self.net.addLink( s20, s41, bw=1, delay='5ms')
        self.net.addLink( s21, s22, bw=1, delay='5ms')
        self.net.addLink( s21, s40, bw=1, delay='5ms')
        self.net.addLink( s22, s23, bw=1, delay='5ms')
        self.net.addLink( s23, s24, bw=1, delay='5ms')
        self.net.addLink( s24, s25, bw=1, delay='5ms')
        self.net.addLink( s25, s26, bw=1, delay='5ms')
        self.net.addLink( s25, s30, bw=1, delay='5ms')
        self.net.addLink( s26, s27, bw=1, delay='5ms')
        self.net.addLink( s26, s29, bw=1, delay='5ms')
        self.net.addLink( s27, s28, bw=1, delay='5ms')
        self.net.addLink( s28, s33, bw=1, delay='5ms')
        self.net.addLink( s28, s29, bw=1, delay='5ms')
        self.net.addLink( s29, s30, bw=1, delay='5ms')
        self.net.addLink( s29, s32, bw=1, delay='5ms')
        self.net.addLink( s30, s31, bw=1, delay='5ms')
        self.net.addLink( s31, s32, bw=1, delay='5ms')
        self.net.addLink( s31, s36, bw=1, delay='5ms')        
        self.net.addLink( s32, s33, bw=1, delay='5ms')
        self.net.addLink( s32, s35, bw=1, delay='5ms')
        self.net.addLink( s33, s34, bw=1, delay='5ms')
        self.net.addLink( s34, s35, bw=1, delay='5ms')
        self.net.addLink( s34, s55, bw=1, delay='5ms')
        self.net.addLink( s35, s36, bw=1, delay='5ms')
        self.net.addLink( s35, s54, bw=1, delay='5ms')       
        self.net.addLink( s36, s37, bw=1, delay='5ms')
        self.net.addLink( s36, s53, bw=1, delay='5ms')
        self.net.addLink( s37, s52, bw=1, delay='5ms')
        self.net.addLink( s37, s38, bw=1, delay='5ms')
        self.net.addLink( s38, s39, bw=1, delay='5ms')
        self.net.addLink( s38, s51, bw=1, delay='5ms')
        self.net.addLink( s39, s40, bw=1, delay='5ms')
        self.net.addLink( s39, s44, bw=1, delay='5ms')
        self.net.addLink( s39, s50, bw=1, delay='5ms')
        self.net.addLink( s40, s41, bw=1, delay='5ms')
        self.net.addLink( s41, s42, bw=1, delay='5ms')
        self.net.addLink( s41, s44, bw=1, delay='5ms')
        self.net.addLink( s42, s43, bw=1, delay='5ms')
        self.net.addLink( s43, s44, bw=1, delay='5ms')
        self.net.addLink( s43, s46, bw=1, delay='5ms')
        self.net.addLink( s44, s45, bw=1, delay='5ms')
        self.net.addLink( s45, s46, bw=1, delay='5ms')
        self.net.addLink( s45, s48, bw=1, delay='5ms')
        self.net.addLink( s45, s50, bw=1, delay='5ms')
        self.net.addLink( s46, s47, bw=1, delay='5ms')
        self.net.addLink( s47, s48, bw=1, delay='5ms')
        self.net.addLink( s48, s49, bw=1, delay='5ms')
        self.net.addLink( s49, s50, bw=1, delay='5ms')
        self.net.addLink( s49, s60, bw=1, delay='5ms')
        self.net.addLink( s50, s51, bw=1, delay='5ms')
        self.net.addLink( s51, s52, bw=1, delay='5ms')
        self.net.addLink( s51, s60, bw=1, delay='5ms')
        self.net.addLink( s52, s53, bw=1, delay='5ms')
        self.net.addLink( s52, s59, bw=1, delay='5ms')
        self.net.addLink( s53, s54, bw=1, delay='5ms')
        self.net.addLink( s53, s58, bw=1, delay='5ms')
        self.net.addLink( s54, s55, bw=1, delay='5ms')
        self.net.addLink( s54, s57, bw=1, delay='5ms')
        self.net.addLink( s55, s56, bw=1, delay='5ms')
        self.net.addLink( s56, s57, bw=1, delay='5ms')
        self.net.addLink( s57, s58, bw=1, delay='5ms')
        self.net.addLink( s58, s59, bw=1, delay='5ms')
        self.net.addLink( s59, s60, bw=1, delay='5ms')
        self.net.addLink( s61, s31, bw=1, delay='5ms')
        self.net.addLink( s61, s37, bw=1, delay='5ms')
        self.net.addLink( s61, s62, bw=1, delay='5ms')
        self.net.addLink( s61, s63, bw=1, delay='5ms')
        self.net.addLink( s62, s38, bw=1, delay='5ms')
        self.net.addLink( s62, s40, bw=1, delay='5ms')
        self.net.addLink( s62, s64, bw=1, delay='5ms')
        self.net.addLink( s63, s24, bw=1, delay='5ms')
        self.net.addLink( s63, s30, bw=1, delay='5ms')
        self.net.addLink( s63, s64, bw=1, delay='5ms')
        self.net.addLink( s64, s21, bw=1, delay='5ms')
        self.net.addLink( s64, s23, bw=1, delay='5ms')     
        self.net.addLink( s100, h100, bw=1)
        self.net.addLink( s100, s10, bw=1, delay='5ms')
        self.net.addLink( s100, s11, bw=1, delay='5ms')
        self.net.addLink( s200, h200, bw=1)
        self.net.addLink( s200, s46, bw=1, delay='5ms')
        self.net.addLink( s200, s48, bw=1, delay='5ms')
        self.net.addLink( s300, h300, bw=1)
        self.net.addLink( s300, s28, bw=1, delay='5ms')
        self.net.addLink( s300, s33, bw=1, delay='5ms')
        self.net.addLink( s400, h400, bw=1)
        self.net.addLink( s400, s6, bw=1, delay='5ms')
        self.net.addLink( s400, s8, bw=1, delay='5ms')
                                
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
        s33.start([c0])
        s34.start([c0])
        s35.start([c0])
        s36.start([c0])
        s37.start([c0]) 
        s38.start([c0])
        s39.start([c0])
        s40.start([c0]) 
        s41.start([c0])
        s42.start([c0])
        s43.start([c0])
        s44.start([c0])
        s45.start([c0])
        s46.start([c0])
        s47.start([c0]) 
        s48.start([c0])
        s49.start([c0])
        s50.start([c0])
        s51.start([c0])
        s52.start([c0])
        s53.start([c0])
        s54.start([c0])
        s55.start([c0])
        s56.start([c0])
        s57.start([c0]) 
        s58.start([c0])
        s59.start([c0])
        s60.start([c0])
        s61.start([c0]) 
        s62.start([c0])
        s63.start([c0])
        s64.start([c0])
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
