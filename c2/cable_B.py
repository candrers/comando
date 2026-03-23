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
    receiveFile(con100, "/drone1-file{}".format(1), "drone1-file-received.{}".format(1),1)
    
    sleep(130)  
    
    '''makeTerm(ndn.net['h300'], title='servidor', cmd="bash -c 'iperf3 -s>server300_B.txt;'")
    
    makeTerm(ndn.net['h200'], title='tarefa3', cmd="bash -c 'iperf3 -c h300 -t 60s -u 5ms> iperf300_B.txt;'")'''    
    
    sendFile(prod200,"/drone1-file{}".format(1), drone2File)
    receiveFile(con300, "/drone1-file{}".format(1), "drone1-file-received.{}".format(1),1)
    
      
    MiniNDNCLI(ndn.net)
    ndn.stop()
