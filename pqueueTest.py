from pqueue import Pqueue

pp = Pqueue()
temp = pp.newNode(4, 1) #head
temp1 = pp.newNode(5,2)
pp.pushN(temp)
pp.pushN(temp1)

temp1 = pp.newNode(6,3)
pp.pushN(temp1)

temp1 = pp.newNode(7,4)
pp.pushN(temp1)

#pp.printNodes()
while pp.isEmpty() == False:
    #print("d:{}  p:{}".format(pp.peek_data(), pp.peek_priority()))
    print(pp.pop())
