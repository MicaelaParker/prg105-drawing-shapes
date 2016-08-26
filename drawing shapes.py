#import gives me access to other functions and code
import turtle

 #create a variable bob and make it a trutle type
 #turtle() is a function in turtle library that makes a trutle object
bob = turtle.Turtle()


 #fd() moves foward  by pixels
 #lt() turns left by degrees
 #rt()turns right degrees
 #bk() move backward by pixels

 #pu() holds pen up
 #pd()holds pen down

 # the "." shows  that this function is part if the turtle  object library
bob.fd(100) #move foward 100 pixels
bob.lt(90)
bob.fd(100)
bob.lt(90)
bob.fd(100)
bob.lt(90)
bob.fd(100)

turtle.mainloop()

