from collections import deque

c = 11
b = 2

# 코니는 처음 위치에서 1초후 +1만큼, 매초마다 이전 이동거리 + 1만큼 이동
# 속도 1 2 3 4 5 ...
# 위치는 0으로 초기화 -> 이동거리 + 위치를 수행 -> 이동거리에 1을 더함

# 브라운은 B - 1, B + 1, B * 2 중 선택
# 1. 2 - 1 = 1
# 2. 2 + 1 = 3
# 3. 2 * 2 = 4

# 모든 경우의 수 나열 -> BFS 사용
# 시간은 1초마다 항상 1씩 증가
# 단 코니와 브라운의 위치값은 항상 바뀐다.(자유자재)
# 자유자재로 바뀌는 자료는 딕셔너리를 사용하면 된다.

def catch_me(cony_loc, brown_loc):
    time = 0
    queue = deque()
    queue.append((brown_loc, 0))
    visited = [{} for _ in range(200001)]

    while cony_loc <= 200000:
        cony_loc += time
        if time in visited[cony_loc]:
            return time

        for i in range(0, len(queue)):
            cur_pos, cur_time = queue.popleft()

            new_position = cur_pos - 1
            new_time = cur_time + 1
            if new_position >= 0 and new_time not in visited[new_position]:
                visited[new_position][new_time] = True
                queue.append((new_position, new_time))

            new_position = cur_pos + 1
            if new_position < 200001 and new_time not in visited[new_position]:
                visited[new_position][new_time] = True
                queue.append((new_position, new_time))

            new_position = cur_pos * 2
            if new_position < 200001 and new_time not in visited[new_position]:
                visited[new_position][new_time] = True
                queue.append((new_position, new_time))

        time += 1


print(catch_me(c, b))  # 5가 나와야 합니다!