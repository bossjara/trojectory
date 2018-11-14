'''
Second python script demostrating a module function call.
This call function returns "nearly" trojectary 
To be improved: (1) Input value interger only
                (2) mathi module handling the Trigonometric function is required.
                (3) math  module converting degrees to radius is required.

2018/11/14 
Jiunn Chen 
'''
gg=9.81  #Gravitation constant m/sec^2
def Troj(v0,theta,xx):
   # b=1
    temp=gg/(2*v0^2*theta)*xx**2
    yy=xx-temp 
    return yy

v0=input("Input the initial velocity (m/sec):")
theta=input("Input the initial angle (degree):")

for i in range(0,100):
    print("The trojectory:", i, Troj(int(v0),int(theta), i))
