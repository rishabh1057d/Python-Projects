
'''#WAP to make a progrqam and search for the words starting with letter s
d={}
n = int(input('enter the number of words to be entered:'))
for i in range(n):
    idd= int(input('enter the unique id:'))
    ele=input('enter the word:')
    a = [ ele ]
    d[idd] = a
print(d)
b= d.values()
print(b)
c= input('enter the letter to be found:')
for i in b:
    
    if i[0][0]==c:
        print('the word found',i[0])
'''        
    
'''    
    
k = [11,-1,22,-3,33,55,44,-50,46,101,77,-100]
for j in k:
    print(j)
    if j<0 or j%2!=0:
            k.remove(j)
print(k)
'''

