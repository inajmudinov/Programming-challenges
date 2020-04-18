"""J = "aA" 
S = "aAAbbbb"
#Output: 3
"""
J = "z" 
S = "ZZ"
#Output: 0

count=0

for i in range (len(J)):
    for j in range (len(S)):
        if J[i]==S[j]:
            count += 1
print(count)