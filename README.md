# ZKP_Based-Authentication
The person who knows the password for the corresponding username will be authenticated to access the server services ,for this purpose the server stores the username and password in the database .If somebody hacks into the database they can access the username and password and hence the security is compromised (even if the password is hashed and salted it contains the signature of the password and it's vulnerable to dictionary attack).
In  __Zero Knowledge Protocol based Authentication__ the server does not store any password ,but it asks to prove the user that he/she knows the password .Only the legitimate user will be able prove that he/she knows the password.

# Registration
1) The user enters username ,password
2) __Hash(password)=x__ (user will hold this , private key)
3) The user computes __y=g<sup>x</sup>__ (where 'g' is the generator of the group 'G',{G,g} is public)
4) User sends __(username,y)__ to the server
5) Server stores __(username,y)__ into the Database

# Authentication
1) The server generates a random token __'a'__ & stores it and sends it to the user 
2) User enters username and password
3) At user end __x=Hash(password)__ & __y=g<sup>x</sup>__ is computed
4) The user generates random token __r__ Є __G__ & calculates __T1 = g<sup>x</sup>__
5) The user computes __Hash(Y,T1,a)=c__ and __z=r-(c*x)__
6) The user sends (c,z) over to the server
7) The Server calculates __T1=y<sup>c</sup>g<sup>z</sup>__ {y=g<sup>x</sup> ; (g<sup>c</sup>)<sup>x</sup>. g<sup>z</sup> = g<sup>cx</sup>. g<sup>z</sup> = g<sup>r-z</sup>. g<sup>z</sup>z = g<sup>r</sup> = T1 ; Hence proved}
8) The Server calculates __Hash(Y,T1,a)=sc__ 
9) If __sc=c__ then 'Successfull Authentication' else 'Authentication Failed'

The main practical difficulty in implementing the above protocol is that a number need to be raised to a power of an enormous 
number (g<sup>x</sup> ; Where x is a very large value 128/256 bit long depending on the hash function we use ).So inorder to solve this 
issue ,we need to make some changes in the practical implementation . 

# Practical implementation
1) __x= Hash(password)mod 10__ 
2) g=2; __y=2<sup>x</sup>__
3) Server saves [Username,y] in the database
4) User: __T1=g<sup>r</sup>__ ; r: random number between 0-10 
5) User: __c=Hash(y+T1+a)mod 10__ ; __z=r-c__
6) User sends (c,z) to the server
7) Server : __T1=Y<sup>c</sup>__ . __g<sup>z</sup>__
8) Server : __Hash(Y+T1+c)mod 10=sc__ ; if __sc=c__ then 'Access Granted' else 'Username or password you entered is wrong'


[Reference Paper](http://ojs.pythonpapers.org/index.php/tppm/article/view/155/142)
