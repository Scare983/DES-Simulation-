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

    def generateEvent(self):
        self.setDstLP(self.thisID+1 % argumentHash['numLP'])
        #constant LP
        if argumentHash['isFixedLatency']:
            latency = argumentHash['maxLatency']
        #randomLatency
        else:
            latency = np.random.randint(low=1, high=argumentHash['maxLatency']+1)

        time_stamp = LPS.staticSim.getCurrTime() + latency #how long it would take to get to next LP
        msgNode = LPS.staticSim.createMessage(self.dstLP, time_stamp)
        LPS.staticSim.sendMessage(msgNode)

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
            else:
                argumentHash['SIM_TIME'] = int(arg)
        elif opts == '-f':
            argumentHash['isFixedLatency'] = True
        elif opts == '-k':
            if not arg.isdigit():
                usage()
            argumentHash['maxLatency'] = int(arg)
        elif opts == '-p':
            if not arg.isdigit():
                usage()
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
print("Number of trip:  {}".format(s.getNumTotalTrips()))