shop_menus = ["만두", "떡볶이", "오뎅", "사이다", "콜라"]
shop_orders = ["오뎅", "콜라", "만두"]


def is_available_to_order(menus, orders):
    menus.sort()
    for order in orders:
        if not is_existing_target_number_binary(order, menus):
            print("다시 주문해주세요!")
            return False

    print("주문이 가능합니다.")
    return True


# 주문한 메뉴와 메뉴판을 비교(이진탐색)
def is_existing_target_number_binary(target, array):
    cur_min = 0
    cur_max = len(array) - 1
    cur_guess = (cur_min + cur_max) // 2

    find_count = 0

    while cur_min <= cur_max:
        find_count += 1
        if array[cur_guess] == target:
            print(find_count, "회 탐색")
            return True
        elif array[cur_guess] < target:
            cur_min = cur_guess + 1
        else:
            cur_max = cur_guess - 1

        cur_guess = (cur_min + cur_max) // 2

    return False


result = is_available_to_order(shop_menus, shop_orders)
print(result)
