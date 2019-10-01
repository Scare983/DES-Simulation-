from pqueue import Node, Pqueue


class Simulation:

    def __init__(self, simTime, latencyUpper, lpList, isLatencyConstant=False, numLP=2):
        #msg node
        self.mySimTime  = 0
        self.maxLatency = latencyUpper
        self.sim_time = simTime
        self.isLatencyConstant = isLatencyConstant
        self.pendingQueue = Pqueue()
        self.numLP = numLP
        #data will be the LP being sent to.
        firstNode = self.pendingQueue.newNode(0,0)
        self.pendingQueue.pushN(firstNode)
        self.lpList = lpList
        self.numTrips = 0
        self.numProcessesInside = 0
    def simulate(self):
        i = 0
        first = True
        while self.mySimTime < self.sim_time and not self.pendingQueue.isEmpty():
            #always looks at head
            #because we made a dummy firstNode in queue, we remove that output.
            self.mySimTime = self.pendingQueue.peek_priority()

            if not first:
                print('LP Process: {}\t time now: {}'.format(self.pendingQueue.peek_data(), self.pendingQueue.peek_priority()))
            self.lpList[i].generateEvent()
            node = self.pendingQueue.pop()
            #handle where it is trying to send to.

            self.numTrips += 1
            i = (i+1) % self.numLP
            first = False
        self.numTrips -= 1


    def getNumTotalTrips(self):
        return self.numTrips

    def getCurrTime(self):
        return self.mySimTime

    def MySimGetMessage(self, time_stamp, dstLp):
        msgNode = self.pendingQueue.newNode(dstLp, time_stamp)
        return msgNode

    def createMessage(self, dstLp, timeStamp):
        return self.pendingQueue.newNode(dstLp,timeStamp )

    def sendMessage(self, msg):
        #start = self.pendingQueue.head
        self.pendingQueue.pushN(msg)

#add events to queue, pop them here, and do small calculations