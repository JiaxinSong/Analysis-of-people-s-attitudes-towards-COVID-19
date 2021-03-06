import numpy as np
import matplotlib.pyplot as plt
import datetime

f = open("alltweets.txt","r")   #set file object

a=0
b=0
c=0
for line in f.readlines():
        x=eval(line)
        if 'positive' in x['sentiment']:
            a=a+1;
        if 'negative' in x['sentiment']:
            b=b+1;
        if 'neutral' in x['sentiment'] :
            c=c+1;
# count whole number of each sentiment

def pro(a,b,c):
    pa= a/(a+b+c)
    pb = b / (a + b + c)
    pc = c / (a + b + c)
    return [pa,pb,pc]
# cal proportion
e=pro(a,b,c)
print(e)
f.close()

#make pie graph
import matplotlib.pyplot as plt
labels ='Positive','Negative','Neutral'
fraces = [e[0],e[1],e[2]]
#three sentiments
plt.axes(aspect=1)
plt.pie(x=fraces,labels= labels,autopct='%0f%%',shadow=True)
plt.title('Sentiment proportion 2.1-4.17',color = 'black',fontsize = 20)
plt.savefig('all pie.png',dpi = 400)
plt.show()

