### Docker

#### Structure of Docker

![](https://ws1.sinaimg.cn/large/006tNc79gy1fmh0lbhpw1j30ro0kq415.jpg)



##### •  Containers

##### •  Docker Engine

##### •  Images

##### •  Docker Client

##### •  Docker Registry



### 1.  Containers

![](https://ws3.sinaimg.cn/large/006tNc79gy1fmh0vhi5lmj31dk0nytcq.jpg)

####•  A group of processes run in isolaAon

####•  Each container has its own set of "namespaces" (isolated view)

​    •  PID -­‐ process IDs

​    •  USER -­‐ user and group IDs

​    •  UTS -­‐ hostname and domain name

​    •  NS -­‐ mount points

​    •  NET -­‐ Network devices, stacks, ports

​    •  IPC -­‐ inter-­‐process communicaAons, message queues

​    •  cgroups -­‐ controls limits and monitoring of resources

#### •  Docker gives it its own root ﬁlesystem

### 2.Docker Images

![](https://ws2.sinaimg.cn/large/006tNc79gy1fmh109i0r5j30f00geq4m.jpg)

#### •  Tar ﬁle containing a container's ﬁlesystem + metadata

#### •  For sharing and redistribuAon

​      •  Global/public registry for sharing: DockerHub

#### •  Similar, in concept, to a VM image



### 3. Docker Registry

![](https://ws1.sinaimg.cn/large/006tNc79gy1fmh14rpsmnj30oe0hytbb.jpg)

#### •  CreaAng and using images is only part of the story

####•  Sharing them is the other

