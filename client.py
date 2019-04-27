# Import socket module 
import socket     
import getpass
import hashlib    
import random       
  
# Create a socket object 
s = socket.socket()          
  
# Define the port on which you want to connect 
port = 12345       
  
# connect to the server on local computer 
s.connect(('127.0.0.1', port)) 
  
# receive data from the server 
print s.recv(1024)
op = raw_input("\nEnter your option : ") 
s.send(op)
op=int(op)
if op==1:
	print s.recv(1024) 
	a=int(s.recv(1024)) #random number from server
	r=random.randint(1,10) #rx

	uid = raw_input("\nEnter Userid : ")
	pw = getpass.getpass('Password: ')
	#pw=raw_input("Enter Password : ")
	s.send(uid)

	hash_object = hashlib.sha1(pw)
	hex_dig = hash_object.hexdigest()
	hsh=int(hex_dig,16)
	x=hsh%10
	#print x
	y=(2**x) # g0 =5
	T1=(2**r) #r :random number

	inpu=y+T1+a
	hash_object = hashlib.sha1(str(inpu))
	hex_dig = hash_object.hexdigest()
	hsh=int(hex_dig,16)
	c=hsh%10
	z=r-(c*x)
	#print z
	#print c
	#print z
	#print T1
	s.send(str(z))
	s.send(str(c))
	print s.recv(1024)

else :
	print s.recv(1024) #signup
	uid = raw_input("\nEnter Userid : ")
	pw = getpass.getpass('Password: ')
	#pw=raw_input("Enter Password : ")
	s.send(uid)

	hash_object = hashlib.sha1(pw)
	hex_dig = hash_object.hexdigest()
	hsh=int(hex_dig,16)
	x=hsh%10
	#print x 
	y=(2**x) # g0 =5
	#print y 
	s.send(str(y))


print s.recv(1024) 
# close the connection 
s.close()        