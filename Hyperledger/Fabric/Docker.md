### Docker

#### Structure of Docker

![](https://github.com/PDfork/blockchainPG/blob/master/Hyperledger/Fabric/Img/Docker1.jpeg)



##### •  Containers

##### •  Docker Engine

##### •  Images

##### •  Docker Client

##### •  Docker Registry



### 1.  Containers

![](https://github.com/PDfork/blockchainPG/blob/master/Hyperledger/Fabric/Img/Docker2.jpeg)

#### •  A group of processes run in isolaAon

#### •  Each container has its own set of "namespaces" (isolated view)

​    •  PID -­‐ process IDs

​    •  USER -­‐ user and group IDs

​    •  UTS -­‐ hostname and domain name

​    •  NS -­‐ mount points

​    •  NET -­‐ Network devices, stacks, ports

​    •  IPC -­‐ inter-­‐process communicaAons, message queues

​    •  cgroups -­‐ controls limits and monitoring of resources

#### •  Docker gives it its own root ﬁlesystem

### 2.Docker Images

![](https://github.com/PDfork/blockchainPG/blob/master/Hyperledger/Fabric/Img/Docker3.jpeg)

#### •  Tar ﬁle containing a container's ﬁlesystem + metadata

#### •  For sharing and redistribuAon

​      •  Global/public registry for sharing: DockerHub

#### •  Similar, in concept, to a VM image



### 3. Docker Registry

![](https://github.com/PDfork/blockchainPG/blob/master/Hyperledger/Fabric/Img/Docker4.jpeg)

#### •  CreaAng and using images is only part of the story

#### •  Sharing them is the other

