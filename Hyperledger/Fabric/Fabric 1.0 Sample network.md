### Fabric 1.0 Sample network

#### Basic/ Sample network

the structure is as follows:

![Structure of basic network](https://github.com/PDfork/blockchainPG/blob/master/Hyperledger/Fabric/Img/Fabric%201.0%20structure.jpeg)

#### Step1: Copy the Fabric Sample file to your computer

```
$ git clone https://github.com/hyperledger/fabric-samples.git
$ cd fabric-samples
```

#### Step2: Download Platform-specific Binaries

```
curl -sSL https://goo.gl/byy2Qj | bash -s 1.0.5
```

#### Step3: Get Started

```
$ cd /first-network
$ ./byfn.sh -m generate
$ ./byfn.sh -m up
```

When everything is correct, you can see the END in the terminal window.

Open another terminal to shut the network down:

```
$ ./byfn.sh -m down
```

#### Step4: To be continued

[More details check here](https://hyperledger-fabric.readthedocs.io/en/release/build_network.html)



