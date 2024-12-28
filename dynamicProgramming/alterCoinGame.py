# import random
#
# def generate_coins():
#     """Generate a random list of coins shuffled in order."""
#     coins = random.sample(range(5, 501, 5), k=10)
#     random.shuffle(coins)
#     return coins
#
# def calculate_optimal_strategy(coins):
#     """Calculate the optimal strategy using dynamic programming."""
#     n = len(coins)
#     dp = [[0] * n for _ in range(n)]
#
#     # Base case: one coin left
#     for i in range(n):
#         dp[i][i] = coins[i]
#
#     # Fill the DP table for subarrays of all lengths
#     for length in range(2, n + 1):
#         for i in range(n - length + 1):
#             j = i + length - 1
#             pick_first = coins[i] + min(dp[i + 2][j] if i + 2 <= j else 0, dp[i + 1][j - 1] if i + 1 <= j - 1 else 0)
#             pick_last = coins[j] + min(dp[i + 1][j - 1] if i + 1 <= j - 1 else 0, dp[i][j - 2] if i <= j - 2 else 0)
#             dp[i][j] = max(pick_first, pick_last)
#
#     return dp
#
# def simulate_game(coins, dp, start_pick):
#     """Simulate the game with optimal strategies for both players."""
#     i, j = 0, len(coins) - 1
#     my_total, opponent_total = 0, 0
#     my_turn = True
#
#     while i <= j:
#         pick_first = coins[i] + min(dp[i + 2][j] if i + 2 <= j else 0, dp[i + 1][j - 1] if i + 1 <= j - 1 else 0)
#         pick_last = coins[j] + min(dp[i + 1][j - 1] if i + 1 <= j - 1 else 0, dp[i][j - 2] if i <= j - 2 else 0)
#
#         if (start_pick == "first" and my_turn) or (start_pick == "last" and not my_turn):
#             if pick_first >= pick_last:
#                 my_total += coins[i]
#                 i += 1
#             else:
#                 my_total += coins[j]
#                 j -= 1
#         else:
#             if pick_first >= pick_last:
#                 opponent_total += coins[i]
#                 i += 1
#             else:
#                 opponent_total += coins[j]
#                 j -= 1
#
#         my_turn = not my_turn
#
#     return my_total, opponent_total
#
# def simulate_opponent_first(coins, dp):
#     """Simulate the game where the opponent starts first."""
#     i, j = 0, len(coins) - 1
#     my_total, opponent_total = 0, 0
#     my_turn = False  # Opponent starts first
#
#     while i <= j:
#         pick_first = coins[i] + min(dp[i + 2][j] if i + 2 <= j else 0, dp[i + 1][j - 1] if i + 1 <= j - 1 else 0)
#         pick_last = coins[j] + min(dp[i + 1][j - 1] if i + 1 <= j - 1 else 0, dp[i][j - 2] if i <= j - 2 else 0)
#
#         if my_turn:
#             if pick_first >= pick_last:
#                 my_total += coins[i]
#                 i += 1
#             else:
#                 my_total += coins[j]
#                 j -= 1
#         else:
#             if pick_first >= pick_last:
#                 opponent_total += coins[i]
#                 i += 1
#             else:
#                 opponent_total += coins[j]
#                 j -= 1
#
#         my_turn = not my_turn
#
#     return my_total, opponent_total
#
# def main():
#     """Main function to generate coins, calculate strategies, and simulate games."""
#     # Generate a random set of coins
#     coins = generate_coins()
#     print("Coins:", coins)
#
#     # Calculate the optimal strategy
#     dp = calculate_optimal_strategy(coins)
#
#     # Simulate starting with the first coin
#     first_case = simulate_game(coins, dp, "first")
#
#     # Simulate starting with the last coin
#     last_case = simulate_game(coins, dp, "last")
#
#     # Simulate opponent starting first
#     opponent_first_case = simulate_opponent_first(coins, dp)
#
#     print("\nResults:")
#     print("Starting with the first coin:", first_case)
#     print("Starting with the last coin:", last_case)
#     print("Opponent starts first:", opponent_first_case)
#
# if __name__ == "__main__":
#     main()

memo = {}
coinList = [5, 10, 100, 25]

def alter_coin_game(i = 0, j = len(coinList) - 1, chooser = "me"):

    if (i, j, chooser) in memo:
        return memo[(i, j, chooser)]

    #base case
    if i > j:
        return 0

    if i == j:
        if chooser == "me":
            memo[(i, j, chooser)] = coinList[i]
            return coinList[i]
        else:
            memo[(i, j, chooser)] = 0
            return 0

    if(chooser == "me"):
        result = max(alter_coin_game(i+1, j, "you") + coinList[i], alter_coin_game(i, j-1, "you") + coinList[j])
        memo[(i, j, chooser)] = result
        return result

    else: #when chooser == "you"
        result = min(alter_coin_game(i+1, j,"me"), alter_coin_game(i, j - 1, "me"))
        memo[(i, j, chooser)] = result
        return result

print(alter_coin_game(chooser="you"))



