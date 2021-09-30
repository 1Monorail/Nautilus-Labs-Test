#Timothy Moses
	#Nautilus Labs Test
	#9/30/2021
	#Method 1

def A(): #turn if and else statements into methods for easier editing and less indents
    A:
        z()
    else:
        s()
        return False    #returns might not do much here but will be left in for readability

def B()
    B:  #can easily change condintions now
        y()
    else:
        t()
        return False
​
def C() #IF and else statements are bundled together for easier reading
    C:  #also makes it easier to comment on the code
        x()
    else:
        u()
        return False
​
def D() #function names can be defined in an easy to understand way.
    D:
        w()
        return True
    else:   #elif can easily be added here aswell for adding conditions
        v()
        return False

def f():    #if the nesting was out of order it is easy to fix and change
    A()
    B()
    C()
    D()
        # drawback is that without added conditions and complexity all else statements will execute.
        # if instance if conditions A and B are true and C and D are false
            #output is z(), y(), u(), v(). where in the nested it would be z(), y(), u()
        # would most likey just need added elif statements in the functions
            #it is more complex but much beter for any colaboration or updating
f() #output
