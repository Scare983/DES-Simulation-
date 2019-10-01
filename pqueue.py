import copy


class Node:

    def __init__(self, data, priority):
        #min bound of data is 1.
        if data < 1:
            data = 1
        self.allData = {
            'data' : data,
            'priority' : priority,
            'nextNode' : None
        }


class Pqueue:

    def __init__(self):
        self.head = None

    def newNode(self, data, priority):
        temp = Node(data, priority)
        temp.allData['nextNode'] = None
        return temp

    def peek_data(self):
        #return data at the head
        return self.head.allData['data']

    def peek_priority(self):
        #returns priority at the head
        return self.head.allData['priority']

    def pop(self):
        #return popped item
        temp = copy.copy(self.head)#shallow copy

        if self.head is None:
            return None
        else:
            self.head = self.head.allData['nextNode']
        #del temp
        return temp

    def push(self,  data, priority):

        startNode = copy.copy(self.head) # same as =
        nodeToPush = self.newNode(data, priority)
        if self.isEmpty():
            self.head = nodeToPush
        else:
            if self.head.allData['priority'] > priority:
                nodeToPush.allData['nextNode'] = self.head
                self.head = nodeToPush
            else:

                while startNode.allData['nextNode'] is not None and startNode.allData['nextNode'].allData['priority'] < priority:
                    startNode = startNode.allData['nextNode']
                nodeToPush.allData['nextNode'] = startNode.allData['nextNode']
                startNode.allData['nextNode'] = nodeToPush

    #push Node
    def pushN(self,  nodeToPush):
        #no return.  Void.
        #edge case
        #print(nodeToPush.allData['data'])
        startNode = copy.copy(self.head)
        if self.isEmpty():
            self.head = nodeToPush
        else:
            if self.head.allData['priority'] > nodeToPush.allData['priority']:
                nodeToPush.allData['nextNode'] = copy.copy(self.head)
                self.head = nodeToPush

            else:
                while startNode.allData['nextNode'] is not None and startNode.allData['nextNode'].allData['priority'] < nodeToPush.allData['priority']:
                    #print(startNode.allData['nextNode'].allData['priority'])
                    startNode = startNode.allData['nextNode']
                nodeToPush.allData['nextNode'] = startNode.allData['nextNode']
                startNode.allData['nextNode'] = nodeToPush

            #print(startNode.nextNode.data)
    def isEmpty(self):
        if self.head is None:
            return True
        else:
            return False
        #place item into priority q

    def printNodes(self):
        temp = self.head
        while(temp is not None):
            print (temp.allData['priority'])
            temp = temp.allData['nextNode']