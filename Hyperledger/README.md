# Prerequisite for Hyperledger blockchain
The following are prerequisites for installing the required development tools:

    Operating Systems: Ubuntu Linux 14.04 / 16.04 LTS (both 64-bit), or Mac OS 10.12
    Docker Engine: Version 17.03 or higher
    Docker-Compose: Version 1.8 or higher
    Node: 8.9 or higher (note version 9 is not supported)
    npm: v5.x
    git: 2.9.x or higher
    Python: 2.7.x
    Go 1.9+ installation
    A code editor of your choice, we recommend VSCode.
    
### One: Curl

#### Step 1：check which version is the latest

[Official Website for curl](https://curl.haxx.se/download.html)

#### Step 2: change the 7.52.1 into the latest version number 

```
$ wget https://curl.haxx.se/download/curl-7.52.1.tar.gz

$ tar -xvf curl-7.52.1.tar.gz

$ cd curl-7*

$ ./configure --with-ssl

$ make

$ sudo make install

```

### Two: Docker-ce && Docker-Compose

#### Step 1: install Docker

[Official Website for Docker installed in Ubuntu](https://docs.docker.com/engine/installation/linux/docker-ce/ubuntu/#prerequisites)

#### Step 2: check the version

```
$ docker --version

$ docker-compose --version
```

### Three: Install Go

#### Step 1: install go

```
$ sudo add-apt-repository ppa:gophers/archive

$ sudo apt update

$ sudo apt-get install golang-1.9-go

# This will give you the latest version of go
$ snap install --classic go
```

#### Step2: check the version

```
$ go version
```
the newest is 1.9.2

#### Step 3: set the correct gopath

```
$ sudo gedit ~/.profile
```

Then add the following lines in the end of the file:

```
export PATH=$PATH:/usr/local/go/bin
export GOPATH=/opt/gopath
```

To get the path useful, you need to run the following command as well:

```
$ source ~/.profile
```

To check if the path really work:

```
$ echo $PATH
```

### Four: Node.js Runtime and NPM

#### Step 1: install nodejs & npm

```
$ curl -sL https://deb.nodesource.com/setup_8.x | sudo -E bash -

$ sudo apt-get install -y nodejs

$ sudo apt-get install -y build-essential
```

#### Step 2: check the version

```
$ node -v

$ npm -v
```

### Five: Get started

[Fabric Official Website](https://hyperledger-fabric.readthedocs.io/en/release-1.1/)



According to our goal, we must know how to use fabric-ca to create more users

[Official Website for Fabric-ca](http://hyperledger-fabric-ca.readthedocs.io/en/latest/users-guide.html#start-server-natively)
