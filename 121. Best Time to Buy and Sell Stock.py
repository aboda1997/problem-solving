class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if prices == sorted(prices, reverse = True) :
            return 0 
        min_ele = 10000000000
        helper_array = []
        for indx  in range(len(prices)): 
            if (prices[indx]<min_ele):
                min_ele = prices[indx]
            else: 
                helper_array.append(prices[indx] - min_ele)

        return max(helper_array)    