# Implementation with an Hyperledger blockchain
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

#### Step 3: set the correct gopath

```
$ sudo gedit ~/.profile
```

Then add the following lines in the end of the file:

```
export PATH=$PATH:/usr/local/go/bin
```

```
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

[Fabric Official Website](https://hyperledger-fabric.readthedocs.io/en/release/samples.html#binaries)
