# Под шаблон LC

class Solution:
    def toLowerCase(self, str: str) -> str:
        b ={"A":"a", "B":"b", "C":"c", "D":"d", "E":"e", "F":"f", "G":"g", "H":"h", "I":"i", "J":"j", "K":"k", "L":"l", "M":"m", "N":"n", "O":"o", "P":"p", "Q":"q", "R":"r", "S":"s", "T":"t", "U":"u", "V":"v", "W":"w", "X":"x", "Y":"y", "Z":"z"}
        c = ""
        for i in str:
            if i not in b.keys():
                c += i
            else:
                c += b[i]
        return c