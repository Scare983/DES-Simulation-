import getopt
import sys
from Simulator import Simulation
import numpy as np

argumentHash = {'SIM_TIME': None, 'isFixedLatency': False, 'maxLatency': None, 'numLP':2}
#if fixed, lower limit is equal to 1


class LPS:
    staticSim = None
    def __init__(self, thisID):
        self.thisID = thisID
        self.dstLP = None
        self.numRecieved = 0
        self.numSent = 0
        self.state = 0
    def generateInitialEvent(self):
        #state 0 means event created and put into queue
        #state 1 means event recieved, send new event, go to eventArrived
        #state 2 means finish.  End state
        #timestamp is estimated arrival
        self.state = 0
        self.setDstLP((self.thisID+1) % argumentHash['numLP'])
        #constant LP
        if argumentHash['isFixedLatency']:
            latency = argumentHash['maxLatency']
        #randomLatency
        else:
            latency = np.random.randint(low=1, high=argumentHash['maxLatency']+1)
        dataList = {'destLP': self.dstLP,  'state': self.state}
        time_stamp = LPS.staticSim.getCurrTime() + latency #depart_time
        msgNode = LPS.staticSim.createMessage(dataList, time_stamp)
        LPS.staticSim.sendMessage(msgNode)

    def generateEvent(self):
        self.state = 1
        self.setDstLP((self.thisID+1) % argumentHash['numLP'])
        #constant LP
        if argumentHash['isFixedLatency']:
            latency = argumentHash['maxLatency']
        #randomLatency
        else:
            latency = np.random.randint(low=1, high=argumentHash['maxLatency']+1)
        dataList = {'destLP': self.dstLP,  'state': self.state}
        time_stamp = LPS.staticSim.getCurrTime() + latency #depart_time
        msgNode = LPS.staticSim.createMessage(dataList, time_stamp)
        LPS.staticSim.sendMessage(msgNode)
    def finishEvent(self):
        #event finished, do nothing
        self.state = 2


    def setDstLP(self, destLP):
        self.dstLP = destLP

    @staticmethod
    def setSim(ss):
        LPS.staticSim = ss


def prossargs():
    try:
        opt, args = getopt.getopt(sys.argv[1:], "s:fk:p:")
    except getopt.GetoptError:
        usage()
        sys.exit(2)
    for opts, arg in opt:
        if opts == '-s':
            if not arg.isdigit():
                usage()
            elif int(arg) <=0:
                print('Cannot have simtime <= 0, exiting...')
            else:
                argumentHash['SIM_TIME'] = int(arg)
        elif opts == '-f':
            argumentHash['isFixedLatency'] = True
        elif opts == '-k':
            if not arg.isdigit():
                usage()
            elif int(arg) <=0:
                print('Cannot have K <= 0, exiting...')
            else:
                argumentHash['maxLatency'] = int(arg)
        elif opts == '-p':
            if not arg.isdigit():
                usage()
            elif int(arg) <= 0:
                print('Cannot have <=0 LP, exiting...')
                exit(2)
            else:
                argumentHash['numLP'] = int(arg)
    for a in argumentHash.keys():
        if argumentHash[a] is None:
            usage()


def usage():
    print('please input only int values for args')
    print(
        "python circling.py -s 'INT-TIME' [-f optional ] -k 'INT -upper Latency'")
    exit(2)


#onLp is the number of which LP currently being created.


prossargs()

listOfLp=list()

for lps in range(argumentHash['numLP']):
    listOfLp.append(LPS(lps))

s = Simulation(simTime=argumentHash['SIM_TIME'], latencyUpper=argumentHash['maxLatency'], isLatencyConstant=argumentHash['isFixedLatency'], lpList=listOfLp, numLP=argumentHash['numLP'])
LPS.setSim(s)
s.simulate()
print("Number of trips:  {}".format(s.getNumTotalTrips()))
print("Number of total round trips:  {}".format(s.getNumRoundTrips()))