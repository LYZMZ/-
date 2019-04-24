import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
def run_game():      #开头函数

	#初始化游戏，并创建一个屏幕对象
	pygame.init()                    
	ai_settings=Settings()       
	screen=pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))     
	pygame.display.set_caption("Alien Invasion")

	#创建一艘飞船
	ship=Ship(screen)
	bullets=Group()

	#开始游戏的主循环
	while True:

		#监控键盘和鼠标事件
		gf.check_events(ai_settings,screen,ship,bullets)
		ship.update()
		gf.update_bullets(bullets)




		gf.update_screen(ai_settings,screen,ship,bullets)
run_game()



