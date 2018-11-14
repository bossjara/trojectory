'''
Trojectory output on output.csv file 
To be improved: (1) Output to matplotlib 
                (2) Real system time
2018/11/14 
Jiunn Chen 
'''
import math
import csv


gg=9.81  #Gravitation constant m/sec^2
csvfile=open('output.csv', 'w', newline='') 
writer=csv.writer(csvfile, delimiter='\t')

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
    yy=Troj(v0, theta, i)
    print(i, yy)
    writer.writerow([i, yy])

csvfile.close()  #close file
