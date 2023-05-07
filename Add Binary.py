# question  https://leetcode.com/problems/add-binary/description/


#ans

class Solution:
    def addBinary(self, a: str, b: str) -> str:
         c = int(a,2) + int(b,2)
         return(bin(c).removeprefix("0b"))
