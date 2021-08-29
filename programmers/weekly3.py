def add_block(r, c):
    for dx, dy in move_pattern:
        px = r + dx
        py = c + dy
        # 이동 가능한 경로가 아닐 경우 다음 이동 패턴으로 넘어가기
        if px < 0 or py < 0 or px >= table_length or py >= table_length:
            continue
        # 이동 가능한 위치가 1이 아닐 경우 다음 이동 패턴으로 넘어가기
        if table[px][py] != 1:
            continue
        # 저장안한 블럭요소일 경우 블럭에 저장하기
        if (px, py) not in check_dup:
            block.append((px, py))
            check_dup.append((px, py))
            # 다음 블럭요소 찾기
            add_block(px, py)

block = set()
game_board = [[1,1,0,0,1,0],
              [0,0,1,0,1,0],
              [0,1,1,0,0,1],
              [1,1,0,1,1,1],
              [1,0,0,0,1,0],
              [0,1,1,1,0,0]]

table = [[1,0,0,1,1,0],
         [1,0,1,0,1,0],
         [0,1,1,0,1,1],
         [0,0,1,0,0,0],
         [1,1,0,1,1,0],
         [0,1,0,0,0,0]]
# table의 길이
table_length = len(table)

# 블럭의 리스트
block_list = list()
# 블럭 중복체크
check_dup = list()
# 이동패턴
move_pattern = [(0,-1), (0,1),(-1,0),(1,0)]

# 테이블의 길이 만큼 순회하며 상하좌우에 인접하는 요소가 1일 경우 한 블럭으로 저장하기
for row in range(table_length):
    for col in range(table_length):
        #
        if table[row][col] == 0:
            continue
        if (row, col) in check_dup:
            continue
        block = list()
        check_dup.append((row, col))
        block.append((row, col))

        add_block(row, col)
        block_list.append(block)

# 블럭단위의 위치 출력
print(block_list)

