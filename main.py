import sys

inp = sys.argv[1]

vowels = ['a','e','i','o','u','y','ó','ą','ę']

connected1=['e']
connected2=['u']

num = 0

outl = []


for x in inp:
    if not inp.isalpha():
        print("Not alphabetic characters detected")
        exit()

if len(inp)<=3:
    print(1)
    print(inp)
    exit()

for ind , x in enumerate(inp):
    outl.append(x)
    x=x.lower()
    if (x in vowels ) and ((ind+1)<len(inp)):
        if (inp[ind+1] not in vowels):
            if not (x in connected1 and inp[ind+1] in connected2):
                outl.append('-')
                num +=1

def listToString(s):  
    str1 = ""  
    for ele in s:  
        str1 += ele   
    return str1  
        
        


print(num)
print(listToString(outl))
