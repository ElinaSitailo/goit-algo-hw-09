# Маємо набір монет [50, 25, 10, 5, 2, 1].
# Уявіть, що ви розробляєте систему для касового апарату,
# яка повинна визначити оптимальний спосіб видачі решти покупцеві.


# Вам необхідно написати дві функції для касової системи, яка видає решту покупцеві:
# 1. Функція жадібного алгоритму find_coins_greedy.
#       Ця функція повинна приймати суму, яку потрібно видати покупцеві,
#       і повертати словник із кількістю монет кожного номіналу, що використовуються для формування цієї суми.
#       Наприклад, для суми 113 це буде словник {50: 2, 10: 1, 2: 1, 1: 1}.
#       Алгоритм повинен бути жадібним, тобто спочатку вибирати найбільш доступні номінали монет.

import time


def find_coins_greedy(amount, coins):
    """Жадібний алгоритм для знаходження монет для заданої суми."""
    result = {}

    for coin in coins:
        count = amount // coin
        if count > 0:
            result[coin] = count
            amount -= coin * count

    return result


# 2. Функція динамічного програмування find_min_coins.
#       Ця функція також повинна приймати суму для видачі решти,
#       але використовувати метод динамічного програмування,
#       щоб знайти мінімальну кількість монет, необхідних для формування цієї суми.
#           Функція повинна повертати словник із номіналами монет та їх кількістю для досягнення заданої суми найефективнішим способом.
#           Наприклад, для суми 113 це буде словник {1: 1, 2: 1, 10: 1, 50: 2}
def find_min_coins(amount, coins):
    """Алгоритм динамічного програмування для знаходження мінімальної кількості монет для заданої суми."""
    max_amount = amount + 1
    dp = [max_amount] * (amount + 1)
    dp[0] = 0
    coin_used = [-1] * (amount + 1)

    for coin in coins:
        for x in range(coin, amount + 1):
            if dp[x - coin] + 1 < dp[x]:
                dp[x] = dp[x - coin] + 1
                coin_used[x] = coin

    if dp[amount] == max_amount:
        return {}

    result = {}
    while amount > 0:
        coin = coin_used[amount]
        if coin in result:
            result[coin] += 1
        else:
            result[coin] = 1
        amount -= coin

    return result


# Порівняйте ефективність жадібного алгоритму та алгоритму динамічного програмування,
# базуючись на часі їх виконання або О великому та звертаючи увагу на їхню продуктивність при великих сумах.
# Висвітліть, як вони справляються з великими сумами та чому один алгоритм може бути більш ефективним за інший у певних ситуаціях.


def compare_coin_algorithms(find_coins_greedy, find_min_coins, test_amount, coins):
    """Порівнює два алгоритми за часом виконання."""

    print(f"Comparing algorithms for amount: {test_amount}. Coins: {coins}")

    greedy_start_time = time.time()
    greedy_result = find_coins_greedy(test_amount, coins)
    greedy_end_time = time.time()
    greedy_processing_time = greedy_end_time - greedy_start_time
    print(f"Greedy algorithm took \t\t\t{greedy_processing_time:.10f} seconds: {greedy_result}")

    dp_start_time = time.time()
    dp_result = find_min_coins(test_amount, coins)
    dp_end_time = time.time()
    dp_processing_time = dp_end_time - dp_start_time
    # сортуємо результат для кращого порівняння
    dp_result = dict(sorted(dp_result.items(), reverse=True))

    print(f"Dynamic programming algorithm took \t{dp_processing_time:.10f} seconds: {dp_result}")

    print(f"That was {dp_processing_time / greedy_processing_time:.2f} times slower than greedy algorithm.\n")
    return greedy_result, dp_result


if __name__ == "__main__":

    coins = [50, 25, 10, 5, 2, 1]
    greedy_result, dp_result = compare_coin_algorithms(find_coins_greedy, find_min_coins, 113, coins)
    assert greedy_result == {50: 2, 10: 1, 2: 1, 1: 1}
    assert dp_result == {50: 2, 10: 1, 2: 1, 1: 1}

    compare_coin_algorithms(find_coins_greedy, find_min_coins, 2345, coins)
    compare_coin_algorithms(find_coins_greedy, find_min_coins, 123456, coins)

    # тестування з різним результатом
    coins_test = [30, 20, 5]
    greedy_result, dp_result = compare_coin_algorithms(find_coins_greedy, find_min_coins, 40, coins_test)


# Порівняння ефективності:
# Жадібний алгоритм має часову складність O(n), де n - кількість різних номіналів монет.
# Алгоритм динамічного програмування має часову складність O(m*n),
# де m - сума, яку потрібно видати, а n - кількість різних номіналів монет.

# Жадібний алгоритм зазвичай працює швидше для невеликих сум,
# але може не знайти оптимальне рішення для певних наборів монет.
# Алгоритм динамічного програмування завжди знаходить оптимальне рішення,
# але може бути повільнішим для дуже великих сум через свою часову складність.
# Вибір між цими двома алгоритмами залежить від конкретних вимог до продуктивності та точності рішення.
# У випадках, коли потрібна максимальна ефективність і сума не є надто великою,

# жадібний алгоритм може бути кращим вибором.
# Якщо ж важлива точність і сума може бути великою, варто використовувати алгоритм динамічного програмування.