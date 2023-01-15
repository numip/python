import pygame
import sys
import time
from settings2 import WIDTH, HEIGHT, FSP, COLOR, COLOR_TEXT, BUSY
from map import Map


class Game:
    """ Задание: Написать программу играющую в ГО-БАН.
    Участвуют два игрока. Каждый получает по 12 шашек. Игрок, получивший белые
    шашки, ставит одну из них на любой из квадратов доски. Затем точно так же выставляется в
    любом месте чѐрная шашка, потом белая и так далее по очереди.
    Цель игры — выставить пять из своих шашек в ряд по прямой линии — горизонтальной,
    вертикальной или по диагонали.
    Когда противники выставили все свои 12 шашек, они по очереди начинают передвигать
    их, стремясь к той же цели — расположить пять своих шашек в ряд по прямой линии.
    Передвигать шашки можно в любую сторону, но только на смежный квадрат, не занятый
    шашкой.
    Каждая получившаяся комбинация из пяти шашек приносит игроку одно очко. Выигрывает игрок, получивший первым 10 очков."""

    def __init__(self):
        pygame.init()
        pygame.display.set_caption('GO-BAN')
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.map = Map()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.map.change_list()
                    self.map.rand_ai()

                elif self.map.win_count == 10:
                    style = pygame.font.SysFont('arial', 30)
                    message = style.render('Поздравляю! Вы победили!', True, COLOR_TEXT)
                    self.screen.blit(message, [WIDTH // 4, HEIGHT // 4])
                    pygame.display.update()
                    time.sleep(5)
                    return False
                elif self.map.win_count_b == 10:
                    style = pygame.font.SysFont('arial', 30)
                    message = style.render('Вы проиграли!', True, COLOR_TEXT)
                    self.screen.blit(message, [WIDTH // 4, HEIGHT // 4])
                    pygame.display.update()
                    time.sleep(5)
                    return False

            pygame.display.update()
            self.screen.fill(COLOR)
            self.map.design_map()
            self.map.show_message(f'White: {self.map.win_count}', BUSY)
            self.map.show_message_b(f'Black: {self.map.win_count_b}', BUSY)
            self.clock.tick(FSP)


if __name__ == '__main__':
    game = Game()
    game.run()
