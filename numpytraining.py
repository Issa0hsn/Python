import numpy as np
 
import sys 
myarray=np.arange(1000)
#print(myarray)
print(myarray.itemsize)
print(myarray.size)

mylist=[ i for i in range(1000)]
#print(mylist)
print(sys.getsizeof(mylist[0]))
print(len(mylist) * sys.getsizeof(mylist[0]))
print(sys.getsizeof(mylist))
m= np.matrix("[[1,2,3];[4,5,6];[7,8,9]]")
#print(m)
print(m.ndim)

frow=np.arange(1,6)
srow=np.arange(11,16)
throw=np.arange(22,27)
a=np.vstack([frow,srow,throw],dtype="int16")
#print(a)
print(type(a))
print(a.shape)
print(a.nbytes)
print(a.ndim)
#print(a[0,1:-1])
b=np.full((3,3),["A","B","C"],)
#print(b)
print(type(b))
print(b.itemsize)
print(b.shape)
print(b.nbytes)
print(b.ndim)
#print(b[0,1:-1])
c=np.arange(12)
c=c.reshape(6,2)
#print(c)
print("*"*10)
d=np.random.randint(1,10,a.shape)
#print(d)
#generate Random array (shape a(2,4) ,range(-4,10-4=6)

e=np.random.randint(-10,10,size=(5,5)) 
print(e)
print(e[::2,::2])


f=np.repeat([[1,2,3],[4,5,6]],3,axis=0)
#axis =0 means row-wise
#axis=1 means column-wise

#print(f) 

help(np.void)
