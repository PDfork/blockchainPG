### Structure of Fabric (Roughly)

#### Fabric 0.6

Before we get known of Fabric 1.0, we need to understand Fabric 0.6 which is a stable version.

![Fabric main parts](https://github.com/PDfork/blockchainPG/blob/master/Hyperledger/Fabric/Img/Fabric1.jpeg)



When you run Fabric 0.6, the architecture is :

![Favric 0.6 architecture](https://github.com/PDfork/blockchainPG/blob/master/Hyperledger/Fabric/Img/Fabric2.jpeg)

The architecture is `application`-`membership`-`peer`, the triangle relationships. The main affairs focus on Peers. 



#### Fabric 1.0

But here comes our problem: Peer affords too many functions, so we improve the architecture into Fabric 1.0 as follows:

![Fabric 1.0 architecture](https://github.com/PDfork/blockchainPG/blob/master/Hyperledger/Fabric/Img/Fabric3.jpeg)

Consensus has been taken out of Peers, and been set into an isolated node `orderer`. Based on the new architecture, Fabric 1.0 also has channels. 

##### Main charaters

Fabric 1.0 supports multi-chaincode and multi-channels.

A `peer` can join different chains through different channels as follows:

![cMulti-channels & Multi-chains](https://github.com/PDfork/blockchainPG/blob/master/Hyperledger/Fabric/Img/Fabric4.jpeg)

About channels: 

Just like the Publish-Subscribe topic, `peer` and `orderer`(Consensus service) get together and that also get `channels` , `ledger` and `worldstate` together, picuture as follows:

![](https://github.com/PDfork/blockchainPG/blob/master/Hyperledger/Fabric/Img/Fabric5.png)

`channel1`: `peer1`, `peer2`, `peer3`

`channel2`: `peer2`,`peerN`

`channel3`: `peer1`,`peer3`

##### Transaction Process

![](https://github.com/PDfork/blockchainPG/blob/master/Hyperledger/Fabric/Img/Fabric6.jpeg)

 1.`Application/SDK` asks `peers`  for Endorse

2. The `endosor` inside `peer` would execute `chaincode` locally, but `endosor` will not hand over the result to local `ledger`, it will give result to `Application/SDK`

3. `Application/SDK` collect all the results from different `endosor`, and broadcasts the result to `Orderers`

4. `Orderers` execute the consensus process (Kafka, etc), and creates `Blocks`. Then `Orderers`  broadcasts the set of `Blocks` to `peer` through `channels`

5. `Peers` will check the `Blocks` and give them to local ledgers.

   ​

   ![](https://github.com/PDfork/blockchainPG/blob/master/Hyperledger/Fabric/Img/Fabric7.jpeg)

    

