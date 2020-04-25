#word = "Hello"

b ={"A":"a", "B":"b", "C":"c", "D":"d", "E":"e", "F":"f", "G":"g", "H":"h", "I":"i", "J":"j", "K":"k", "L":"l", "M":"m", "N":"n", "O":"o", "P":"p", "Q":"q", "R":"r", "S":"s", "T":"t", "U":"u", "V":"v", "W":"w", "X":"x", "Y":"y", "Z":"z" }



def ToLowerCase(word):
    c = ""
    for i in word:
         if i not in b.keys():
             c += i
         else:
             c += b[i]
    print(c)
         
ToLowerCase("Hello")



#        i == b[i]
        
        
#print(b.keys())







#print(ord("a") - ord("A"))