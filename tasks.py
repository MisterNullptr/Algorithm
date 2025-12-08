def greedy_schedule(jobs, n):
    slots = [False] * (n + 1)
    total_profit = 0
    jobs.sort(key=lambda x: x["profit"], reverse=True)

    for i in jobs:
        deadline = min(i["deadline"], n)
        for time in range(deadline, 0, -1):
            if not slots[time]:
                slots[time] = True
                total_profit += i["profit"]
                break
    return total_profit

input_line = input().split()
if input_line:
    n = int(input_line[0])

    jobs = []
    for i in range(n):
        d, p = map(int, input().split())
        jobs.append({"deadline": d, "profit": p})

    print(greedy_schedule(jobs, n))