---
title: "Dynamic Stability"
tags: ['cloudcomputing']
date: 2023-03-21
---

## Components of Dynamic Stability 
### Load Balancer
distribute incoming traffic
![[load balancer]]
### Autoscaling
### Elastic Storage
### Containerization
modular 
### Cloud Provider Service

## Types 
- Dynamic Horizontal
- Dynamic Vertical 
- Dynamic Relocation

```mermaid
flowchart
A --> B(Horizontal)
A --> C(Vertical) 
A --> D(Relocation) 
A(Dynamic Scalability)
B---Z(add resources)
C---Y(increase capacity of a resource)
D---X(move to host w more resources)
```

## Benefits
ability to handle sudden spikes in traffic or demand [^1]


