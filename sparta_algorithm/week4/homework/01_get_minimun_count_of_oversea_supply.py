import heapq

ramen_stock = 4
supply_dates = [4, 10, 15]
supply_supplies = [20, 5, 10]
supply_recover_k = 30


def get_minimum_count_of_overseas_supply(stock, dates, supplies, k):
    answer = 0
    cur_day_idx = 0
    max_heap = []
    while stock < k:
        for date_idx in range(cur_day_idx,len(dates)):
            if dates[date_idx] <= stock:
                heapq.heappush(max_heap, -supplies[date_idx])
            else:
                cur_day_idx = date_idx
                break

        answer += 1
        stock += -heapq.heappop(max_heap)
    return answer


print(get_minimum_count_of_overseas_supply(ramen_stock, supply_dates, supply_supplies, supply_recover_k))