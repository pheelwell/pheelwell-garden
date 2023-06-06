---
title: "Distributed Computing"
date: 2023-05-04
tags: ['cloudcomputing']
---

## Distributed Computing 

> "A distributed system is a collection of independent computers that appears to its users as a single coherent system."

 ![distributedcomputing](images/distributedcomputing.svg)

a single task is divided **among multiple computers** that communicate with **each other over a network** 

### Features 
several **autonomous** computational entities called **NODES**
each with their own local memory (no shared memory)
communicate via **message passing** 
scalable  

can have master/slave relationship
can be peer-to-peer (p2p)

### Elements of Distributed 

(a controller manages or directs the flow of data between two entities; example something that interfaces with the CPU and printer 
handles the incoming and outgoing signals of the CPU)

![distributed computing components](images/distributedcomputingcomponents.svg)
**user interface client** 
	provides info 
	helps monitor and control the system
	not on the same system as primary controller usually

**primary system controller** (??)
_Main Controller_ 
which acts as a **broker** of information between the frontends and the solvers
I/O access 
maintains information, controls the management and dispatching of requests

**secondary controller**
	*process or communications controller* 
	regulating the flow of server processing requests and managing the system’s translation load

**system datastore** 
	shared system datastore, either in one computer or distributed among many 
	each computer has local memory 
	different methods to store and retrieve information (file, block,object)

***database*** 
	relational database 
	store data in tables
	allows multiple users to access same info simultaneously 
	shared database helps synchronization

### Advantages of Distributed  
- larger storage and memory, faster compute, and higher bandwidth than a single machine
- might be more cost efficient (compared to a single big powerful computer)
- no single point of failure
- redundancy, fault tolerance 
- SCALABLE 
- **Decentralized**

### Types 
1. Mainframe
   not a distributed computer (no idea why it is here then)
2. Cluster 
   network of similar computers; homogenous; 
   eg raspberry pi cluster 
3. Grid 
   usually geographically dispersed (different location)
   heterogenous


### Applications 
- email by ARPANET was the largest and most successful implementation of distributed computing 
- Peer-2-Peer (such as Torrents, file sharing)
##
see also
[[Parallel Computing]]
[[Parallel vs Distributed Computing]]

--- 
<sub>sources: <br>
M. van Steen and A.S. Tanenbaum, Distributed Systems, 4th ed., distributed-systems.net, 2023 <br>
https://aws.amazon.com/what-is/data-store/, retrieved 2023 <br>
https://www.spiceworks.com/tech/cloud/articles/what-is-distributed-computing/#_003 (?? recheck legitimacy)
</sub>
