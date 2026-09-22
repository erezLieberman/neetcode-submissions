class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        amount_to_coins = [float("inf") for i in range(amount + 1)]
        amount_to_coins[0] = 0
        for current_amount in range(1,len(amount_to_coins)):
            for coin in coins:
                if current_amount - coin >= 0:
                    amount_to_coins[current_amount] = min(amount_to_coins[current_amount], 1 + amount_to_coins[current_amount - coin])
        return amount_to_coins[amount] if amount_to_coins[amount] != float("inf") else -1