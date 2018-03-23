### Structure of Fabric (Roughly)

#### Fabric 0.6

Before we get known of Fabric 1.0, we need to understand Fabric 0.6 which is a stable version.

![Fabric main parts](https://ws2.sinaimg.cn/large/006tKfTcgy1fmd8vtbae0j30ki0cawet.jpg)



When you run Fabric 0.6, the architecture is :

![Favric 0.6 architecture](https://ws4.sinaimg.cn/large/006tNc79gy1fmdez0utojj30db0ccdg0.jpg)

The architecture is `application`-`membership`-`peer`, the triangle relationships. The main affairs focus on Peers. 



#### Fabric 1.0

But here comes our problem: Peer affords too many functions, so we improve the architecture into Fabric 1.0 as follows:

![Fabric 1.0 architecture](https://ws2.sinaimg.cn/large/006tNc79gy1fmdf5lf5j0j30n30aiwey.jpg)

Consensus has been taken out of Peers, and been set into an isolated node `orderer`. Based on the new architecture, Fabric 1.0 also has channels. 

##### Main charaters

Fabric 1.0 supports multi-chaincode and multi-channels.

A `peer` can join different chains through different channels as follows:

![cMulti-channels & Multi-chains](https://ws1.sinaimg.cn/large/006tNc79gy1fmdfznp3rfj30mr0csq3a.jpg)

About channels: 

Just like the Publish-Subscribe topic, `peer` and `orderer`(Consensus service) get together and that also get `channels` , `ledger` and `worldstate` together, picuture as follows:

![](https://ws4.sinaimg.cn/large/006tNc79gy1fmdgqw35g5j30pm0m4acq.jpg)

`channel1`: `peer1`, `peer2`, `peer3`

`channel2`: `peer2`,`peerN`

`channel3`: `peer1`,`peer3`

##### Transaction Process

![](https://ws1.sinaimg.cn/large/006tNc79gy1fmdgz7wm5yj30m908f0ss.jpg)

 1.`Application/SDK` asks `peers`  for Endorse

2. The `endosor` inside `peer` would execute `chaincode` locally, but `endosor` will not hand over the result to local `ledger`, it will give result to `Application/SDK`

3. `Application/SDK` collect all the results from different `endosor`, and broadcasts the result to `Orderers`

4. `Orderers` execute the consensus process (Kafka, etc), and creates `Blocks`. Then `Orderers`  broadcasts the set of `Blocks` to `peer` through `channels`

5. `Peers` will check the `Blocks` and give them to local ledgers.

   ​

   ![](https://ws3.sinaimg.cn/large/006tNc79gy1fmdhiax9fjj31310m1gm6.jpg)

    

