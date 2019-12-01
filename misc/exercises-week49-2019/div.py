#Example 1
for c in range(2000):
    a=1.0
    for i in range(c):
        a=a/2
    
    for i in range(c):
        a=a*2
    
    print(c,a)

#Example 2
for c in range(100):
    a=1.0
    for i in range(c):
        a=a/2+1.0
    
    for i in range(c):
        a=(a-1.0)*2
    
    print(c,a)

#Example 3
for c in range(100):
    a=1.0
    for i in range(c):
        a=a/2+10000.0
    
    for i in range(c):
        a=(a-10000.0)*2
    
    print(c,a)

