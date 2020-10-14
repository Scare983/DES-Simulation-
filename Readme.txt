 Discrete Event Simulation ("DES") Executive. This is an Event oriented, and event driven simulator. Project learning goals:(1) Learn about event driven simulation, (2) learn about abstractions (i.e., the simulation executive can support a number of applications, and (3) realize this can extend to even more abstractions, such as running on different number of processors, and different computers.

For this project we view a simulation "executive" as a program that process events from an pending event queue, in time stamp order, until the event queue is empty or reaching end of simulation time. Events are scheduled by a logical process, and then inserted into the event queue. For this project time stamps will be integers, and you may use python's priority queues to 'implement your pending event list. You do not have to implement the queue from 'scratch'.

Your DES Executive should support 3 applications, of increasing complexity. A correct implementation of the more simple applications have a heavier impact of your project score.

The applications are described first, then we describe features of your kernel, and its syntax, such as events, logical processes, and messages, and their relationships.


Three different programs are included.

Program 1: 
________________________________________
python ping.py -s 1000 -f -k 1
python ping.py -s 1000 -k 10

-s indicated end of simulation time.

-f indicates that the latency between logical processes is fixed, and does not vary (boolean).

-k indicates the upper limit of latency between processes (if fixed it is what it is, if varied, the lower limit is 1).

Output:
Just a number, indicating the number of trips between ping and pong. Example: The output of 1 round trip is 2.



Program 2
________________________________________
python circling.py -p 3 -s 1000 -f -k 1
python circling.py -p 3 -s 1000 -k 10

Output:
Just a number, indicating the number of trips between between logical processes. Example: The output of 1 roundtrip is still 2 for two LPsn (2 LPs are set by the paramater -p 2). If there are 3 logical processes (-p 3) in the system then the output is 3 --> LP0->LP1->LP2->LP0 for 1 round trip.

Program 3
________________________________________
Priority Queue is implemented for this. 
 
python phold.py -p 3 -s 1000 -f  -k 1 -m 2

-s indicated end of simulation time.

-f indicates that the latency between logical processes is fixed, and does not vary (boolean).

-k indicates the upper limit of latency between processes (if fixed it is what it is, if varied, the lower limit is 1).

-m indicates the number of balls being sent to different processes



All programs are influenced and create outptut for different paramaterized executions.