'''
Trojectory output on terminal.
To be improved: (1) Output to a CVS file
                (2) Output to matplotlib
                (2) Real system time
2018/11/14 
Jiunn Chen 
'''
import math

gg=9.81  #Gravitation constant m/sec^2

def Troj(v0,theta,xx):
   temp=math.cos(theta)
   temp=temp**2 
   temp=2*v0**2*temp 
   temp=(gg/temp)*xx**2
   yy=xx*math.tan(theta)-temp 
   return yy

v0=float(input("Input the initial velocity (m/sec):"))
theta=float(input("Input the initial angle (degree):"))

theta=theta*math.pi/180

for i in range(0,100):
    print(i, Troj(v0,theta, i))
