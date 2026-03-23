from time import sleep
import asyncio
import subprocess
from mininet.term import makeTerm
from mininet.log import setLogLevel, info
from minindn.minindn import Minindn
from minindn.util import MiniNDNCLI
from time import sleep
from minindn.apps.app_manager import AppManager
from minindn.apps.nfd import Nfd
from minindn.apps.nlsr import Nlsr
from minindn.helpers.nfdc import Nfdc

def sendFile(node, prefix, file):
    info ("File published:", file)
    cmd = 'ndnputchunks {}/{} < {} > putchunks.log 2>&1 &'.format(prefix, "fname", file)
    node.cmd(cmd)

def receiveFile(node, prefix, filename,number):
    info ("Fething file: ", filename)
    cmd = 'ndncatchunks -r 20 -l 30000 {}/{} > {} 2> catchunks{}.log &'.format(prefix, "fname", filename,number)
    node.cmd(cmd)

if __name__ == '__main__':
    setLogLevel('info')    
    Minindn.cleanUp()
    Minindn.verifyDependencies()  
    ndn = Minindn()
    ndn.start()
    con1 = ndn.net["h1"]
    con2 = ndn.net["h2"]
    con3 = ndn.net["h3"]
    con5 = ndn.net["h5"]
    con6 = ndn.net["h6"]
    con7 = ndn.net["h7"]
    con9 = ndn.net["h9"]
    con10 = ndn.net["h10"]
    con18 = ndn.net["h18"]
    con24 = ndn.net["h24"]
    con25 = ndn.net["h25"]
    con100 = ndn.net["h100"]
    prod200 = ndn.net["h200"]
    con300 = ndn.net["h300"]
    con400 = ndn.net["h400"]
    
    
    con400.cmd('fping -c1 -t500 10.0.0.1 10.0.0.2 10.0.0.3 10.0.0.4 10.0.0.5 10.0.0.6 10.0.0.7 10.0.0.8 10.0.0.9 10.0.0.10 10.0.0.11 10.0.0.12 10.0.0.13 10.0.0.14 10.0.0.15 10.0.0.16 10.0.0.17 10.0.0.18 10.0.0.19 10.0.0.4 10.0.0.20 10.0.0.21 10.0.0.22 10.0.0.23 10.0.0.24 10.0.0.25 10.0.0.26 10.0.0.27 10.0.0.28 10.0.0.29 10.0.0.30 10.0.0.31 10.0.0.32 10.0.0.33 10.0.0.34 10.0.0.35 10.0.0.36')	
    drone2File= "/home/carlos/c2/custom/img/Task2.png"
    #drone1File= "/home/carlos/c2/custom/img/Task1.png"
       
    con400.cmd("xterm")
    
    nfds = AppManager(ndn, ndn.net.hosts, Nfd, logLevel='DEBUG')
    #nfds = AppManager(ndn, ndn.net.hosts, Nfd)
    Nfdc.createFace(con1, con100.IP(),isPermanent=True)   
    Nfdc.createFace(con1, con2.IP(),isPermanent=True)   
    Nfdc.createFace(con2, con3.IP(),isPermanent=True)   
    Nfdc.createFace(con3, con10.IP(),isPermanent=True)
    Nfdc.createFace(con5, con6.IP(),isPermanent=True)   
    Nfdc.createFace(con5, con10.IP(),isPermanent=True)
    Nfdc.createFace(con6, con7.IP(),isPermanent=True)         
    Nfdc.createFace(con7, con300.IP(),isPermanent=True)   
    Nfdc.createFace(con9, con10.IP(),isPermanent=True)
    Nfdc.createFace(con9, con18.IP(),isPermanent=True)    
    Nfdc.createFace(con18, con25.IP(),isPermanent=True)
    Nfdc.createFace(con24, con25.IP(),isPermanent=True)
    Nfdc.createFace(con24, prod200.IP(),isPermanent=True)  
    
    Nfdc.registerRoute(con100, "/drone1-file{}".format(1), con1.IP())
    Nfdc.registerRoute(con1, "/drone1-file{}".format(1), con2.IP())
    Nfdc.registerRoute(con2, "/drone1-file{}".format(1), con3.IP())
    Nfdc.registerRoute(con3, "/drone1-file{}".format(1), con10.IP())    
    Nfdc.registerRoute(con10, "/drone1-file{}".format(1), con9.IP())
    Nfdc.registerRoute(con9, "/drone1-file{}".format(1), con18.IP())
    Nfdc.registerRoute(con18, "/drone1-file{}".format(1), con25.IP())
    Nfdc.registerRoute(con25, "/drone1-file{}".format(1), con24.IP())
    Nfdc.registerRoute(con24, "/drone1-file{}".format(1), prod200.IP())
    Nfdc.registerRoute(con300, "/drone1-file{}".format(1), con7.IP())    
    Nfdc.registerRoute(con7, "/drone1-file{}".format(1), con6.IP())
    Nfdc.registerRoute(con6, "/drone1-file{}".format(1), con5.IP())
    Nfdc.registerRoute(con5, "/drone1-file{}".format(1), con10.IP())    
    
    makeTerm(ndn.net['h4'], title='tarefa1', cmd="bash -c 'ping -f -w 350 h3;'")
    makeTerm(ndn.net['h4'], title='tarefa1', cmd="bash -c 'ping -f -w 350 h12;'")
    makeTerm(ndn.net['h4'], title='tarefa1', cmd="bash -c 'ping -f -w 350 h20;'") 
    makeTerm(ndn.net['h4'], title='tarefa1', cmd="bash -c 'ping -f -w 350 h25;'")
    makeTerm(ndn.net['h4'], title='tarefa1', cmd="bash -c 'ping -f -w 350 h30;'")
    makeTerm(ndn.net['h4'], title='tarefa1', cmd="bash -c 'ping -f -w 350 h200;'") 
    
    makeTerm(ndn.net['h11'], title='tarefa1', cmd="bash -c 'ping -f -w 350 h1;'")
    makeTerm(ndn.net['h11'], title='tarefa1', cmd="bash -c 'ping -f -w 350 h6;'")
    makeTerm(ndn.net['h11'], title='tarefa1', cmd="bash -c 'ping -f -w 350 h10;'")
    makeTerm(ndn.net['h11'], title='tarefa1', cmd="bash -c 'ping -f -w 350 h22;'") 
    makeTerm(ndn.net['h11'], title='tarefa1', cmd="bash -c 'ping -f -w 350 h400;'") 
    
    makeTerm(ndn.net['h13'], title='tarefa1', cmd="bash -c 'ping -f -w 350 h5;'")   
    makeTerm(ndn.net['h13'], title='tarefa1', cmd="bash -c 'ping -f -w 350 h9;'")
    makeTerm(ndn.net['h13'], title='tarefa1', cmd="bash -c 'ping -f -w 350 h14;'")
    makeTerm(ndn.net['h13'], title='tarefa1', cmd="bash -c 'ping -f -w 350 h18;'")
    makeTerm(ndn.net['h13'], title='tarefa1', cmd="bash -c 'ping -f -w 350 h26;'")
    makeTerm(ndn.net['h13'], title='tarefa1', cmd="bash -c 'ping -f -w 350 h28;'")
    
    makeTerm(ndn.net['h21'], title='tarefa1', cmd="bash -c 'ping -f -w 350 h1;'")
    makeTerm(ndn.net['h21'], title='tarefa1', cmd="bash -c 'ping -f -w 350 h6;'")
    makeTerm(ndn.net['h21'], title='tarefa1', cmd="bash -c 'ping -f -w 350 h10;'")
    makeTerm(ndn.net['h21'], title='tarefa1', cmd="bash -c 'ping -f -w 350 h12;'")
    makeTerm(ndn.net['h21'], title='tarefa1', cmd="bash -c 'ping -f -w 350 h16;'")
    makeTerm(ndn.net['h21'], title='tarefa1', cmd="bash -c 'ping -f -w 350 h32;'")
     
    makeTerm(ndn.net['h23'], title='tarefa1', cmd="bash -c 'ping -f -w 350 h2;'")
    makeTerm(ndn.net['h23'], title='tarefa1', cmd="bash -c 'ping -f -w 350 h16;'")
    makeTerm(ndn.net['h23'], title='tarefa1', cmd="bash -c 'ping -f -w 350 h26'")
    makeTerm(ndn.net['h23'], title='tarefa1', cmd="bash -c 'ping -f -w 350 h32;'")
    makeTerm(ndn.net['h23'], title='tarefa1', cmd="bash -c 'ping -f -w 350 h200;'")
    makeTerm(ndn.net['h23'], title='tarefa1', cmd="bash -c 'ping -f -w 350 h300;'")
    
    makeTerm(ndn.net['h27'], title='tarefa1', cmd="bash -c 'ping -f -w 350 h2;'") 
    makeTerm(ndn.net['h27'], title='tarefa1', cmd="bash -c 'ping -f -w 350 h5")        
    makeTerm(ndn.net['h27'], title='tarefa1', cmd="bash -c 'ping -f -w 350 h8;'")         
    makeTerm(ndn.net['h27'], title='tarefa1', cmd="bash -c 'ping -f -w 350 h15;'")
    makeTerm(ndn.net['h27'], title='tarefa1', cmd="bash -c 'ping -f -w 350 h30;'")
    makeTerm(ndn.net['h27'], title='tarefa1', cmd="bash -c 'ping -f -w 350 h100;'")   
    
    makeTerm(ndn.net['h29'], title='tarefa1', cmd="bash -c 'ping -f -w 350 h3;'")
    makeTerm(ndn.net['h29'], title='tarefa1', cmd="bash -c 'ping -f -w 350 h8;'")         
    makeTerm(ndn.net['h29'], title='tarefa1', cmd="bash -c 'ping -f -w 350 h15;'")         
    makeTerm(ndn.net['h29'], title='tarefa1', cmd="bash -c 'ping -f -w 350 h19;'")
    makeTerm(ndn.net['h29'], title='tarefa1', cmd="bash -c 'ping -f -w 350 h25;'")
    makeTerm(ndn.net['h29'], title='tarefa1', cmd="bash -c 'ping -f -w 350 h300;'")            
    
    makeTerm(ndn.net['h31'], title='tarefa1', cmd="bash -c 'ping -f -w 350 h9;'")
    makeTerm(ndn.net['h31'], title='tarefa1', cmd="bash -c 'ping -f -w 350 h18;'")
    makeTerm(ndn.net['h31'], title='tarefa1', cmd="bash -c 'ping -f -w 350 h22;'")         
    makeTerm(ndn.net['h31'], title='tarefa1', cmd="bash -c 'ping -f -w 350 h24;'")
    makeTerm(ndn.net['h31'], title='tarefa1', cmd="bash -c 'ping -f -w 350 h100;'")
    makeTerm(ndn.net['h31'], title='tarefa1', cmd="bash -c 'ping -f -w 350 h400;'")
    
       
    sendFile(prod200,"/drone1-file{}".format(1), drone2File)
    receiveFile(con300, "/drone1-file{}".format(1), "drone1-file-received.{}".format(1),1)
    
    #sleep(130)  
    
    '''makeTerm(ndn.net['h100'], title='servidor', cmd="bash -c 'iperf3 -s>server100_A.txt;'")
    
    makeTerm(ndn.net['h200'], title='tarefa3', cmd="bash -c 'iperf3 -c h100 -t 60s -u 5ms> iperf100_A.txt;'")'''    
    
    sendFile(prod200,"/drone1-file{}".format(1), drone2File)
    receiveFile(con100, "/drone1-file{}".format(1), "drone1-file-received.{}".format(1),1)
    
      
    MiniNDNCLI(ndn.net)
    ndn.stop()
