print "Starting Factory 3";
print "Launching services... please wait"
import requests;
import sys;
data ={"$class":"org.production.auction.Update", "updateproduction":0, "flag":0, "listing":"org.production.auction.ProductionListing#opt1", "producer":"org.production.auction.Producer#F3"};

a = requests.get("http://10.0.2.15:3000/api/ProductionListing");
ac = a.status_code
if ac == 200:
	print("Comunication stablished with ledger... the magic is comming");

	at= a.content;
	
	if at == '[]':
   		print "Network not started. Run sf1.py"
#	else: 

		#aj= a.json();

#		data['updateproduction']=14;
#		p = requests.post("http://10.0.2.15:3000/api/Update",data);
#		pc = p.status_code
#		if pc == 200:
#			print "Initialization done.";
#		else:   print "Network error. Check the configuration"
	else:
		aj= a.json();
		Lambda = aj[0]['LAMBDA']; 	#(chek the apostrofes)
		f = aj[0]['f'];

		#if (f==7):
		#	print "NEW LAMBDA = %f"%(Lambda);		
		#else:
			#print(f);
		b = f&4;
			#print(b);
		
		if (b==4): 
			print "Lambda current value %f" % (Lambda); 
			sys.exit();
	  	else:
			l=float(Lambda);
			#print "Lambda current value %f" % (l) 
			a=-l/2;			#local objetive function
			data['updateproduction']=a;
			data['flag']=4;
			print "Computing new X3 value"
			#print(data);

			p = requests.post("http://10.0.2.15:3000/api/Update",data);
			pc = p.status_code
			print "X2 = %f" %(a)

			if pc == 200:
				print("Updated X3 correctly to ledger")
				a = requests.get("http://10.0.2.15:3000/api/ProductionListing");
				aj= a.json();
				Lambda = aj[0]['LAMBDA'];
				f = aj[0]['f'];
				print "Lambda current value %f" % (Lambda) 
			else:
				print("Comunication error. Please check the network")
else: print "Network error. Check IPs"
#for x in range(0, 3):
 #   print "We're on time %d" % (x)
#	else: print("Comunications not stablished. Please check network configuration.")
