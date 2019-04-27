# first of all import the socket library 
import socket    
import csv   
import random  
import hashlib       
  
# next create a socket object 
s = socket.socket()          
print "Socket successfully created"
  
# reserve a port on your computer in our 
# case it is 12345 but it can be anything 
port = 12345           
  
# Next bind to the port 
# we have not typed any ip in the ip field 
# instead we have inputted an empty string 
# this makes the server listen to requests  
# coming from other computers on the network 
s.bind(('', port))         
print "socket binded to %s" %(port) 
  
# put the socket into listening mode 
s.listen(5)      
print "socket is listening"            
  
# a forever loop until we interrupt it or  
# an error occurs 
req= 2
#with open('Users.csv','w') as newFile:
#	newFileWriter = csv.writer(newFile)
#	newFileWriter.writerow(['user_id','Password'])



while True: 
  
   # Establish connection with client. 
   c, addr = s.accept()      
   print 'Got connection from', addr 
   c.send('\n1->Login\n2->NewUser')
   req=c.recv(1024)
   req=int(req)

   rows=[]

   if req==1:
   		c.send('Login Procedure initiating')
   		a=random.randint(1,10)
   		c.send(str(a)) #random number a is generated
   		uid=c.recv(1024)
   		
   		z=c.recv(1024)
   		c1=c.recv(1024)
   		c1=int(c1)
   		z=int(z)
   		#print z
   		#print uid + pw

   		csvfile=open('Signin.csv','r') 
   		csvreader=csv.reader(csvfile)# creating a csv reader object
   		fields=csvreader.next() 

   		for row in csvreader:
   			rows.append(row)
   		#rows=rows[1:]
   		#print rows
   		for data in rows :
   			if data[0]==uid:
   				y= data[1]
   				break

   		y=int(y)
   		T1=(y**c1)*(2**z)
   		T1=int(T1)
   		#print T1

   		inpu=y+T1+a
		hash_object = hashlib.sha1(str(inpu))
		hex_dig = hash_object.hexdigest()
		hsh=int(hex_dig,16)
		c2=hsh%10

		if c2==c1:
			c.send('Access Granted ,You have been successfully logged in')
		else :
			c.send('The user_name or Password you entered is wrong')


      
    # extracting field names through first row 
  
    # extracting each data row one by one 

       	

   elif req==2:
   		c.send('Sign up')
   		uid=c.recv(1024)
   		pw=c.recv(1024)

   		with open('Signin.csv', 'a') as newFile:
   			newFileWriter=csv.writer(newFile)
   			newFileWriter.writerow([uid, pw])
   else:
   	print 'Invalid input '

    	


  
   # send a thank you message to the client.  
   c.send('\nThank you for connecting') 
  
   # Close the connection with the client 
   c.close() 