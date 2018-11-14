'''
Trojectory output on output.csv file 
To be improved: (1) Output to matplotlib 
                (2) Real system time
2018/11/14 
Jiunn Chen 
'''
import math
import csv
import matplotlib.pyplot as plt

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


#open file to write
csvfile=open('output.csv', 'w', newline='') 
writer=csv.writer(csvfile, delimiter='\t')
for i in range(0,100):
    yy=Troj(v0, theta, i)
    print(i, yy)
    writer.writerow([i, yy])

csvfile.close()  #close file

#read file to plot
with open('output.csv') as f:
    lines=f.readlines()
    x=[line.split()[0] for line in lines]
    y=[line.split()[1] for line in lines]


plt.plot(x,y)
plt.ylabel('height(meter)')
plt.xlabel('distance(meter)')
plt.show()

