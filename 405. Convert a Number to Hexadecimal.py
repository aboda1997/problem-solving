class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        hex_String = "0123456789abcdef"
        res = ""
        if num < 0 :
            num = (1<< 32) + num
        if num == 0 : 
            return "0"    
        while num > 0 :
            index = num % 16
            res=hex_String[index] +res  
            num //=16 
        return res   

