# Под шаблон Leetcode
class Solution:
    def defangIPaddr(self, address: str) -> str:
        a = ""
        for i in address:
            if i != ".":
                a += i
            else:
                a += "[.]"
        return a
        
print(Solution().defangIPaddr( "255.100.50.0"))