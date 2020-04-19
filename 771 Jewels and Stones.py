import sys

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        count=0
        for i in range (len(J)):
            for j in range (len(S)):
                if J[i]==S[j]:
                    count += 1
        return count
                  

    # здесь твой код

# здесь напишем все тесты
def run_tests():
    
    
  # создаём объект экземпляр Solution (совсем простенькое ООП)
    sol = Solution()
    
  # печатаем тесты, вызываю метод этого объекта
    print(sol.numJewelsInStones("aA", "aAAbbbb"))
    print(sol.numJewelsInStones("aA", "bb"))

# вот это запустится только если будешь запускать скрипт из консоли
# $ python 771 Jewels and Stones.py
# а когда этот код будет запускать LeetCode, то выполняться не будет, что нам и нужно
if sys.stdin.isatty():
    run_tests()

        