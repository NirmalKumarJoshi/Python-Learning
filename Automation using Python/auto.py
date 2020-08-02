f=open('Hello.txt','r')

passfile= open('Testing.txt','w')


count=0;
for line in f:
    passfile.write(line)
    count=count+1
    
    
f.close();
