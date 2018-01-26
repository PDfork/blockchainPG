import requests
print "Defining factories F1 F2 F3 and productions X1 X2 X3. Please wait."
p = requests.post("http://10.0.2.15:3000/api/Producer",data ={"$class": "org.production.auction.Producer","product": "X1","factory": "F1"})

p = requests.post("http://10.0.2.15:3000/api/Producttion",data ={"$class": "org.production.auction.Producttion","comodity": "X1", "owner":"org.production.auction.Producer#F1"})


p = requests.post("http://10.0.2.15:3000/api/Producer",data ={"$class": "org.production.auction.Producer","product": "X2","factory": "F2"})

p = requests.post("http://10.0.2.15:3000/api/Producttion",data ={"$class": "org.production.auction.Producttion","comodity": "X2", "owner":"org.production.auction.Producer#F2"})


p = requests.post("http://10.0.2.15:3000/api/Producer",data ={"$class": "org.production.auction.Producer","product": "X3","factory": "F3"})

p = requests.post("http://10.0.2.15:3000/api/Producttion",data ={"$class": "org.production.auction.Producttion","comodity": "X3", "owner":"org.production.auction.Producer#F3"})

p = requests.post("http://10.0.2.15:3000/api/ProductionListing",data ={"$class": "org.production.auction.ProductionListing","listingId": "opt1",  "LAMBDA": 0, "acc":0, "f":0,"description":"first optimization",  "production":"org.production.auction.Producttion#X1"})



