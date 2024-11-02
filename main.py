d1={'Codingal':2,'is':3,'best':2,'for':1,'Coding':3}
print(d1,'\nTest dictionary')
f=int(input('Write the number you want to check the frequency of: '))
c=0
for i in d1.values():
    if i==f:
        c=c+1
print(c,'is the frequency of number',f)