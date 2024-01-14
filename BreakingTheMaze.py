import pygame
import sys
import random

# Pygameの初期化
pygame.init()

# 画面のサイズと色を設定
width, height = 900, 900
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("BreakingTheMaze")

# 迷路のセルのサイズと色を設定
cell_size = 45
brown_color = (148, 133, 98)  # 茶色
green_color = (0, 128, 0)    # 緑色
blue_color = (0, 0, 255)     # 青色
yellow_color = (255, 255, 0) # 黄色

# キャラクターの初期位置
character_pos = [0, 0]

# アイテムの位置（画面の一番右下）
item_pos = [19, 19]

# 迷路のサイズを計算
rows = height // cell_size
cols = width // cell_size

# 迷路の定義 (0は通れる道、1は通れない道)
maze1 = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0],
    [0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0],
    [0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0],
    [0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0],
    [0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1],
    [0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0],
    [0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0],
    [0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0],
    [0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1],
    [0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0],
    [0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1],
    [0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0]
]

maze2 = [
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0],
    [0, 0, 0, 1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1],
    [0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0],
    [1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0],
    [0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0],
    [0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0],
    [1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0],
    [0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0],
    [0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0],
    [0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 0],
    [1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0]
]

maze3 = [
    [0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0],
    [0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0],
    [0, 1, 1, 1, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0],
    [0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0],
    [1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0],
    [0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0],
    [0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1],
    [0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0],
    [0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0],
    [0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0],
    [0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1],
    [0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0],
    [0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
    [0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

maze4 = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
    [0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1],
    [0, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1],
    [0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1],
    [0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1],
    [0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1],
    [0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1],
    [0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0],
    [1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0],
    [1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0],
    [0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0]
]

maze5 = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1],
    [0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0],
    [0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0],
    [0, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0],
    [1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
    [0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
    [0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0],
    [0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0],
    [0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1],
    [0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1],
    [0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0]
]

# 5つの迷路をリストに格納
mazes = [maze1, maze2, maze3, maze4, maze5]

# カスタム迷路の定義 (初期迷路)
custom_maze = random.choice(mazes)  # 最初はランダムに1つ選ぶ

# ランダムに1つの迷路を選択
selected_maze = random.choice(mazes)
custom_maze = selected_maze  # 選択された迷路を使用

# キャラクターの移動速度
move_speed = 1

# キャラクターが黄色くなったかどうかのフラグ
character_yellow = False

# キャラクターが向いている方向
character_direction = "right"  # 初期状態では右向き

# Pygameのクロックを初期化
clock = pygame.time.Clock()

# スペースキーが押されたかどうかのフラグ
space_pressed = False

# ゲームクリアのフラグ
game_clear = False

# やめるの選択フラグ
quit_selected = False

# 時間関連
start_time = 0  # ゲーム開始時刻
display_time = 0  # 表示用のゲームクリアまでの時間
game_clear_time = 0  # ゲームクリアまでの時間
time_displayed = False  # 表示用のゲームクリアまでの時間が既に表示されたかどうかのフラグ

# キャラクターが向いている方向の座標を計算
def get_front_cells(character_pos, direction, num_cells=5):
    front_cells = []

    for i in range(1, num_cells + 1):
        x, y = character_pos
        if direction == 'UP':
            y -= i
        elif direction == 'DOWN':
            y += i
        elif direction == 'LEFT':
            x -= i
        elif direction == 'RIGHT':
            x += i

        front_cells.append((x, y))

    return front_cells


# メインのイベントループ
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                space_pressed = True
            if event.key == pygame.K_q:  # キーが q の場合
                quit_selected = True


    # キー入力の取得
    keys = pygame.key.get_pressed()
    
    # キャラクターの移動
    if keys[pygame.K_w] and character_pos[1] > 0 and custom_maze[character_pos[1]-1][character_pos[0]] == 0:
        character_pos[1] -= move_speed
        character_direction = "up"
    if keys[pygame.K_s] and character_pos[1] < rows - 1 and custom_maze[character_pos[1]+1][character_pos[0]] == 0:
        character_pos[1] += move_speed
        character_direction = "down"
    if keys[pygame.K_a] and character_pos[0] > 0 and custom_maze[character_pos[1]][character_pos[0]-1] == 0:
        character_pos[0] -= move_speed
        character_direction = "left"
    if keys[pygame.K_d] and character_pos[0] < cols - 1 and custom_maze[character_pos[1]][character_pos[0]+1] == 0:
        character_pos[0] += move_speed
        character_direction = "right"

    # 画面をクリア
    screen.fill((0, 0, 0))

    # 迷路を描画
    for row in range(rows):
        for col in range(cols):
            if row < len(custom_maze) and col < len(custom_maze[row]):
                if custom_maze[row][col] == 1:
                    pygame.draw.rect(screen, green_color, (col * cell_size, row * cell_size, cell_size, cell_size))
                else:
                    pygame.draw.rect(screen, brown_color, (col * cell_size, row * cell_size, cell_size, cell_size))

    # 右下に到達したかどうかの判定
    if character_pos == item_pos:
        character_yellow = True
        # アイテムを削除し、茶色に戻す
        custom_maze[item_pos[1]][item_pos[0]] = 0

    # アイテムを描画
    if not character_yellow:
        pygame.draw.rect(screen, blue_color, (item_pos[0] * cell_size, item_pos[1] * cell_size, cell_size, cell_size))

    # キャラクターを描画（三角形）
    if character_yellow:
        if character_direction == "up":
            pygame.draw.polygon(screen, yellow_color, [
                (int((character_pos[0] + 0.5) * cell_size), int(character_pos[1] * cell_size)),
                (int(character_pos[0] * cell_size), int((character_pos[1] + 1) * cell_size)),
                (int((character_pos[0] + 1) * cell_size), int((character_pos[1] + 1) * cell_size))
            ])
        elif character_direction == "down":
            pygame.draw.polygon(screen, yellow_color, [
                (int((character_pos[0] + 0.5) * cell_size), int((character_pos[1] + 1) * cell_size)),
                (int(character_pos[0] * cell_size), int(character_pos[1] * cell_size)),
                (int((character_pos[0] + 1) * cell_size), int(character_pos[1] * cell_size))
            ])
        elif character_direction == "left":
            pygame.draw.polygon(screen, yellow_color, [
                (int(character_pos[0] * cell_size), int((character_pos[1] + 0.5) * cell_size)),
                (int((character_pos[0] + 1) * cell_size), int(character_pos[1] * cell_size)),
                (int((character_pos[0] + 1) * cell_size), int((character_pos[1] + 1) * cell_size))
            ])
        elif character_direction == "right":
            pygame.draw.polygon(screen, yellow_color, [
                (int((character_pos[0] + 1) * cell_size), int((character_pos[1] + 0.5) * cell_size)),
                (int(character_pos[0] * cell_size), int((character_pos[1] + 1) * cell_size)),
                (int(character_pos[0] * cell_size), int(character_pos[1] * cell_size))
            ])
        # キャラクターが向いている方向の前方5マスを白く縁取り
        if character_direction == "up":
            front_cells = get_front_cells(character_pos, "UP")
        elif character_direction == "down":
            front_cells = get_front_cells(character_pos, "DOWN")
        elif character_direction == "left":
            front_cells = get_front_cells(character_pos, "LEFT")
        elif character_direction == "right":
            front_cells = get_front_cells(character_pos, "RIGHT")

        for cell in front_cells:
            x, y = cell
            pygame.draw.rect(screen, (255, 255, 255), (x * cell_size, y * cell_size, cell_size, cell_size), 2)

    else:
        if character_direction == "up":
            pygame.draw.polygon(screen, (255, 0, 0), [
                (int((character_pos[0] + 0.5) * cell_size), int(character_pos[1] * cell_size)),
                (int(character_pos[0] * cell_size), int((character_pos[1] + 1) * cell_size)),
                (int((character_pos[0] + 1) * cell_size), int((character_pos[1] + 1) * cell_size))
            ])
        elif character_direction == "down":
            pygame.draw.polygon(screen, (255, 0, 0), [
                (int((character_pos[0] + 0.5) * cell_size), int((character_pos[1] + 1) * cell_size)),
                (int(character_pos[0] * cell_size), int(character_pos[1] * cell_size)),
                (int((character_pos[0] + 1) * cell_size), int(character_pos[1] * cell_size))
            ])
        elif character_direction == "left":
            pygame.draw.polygon(screen, (255, 0, 0), [
                (int(character_pos[0] * cell_size), int((character_pos[1] + 0.5) * cell_size)),
                (int((character_pos[0] + 1) * cell_size), int(character_pos[1] * cell_size)),
                (int((character_pos[0] + 1) * cell_size), int((character_pos[1] + 1) * cell_size))
            ])
        elif character_direction == "right":
            pygame.draw.polygon(screen, (255, 0, 0), [
                (int((character_pos[0] + 1) * cell_size), int((character_pos[1] + 0.5) * cell_size)),
                (int(character_pos[0] * cell_size), int((character_pos[1] + 1) * cell_size)),
                (int(character_pos[0] * cell_size), int(character_pos[1] * cell_size))
            ])

    # スペースキーが押された場合
    if space_pressed and character_yellow:
        for i in range(1, 6):
            # 向いている方向の前方5マスを通れる道に変更
            if character_direction == "up" and character_pos[1] - i >= 0:
                custom_maze[character_pos[1] - i][character_pos[0]] = 0
            elif character_direction == "down" and character_pos[1] + i < rows:
                custom_maze[character_pos[1] + i][character_pos[0]] = 0
            elif character_direction == "left" and character_pos[0] - i >= 0:
                custom_maze[character_pos[1]][character_pos[0] - i] = 0
            elif character_direction == "right" and character_pos[0] + i < cols:
                custom_maze[character_pos[1]][character_pos[0] + i] = 0

        # スペースキーが離されたらフラグをリセット
        space_pressed = False

    # ゲーム開始時にタイマーをスタート
    if not game_clear and start_time == 0:
        start_time = pygame.time.get_ticks()

    # ゲームクリアの判定
    if all(row.count(0) == len(row) for row in custom_maze):
        game_clear = True
        # ゲームクリアまでの時間を計算（秒単位に変換）
        game_clear_time = (pygame.time.get_ticks() - start_time) // 1000
        # 表示用のゲームクリアまでの時間を設定（初回のみ）
        if not time_displayed:
            display_time = game_clear_time
            time_displayed = True

    # 画面を更新
    pygame.display.flip()

    # ゲームクリアの場合
    if game_clear:
        font_game_clear = pygame.font.Font(None, 74)
        text_game_clear = font_game_clear.render("GAME CLEAR", True, (0, 0, 0))
        screen.blit(text_game_clear, (width // 2 - text_game_clear.get_width() // 2, height // 2 - text_game_clear.get_height() // 2))

        # 固定されたクリアまでの時間を表示
        font_time = pygame.font.Font(None, 36)
        text_time = font_time.render(f"Time: {display_time} seconds", True, (0, 0, 0))
        screen.blit(text_time, (width // 2 - text_time.get_width() // 2, height // 2 + text_game_clear.get_height() // 2 + 20))

        # 「やめる：Q」の表示
        font_choice = pygame.font.Font(None, 36)
        text_quit = font_choice.render("Quit : Q", True, (0, 0, 0) if quit_selected else (0,0,0))
        screen.blit(text_quit, (width // 2 - text_quit.get_width() // 2, height // 2 + text_game_clear.get_height() // 2 + text_time.get_height() + 40))

        pygame.display.flip()

        # Qが押されたら終了
        if quit_selected:
            pygame.time.wait(1000)  # 1秒待機してから終了
            pygame.quit()
            sys.exit()

    # 画面を更新
    pygame.display.flip()

    # フレームレートを制御
    clock.tick(10)

input()