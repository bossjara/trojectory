'''
First python script demostrating a module function call.
This function return x!. 
2018/11/14 
Jiunn Chen 
'''

def Fact(a):
    b=1
    for i in range(0,a):
        i+=1
        b=b*i
    return b

x=input("Input a number for calculating x!:")
print("The answer is", Fact(int(x)))
