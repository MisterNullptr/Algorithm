def profit_greedy(stock, budget):
    current_money = budget

    stock.sort(key=lambda x: x["cost"])

    for i in stock:
        net_gain = i["profit"] - i["cost"]

        if net_gain > 0:

            if i["cost"] <= current_money:
                current_money += net_gain
            else:
                break

    return current_money


input_line = input().split()
if input_line:
    number_of_stock = int(input_line[0])
    budget = int(input_line[1])

    stock = []
    for i in range(number_of_stock):
        cost, profit = map(int, input().split())
        stock.append({"cost": cost, "profit": profit})

    print(profit_greedy(stock, budget))