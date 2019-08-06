# Say you have an array for which the ith element is the price of a given stock on day i
# If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock),
# design an algorithm to find the maximum profit
# Note that you cannot sell a stock before you buy one

# We need to find the largest peak following the smallest valley
# We can maintain two variables - low and max_profit corresponding to the smallest valley and maximum profit
# (maximum difference between selling price and low) obtained so far respectively


class Solution:
    def max_profit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0:
            return 0
        else:
            low = 99999
            max_profit = 0
            for price in prices:
                if price > low:
                    if price - low > max_profit:
                        max_profit = price - low
                elif price < low:
                    low = price

            return max_profit


# driver script
if __name__ == "__main__":

    # set inputs and run solution
    prices1 = [7, 1, 5, 3, 6, 4]
    prices2 = [7, 6, 4, 3, 1]
    solution = Solution()

    # print result
    print(solution.max_profit(prices1))
    print(solution.max_profit(prices2))
