### Fabric 0.6

#### Step0: Install Postman

[A Good Website recommend](https://blog.bluematador.com/posts/postman-how-to-install-on-ubuntu-1604/)

#### Step1: Download the whole documents of Fabric 0.6 

```
$ git clone https://github.com/yeasy/docker-compose-files
```

After copy the files we also need to pull the images:

```
$ docker pull hyperledger/fabric-peer:x86_64-0.6.1-preview \
&& docker pull hyperledger/fabric-membersrvc:x86_64-0.6.1-preview \
&& docker pull yeasy/blockchain-explorer:latest \
&& docker tag hyperledger/fabric-peer:x86_64-0.6.1-preview hyperledger/fabric-peer \
&& docker tag hyperledger/fabric-peer:x86_64-0.6.1-preview hyperledger/fabric-baseimage \
&& docker tag hyperledger/fabric-membersrvc:x86_64-0.6.1-preview hyperledger/fabric-membersrvc
```

#### Step2: open the directory & edit 2 files

```
$ cd ~/hyperledger/0.6/pbft
```

we need to comment some lines to let the file run locally:

```
$ gedit 4-peers-with-membersrvc-explorer.yml
```

then make the end of the file look like this and save it: 

```
networks:
 default:
   external:
     name: fabric_pbft
```

then edit the other one:

```
$ gedit peer.yml
```

delete the '#' of only one line inside(uncomment it) and save:

```
- CORE_VM_DOCKER_HOSTCONFIG_NETWORKMODE=fabric_pbft
```

#### Step3: Create the network

Before we create the network, let's check the network we already have:

```
$ docker network ls
```

Create the network just in the normal terminal window:

```
$ docker network create fabric_pbft
```

then check it:

```
$ docker network ls
```

#### Step4: Generate the 4 BPFT nodes+1 CA node 

```
$ docker-compose -f 4-peers-with-membersrvc.yml up
```

#### Step5: Copy Chaincode to Peers

In the network, `VP0` is the `Root VP` node, we can check the directory:

```
$ docker exec -it pbft_vp0_1 bash
root@vp0:/opt/gopath/src/github.com/hyperledger/fabric#
```

Use example02 as an example to copy:(But you need to check where you store the example02)

```
$ docker cp chaincode_example02/ pbft_vp0_1:/opt/gopath/src/github.com/
```

####Step6: Check the address of docker0 

```
$ ifconfig
```

then we could fine the ip of `docker0`, for example "172.17.0.1"

####Step7: Open Postman and post the  address 

Set the option to `POST`, and the address should be like as follows:

```
http://172.17.0.1:7050/registrar
```

Click `Body` , choose `raw` , choose the format as `JSON`. Then paste following code into the blank block and click `Send`:

```
{
  "enrollId": "jim",
  "enrollSecret": "6avZQLwcUe9b"
}
```

If everything runs correctly , the result will show up at the bottom of the Postman window:

```
{
  "OK": "Login successful for user 'jim'."
}
```

and we can also check the result in the terminal we opened.

#### Step8: Deploy the Chaincode

Create another file in Postman, Set the option to `POST`, Click `Body` , choose `raw` , choose the format as `JSON`. Then paste following code into the blank block and click `Send`:

```
{
  "jsonrpc": "2.0",
  "method": "deploy",
  "params": {
    "type": 1,
    "chaincodeID":{
        "path": "github.com/chaincode_example02"
    },
    "ctorMsg": {
        "args":["init"]
    },
    "secureContext": "jim"
  },
  "id": 1
}
```

If everything runs correctly , the result will show up at the bottom of the Postman window:

```
{
  "jsonrpc": "2.0",
  "result": {
    "status": "OK",
    "message": "28a49ca95eb0e0dbf3ee7e41ff2172c174b13aa1539db3c4977bb0b7a78d26cb4a0ea26252358ddc184f8d44172af1284dc3f914caa13ccd2137611c70059b59"
  },
  "id": 1
}
```

#### Step additional: Video to follow:

[Just check if you set everything rightly](https://www.youtube.com/watch?v=h48tgs2AWdQ)



