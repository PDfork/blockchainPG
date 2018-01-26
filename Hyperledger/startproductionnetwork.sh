composer archive create -t dir -n .

composer runtime install --card PeerAdmin@hlfv1 --businessNetworkName production-network

composer network start --card PeerAdmin@hlfv1 --networkAdmin admin --networkAdminEnrollSecret adminpw --archiveFile production-network@0.1.bna

composer network ping --card admin@production-network

composer-rest-server -c admin@production-network -n never -w true

