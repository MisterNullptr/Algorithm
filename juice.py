def juice_greedy(juice_list, max_cap):
    available_cap = max_cap
    happiness = 0
    juice_ratio = []
    for juice in juice_list:
        juice_ratio.append({"ratio" : juice["value"]/ juice["volume"],"value" : juice["value"], "volume" : juice["volume"]})

    juice_ratio.sort(key=lambda x: x["ratio"], reverse=True)

    for  i in juice_ratio:
        if i["volume"] < available_cap:
            available_cap -= i["volume"]
            happiness += i["value"]
        else:
            frac = available_cap / i["volume"]
            happiness += frac * i["value"]
            available_cap = 0
            break

    return happiness


j = [{"value" : 6, "volume" : 1},{"value": 3,"volume": 3},{"value": 1000, "volume": 1000}]


print(juice_greedy(j, 3))




