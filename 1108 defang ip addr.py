"""
address = "1.1.1.1"
# Output: "1[.]1[.]1[.]1"

"""
address = "255.100.50.0"
# Output: "255[.]100[.]50[.]0"
"""
print(address.replace(".", "[.]"))
"""
# Для Leetcode
class Solution:
    def defangIPaddr(self, address: str) -> str:
        return(address.replace(".", "[.]"))