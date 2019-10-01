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
        #firstNode = self.pendingQueue.newNode(0,0)
        #self.pendingQueue.pushN(firstNode)
        self.lpList = lpList
        self.numTrips = 0
        self.numProcessesInside = 0
        self.ballInTransit = False
        self.numRoundTrips = 0
        #first is equal to
        #create first event from


    def simulate(self):
        self.lpList[0].generateInitialEvent()
        while self.mySimTime < self.sim_time:
            #always looks at head
            #because we made a dummy firstNode in queue, we remove that output.
            self.mySimTime = self.pendingQueue.peek_priority()
            if self.pendingQueue.peek_data()['destLP'] == 0:
                self.numRoundTrips +=1
            print('LP Process: {}\t time now: {}'.format(self.pendingQueue.peek_data(), self.pendingQueue.peek_priority()))

            if self.pendingQueue.peek_data()['state'] == 0:#event created and we want to send the message
                self.handleDepart()
            if self.pendingQueue.peek_data()['state'] == 1:#event estArrive is in queue and we want to say we recieved the message
                self.handleArrive()
            node = self.pendingQueue.pop()
            #handle where it is trying to send to.
            self.numTrips += 1

    def handleDepart(self):
        if self.pendingQueue.size() <= 1 and not self.ballInTransit:
            self.lpList[self.pendingQueue.peek_data()['destLP']].generateInitialEvent()
        else:
            self.lpList[self.pendingQueue.peek_data()['destLP']].generateEvent()
        self.ballInTransit = True

    def handleArrive(self):
        self.lpList[self.pendingQueue.peek_data()['destLP']].finishEvent()

        if self.pendingQueue.size() <= 1:
            self.lpList[self.pendingQueue.peek_data()['destLP']].generateInitialEvent()

        #set state lf lp to 2, aka lp.finalState
    def getNumRoundTrips(self):
        return self.numRoundTrips

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