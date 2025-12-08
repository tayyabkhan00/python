import matplotlib.pyplot as plt

import matplotlib.pyplot as plt
import numpy as np

#x=['c++','python','ruby','java']
#y=[10,20,30,40]
#c=['r','g','b','y']
#plt.bar(x,y,color=c,align='center',width=0.5,edgecolor='black',linewidth=1)
#plt.show()


x=['c++','python','ruby','java']
y=[10,20,30,40]
z=[2,10,15,28]    #the height of the second bar
                   #there's no z axis here this is just the second dataset
width=0.2
p=np.arange(len(x))#this creates positions for the bars on the x axis
p1=p+width# to not overlap
plt.xlabel('language')
plt.ylabel('no.')
plt.title('bar chart')
plt.bar(p,y,width,color='y',label='popularity')
plt.bar(p1,z,width,color='r',label='popularity1')
plt.xticks(p+width/2,x,rotation=20)
plt.legend()
plt.show()