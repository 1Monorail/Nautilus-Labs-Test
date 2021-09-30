#Timothy Moses
	#Nautilus Labs Test
	#9/30/2021
	#Method 2

def f(): # a second method
	if not A:  #inverse conditioning to reduce indenting
        s()		#Raising what would be the else statement for the nested case
        raise False #can raise false or create an escape if needed

	if not B:  #this may or may not work depending on the code.
        #z()    #It doesn't seem to work with this code because there are functions between the nested expressions
        t()
        raise False #raise is like a throw.

	if not C: #It still reduces indenting which is good for python code.
        #z()
        #y()  #It acts similarly to an "IF... THEN" statement in Java
        u()
        raise False

	if  D:         #Normal If for the last check
        #z()
        #y()
        #x()
        w()         # and this was the function that needed to be called after all conditions were met
        raise True

	else:  #the part of the code that would work the best.
        z()	#I was thinking about try blocks aswell but I think it would have beceome complex and not easy to read
        y()
        x()
        v()
f() #output
