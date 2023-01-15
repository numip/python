import pygame
import random
from settings2 import *


class Map:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        _: int
        self.mas_map = [[0] * 18 for _ in range(18)]  # Это генератор списка заполненного 0
        self.design_map()
        self.change_list()
        self.new_list = []
        self.place = []
        self.win_count = 0
        self.win_count_b = 0
        self.win()
        self.win_black()
        self.count_b = 0
        self.black_list = []
        self.new_list_b = []
        self.rand_ai()
        self.rael_pos()

    def design_map(self):  # Создаем доску для игры
        count1 = 0

        for r in range(18):
            for c in range(18):
                if self.mas_map[r][c] == 1:
                    count1 += 1

        for row in range(18):  # цикл создания 18 строк
            for col in range(18):  # цикл создания 18 столбцов
                x = col * BOX_WIDTH + (col + 1) * MARGIN  # создание квадрата
                y = row * BOX_HEIGHT + (row + 1) * MARGIN  # создание квадрата
                pygame.draw.rect(self.display_surface, COLOR_MAP, [x, y, BOX_WIDTH, BOX_HEIGHT])
                if count1 <= 12:
                    if self.mas_map[col][row] == 1:  # игрок
                        pygame.draw.circle(self.display_surface, WHITE,
                                           ((col * BOX_WIDTH + (col + 7.5) * MARGIN),
                                            (row * BOX_HEIGHT + (row + 7.5) * MARGIN)),
                                           RADIUS)

                    if self.mas_map[col][row] == 2:  # ии
                        pygame.draw.circle(self.display_surface, BLACK,
                                           ((col * BOX_WIDTH + (col + 7.5) * MARGIN),
                                            (row * BOX_HEIGHT + (row + 7.5) * MARGIN)),
                                           RADIUS)

                    elif count1 == 12:
                        self.message_list(f'Фишки кончились', BUSY)

                elif count1 > 12:
                    self.message_break(f'Нарушение правил!', BUSY)

    def show_message_b(self, msg, color):
        font_style = pygame.font.SysFont('cambria', 30)
        message = font_style.render(msg, True, color)
        self.display_surface.blit(message, [WIDTH // 1.25, HEIGHT // 1.6])

    def message_list(self, msg, color):  # для фишек
        font_style = pygame.font.SysFont('cambria', 25)
        message = font_style.render(msg, True, color)
        self.display_surface.blit(message, [WIDTH // 1.3, HEIGHT // 3])

    def message_break(self, msg, color):  # для фишек > 12
        font_style = pygame.font.SysFont('cambria', 25)
        message = font_style.render(msg, True, color)
        self.display_surface.blit(message, [WIDTH // 1.3, HEIGHT // 4])

    def show_message(self, msg, color):  # для счетчика
        font_style = pygame.font.SysFont('cambria', 30)
        message = font_style.render(msg, True, color)
        self.display_surface.blit(message, [WIDTH // 1.25, HEIGHT // 1.4])

    def change_list(self):  # функция меняющая в списке 0 на 1 по координатам с мыши
        new_x, new_y = pygame.mouse.get_pos()
        print(new_x, new_y)
        new_col = new_x // (MARGIN + BOX_WIDTH)  # столбец (индекс)
        new_row = new_y // (MARGIN + BOX_HEIGHT)  # строка (индекс)
        if pygame.mouse.get_pressed()[2]:
            self.mas_map[new_col][new_row] = 1
            self.new_list.extend([[new_col, new_row]])
            self.win()
            self.rael_pos()

        if pygame.mouse.get_pressed()[0]:
            self.mas_map[new_col][new_row] = 0

    def rand_ai(self):
        if pygame.mouse.get_pressed()[2]:
            if len(self.new_list) > 0:
                if self.count_b < 12:
                    v = random.randrange(len(self.place))
                    print(v)
                    id_x = self.place[v][0]
                    id_y = self.place[v][1]
                    while self.mas_map[id_x][id_y] != 0:
                        print(self.mas_map[id_x][id_y])
                        v = random.randrange(len(self.place))
                        print('else', v)
                        id_x = self.place[v][0]
                        id_y = self.place[v][1]
                        print(self.mas_map[id_x][id_y])
                        continue
                    if self.mas_map[id_x][id_y] == 0:
                        self.mas_map[id_x][id_y] = 2
                        print(id_x, id_y)
                        print(self.mas_map[id_x][id_y])
                        self.count_b += 1
                        print(self.count_b)
                        print(self.mas_map)
                        self.black_list.extend([[id_x, id_y]])
                        print(self.black_list)

                elif self.count_b == 12:
                    way = random.randint(1, 8)
                    w = random.randrange(len(self.black_list))
                    print(self.black_list)
                    n = self.black_list[w][0]
                    m = self.black_list[w][1]
                    print(n)
                    if way == 1:  # проверяем левый элемент
                        if n > 0:
                            elem_n = n - 1
                            print(elem_n)
                            while self.mas_map[elem_n][m] != 0:
                                w = random.randrange(len(self.black_list))
                                print('1!=', w)
                                n = self.black_list[w][0]
                                m = self.black_list[w][1]
                                elem_n = n - 1
                                continue
                            if self.mas_map[elem_n][m] == 0:
                                self.mas_map[n][m] = 0
                                self.mas_map[elem_n][m] = 2
                                self.black_list[w][0] = elem_n
                                print(self.black_list[w][0])
                                print(self.black_list)
                    if way == 2:   # проверяем правый элемент
                        if n >= 0:
                            elem_n = n + 1
                            print(elem_n)
                            if elem_n <= 17:
                                while self.mas_map[elem_n][m] != 0:
                                    w = random.randrange(len(self.black_list))
                                    print('2!=', w)
                                    n = self.black_list[w][0]
                                    m = self.black_list[w][1]
                                    elem_n = n + 1
                                    continue
                                if self.mas_map[elem_n][m] == 0:
                                    self.mas_map[n][m] = 0
                                    self.black_list[w][0] = elem_n
                                    self.mas_map[elem_n][m] = 2
                                    print(self.black_list[w][0])

                                    print(self.black_list)
                            else:
                                return
                    if way == 3:
                        if m > 0:
                            elem_m = m - 1
                            while self.mas_map[n][elem_m] != 0:
                                w = random.randrange(len(self.black_list))
                                print('3!=', w)
                                n = self.black_list[w][0]
                                m = self.black_list[w][1]
                                elem_m = m - 1
                                continue
                            if self.mas_map[n][elem_m] == 0:
                                self.mas_map[n][m] = 0
                                self.mas_map[n][elem_m] = 2
                                self.black_list[w][1] = elem_m
                                print(self.black_list[w][0])
                                print(self.black_list)
                    if way == 4:
                        if m >= 0:
                            elem_m = m + 1
                            if elem_m <= 17:
                                while self.mas_map[n][elem_m] != 0:
                                    w = random.randrange(len(self.black_list))
                                    print('4!=', w)
                                    n = self.black_list[w][0]
                                    m = self.black_list[w][1]
                                    elem_m = m + 1
                                    continue
                                if self.mas_map[n][elem_m] == 0:
                                    self.mas_map[n][m] = 0
                                    self.mas_map[n][elem_m] = 2
                                    self.black_list[w][1] = elem_m
                                    print(self.black_list[w][0])
                                    print(self.black_list)
                            else:
                                return
                    if way == 5:
                        if n and m > 0:
                            elem_n = n - 1
                            elem_m = m + 1
                            while self.mas_map[elem_n][elem_m] != 0:
                                w = random.randrange(len(self.black_list))
                                print('5!=', w)
                                n = self.black_list[w][0]
                                m = self.black_list[w][1]
                                elem_n = n - 1
                                elem_m = m + 1
                                continue
                            if self.mas_map[elem_n][elem_m] == 0:
                                self.mas_map[n][m] = 0
                                self.mas_map[elem_n][elem_m] = 2
                                self.black_list[w][0] = elem_n
                                self.black_list[w][1] = elem_m
                                print(self.black_list[w][0])
                                print(self.black_list[w][1])
                                print(self.black_list)
                    if way == 6:
                        if n and m > 0:
                            elem_n = n - 1
                            elem_m = m - 1
                            while self.mas_map[elem_n][elem_m] != 0:
                                w = random.randrange(len(self.black_list))
                                print('6!=', w)
                                n = self.black_list[w][0]
                                m = self.black_list[w][1]
                                elem_n = n - 1
                                elem_m = m - 1
                                continue
                            if self.mas_map[elem_n][elem_m] == 0:
                                self.mas_map[n][m] = 0
                                self.mas_map[elem_n][elem_m] = 2
                                self.black_list[w][0] = elem_n
                                self.black_list[w][1] = elem_m
                                print(self.black_list[w][0])
                                print(self.black_list[w][1])
                                print(self.black_list)
                    if way == 7:
                        if n and m >= 0:
                            elem_n = n + 1
                            elem_m = m - 1
                            while self.mas_map[elem_n][elem_m] != 0:
                                w = random.randrange(len(self.black_list))
                                print('7!=', w)
                                n = self.black_list[w][0]
                                m = self.black_list[w][1]
                                elem_n = n + 1
                                elem_m = m - 1
                                continue
                            if self.mas_map[elem_n][elem_m] == 0:
                                self.mas_map[n][m] = 0
                                self.mas_map[elem_n][elem_m] = 2
                                self.black_list[w][0] = elem_n
                                self.black_list[w][1] = elem_m
                                print(self.black_list[w][0])
                                print(self.black_list[w][1])
                                print(self.black_list)
                    if way == 8:
                        if n and m >= 0:
                            elem_n = n + 1
                            elem_m = m + 1
                            while self.mas_map[elem_n][elem_m] != 0:
                                w = random.randrange(len(self.black_list))
                                print('8!=', w)
                                n = self.black_list[w][0]
                                m = self.black_list[w][1]
                                elem_n = n + 1
                                elem_m = m + 1
                                continue
                            if self.mas_map[elem_n][elem_m] == 0:
                                self.mas_map[n][m] = 0
                                self.mas_map[elem_n][elem_m] = 2
                                self.black_list[w][0] = elem_n
                                self.black_list[w][1] = elem_m
                                print(self.black_list[w][0])
                                print(self.black_list[w][1])
                                print(self.black_list)
            self.win_black()

    def win_ver(self):  # победа вертикально
        new_x, new_y = pygame.mouse.get_pos()
        x1 = new_x // (MARGIN + BOX_WIDTH)  # столбец
        y1 = new_y // (MARGIN + BOX_HEIGHT)  # строка

        count_x = 0
        v = 0

        if len(self.new_list) > 0:
            if count_x < 5:
                # i = 1
                for i in self.mas_map[x1]:
                    if i == self.mas_map[x1][y1]:
                        while i != self.mas_map[x1][v]:
                            v += 1
                            print(v)
                            count_x = 0
                            print('if !=', count_x)
                            continue
                        if i == self.mas_map[x1][v]:
                            count_x += 1
                            v += 1
                            print(count_x, 'i ==')
                            print(v)
            if count_x == 5:
                print('WIN')
                count_x = 0
                print(count_x)
                self.win_count += 1
                print(self.win_count)

    def win_ver_b(self):
        count_x_b = 0
        if len(self.new_list) > 0:
            if count_x_b < 5:
                for i in self.mas_map:
                    x = self.mas_map.index(i)
                    if self.mas_map[x].count(2) > 0:
                        print('x', x)
                        for j in i:
                            if j == 2:
                                count_x_b += 1
                                print('j', count_x_b)
                            else:
                                count_x_b = 0

                            if count_x_b == 5:
                                count_x_b = 0
                                print(count_x_b)
                                print('WIN')
                                self.win_count_b += 1
                                return

    def win_hor(self):  # победа горизонтально
        new_x, new_y = pygame.mouse.get_pos()
        x1 = new_x // (MARGIN + BOX_WIDTH)  # столбец (индекс)
        y1 = new_y // (MARGIN + BOX_HEIGHT)  # строка
        count_y = 0

        # Проверяем все списки на наличие 1 в одном и том же месте, списки должны идти подряд
        if len(self.new_list) > 0:
            if count_y < 5:
                for i in self.mas_map:
                    if i.count(1) > 0:
                        if i[y1] != self.mas_map[x1][y1]:
                            count_y = 0
                            print('el')
                            continue
                        if i[y1] == self.mas_map[x1][y1]:
                            if x1 + 1 <= 17:
                                if i[y1] == self.mas_map[x1+1][y1] or i[y1] == self.mas_map[x1-1][y1]:
                                    count_y += 1
                                    print('c', count_y)
                                else:
                                    count_y = 0

                    else:
                        continue

                    if count_y == 5:
                        count_y = 0
                        print(count_y)
                        print('WIN')
                        self.win_count += 1

    def win_hor_b(self):

        count_y_b = 0

        if len(self.new_list) > 0:
            if count_y_b < 5:
                for i in self.mas_map:
                    x = self.mas_map.index(i)
                    x1 = x
                    if i.count(2) > 0:
                        y = i.index(2)
                        y1 = y
                        print('y', y1)

                        if i[y1] == 2:
                            if x1 + 1 <= 17:
                                if self.mas_map[x1][y1] == self.mas_map[x1 + 1][y1] or \
                                        self.mas_map[x1][y1] == self.mas_map[x1 - 1][y1]:
                                    count_y_b += 1
                                    print('c', count_y_b)

                            if y1 == 17:
                                y = 0
                                print(y)
                                break

                    else:
                        continue

                if count_y_b == 5:
                    count_y_b = 0
                    print(count_y_b)
                    print('WIN')
                    self.win_count_b += 1

    def diag(self):
        new_x, new_y = pygame.mouse.get_pos()
        x1 = new_x // (MARGIN + BOX_WIDTH)  # столбец
        y1 = new_y // (MARGIN + BOX_HEIGHT)  # строка
        x = 0
        count_d = 0
        # Найти подряд идущие 1 по диагонали. Их должно быть 5
        # Check positively sloped diagonal
        if len(self.new_list) > 0:
            if count_d < 5:
                # Проверяем строки на наличие в них 1
                while x != x1:
                    x += 1
                    print('!= x1', x)
                else:
                    if self.mas_map[x].count(1) > 0:
                        for elem in self.mas_map[x]:
                            if elem != self.mas_map[x1][y1]:
                                continue
                            if x1 + 1 <= 17 and y1 + 1 <= 17:
                                if self.mas_map[x1][y1] == self.mas_map[x1-1][y1-1] or \
                                        self.mas_map[x1][y1] == self.mas_map[x1+1][y1+1]:
                                    count_d = 2
                                    print('-1', count_d)
                                    if x1 + 2 <= 17 and y1 + 2 <= 17:
                                        if self.mas_map[x1][y1] == self.mas_map[x1-2][y1-2] or \
                                                self.mas_map[x1][y1] == self.mas_map[x1+2][y1+2]:
                                            count_d += 1
                                            print('-2', count_d)
                                            if x1 + 3 <= 17 and y1 + 3 <= 17:
                                                if self.mas_map[x1][y1] == self.mas_map[x1-3][y1-3] or \
                                                        self.mas_map[x1][y1] == self.mas_map[x1+3][y1+3]:
                                                    count_d += 1
                                                    print('-3', count_d)
                                                    if x1 + 4 <= 17 and y1 + 4 <= 17:
                                                        if self.mas_map[x1][y1] == self.mas_map[x1-4][y1-4] or \
                                                                self.mas_map[x1][y1] == self.mas_map[x1+4][y1+4]:
                                                            count_d += 1
                                                            print('-4', count_d)

            if count_d == 5:
                print('win!')
                count_d = 0
                print(count_d)
                self.win_count += 1

    def diag_b(self):
        count_d_b = 0
        if len(self.new_list) > 0:
            if count_d_b < 5:
                for i in self.mas_map:
                    x = self.mas_map.index(i)
                    x1 = x

                    if i.count(2) > 0:
                        for elem in i:
                            y = i.index(elem)
                            y1 = y
                            if elem != 2:
                                continue
                            if x1 + 1 <= 17 and y1 + 1 <= 17:
                                if self.mas_map[x1][y1] == self.mas_map[x1 - 1][y1 - 1] or \
                                        self.mas_map[x1][y1] == self.mas_map[x1 + 1][y1 + 1]:
                                    count_d_b = 2
                                    print('-1', count_d_b)
                                    if x1 + 2 <= 17 and y1 + 2 <= 17:
                                        if self.mas_map[x1][y1] == self.mas_map[x1 - 2][y1 - 2] or \
                                                self.mas_map[x1][y1] == self.mas_map[x1 + 2][y1 + 2]:
                                            count_d_b += 1
                                            print('-2', count_d_b)
                                            if x1 + 3 <= 17 and y1 + 3 <= 17:
                                                if self.mas_map[x1][y1] == self.mas_map[x1 - 3][y1 - 3] or \
                                                        self.mas_map[x1][y1] == self.mas_map[x1 + 3][y1 + 3]:
                                                    count_d_b += 1
                                                    print('-3', count_d_b)
                                                    if x1 + 4 <= 17 and y1 + 4 <= 17:
                                                        if self.mas_map[x1][y1] == self.mas_map[x1 - 4][y1 - 4] or \
                                                                self.mas_map[x1][y1] == self.mas_map[x1 + 4][y1 + 4]:
                                                            count_d_b += 1
                                                            print('-4', count_d_b)

            if count_d_b == 5:
                print('win!')
                count_d_b = 0
                print(count_d_b)
                self.win_count_b += 1

    def rev_diag(self):
        new_x, new_y = pygame.mouse.get_pos()
        x1 = new_x // (MARGIN + BOX_WIDTH)  # столбец
        y1 = new_y // (MARGIN + BOX_HEIGHT)  # строка

        x = 0
        count_r = 0

        if len(self.new_list) > 0:
            if count_r < 5:
                while x != x1:
                    x += 1
                    continue
                else:
                    for y in self.mas_map[x]:
                        if y != self.mas_map[x1][y1]:
                            continue
                        if x1 + 1 <= 17 and y1 + 1 <= 17:
                            if self.mas_map[x1][y1] == self.mas_map[x1 + 1][y1 - 1] or \
                                    self.mas_map[x1][y1] == self.mas_map[x1 - 1][y1 + 1]:
                                count_r = 2
                                print('+1', count_r)
                                if x1 + 2 <= 17 and y1 + 2 <= 17:
                                    if self.mas_map[x1][y1] == self.mas_map[x1 + 2][y1 - 2] or \
                                            self.mas_map[x1][y1] == self.mas_map[x1 - 2][y1 + 2]:
                                        count_r += 1
                                        print('+2', count_r)
                                        if x1 + 3 <= 17 and y1 + 3 <= 17:
                                            if self.mas_map[x1][y1] == self.mas_map[x1 + 3][y1 - 3] or \
                                                    self.mas_map[x1][y1] == self.mas_map[x1 - 3][y1 + 3]:
                                                count_r += 1
                                                print('+3', count_r)
                                                if x1 + 4 <= 17 and y1 + 4 <= 17:
                                                    if self.mas_map[x1][y1] == self.mas_map[x1 + 4][y1 - 4] or \
                                                            self.mas_map[x1][y1] == self.mas_map[x1 - 4][y1 + 4]:
                                                        count_r += 1
                                                        print('+4', count_r)
            if count_r == 5:
                count_r = 0
                print(count_r)
                print('wiiin')
                self.win_count += 1

    def rev_diag_b(self):
        count_r_b = 0
        if len(self.new_list) > 0:
            if count_r_b < 5:
                for i in self.mas_map:
                    x = self.mas_map.index(i)
                    x1 = x
                    if i.count(2) > 0:
                        for elem in i:
                            y = i.index(elem)
                            y1 = y
                            if elem != 2:
                                continue
                            if x1 + 1 <= 17 and y1 + 1 <= 17:
                                if self.mas_map[x1][y1] == self.mas_map[x1 + 1][y1 - 1] or \
                                        self.mas_map[x1][y1] == self.mas_map[x1 - 1][y1 + 1]:
                                    count_r_b = 2
                                    print('+1', count_r_b)
                                    if x1 + 2 <= 17 and y1 + 2 <= 17:
                                        if self.mas_map[x1][y1] == self.mas_map[x1 + 2][y1 - 2] or \
                                                self.mas_map[x1][y1] == self.mas_map[x1 - 2][y1 + 2]:
                                            count_r_b += 1
                                            print('+2', count_r_b)
                                            if x1 + 3 <= 17 and y1 + 3 <= 17:
                                                if self.mas_map[x1][y1] == self.mas_map[x1 + 3][y1 - 3] or \
                                                        self.mas_map[x1][y1] == self.mas_map[x1 - 3][y1 + 3]:
                                                    count_r_b += 1
                                                    print('+3', count_r_b)
                                                    if x1 + 4 <= 17 and y1 + 4 <= 17:
                                                        if self.mas_map[x1][y1] == self.mas_map[x1 + 4][y1 - 4] or \
                                                                self.mas_map[x1][y1] == self.mas_map[x1 - 4][y1 + 4]:
                                                            count_r_b += 1
                                                            print('+4', count_r_b)
            if count_r_b == 5:
                count_r_b = 0
                print(count_r_b)
                print('wiiin')
                self.win_count_b += 1

    def win(self):  # Win white
        self.rev_diag()
        self.win_ver()
        self.win_hor()
        self.diag()

    def win_black(self):  # Win black
        self.win_hor_b()
        self.win_ver_b()
        self.diag_b()
        self.rev_diag_b()

    def rael_pos(self):
        new_x, new_y = pygame.mouse.get_pos()
        new_col = new_x // (MARGIN + BOX_WIDTH)  # столбец (индекс)
        new_row = new_y // (MARGIN + BOX_HEIGHT)  # строка (индекс)
        if self.mas_map[new_col][new_row] != 0:
            if new_col > 0:
                elem_x = new_col - 1  # проверяем левый элемент
                if self.mas_map[elem_x][new_row] == 0:
                    self.place.extend([[elem_x, new_row]])
            if new_col >= 0:
                elem_x = new_col + 1
                if elem_x <= 17:
                    if self.mas_map[elem_x][new_row] == 0:
                        self.place.extend([[elem_x, new_row]])
                else:
                    return
            if new_row > 0:
                elem_y = new_row - 1
                if self.mas_map[new_col][elem_y] == 0:
                    self.place.extend([[new_col, elem_y]])
            if new_row >= 0:
                elem_y = new_row + 1
                if elem_y <= 17:
                    if self.mas_map[new_col][elem_y] == 0:
                        self.place.extend([[new_col, elem_y]])
                else:
                    return
            # diagonal
            if new_col and new_row > 0:
                elem_x = new_col - 1
                elem_y = new_row + 1
                if self.mas_map[elem_x][elem_y] == 0:
                    self.place.extend([[elem_x, elem_y]])
                elem_y = new_row - 1
                elem_x = new_col - 1
                if self.mas_map[elem_x][elem_y] == 0:
                    self.place.extend([[elem_x, elem_y]])
            if new_col and new_row >= 0:
                elem_x = new_col + 1
                elem_y = new_row - 1
                if self.mas_map[elem_x][elem_y] == 0:
                    self.place.extend([[elem_x, elem_y]])
                elem_x = new_col + 1
                elem_y = new_row + 1
                if self.mas_map[elem_x][elem_y] == 0:
                    self.place.extend([[elem_x, elem_y]])
        return self.place
