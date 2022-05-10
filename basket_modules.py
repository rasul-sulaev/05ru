import sys
from os import listdir
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QLabel, QGridLayout, QMainWindow
from PyQt5 import QtGui
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize


def func_basket_product_1_count_apply_btn(self):
	''' Функция Извемения кол-ва товара №1 '''
	user_products_r = open(self.login_user + '_list_basket.txt', 'r')
	user_products_read = user_products_r.read()
	if ( user_products_read.count(';') == 1 ):
		user_products_read = user_products_read.split(';')
		user_products_r.close()

		user_products_w = open(self.login_user + '_list_basket.txt', 'w')
		user_products_w.write(user_products_read[0].split(':')[0] + ':' + user_products_read[0].split(':')[1] + ':' + user_products_read[0].split(':')[2] + ':' + self.basket_product_1_count.text() + ':' + str( int(user_products_read[0].split(':')[2]) * int(self.basket_product_1_count.text()) ) + ';')
		user_products_w.close()
	elif ( user_products_read.count(';') == 2 ):
		user_products_read = user_products_read.split(';')
		user_products_r.close()

		user_products_w = open(self.login_user + '_list_basket.txt', 'w')
		user_products_w.write(user_products_read[0].split(':')[0] + ':' + user_products_read[0].split(':')[1] + ':' + user_products_read[0].split(':')[2] + ':' + self.basket_product_1_count.text() + ':' + str( int(user_products_read[0].split(':')[2]) * int(self.basket_product_1_count.text()) ) + ';' + user_products_read[1] + ';')
		user_products_w.close()
	elif ( user_products_read.count(';') == 3 ):
		user_products_read = user_products_read.split(';')
		user_products_r.close()

		user_products_w = open(self.login_user + '_list_basket.txt', 'w')
		user_products_w.write(user_products_read[0].split(':')[0] + ':' + user_products_read[0].split(':')[1] + ':' + user_products_read[0].split(':')[2] + ':' + self.basket_product_1_count.text() + ':' + str( int(user_products_read[0].split(':')[2]) * int(self.basket_product_1_count.text()) ) + ';' + user_products_read[1] + ';' + user_products_read[2] + ';')
		user_products_w.close()
	elif ( user_products_read.count(';') == 4 ):
		user_products_read = user_products_read.split(';')
		user_products_r.close()

		user_products_w = open(self.login_user + '_list_basket.txt', 'w')
		user_products_w.write(user_products_read[0].split(':')[0] + ':' + user_products_read[0].split(':')[1] + ':' + user_products_read[0].split(':')[2] + ':' + self.basket_product_1_count.text() + ':' + str( int(user_products_read[0].split(':')[2]) * int(self.basket_product_1_count.text()) ) + ';' + user_products_read[1] + ';' + user_products_read[2] + ';' + user_products_read[3] + ';')
		user_products_w.close()
	elif ( user_products_read.count(';') == 5 ):
		user_products_read = user_products_read.split(';')
		user_products_r.close()

		user_products_w = open(self.login_user + '_list_basket.txt', 'w')
		user_products_w.write(user_products_read[0].split(':')[0] + ':' + user_products_read[0].split(':')[1] + ':' + user_products_read[0].split(':')[2] + ':' + self.basket_product_1_count.text() + ':' + str( int(user_products_read[0].split(':')[2]) * int(self.basket_product_1_count.text()) ) + ';' + user_products_read[1] + ';' + user_products_read[2] + ';' + user_products_read[3] + ';' + user_products_read[4] + ';')
		user_products_w.close()
	elif ( user_products_read.count(';') == 6 ):
		user_products_read = user_products_read.split(';')
		user_products_r.close()

		user_products_w = open(self.login_user + '_list_basket.txt', 'w')
		user_products_w.write(user_products_read[0].split(':')[0] + ':' + user_products_read[0].split(':')[1] + ':' + user_products_read[0].split(':')[2] + ':' + self.basket_product_1_count.text() + ':' + str( int(user_products_read[0].split(':')[2]) * int(self.basket_product_1_count.text()) ) + ';' + user_products_read[1] + ';' + ';' + user_products_read[2] + ';' + user_products_read[3] + ';' + user_products_read[4] + ';' + user_products_read[5] + ';')
		user_products_w.close()
	elif ( user_products_read.count(';') == 7 ):
		user_products_read = user_products_read.split(';')
		user_products_r.close()

		user_products_w = open(self.login_user + '_list_basket.txt', 'w')
		user_products_w.write(user_products_read[0].split(':')[0] + ':' + user_products_read[0].split(':')[1] + ':' + user_products_read[0].split(':')[2] + ':' + self.basket_product_1_count.text() + ':' + str( int(user_products_read[0].split(':')[2]) * int(self.basket_product_1_count.text()) ) + ';' + user_products_read[1] + ';' + user_products_read[2] + ';' + user_products_read[3] + ';' + user_products_read[4] + ';' + user_products_read[5] + ';' + user_products_read[6] + ';')
		user_products_w.close()
	elif ( user_products_read.count(';') == 8 ):
		user_products_read = user_products_read.split(';')
		user_products_r.close()

		user_products_w = open(self.login_user + '_list_basket.txt', 'w')
		user_products_w.write(user_products_read[0].split(':')[0] + ':' + user_products_read[0].split(':')[1] + ':' + user_products_read[0].split(':')[2] + ':' + self.basket_product_1_count.text() + ':' + str( int(user_products_read[0].split(':')[2]) * int(self.basket_product_1_count.text()) ) + ';' + user_products_read[1] + ';' + user_products_read[2] + ';' + user_products_read[3] + ';' + user_products_read[4] + ';' + user_products_read[5] + ';' + user_products_read[6] + ';' + user_products_read[7] + ';')
		user_products_w.close()
	elif ( user_products_read.count(';') == 9 ):
		user_products_read = user_products_read.split(';')
		user_products_r.close()

		user_products_w = open(self.login_user + '_list_basket.txt', 'w')
		user_products_w.write(user_products_read[0].split(':')[0] + ':' + user_products_read[0].split(':')[1] + ':' + user_products_read[0].split(':')[2] + ':' + self.basket_product_1_count.text() + ':' + str( int(user_products_read[0].split(':')[2]) * int(self.basket_product_1_count.text()) ) + ';' + user_products_read[1] + ';' + user_products_read[2] + ';' + user_products_read[3] + ';' + user_products_read[4] + ';' + user_products_read[5] + ';' + user_products_read[6] + ';' + user_products_read[7] + ';' + user_products_read[8] + ';')
		user_products_w.close()
	elif ( user_products_read.count(';') == 10 ):
		user_products_read = user_products_read.split(';')
		user_products_r.close()

		user_products_w = open(self.login_user + '_list_basket.txt', 'w')
		user_products_w.write(user_products_read[0].split(':')[0] + ':' + user_products_read[0].split(':')[1] + ':' + user_products_read[0].split(':')[2] + ':' + self.basket_product_1_count.text() + ':' + str( int(user_products_read[0].split(':')[2]) * int(self.basket_product_1_count.text()) ) + ';' + user_products_read[1] + ';' + user_products_read[2] + ';' + user_products_read[3] + ';' + user_products_read[4] + ';' + user_products_read[5] + ';' + user_products_read[6] + ';' + user_products_read[7] + ';' + user_products_read[8] + ';' + user_products_read[9] + ';')
		user_products_w.close()
	self.basket_big_window()


def func_basket_product_2_count_apply_btn(self):
	''' Функция Извемения кол-ва товара №2 '''
	user_products_r = open(self.login_user + '_list_basket.txt', 'r')
	user_products_read = user_products_r.read()
	if ( user_products_read.count(';') == 2 ):
		user_products_read = user_products_read.split(';')
		user_products_r.close()

		user_products_w = open(self.login_user + '_list_basket.txt', 'w')
		user_products_w.write(user_products_read[0] + ';' + user_products_read[1].split(':')[0] + ':' + user_products_read[1].split(':')[1] + ':' + user_products_read[1].split(':')[2] + ':' + self.basket_product_2_count.text() + ':' + str( int(user_products_read[1].split(':')[2]) * int(self.basket_product_2_count.text()) ) + ';')
		user_products_w.close()
	elif ( user_products_read.count(';') == 3 ):
		user_products_read = user_products_read.split(';')
		user_products_r.close()

		user_products_w = open(self.login_user + '_list_basket.txt', 'w')
		user_products_w.write(user_products_read[0] + ';' + user_products_read[1].split(':')[0] + ':' + user_products_read[1].split(':')[1] + ':' + user_products_read[1].split(':')[2] + ':' + self.basket_product_2_count.text() + ':' + str( int(user_products_read[1].split(':')[2]) * int(self.basket_product_2_count.text()) ) + ';' + user_products_read[2] + ';')
		user_products_w.close()
	elif ( user_products_read.count(';') == 4 ):
		user_products_read = user_products_read.split(';')
		user_products_r.close()

		user_products_w = open(self.login_user + '_list_basket.txt', 'w')
		user_products_w.write(user_products_read[0] + ';' + user_products_read[1].split(':')[0] + ':' + user_products_read[1].split(':')[1] + ':' + user_products_read[1].split(':')[2] + ':' + self.basket_product_2_count.text() + ':' + str( int(user_products_read[1].split(':')[2]) * int(self.basket_product_2_count.text()) ) + ';' + user_products_read[2] + ';' + user_products_read[3] + ';')
		user_products_w.close()
	elif ( user_products_read.count(';') == 5 ):
		user_products_read = user_products_read.split(';')
		user_products_r.close()

		user_products_w = open(self.login_user + '_list_basket.txt', 'w')
		user_products_w.write(user_products_read[0] + ';' + user_products_read[1].split(':')[0] + ':' + user_products_read[1].split(':')[1] + ':' + user_products_read[1].split(':')[2] + ':' + self.basket_product_2_count.text() + ':' + str( int(user_products_read[1].split(':')[2]) * int(self.basket_product_2_count.text()) ) + ';' + user_products_read[2] + ';' + user_products_read[3] + ';' + user_products_read[4] + ';')
		user_products_w.close()
	elif ( user_products_read.count(';') == 6 ):
		user_products_read = user_products_read.split(';')
		user_products_r.close()

		user_products_w = open(self.login_user + '_list_basket.txt', 'w')
		user_products_w.write(user_products_read[0] + ';' + user_products_read[1].split(':')[0] + ':' + user_products_read[1].split(':')[1] + ':' + user_products_read[1].split(':')[2] + ':' + self.basket_product_2_count.text() + ':' + str( int(user_products_read[1].split(':')[2]) * int(self.basket_product_2_count.text()) ) + ';' + user_products_read[2] + ';' + user_products_read[3] + ';' + user_products_read[4] + ';' + user_products_read[5] + ';')
		user_products_w.close()
	elif ( user_products_read.count(';') == 7 ):
		user_products_read = user_products_read.split(';')
		user_products_r.close()

		user_products_w = open(self.login_user + '_list_basket.txt', 'w')
		user_products_w.write(user_products_read[0] + ';' + user_products_read[1].split(':')[0] + ':' + user_products_read[1].split(':')[1] + ':' + user_products_read[1].split(':')[2] + ':' + self.basket_product_2_count.text() + ':' + str( int(user_products_read[1].split(':')[2]) * int(self.basket_product_2_count.text()) ) + ';' + user_products_read[2] + ';' + user_products_read[3] + ';' + user_products_read[4] + ';' + user_products_read[5] + ';' + user_products_read[6] + ';')
		user_products_w.close()
	elif ( user_products_read.count(';') == 8 ):
		user_products_read = user_products_read.split(';')
		user_products_r.close()

		user_products_w = open(self.login_user + '_list_basket.txt', 'w')
		user_products_w.write(user_products_read[0] + ';' + user_products_read[1].split(':')[0] + ':' + user_products_read[1].split(':')[1] + ':' + user_products_read[1].split(':')[2] + ':' + self.basket_product_2_count.text() + ':' + str( int(user_products_read[1].split(':')[2]) * int(self.basket_product_2_count.text()) ) + ';' + user_products_read[2] + ';' + user_products_read[3] + ';' + user_products_read[4] + ';' + user_products_read[5] + ';' + user_products_read[6] + ';' + user_products_read[7] + ';')
		user_products_w.close()
	elif ( user_products_read.count(';') == 9 ):
		user_products_read = user_products_read.split(';')
		user_products_r.close()

		user_products_w = open(self.login_user + '_list_basket.txt', 'w')
		user_products_w.write(user_products_read[0] + ';' + user_products_read[1].split(':')[0] + ':' + user_products_read[1].split(':')[1] + ':' + user_products_read[1].split(':')[2] + ':' + self.basket_product_2_count.text() + ':' + str( int(user_products_read[1].split(':')[2]) * int(self.basket_product_2_count.text()) ) + ';' + user_products_read[2] + ';' + user_products_read[3] + ';' + user_products_read[4] + ';' + user_products_read[5] + ';' + user_products_read[6] + ';' + user_products_read[7] + ';' + user_products_read[8] + ';')
		user_products_w.close()
	elif ( user_products_read.count(';') == 10 ):
		user_products_read = user_products_read.split(';')
		user_products_r.close()

		user_products_w = open(self.login_user + '_list_basket.txt', 'w')
		user_products_w.write(user_products_read[0] + ';' + user_products_read[1].split(':')[0] + ':' + user_products_read[1].split(':')[1] + ':' + user_products_read[1].split(':')[2] + ':' + self.basket_product_2_count.text() + ':' + str( int(user_products_read[1].split(':')[2]) * int(self.basket_product_2_count.text()) ) + ';' + user_products_read[2] + ';' + user_products_read[3] + ';' + user_products_read[4] + ';' + user_products_read[5] + ';' + user_products_read[6] + ';' + user_products_read[7] + ';' + user_products_read[8] + ';' + user_products_read[9] + ';')
		user_products_w.close()
	self.basket_big_window()


def func_basket_product_3_count_apply_btn(self):
	''' Функция Извемения кол-ва товара №2 '''
	user_products_r = open(self.login_user + '_list_basket.txt', 'r')
	user_products_read = user_products_r.read()
	if ( user_products_read.count(';') == 3 ):
		user_products_read = user_products_read.split(';')
		user_products_r.close()

		user_products_w = open(self.login_user + '_list_basket.txt', 'w')
		user_products_w.write(user_products_read[0] + ';' + user_products_read[1] + ';' + user_products_read[2].split(':')[0] + ':' + user_products_read[2].split(':')[1] + ':' + user_products_read[2].split(':')[2] + ':' + self.basket_product_3_count.text() + ':' + str( int(user_products_read[2].split(':')[2]) * int(self.basket_product_3_count.text()) ) + ';')
		user_products_w.close()
	elif ( user_products_read.count(';') == 4 ):
		user_products_read = user_products_read.split(';')
		user_products_r.close()

		user_products_w = open(self.login_user + '_list_basket.txt', 'w')
		user_products_w.write(user_products_read[0] + ';' + user_products_read[1] + ';' + user_products_read[2].split(':')[0] + ':' + user_products_read[2].split(':')[1] + ':' + user_products_read[2].split(':')[2] + ':' + self.basket_product_3_count.text() + ':' + str( int(user_products_read[2].split(':')[2]) * int(self.basket_product_3_count.text()) ) + ';' + user_products_read[3] + ';')
		user_products_w.close()
	elif ( user_products_read.count(';') == 5 ):
		user_products_read = user_products_read.split(';')
		user_products_r.close()

		user_products_w = open(self.login_user + '_list_basket.txt', 'w')
		user_products_w.write(user_products_read[0] + ';' + user_products_read[1] + ';' + user_products_read[2].split(':')[0] + ':' + user_products_read[2].split(':')[1] + ':' + user_products_read[2].split(':')[2] + ':' + self.basket_product_3_count.text() + ':' + str( int(user_products_read[2].split(':')[2]) * int(self.basket_product_3_count.text()) ) + ';' + user_products_read[3] + ';' + user_products_read[4] + ';')
		user_products_w.close()
	elif ( user_products_read.count(';') == 6 ):
		user_products_read = user_products_read.split(';')
		user_products_r.close()

		user_products_w = open(self.login_user + '_list_basket.txt', 'w')
		user_products_w.write(user_products_read[0] + ';' + user_products_read[1] + ';' + user_products_read[2].split(':')[0] + ':' + user_products_read[2].split(':')[1] + ':' + user_products_read[2].split(':')[2] + ':' + self.basket_product_3_count.text() + ':' + str( int(user_products_read[2].split(':')[2]) * int(self.basket_product_3_count.text()) ) + ';' + user_products_read[3] + ';' + user_products_read[4] + ';' + user_products_read[5] + ';')
		user_products_w.close()
	elif ( user_products_read.count(';') == 7 ):
		user_products_read = user_products_read.split(';')
		user_products_r.close()

		user_products_w = open(self.login_user + '_list_basket.txt', 'w')
		user_products_w.write(user_products_read[0] + ';' + user_products_read[1] + ';' + user_products_read[2].split(':')[0] + ':' + user_products_read[2].split(':')[1] + ':' + user_products_read[2].split(':')[2] + ':' + self.basket_product_3_count.text() + ':' + str( int(user_products_read[2].split(':')[2]) * int(self.basket_product_3_count.text()) ) + ';' + user_products_read[3] + ';' + user_products_read[4] + ';' + user_products_read[5] + ';' + user_products_read[6] + ';')
		user_products_w.close()
	elif ( user_products_read.count(';') == 8 ):
		user_products_read = user_products_read.split(';')
		user_products_r.close()

		user_products_w = open(self.login_user + '_list_basket.txt', 'w')
		user_products_w.write(user_products_read[0] + ';' + user_products_read[1] + ';' + user_products_read[2].split(':')[0] + ':' + user_products_read[2].split(':')[1] + ':' + user_products_read[2].split(':')[2] + ':' + self.basket_product_3_count.text() + ':' + str( int(user_products_read[2].split(':')[2]) * int(self.basket_product_3_count.text()) ) + ';' + user_products_read[3] + ';' + user_products_read[4] + ';' + user_products_read[5] + ';' + user_products_read[6] + ';' + user_products_read[7] + ';')
		user_products_w.close()
	elif ( user_products_read.count(';') == 9 ):
		user_products_read = user_products_read.split(';')
		user_products_r.close()

		user_products_w = open(self.login_user + '_list_basket.txt', 'w')
		user_products_w.write(user_products_read[0] + ';' + user_products_read[1] + ';' + user_products_read[2].split(':')[0] + ':' + user_products_read[2].split(':')[1] + ':' + user_products_read[2].split(':')[2] + ':' + self.basket_product_3_count.text() + ':' + str( int(user_products_read[2].split(':')[2]) * int(self.basket_product_3_count.text()) ) + ';' + user_products_read[3] + ';' + user_products_read[4] + ';' + user_products_read[5] + ';' + user_products_read[6] + ';' + user_products_read[7] + ';' + user_products_read[8] + ';')
		user_products_w.close()
	elif ( user_products_read.count(';') == 10 ):
		user_products_read = user_products_read.split(';')
		user_products_r.close()

		user_products_w = open(self.login_user + '_list_basket.txt', 'w')
		user_products_w.write(user_products_read[0] + ';' + user_products_read[1] + ';' + user_products_read[2].split(':')[0] + ':' + user_products_read[2].split(':')[1] + ':' + user_products_read[2].split(':')[2] + ':' + self.basket_product_3_count.text() + ':' + str( int(user_products_read[2].split(':')[2]) * int(self.basket_product_3_count.text()) ) + ';' + user_products_read[3] + ';' + user_products_read[4] + ';' + user_products_read[5] + ';' + user_products_read[6] + ';' + user_products_read[7] + ';' + user_products_read[8] + ';' + user_products_read[9] + ';')
		user_products_w.close()
	self.basket_big_window()


def func_basket_product_4_count_apply_btn(self):
	''' Функция Извемения кол-ва товара №4 '''
	user_products_r = open(self.login_user + '_list_basket.txt', 'r')
	user_products_read = user_products_r.read()
	if ( user_products_read.count(';') == 4 ):
		user_products_read = user_products_read.split(';')
		user_products_r.close()

		user_products_w = open(self.login_user + '_list_basket.txt', 'w')
		user_products_w.write(user_products_read[0] + ';' + user_products_read[1] + ';' + user_products_read[2] + ';' + user_products_read[3].split(':')[0] + ':' + user_products_read[3].split(':')[1] + ':' + user_products_read[3].split(':')[2] + ':' + self.basket_product_4_count.text() + ':' + str( int(user_products_read[3].split(':')[2]) * int(self.basket_product_4_count.text()) ) + ';')
		user_products_w.close()
	elif ( user_products_read.count(';') == 5 ):
		user_products_read = user_products_read.split(';')
		user_products_r.close()

		user_products_w = open(self.login_user + '_list_basket.txt', 'w')
		user_products_w.write(user_products_read[0] + ';' + user_products_read[1] + ';' + user_products_read[2] + ';' + user_products_read[3].split(':')[0] + ':' + user_products_read[3].split(':')[1] + ':' + user_products_read[3].split(':')[2] + ':' + self.basket_product_4_count.text() + ':' + str( int(user_products_read[3].split(':')[2]) * int(self.basket_product_4_count.text()) ) + ';' + user_products_read[4] + ';')
		user_products_w.close()
	elif ( user_products_read.count(';') == 6 ):
		user_products_read = user_products_read.split(';')
		user_products_r.close()

		user_products_w = open(self.login_user + '_list_basket.txt', 'w')
		user_products_w.write(user_products_read[0] + ';' + user_products_read[1] + ';' + user_products_read[2] + ';' + user_products_read[3].split(':')[0] + ':' + user_products_read[3].split(':')[1] + ':' + user_products_read[3].split(':')[2] + ':' + self.basket_product_4_count.text() + ':' + str( int(user_products_read[3].split(':')[2]) * int(self.basket_product_4_count.text()) ) + ';' + user_products_read[4] + ';' + user_products_read[5] + ';')
		user_products_w.close()
	elif ( user_products_read.count(';') == 7 ):
		user_products_read = user_products_read.split(';')
		user_products_r.close()

		user_products_w = open(self.login_user + '_list_basket.txt', 'w')
		user_products_w.write(user_products_read[0] + ';' + user_products_read[1] + ';' + user_products_read[2] + ';' + user_products_read[3].split(':')[0] + ':' + user_products_read[3].split(':')[1] + ':' + user_products_read[3].split(':')[2] + ':' + self.basket_product_4_count.text() + ':' + str( int(user_products_read[3].split(':')[2]) * int(self.basket_product_4_count.text()) ) + ';' + user_products_read[4] + ';' + user_products_read[5] + ';' + user_products_read[6] + ';')
		user_products_w.close()
	elif ( user_products_read.count(';') == 8 ):
		user_products_read = user_products_read.split(';')
		user_products_r.close()

		user_products_w = open(self.login_user + '_list_basket.txt', 'w')
		user_products_w.write(user_products_read[0] + ';' + user_products_read[1] + ';' + user_products_read[2] + ';' + user_products_read[3].split(':')[0] + ':' + user_products_read[3].split(':')[1] + ':' + user_products_read[3].split(':')[2] + ':' + self.basket_product_4_count.text() + ':' + str( int(user_products_read[3].split(':')[2]) * int(self.basket_product_4_count.text()) ) + ';' + user_products_read[4] + ';' + user_products_read[5] + ';' + user_products_read[6] + ';' + user_products_read[7] + ';')
		user_products_w.close()
	elif ( user_products_read.count(';') == 9 ):
		user_products_read = user_products_read.split(';')
		user_products_r.close()

		user_products_w = open(self.login_user + '_list_basket.txt', 'w')
		user_products_w.write(user_products_read[0] + ';' + user_products_read[1] + ';' + user_products_read[2] + ';' + user_products_read[3].split(':')[0] + ':' + user_products_read[3].split(':')[1] + ':' + user_products_read[3].split(':')[2] + ':' + self.basket_product_4_count.text() + ':' + str( int(user_products_read[3].split(':')[2]) * int(self.basket_product_4_count.text()) ) + ';' + user_products_read[4] + ';' + user_products_read[5] + ';' + user_products_read[6] + ';' + user_products_read[7] + ';' + user_products_read[8] + ';')
		user_products_w.close()
	elif ( user_products_read.count(';') == 10 ):
		user_products_read = user_products_read.split(';')
		user_products_r.close()

		user_products_w = open(self.login_user + '_list_basket.txt', 'w')
		user_products_w.write(user_products_read[0] + ';' + user_products_read[1] + ';' + user_products_read[2] + ';' + user_products_read[3].split(':')[0] + ':' + user_products_read[3].split(':')[1] + ':' + user_products_read[3].split(':')[2] + ':' + self.basket_product_4_count.text() + ':' + str( int(user_products_read[3].split(':')[2]) * int(self.basket_product_4_count.text()) ) + ';' + user_products_read[4] + ';' + user_products_read[5] + ';' + user_products_read[6] + ';' + user_products_read[7] + ';' + user_products_read[8] + ';' + user_products_read[9] + ';')
		user_products_w.close()
	self.basket_big_window()


def func_basket_product_5_count_apply_btn(self):
	''' Функция Извемения кол-ва товара №4 '''
	user_products_r = open(self.login_user + '_list_basket.txt', 'r')
	user_products_read = user_products_r.read()
	if ( user_products_read.count(';') == 5 ):
		user_products_read = user_products_read.split(';')
		user_products_r.close()

		user_products_w = open(self.login_user + '_list_basket.txt', 'w')
		user_products_w.write(user_products_read[0] + ';' + user_products_read[1] + ';' + user_products_read[2] + ';' + user_products_read[3] + ';' + user_products_read[4].split(':')[0] + ':' + user_products_read[4].split(':')[1] + ':' + user_products_read[4].split(':')[2] + ':' + self.basket_product_5_count.text() + ':' + str( int(user_products_read[4].split(':')[2]) * int(self.basket_product_5_count.text()) ) + ';')
		user_products_w.close()
	elif ( user_products_read.count(';') == 6 ):
		user_products_read = user_products_read.split(';')
		user_products_r.close()

		user_products_w = open(self.login_user + '_list_basket.txt', 'w')
		user_products_w.write(user_products_read[0] + ';' + user_products_read[1] + ';' + user_products_read[2] + ';' + user_products_read[3] + ';' + user_products_read[4].split(':')[0] + ':' + user_products_read[4].split(':')[1] + ':' + user_products_read[4].split(':')[2] + ':' + self.basket_product_5_count.text() + ':' + str( int(user_products_read[4].split(':')[2]) * int(self.basket_product_5_count.text()) ) + ';' + user_products_read[5] + ';')
		user_products_w.close()
	elif ( user_products_read.count(';') == 7 ):
		user_products_read = user_products_read.split(';')
		user_products_r.close()

		user_products_w = open(self.login_user + '_list_basket.txt', 'w')
		user_products_w.write(user_products_read[0] + ';' + user_products_read[1] + ';' + user_products_read[2] + ';' + user_products_read[3] + ';' + user_products_read[4].split(':')[0] + ':' + user_products_read[4].split(':')[1] + ':' + user_products_read[4].split(':')[2] + ':' + self.basket_product_5_count.text() + ':' + str( int(user_products_read[4].split(':')[2]) * int(self.basket_product_5_count.text()) ) + ';' + user_products_read[5] + ';' + user_products_read[6] + ';')
		user_products_w.close()
	elif ( user_products_read.count(';') == 8 ):
		user_products_read = user_products_read.split(';')
		user_products_r.close()

		user_products_w = open(self.login_user + '_list_basket.txt', 'w')
		user_products_w.write(user_products_read[0] + ';' + user_products_read[1] + ';' + user_products_read[2] + ';' + user_products_read[3] + ';' + user_products_read[4].split(':')[0] + ':' + user_products_read[4].split(':')[1] + ':' + user_products_read[4].split(':')[2] + ':' + self.basket_product_5_count.text() + ':' + str( int(user_products_read[4].split(':')[2]) * int(self.basket_product_5_count.text()) ) + ';' + user_products_read[5] + ';' + user_products_read[6] + ';' + user_products_read[7] + ';')
		user_products_w.close()
	elif ( user_products_read.count(';') == 9 ):
		user_products_read = user_products_read.split(';')
		user_products_r.close()

		user_products_w = open(self.login_user + '_list_basket.txt', 'w')
		user_products_w.write(user_products_read[0] + ';' + user_products_read[1] + ';' + user_products_read[2] + ';' + user_products_read[3] + ';' + user_products_read[4].split(':')[0] + ':' + user_products_read[4].split(':')[1] + ':' + user_products_read[4].split(':')[2] + ':' + self.basket_product_5_count.text() + ':' + str( int(user_products_read[4].split(':')[2]) * int(self.basket_product_5_count.text()) ) + ';' + user_products_read[5] + ';' + user_products_read[6] + ';' + user_products_read[7] + ';' + user_products_read[8] + ';')
		user_products_w.close()
	elif ( user_products_read.count(';') == 10 ):
		user_products_read = user_products_read.split(';')
		user_products_r.close()

		user_products_w = open(self.login_user + '_list_basket.txt', 'w')
		user_products_w.write(user_products_read[0] + ';' + user_products_read[1] + ';' + user_products_read[2] + ';' + user_products_read[3] + ';' + user_products_read[4].split(':')[0] + ':' + user_products_read[4].split(':')[1] + ':' + user_products_read[4].split(':')[2] + ':' + self.basket_product_5_count.text() + ':' + str( int(user_products_read[4].split(':')[2]) * int(self.basket_product_5_count.text()) ) + ';' + user_products_read[5] + ';' + user_products_read[6] + ';' + user_products_read[7] + ';' + user_products_read[8] + ';' + user_products_read[9] + ';')
		user_products_w.close()
	self.basket_big_window()


def func_basket_product_6_count_apply_btn(self):
	''' Функция Извемения кол-ва товара №4 '''
	user_products_r = open(self.login_user + '_list_basket.txt', 'r')
	user_products_read = user_products_r.read()
	if ( user_products_read.count(';') == 6 ):
		user_products_read = user_products_read.split(';')
		user_products_r.close()

		user_products_w = open(self.login_user + '_list_basket.txt', 'w')
		user_products_w.write(user_products_read[0] + ';' + user_products_read[1] + ';' + user_products_read[2] + ';' + user_products_read[3] + ';'+ user_products_read[4] + ';' + user_products_read[5].split(':')[0] + ':' + user_products_read[5].split(':')[1] + ':' + user_products_read[5].split(':')[2] + ':' + self.basket_product_6_count.text() + ':' + str( int(user_products_read[5].split(':')[2]) * int(self.basket_product_6_count.text()) ) + ';')
		user_products_w.close()
	elif ( user_products_read.count(';') == 7 ):
		user_products_read = user_products_read.split(';')
		user_products_r.close()

		user_products_w = open(self.login_user + '_list_basket.txt', 'w')
		user_products_w.write(user_products_read[0] + ';' + user_products_read[1] + ';' + user_products_read[2] + ';' + user_products_read[3] + ';'+ user_products_read[4] + ';' + user_products_read[5].split(':')[0] + ':' + user_products_read[5].split(':')[1] + ':' + user_products_read[5].split(':')[2] + ':' + self.basket_product_6_count.text() + ':' + str( int(user_products_read[5].split(':')[2]) * int(self.basket_product_6_count.text()) ) + ';' + user_products_read[6] + ';')
		user_products_w.close()
	elif ( user_products_read.count(';') == 8 ):
		user_products_read = user_products_read.split(';')
		user_products_r.close()

		user_products_w = open(self.login_user + '_list_basket.txt', 'w')
		user_products_w.write(user_products_read[0] + ';' + user_products_read[1] + ';' + user_products_read[2] + ';' + user_products_read[3] + ';'+ user_products_read[4] + ';' + user_products_read[5].split(':')[0] + ':' + user_products_read[5].split(':')[1] + ':' + user_products_read[5].split(':')[2] + ':' + self.basket_product_6_count.text() + ':' + str( int(user_products_read[5].split(':')[2]) * int(self.basket_product_6_count.text()) ) + ';' + user_products_read[6] + ';' + user_products_read[7] + ';')
		user_products_w.close()
	elif ( user_products_read.count(';') == 9 ):
		user_products_read = user_products_read.split(';')
		user_products_r.close()

		user_products_w = open(self.login_user + '_list_basket.txt', 'w')
		user_products_w.write(user_products_read[0] + ';' + user_products_read[1] + ';' + user_products_read[2] + ';' + user_products_read[3] + ';'+ user_products_read[4] + ';' + user_products_read[5].split(':')[0] + ':' + user_products_read[5].split(':')[1] + ':' + user_products_read[5].split(':')[2] + ':' + self.basket_product_6_count.text() + ':' + str( int(user_products_read[5].split(':')[2]) * int(self.basket_product_6_count.text()) ) + ';' + user_products_read[6] + ';' + user_products_read[7] + ';' + user_products_read[8] + ';')
		user_products_w.close()
	elif ( user_products_read.count(';') == 10 ):
		user_products_read = user_products_read.split(';')
		user_products_r.close()

		user_products_w = open(self.login_user + '_list_basket.txt', 'w')
		user_products_w.write(user_products_read[0] + ';' + user_products_read[1] + ';' + user_products_read[2] + ';' + user_products_read[3] + ';'+ user_products_read[4] + ';' + user_products_read[5].split(':')[0] + ':' + user_products_read[5].split(':')[1] + ':' + user_products_read[5].split(':')[2] + ':' + self.basket_product_6_count.text() + ':' + str( int(user_products_read[5].split(':')[2]) * int(self.basket_product_6_count.text()) ) + ';' + user_products_read[6] + ';' + user_products_read[7] + ';' + user_products_read[8] + ';' + user_products_read[9] + ';')
		user_products_w.close()
	self.basket_big_window()


def func_basket_product_7_count_apply_btn(self):
	''' Функция Извемения кол-ва товара №4 '''
	user_products_r = open(self.login_user + '_list_basket.txt', 'r')
	user_products_read = user_products_r.read()
	if ( user_products_read.count(';') == 7 ):
		user_products_read = user_products_read.split(';')
		user_products_r.close()

		user_products_w = open(self.login_user + '_list_basket.txt', 'w')
		user_products_w.write(user_products_read[0] + ';' + user_products_read[1] + ';' + user_products_read[2] + ';' + user_products_read[3] + ';' + user_products_read[4] + ';' + user_products_read[5] + ';' + user_products_read[6].split(':')[0] + ':' + user_products_read[6].split(':')[1] + ':' + user_products_read[6].split(':')[2] + ':' + self.basket_product_7_count.text() + ':' + str( int(user_products_read[6].split(':')[2]) * int(self.basket_product_7_count.text()) ) + ';')
		user_products_w.close()
	elif ( user_products_read.count(';') == 8 ):
		user_products_read = user_products_read.split(';')
		user_products_r.close()

		user_products_w = open(self.login_user + '_list_basket.txt', 'w')
		user_products_w.write(user_products_read[0] + ';' + user_products_read[1] + ';' + user_products_read[2] + ';' + user_products_read[3] + ';' + user_products_read[4] + ';' + user_products_read[5] + ';' + user_products_read[6].split(':')[0] + ':' + user_products_read[6].split(':')[1] + ':' + user_products_read[6].split(':')[2] + ':' + self.basket_product_7_count.text() + ':' + str( int(user_products_read[6].split(':')[2]) * int(self.basket_product_7_count.text()) ) + ';' + user_products_read[7] + ';')
		user_products_w.close()
	elif ( user_products_read.count(';') == 9 ):
		user_products_read = user_products_read.split(';')
		user_products_r.close()

		user_products_w = open(self.login_user + '_list_basket.txt', 'w')
		user_products_w.write(user_products_read[0] + ';' + user_products_read[1] + ';' + user_products_read[2] + ';' + user_products_read[3] + ';' + user_products_read[4] + ';' + user_products_read[5] + ';' + user_products_read[6].split(':')[0] + ':' + user_products_read[6].split(':')[1] + ':' + user_products_read[6].split(':')[2] + ':' + self.basket_product_7_count.text() + ':' + str( int(user_products_read[6].split(':')[2]) * int(self.basket_product_7_count.text()) ) + ';' + user_products_read[7] + ';' + user_products_read[8] + ';')
		user_products_w.close()
	elif ( user_products_read.count(';') == 10 ):
		user_products_read = user_products_read.split(';')
		user_products_r.close()

		user_products_w = open(self.login_user + '_list_basket.txt', 'w')
		user_products_w.write(user_products_read[0] + ';' + user_products_read[1] + ';' + user_products_read[2] + ';' + user_products_read[3] + ';' + user_products_read[4] + ';' + user_products_read[5] + ';' + user_products_read[6].split(':')[0] + ':' + user_products_read[6].split(':')[1] + ':' + user_products_read[6].split(':')[2] + ':' + self.basket_product_7_count.text() + ':' + str( int(user_products_read[6].split(':')[2]) * int(self.basket_product_7_count.text()) ) + ';' + user_products_read[7] + ';' + user_products_read[8] + ';' + user_products_read[9] + ';')
		user_products_w.close()
	self.basket_big_window()


def func_basket_product_8_count_apply_btn(self):
	''' Функция Извемения кол-ва товара №4 '''
	user_products_r = open(self.login_user + '_list_basket.txt', 'r')
	user_products_read = user_products_r.read()
	if ( user_products_read.count(';') == 8 ):
		user_products_read = user_products_read.split(';')
		user_products_r.close()

		user_products_w = open(self.login_user + '_list_basket.txt', 'w')
		user_products_w.write(user_products_read[0] + ';' + user_products_read[1] + ';' + user_products_read[2] + ';' + user_products_read[3] + ';' + user_products_read[4] + ';' + user_products_read[5] + ';' + user_products_read[6] + ';' + user_products_read[7].split(':')[0] + ':' + user_products_read[7].split(':')[1] + ':' + user_products_read[7].split(':')[2] + ':' + self.basket_product_8_count.text() + ':' + str( int(user_products_read[7].split(':')[2]) * int(self.basket_product_8_count.text()) ) + ';')
		user_products_w.close()
	elif ( user_products_read.count(';') == 9 ):
		user_products_read = user_products_read.split(';')
		user_products_r.close()

		user_products_w = open(self.login_user + '_list_basket.txt', 'w')
		user_products_w.write(user_products_read[0] + ';' + user_products_read[1] + ';' + user_products_read[2] + ';' + user_products_read[3] + ';' + user_products_read[4] + ';' + user_products_read[5] + ';' + user_products_read[6] + ';' + user_products_read[7].split(':')[0] + ':' + user_products_read[7].split(':')[1] + ':' + user_products_read[7].split(':')[2] + ':' + self.basket_product_8_count.text() + ':' + str( int(user_products_read[7].split(':')[2]) * int(self.basket_product_8_count.text()) ) + ';' + user_products_read[8] + ';')
		user_products_w.close()
	elif ( user_products_read.count(';') == 10 ):
		user_products_read = user_products_read.split(';')
		user_products_r.close()

		user_products_w = open(self.login_user + '_list_basket.txt', 'w')
		user_products_w.write(user_products_read[0] + ';' + user_products_read[1] + ';' + user_products_read[2] + ';' + user_products_read[3] + ';' + user_products_read[4] + ';' + user_products_read[5] + ';' + user_products_read[6] + ';' + user_products_read[7].split(':')[0] + ':' + user_products_read[7].split(':')[1] + ':' + user_products_read[7].split(':')[2] + ':' + self.basket_product_8_count.text() + ':' + str( int(user_products_read[7].split(':')[2]) * int(self.basket_product_8_count.text()) ) + ';' + user_products_read[8] + ';' + user_products_read[9] + ';')
		user_products_w.close()
	self.basket_big_window()


def func_basket_product_9_count_apply_btn(self):
	''' Функция Извемения кол-ва товара №4 '''
	user_products_r = open(self.login_user + '_list_basket.txt', 'r')
	user_products_read = user_products_r.read()
	if ( user_products_read.count(';') == 9 ):
		user_products_read = user_products_read.split(';')
		user_products_r.close()

		user_products_w = open(self.login_user + '_list_basket.txt', 'w')
		user_products_w.write(user_products_read[0] + ';' + user_products_read[1] + ';' + user_products_read[2] + ';' + user_products_read[3] + ';' + user_products_read[4] + ';' + user_products_read[5] + ';' + user_products_read[6] + ';' + user_products_read[7] + ';' + user_products_read[8].split(':')[0] + ':' + user_products_read[8].split(':')[1] + ':' + user_products_read[8].split(':')[2] + ':' + self.basket_product_9_count.text() + ':' + str( int(user_products_read[8].split(':')[2]) * int(self.basket_product_9_count.text()) ) + ';')
		user_products_w.close()
	elif ( user_products_read.count(';') == 10 ):
		user_products_read = user_products_read.split(';')
		user_products_r.close()

		user_products_w = open(self.login_user + '_list_basket.txt', 'w')
		user_products_w.write(user_products_read[0] + ';' + user_products_read[1] + ';' + user_products_read[2] + ';' + user_products_read[3] + ';' + user_products_read[4] + ';' + user_products_read[5] + ';' + user_products_read[6] + ';' + user_products_read[7] + ';' + user_products_read[8].split(':')[0] + ':' + user_products_read[8].split(':')[1] + ':' + user_products_read[8].split(':')[2] + ':' + self.basket_product_9_count.text() + ':' + str( int(user_products_read[8].split(':')[2]) * int(self.basket_product_9_count.text()) ) + ';' + user_products_read[9] + ';')
		user_products_w.close()
	self.basket_big_window()


def func_basket_product_10_count_apply_btn(self):
	''' Функция Извемения кол-ва товара №10 '''
	user_products_r = open(self.login_user + '_list_basket.txt', 'r')
	user_products_read = user_products_r.read()
	if ( user_products_read.count(';') == 10 ):
		user_products_read = user_products_read.split(';')
		user_products_r.close()

		user_products_w = open(self.login_user + '_list_basket.txt', 'w')
		user_products_w.write(user_products_read[0] + ';' + user_products_read[1] + ';' + user_products_read[2] + ';' + user_products_read[3] + ';' + user_products_read[4] + ';' + user_products_read[5] + ';' + user_products_read[6] + ';' + user_products_read[7] + ';' + user_products_read[8] + ';' + user_products_read[9].split(':')[0] + ':' + user_products_read[9].split(':')[1] + ':' + user_products_read[9].split(':')[2] + ':' + self.basket_product_10_count.text() + ':' + str( int(user_products_read[9].split(':')[2]) * int(self.basket_product_10_count.text()) ) + ';')
		user_products_w.close()
	self.basket_big_window()


def func_basket_product_1_del(self):
	''' Функция Удаление товара №1 '''
	user_products_r = open(self.login_user + '_list_basket.txt', 'r')
	user_products_read = user_products_r.read()
	if ( user_products_read.count(';') == 1 ):
		user_products_read = user_products_read.split(';')
		del user_products_read[0]
		user_products_r.close()

		user_products_w = open(self.login_user + '_list_basket.txt', 'w')
		user_products_w.write('')
		user_products_w.close()
	elif ( user_products_read.count(';') == 2 ):
		user_products_read = user_products_read.split(';')
		del user_products_read[0]
		user_products_r.close()

		user_products_w = open(self.login_user + '_list_basket.txt', 'w')
		user_products_w.write(user_products_read[0] + ';')
		user_products_w.close()
	elif ( user_products_read.count(';') == 3 ):
		user_products_read = user_products_read.split(';')
		del user_products_read[0]
		user_products_r.close()

		user_products_w = open(self.login_user + '_list_basket.txt', 'w')
		user_products_w.write(user_products_read[0] + ';' + user_products_read[1] + ';')
		user_products_w.close()
	elif ( user_products_read.count(';') == 4 ):
		user_products_read = user_products_read.split(';')
		del user_products_read[0]
		user_products_r.close()

		user_products_w = open(self.login_user + '_list_basket.txt', 'w')
		user_products_w.write(user_products_read[0] + ';' + user_products_read[1] + ';' + user_products_read[2] + ';')
		user_products_w.close()
	elif ( user_products_read.count(';') == 5 ):
		user_products_read = user_products_read.split(';')
		del user_products_read[0]
		user_products_r.close()

		user_products_w = open(self.login_user + '_list_basket.txt', 'w')
		user_products_w.write(user_products_read[0] + ';' + user_products_read[1] + ';' + user_products_read[2] + ';' + user_products_read[3] + ';')
		user_products_w.close()
	elif ( user_products_read.count(';') == 6 ):
		user_products_read = user_products_read.split(';')
		del user_products_read[0]
		user_products_r.close()

		user_products_w = open(self.login_user + '_list_basket.txt', 'w')
		user_products_w.write(user_products_read[0] + ';' + user_products_read[1] + ';' + user_products_read[2] + ';' + user_products_read[3] + ';' + user_products_read[4] + ';')
		user_products_w.close()
	elif ( user_products_read.count(';') == 7 ):
		user_products_read = user_products_read.split(';')
		del user_products_read[0]
		user_products_r.close()

		user_products_w = open(self.login_user + '_list_basket.txt', 'w')
		user_products_w.write(user_products_read[0] + ';' + user_products_read[1] + ';' + user_products_read[2] + ';' + user_products_read[3] + ';' + user_products_read[4] + ';' + user_products_read[5] + ';')
		user_products_w.close()
	elif ( user_products_read.count(';') == 8 ):
		user_products_read = user_products_read.split(';')
		del user_products_read[0]
		user_products_r.close()

		user_products_w = open(self.login_user + '_list_basket.txt', 'w')
		user_products_w.write(user_products_read[0] + ';' + user_products_read[1] + ';' + user_products_read[2] + ';' + user_products_read[3] + ';' + user_products_read[4] + ';' + user_products_read[5] + ';' + user_products_read[6] + ';')
		user_products_w.close()
	elif ( user_products_read.count(';') == 9 ):
		user_products_read = user_products_read.split(';')
		del user_products_read[0]
		user_products_r.close()

		user_products_w = open(self.login_user + '_list_basket.txt', 'w')
		user_products_w.write(user_products_read[0] + ';' + user_products_read[1] + ';' + user_products_read[2] + ';' + user_products_read[3] + ';' + user_products_read[4] + ';' + user_products_read[5] + ';' + user_products_read[6] + ';' + user_products_read[7] + ';')
		user_products_w.close()
	elif ( user_products_read.count(';') == 10 ):
		user_products_read = user_products_read.split(';')
		del user_products_read[0]
		user_products_r.close()

		user_products_w = open(self.login_user + '_list_basket.txt', 'w')
		user_products_w.write(user_products_read[0] + ';' + user_products_read[1] + ';' + user_products_read[2] + ';' + user_products_read[3] + ';' + user_products_read[4] + ';' + user_products_read[5] + ';' + user_products_read[6] + ';' + user_products_read[7] + ';' + user_products_read[8] + ';')
		user_products_w.close()
	self.basket_big_window()

def func_basket_product_2_del(self):
	''' Функция Удаление товара №2 '''
	user_products_r = open(self.login_user + '_list_basket.txt', 'r')
	user_products_read = user_products_r.read()
	if ( user_products_read.count(';') == 1 ):
		user_products_read = user_products_read.split(';')
		del user_products_read[1]
		user_products_r.close()

		user_products_w = open(self.login_user + '_list_basket.txt', 'w')
		user_products_w.write('')
		user_products_w.close()
	elif ( user_products_read.count(';') == 2 ):
		user_products_read = user_products_read.split(';')
		del user_products_read[1]
		user_products_r.close()

		user_products_w = open(self.login_user + '_list_basket.txt', 'w')
		user_products_w.write(user_products_read[0] + ';')
		user_products_w.close()
	elif ( user_products_read.count(';') == 3 ):
		user_products_read = user_products_read.split(';')
		del user_products_read[1]
		user_products_r.close()

		user_products_w = open(self.login_user + '_list_basket.txt', 'w')
		user_products_w.write(user_products_read[0] + ';' + user_products_read[1] + ';')
		user_products_w.close()
	elif ( user_products_read.count(';') == 4 ):
		user_products_read = user_products_read.split(';')
		del user_products_read[1]
		user_products_r.close()

		user_products_w = open(self.login_user + '_list_basket.txt', 'w')
		user_products_w.write(user_products_read[0] + ';' + user_products_read[1] + ';' + user_products_read[2] + ';')
		user_products_w.close()
	elif ( user_products_read.count(';') == 5 ):
		user_products_read = user_products_read.split(';')
		del user_products_read[1]
		user_products_r.close()

		user_products_w = open(self.login_user + '_list_basket.txt', 'w')
		user_products_w.write(user_products_read[0] + ';' + user_products_read[1] + ';' + user_products_read[2] + ';' + user_products_read[3] + ';')
		user_products_w.close()
	elif ( user_products_read.count(';') == 6 ):
		user_products_read = user_products_read.split(';')
		del user_products_read[1]
		user_products_r.close()

		user_products_w = open(self.login_user + '_list_basket.txt', 'w')
		user_products_w.write(user_products_read[0] + ';' + user_products_read[1] + ';' + user_products_read[2] + ';' + user_products_read[3] + ';' + user_products_read[4] + ';')
		user_products_w.close()
	elif ( user_products_read.count(';') == 7 ):
		user_products_read = user_products_read.split(';')
		del user_products_read[1]
		user_products_r.close()

		user_products_w = open(self.login_user + '_list_basket.txt', 'w')
		user_products_w.write(user_products_read[0] + ';' + user_products_read[1] + ';' + user_products_read[2] + ';' + user_products_read[3] + ';' + user_products_read[4] + ';' + user_products_read[5] + ';')
		user_products_w.close()
	elif ( user_products_read.count(';') == 8 ):
		user_products_read = user_products_read.split(';')
		del user_products_read[1]
		user_products_r.close()

		user_products_w = open(self.login_user + '_list_basket.txt', 'w')
		user_products_w.write(user_products_read[0] + ';' + user_products_read[1] + ';' + user_products_read[2] + ';' + user_products_read[3] + ';' + user_products_read[4] + ';' + user_products_read[5] + ';' + user_products_read[6] + ';')
		user_products_w.close()
	elif ( user_products_read.count(';') == 9 ):
		user_products_read = user_products_read.split(';')
		del user_products_read[1]
		user_products_r.close()

		user_products_w = open(self.login_user + '_list_basket.txt', 'w')
		user_products_w.write(user_products_read[0] + ';' + user_products_read[1] + ';' + user_products_read[2] + ';' + user_products_read[3] + ';' + user_products_read[4] + ';' + user_products_read[5] + ';' + user_products_read[6] + ';' + user_products_read[7] + ';')
		user_products_w.close()
	elif ( user_products_read.count(';') == 10 ):
		user_products_read = user_products_read.split(';')
		del user_products_read[1]
		user_products_r.close()

		user_products_w = open(self.login_user + '_list_basket.txt', 'w')
		user_products_w.write(user_products_read[0] + ';' + user_products_read[1] + ';' + user_products_read[2] + ';' + user_products_read[3] + ';' + user_products_read[4] + ';' + user_products_read[5] + ';' + user_products_read[6] + ';' + user_products_read[7] + ';' + user_products_read[8] + ';')
		user_products_w.close()
	self.basket_big_window()

def func_basket_product_3_del(self):
	''' Функция Удаление товара №3 '''
	user_products_r = open(self.login_user + '_list_basket.txt', 'r')
	user_products_read = user_products_r.read()
	if ( user_products_read.count(';') == 1 ):
		user_products_read = user_products_read.split(';')
		del user_products_read[2]
		user_products_r.close()

		user_products_w = open(self.login_user + '_list_basket.txt', 'w')
		user_products_w.write('')
		user_products_w.close()
	elif ( user_products_read.count(';') == 2 ):
		user_products_read = user_products_read.split(';')
		del user_products_read[2]
		user_products_r.close()

		user_products_w = open(self.login_user + '_list_basket.txt', 'w')
		user_products_w.write(user_products_read[0] + ';')
		user_products_w.close()
	elif ( user_products_read.count(';') == 3 ):
		user_products_read = user_products_read.split(';')
		del user_products_read[2]
		user_products_r.close()

		user_products_w = open(self.login_user + '_list_basket.txt', 'w')
		user_products_w.write(user_products_read[0] + ';' + user_products_read[1] + ';')
		user_products_w.close()
	elif ( user_products_read.count(';') == 4 ):
		user_products_read = user_products_read.split(';')
		del user_products_read[2]
		user_products_r.close()

		user_products_w = open(self.login_user + '_list_basket.txt', 'w')
		user_products_w.write(user_products_read[0] + ';' + user_products_read[1] + ';' + user_products_read[2] + ';')
		user_products_w.close()
	elif ( user_products_read.count(';') == 5 ):
		user_products_read = user_products_read.split(';')
		del user_products_read[2]
		user_products_r.close()

		user_products_w = open(self.login_user + '_list_basket.txt', 'w')
		user_products_w.write(user_products_read[0] + ';' + user_products_read[1] + ';' + user_products_read[2] + ';' + user_products_read[3] + ';')
		user_products_w.close()
	elif ( user_products_read.count(';') == 6 ):
		user_products_read = user_products_read.split(';')
		del user_products_read[2]
		user_products_r.close()

		user_products_w = open(self.login_user + '_list_basket.txt', 'w')
		user_products_w.write(user_products_read[0] + ';' + user_products_read[1] + ';' + user_products_read[2] + ';' + user_products_read[3] + ';' + user_products_read[4] + ';')
		user_products_w.close()
	elif ( user_products_read.count(';') == 7 ):
		user_products_read = user_products_read.split(';')
		del user_products_read[2]
		user_products_r.close()

		user_products_w = open(self.login_user + '_list_basket.txt', 'w')
		user_products_w.write(user_products_read[0] + ';' + user_products_read[1] + ';' + user_products_read[2] + ';' + user_products_read[3] + ';' + user_products_read[4] + ';' + user_products_read[5] + ';')
		user_products_w.close()
	elif ( user_products_read.count(';') == 8 ):
		user_products_read = user_products_read.split(';')
		del user_products_read[2]
		user_products_r.close()

		user_products_w = open(self.login_user + '_list_basket.txt', 'w')
		user_products_w.write(user_products_read[0] + ';' + user_products_read[1] + ';' + user_products_read[2] + ';' + user_products_read[3] + ';' + user_products_read[4] + ';' + user_products_read[5] + ';' + user_products_read[6] + ';')
		user_products_w.close()
	elif ( user_products_read.count(';') == 9 ):
		user_products_read = user_products_read.split(';')
		del user_products_read[2]
		user_products_r.close()

		user_products_w = open(self.login_user + '_list_basket.txt', 'w')
		user_products_w.write(user_products_read[0] + ';' + user_products_read[1] + ';' + user_products_read[2] + ';' + user_products_read[3] + ';' + user_products_read[4] + ';' + user_products_read[5] + ';' + user_products_read[6] + ';' + user_products_read[7] + ';')
		user_products_w.close()
	elif ( user_products_read.count(';') == 10 ):
		user_products_read = user_products_read.split(';')
		del user_products_read[2]
		user_products_r.close()

		user_products_w = open(self.login_user + '_list_basket.txt', 'w')
		user_products_w.write(user_products_read[0] + ';' + user_products_read[1] + ';' + user_products_read[2] + ';' + user_products_read[3] + ';' + user_products_read[4] + ';' + user_products_read[5] + ';' + user_products_read[6] + ';' + user_products_read[7] + ';' + user_products_read[8] + ';')
		user_products_w.close()
	self.basket_big_window()


def func_basket_product_4_del(self):
	''' Функция Удаление товара №4 '''
	user_products_r = open(self.login_user + '_list_basket.txt', 'r')
	user_products_read = user_products_r.read()
	if ( user_products_read.count(';') == 1 ):
		user_products_read = user_products_read.split(';')
		del user_products_read[3]
		user_products_r.close()

		user_products_w = open(self.login_user + '_list_basket.txt', 'w')
		user_products_w.write('')
		user_products_w.close()
	elif ( user_products_read.count(';') == 2 ):
		user_products_read = user_products_read.split(';')
		del user_products_read[3]
		user_products_r.close()

		user_products_w = open(self.login_user + '_list_basket.txt', 'w')
		user_products_w.write(user_products_read[0] + ';')
		user_products_w.close()
	elif ( user_products_read.count(';') == 3 ):
		user_products_read = user_products_read.split(';')
		del user_products_read[3]
		user_products_r.close()

		user_products_w = open(self.login_user + '_list_basket.txt', 'w')
		user_products_w.write(user_products_read[0] + ';' + user_products_read[1] + ';')
		user_products_w.close()
	elif ( user_products_read.count(';') == 4 ):
		user_products_read = user_products_read.split(';')
		del user_products_read[3]
		user_products_r.close()

		user_products_w = open(self.login_user + '_list_basket.txt', 'w')
		user_products_w.write(user_products_read[0] + ';' + user_products_read[1] + ';' + user_products_read[2] + ';')
		user_products_w.close()
	elif ( user_products_read.count(';') == 5 ):
		user_products_read = user_products_read.split(';')
		del user_products_read[3]
		user_products_r.close()

		user_products_w = open(self.login_user + '_list_basket.txt', 'w')
		user_products_w.write(user_products_read[0] + ';' + user_products_read[1] + ';' + user_products_read[2] + ';' + user_products_read[3] + ';')
		user_products_w.close()
	elif ( user_products_read.count(';') == 6 ):
		user_products_read = user_products_read.split(';')
		del user_products_read[3]
		user_products_r.close()

		user_products_w = open(self.login_user + '_list_basket.txt', 'w')
		user_products_w.write(user_products_read[0] + ';' + user_products_read[1] + ';' + user_products_read[2] + ';' + user_products_read[3] + ';' + user_products_read[4] + ';')
		user_products_w.close()
	elif ( user_products_read.count(';') == 7 ):
		user_products_read = user_products_read.split(';')
		del user_products_read[3]
		user_products_r.close()

		user_products_w = open(self.login_user + '_list_basket.txt', 'w')
		user_products_w.write(user_products_read[0] + ';' + user_products_read[1] + ';' + user_products_read[2] + ';' + user_products_read[3] + ';' + user_products_read[4] + ';' + user_products_read[5] + ';')
		user_products_w.close()
	elif ( user_products_read.count(';') == 8 ):
		user_products_read = user_products_read.split(';')
		del user_products_read[3]
		user_products_r.close()

		user_products_w = open(self.login_user + '_list_basket.txt', 'w')
		user_products_w.write(user_products_read[0] + ';' + user_products_read[1] + ';' + user_products_read[2] + ';' + user_products_read[3] + ';' + user_products_read[4] + ';' + user_products_read[5] + ';' + user_products_read[6] + ';')
		user_products_w.close()
	elif ( user_products_read.count(';') == 9 ):
		user_products_read = user_products_read.split(';')
		del user_products_read[3]
		user_products_r.close()

		user_products_w = open(self.login_user + '_list_basket.txt', 'w')
		user_products_w.write(user_products_read[0] + ';' + user_products_read[1] + ';' + user_products_read[2] + ';' + user_products_read[3] + ';' + user_products_read[4] + ';' + user_products_read[5] + ';' + user_products_read[6] + ';' + user_products_read[7] + ';')
		user_products_w.close()
	elif ( user_products_read.count(';') == 10 ):
		user_products_read = user_products_read.split(';')
		del user_products_read[3]
		user_products_r.close()

		user_products_w = open(self.login_user + '_list_basket.txt', 'w')
		user_products_w.write(user_products_read[0] + ';' + user_products_read[1] + ';' + user_products_read[2] + ';' + user_products_read[3] + ';' + user_products_read[4] + ';' + user_products_read[5] + ';' + user_products_read[6] + ';' + user_products_read[7] + ';' + user_products_read[8] + ';')
		user_products_w.close()
	self.basket_big_window()


def func_basket_product_5_del(self):
	''' Функция Удаление товара №5 '''
	user_products_r = open(self.login_user + '_list_basket.txt', 'r')
	user_products_read = user_products_r.read()
	if ( user_products_read.count(';') == 1 ):
		user_products_read = user_products_read.split(';')
		del user_products_read[4]
		user_products_r.close()

		user_products_w = open(self.login_user + '_list_basket.txt', 'w')
		user_products_w.write('')
		user_products_w.close()
	elif ( user_products_read.count(';') == 2 ):
		user_products_read = user_products_read.split(';')
		del user_products_read[4]
		user_products_r.close()

		user_products_w = open(self.login_user + '_list_basket.txt', 'w')
		user_products_w.write(user_products_read[0] + ';')
		user_products_w.close()
	elif ( user_products_read.count(';') == 3 ):
		user_products_read = user_products_read.split(';')
		del user_products_read[4]
		user_products_r.close()

		user_products_w = open(self.login_user + '_list_basket.txt', 'w')
		user_products_w.write(user_products_read[0] + ';' + user_products_read[1] + ';')
		user_products_w.close()
	elif ( user_products_read.count(';') == 4 ):
		user_products_read = user_products_read.split(';')
		del user_products_read[4]
		user_products_r.close()

		user_products_w = open(self.login_user + '_list_basket.txt', 'w')
		user_products_w.write(user_products_read[0] + ';' + user_products_read[1] + ';' + user_products_read[2] + ';')
		user_products_w.close()
	elif ( user_products_read.count(';') == 5 ):
		user_products_read = user_products_read.split(';')
		del user_products_read[4]
		user_products_r.close()

		user_products_w = open(self.login_user + '_list_basket.txt', 'w')
		user_products_w.write(user_products_read[0] + ';' + user_products_read[1] + ';' + user_products_read[2] + ';' + user_products_read[3] + ';')
		user_products_w.close()
	elif ( user_products_read.count(';') == 6 ):
		user_products_read = user_products_read.split(';')
		del user_products_read[4]
		user_products_r.close()

		user_products_w = open(self.login_user + '_list_basket.txt', 'w')
		user_products_w.write(user_products_read[0] + ';' + user_products_read[1] + ';' + user_products_read[2] + ';' + user_products_read[3] + ';' + user_products_read[4] + ';')
		user_products_w.close()
	elif ( user_products_read.count(';') == 7 ):
		user_products_read = user_products_read.split(';')
		del user_products_read[4]
		user_products_r.close()

		user_products_w = open(self.login_user + '_list_basket.txt', 'w')
		user_products_w.write(user_products_read[0] + ';' + user_products_read[1] + ';' + user_products_read[2] + ';' + user_products_read[3] + ';' + user_products_read[4] + ';' + user_products_read[5] + ';')
		user_products_w.close()
	elif ( user_products_read.count(';') == 8 ):
		user_products_read = user_products_read.split(';')
		del user_products_read[4]
		user_products_r.close()

		user_products_w = open(self.login_user + '_list_basket.txt', 'w')
		user_products_w.write(user_products_read[0] + ';' + user_products_read[1] + ';' + user_products_read[2] + ';' + user_products_read[3] + ';' + user_products_read[4] + ';' + user_products_read[5] + ';' + user_products_read[6] + ';')
		user_products_w.close()
	elif ( user_products_read.count(';') == 9 ):
		user_products_read = user_products_read.split(';')
		del user_products_read[4]
		user_products_r.close()

		user_products_w = open(self.login_user + '_list_basket.txt', 'w')
		user_products_w.write(user_products_read[0] + ';' + user_products_read[1] + ';' + user_products_read[2] + ';' + user_products_read[3] + ';' + user_products_read[4] + ';' + user_products_read[5] + ';' + user_products_read[6] + ';' + user_products_read[7] + ';')
		user_products_w.close()
	elif ( user_products_read.count(';') == 10 ):
		user_products_read = user_products_read.split(';')
		del user_products_read[4]
		user_products_r.close()

		user_products_w = open(self.login_user + '_list_basket.txt', 'w')
		user_products_w.write(user_products_read[0] + ';' + user_products_read[1] + ';' + user_products_read[2] + ';' + user_products_read[3] + ';' + user_products_read[4] + ';' + user_products_read[5] + ';' + user_products_read[6] + ';' + user_products_read[7] + ';' + user_products_read[8] + ';')
		user_products_w.close()
	self.basket_big_window()


def func_basket_product_6_del(self):
	''' Функция Удаление товара №6 '''
	user_products_r = open(self.login_user + '_list_basket.txt', 'r')
	user_products_read = user_products_r.read()
	if ( user_products_read.count(';') == 1 ):
		user_products_read = user_products_read.split(';')
		del user_products_read[5]
		user_products_r.close()

		user_products_w = open(self.login_user + '_list_basket.txt', 'w')
		user_products_w.write('')
		user_products_w.close()
	elif ( user_products_read.count(';') == 2 ):
		user_products_read = user_products_read.split(';')
		del user_products_read[5]
		user_products_r.close()

		user_products_w = open(self.login_user + '_list_basket.txt', 'w')
		user_products_w.write(user_products_read[0] + ';')
		user_products_w.close()
	elif ( user_products_read.count(';') == 3 ):
		user_products_read = user_products_read.split(';')
		del user_products_read[5]
		user_products_r.close()

		user_products_w = open(self.login_user + '_list_basket.txt', 'w')
		user_products_w.write(user_products_read[0] + ';' + user_products_read[1] + ';')
		user_products_w.close()
	elif ( user_products_read.count(';') == 4 ):
		user_products_read = user_products_read.split(';')
		del user_products_read[5]
		user_products_r.close()

		user_products_w = open(self.login_user + '_list_basket.txt', 'w')
		user_products_w.write(user_products_read[0] + ';' + user_products_read[1] + ';' + user_products_read[2] + ';')
		user_products_w.close()
	elif ( user_products_read.count(';') == 5 ):
		user_products_read = user_products_read.split(';')
		del user_products_read[5]
		user_products_r.close()

		user_products_w = open(self.login_user + '_list_basket.txt', 'w')
		user_products_w.write(user_products_read[0] + ';' + user_products_read[1] + ';' + user_products_read[2] + ';' + user_products_read[3] + ';')
		user_products_w.close()
	elif ( user_products_read.count(';') == 6 ):
		user_products_read = user_products_read.split(';')
		del user_products_read[5]
		user_products_r.close()

		user_products_w = open(self.login_user + '_list_basket.txt', 'w')
		user_products_w.write(user_products_read[0] + ';' + user_products_read[1] + ';' + user_products_read[2] + ';' + user_products_read[3] + ';' + user_products_read[4] + ';')
		user_products_w.close()
	elif ( user_products_read.count(';') == 7 ):
		user_products_read = user_products_read.split(';')
		del user_products_read[5]
		user_products_r.close()

		user_products_w = open(self.login_user + '_list_basket.txt', 'w')
		user_products_w.write(user_products_read[0] + ';' + user_products_read[1] + ';' + user_products_read[2] + ';' + user_products_read[3] + ';' + user_products_read[4] + ';' + user_products_read[5] + ';')
		user_products_w.close()
	elif ( user_products_read.count(';') == 8 ):
		user_products_read = user_products_read.split(';')
		del user_products_read[5]
		user_products_r.close()

		user_products_w = open(self.login_user + '_list_basket.txt', 'w')
		user_products_w.write(user_products_read[0] + ';' + user_products_read[1] + ';' + user_products_read[2] + ';' + user_products_read[3] + ';' + user_products_read[4] + ';' + user_products_read[5] + ';' + user_products_read[6] + ';')
		user_products_w.close()
	elif ( user_products_read.count(';') == 9 ):
		user_products_read = user_products_read.split(';')
		del user_products_read[5]
		user_products_r.close()

		user_products_w = open(self.login_user + '_list_basket.txt', 'w')
		user_products_w.write(user_products_read[0] + ';' + user_products_read[1] + ';' + user_products_read[2] + ';' + user_products_read[3] + ';' + user_products_read[4] + ';' + user_products_read[5] + ';' + user_products_read[6] + ';' + user_products_read[7] + ';')
		user_products_w.close()
	elif ( user_products_read.count(';') == 10 ):
		user_products_read = user_products_read.split(';')
		del user_products_read[5]
		user_products_r.close()

		user_products_w = open(self.login_user + '_list_basket.txt', 'w')
		user_products_w.write(user_products_read[0] + ';' + user_products_read[1] + ';' + user_products_read[2] + ';' + user_products_read[3] + ';' + user_products_read[4] + ';' + user_products_read[5] + ';' + user_products_read[6] + ';' + user_products_read[7] + ';' + user_products_read[8] + ';')
		user_products_w.close()
	self.basket_big_window()


def func_basket_product_7_del(self):
	''' Функция Удаление товара №7 '''
	user_products_r = open(self.login_user + '_list_basket.txt', 'r')
	user_products_read = user_products_r.read()
	if ( user_products_read.count(';') == 1 ):
		user_products_read = user_products_read.split(';')
		del user_products_read[6]
		user_products_r.close()

		user_products_w = open(self.login_user + '_list_basket.txt', 'w')
		user_products_w.write('')
		user_products_w.close()
	elif ( user_products_read.count(';') == 2 ):
		user_products_read = user_products_read.split(';')
		del user_products_read[6]
		user_products_r.close()

		user_products_w = open(self.login_user + '_list_basket.txt', 'w')
		user_products_w.write(user_products_read[0] + ';')
		user_products_w.close()
	elif ( user_products_read.count(';') == 3 ):
		user_products_read = user_products_read.split(';')
		del user_products_read[6]
		user_products_r.close()

		user_products_w = open(self.login_user + '_list_basket.txt', 'w')
		user_products_w.write(user_products_read[0] + ';' + user_products_read[1] + ';')
		user_products_w.close()
	elif ( user_products_read.count(';') == 4 ):
		user_products_read = user_products_read.split(';')
		del user_products_read[6]
		user_products_r.close()

		user_products_w = open(self.login_user + '_list_basket.txt', 'w')
		user_products_w.write(user_products_read[0] + ';' + user_products_read[1] + ';' + user_products_read[2] + ';')
		user_products_w.close()
	elif ( user_products_read.count(';') == 5 ):
		user_products_read = user_products_read.split(';')
		del user_products_read[6]
		user_products_r.close()

		user_products_w = open(self.login_user + '_list_basket.txt', 'w')
		user_products_w.write(user_products_read[0] + ';' + user_products_read[1] + ';' + user_products_read[2] + ';' + user_products_read[3] + ';')
		user_products_w.close()
	elif ( user_products_read.count(';') == 6 ):
		user_products_read = user_products_read.split(';')
		del user_products_read[6]
		user_products_r.close()

		user_products_w = open(self.login_user + '_list_basket.txt', 'w')
		user_products_w.write(user_products_read[0] + ';' + user_products_read[1] + ';' + user_products_read[2] + ';' + user_products_read[3] + ';' + user_products_read[4] + ';')
		user_products_w.close()
	elif ( user_products_read.count(';') == 7 ):
		user_products_read = user_products_read.split(';')
		del user_products_read[6]
		user_products_r.close()

		user_products_w = open(self.login_user + '_list_basket.txt', 'w')
		user_products_w.write(user_products_read[0] + ';' + user_products_read[1] + ';' + user_products_read[2] + ';' + user_products_read[3] + ';' + user_products_read[4] + ';' + user_products_read[5] + ';')
		user_products_w.close()
	elif ( user_products_read.count(';') == 8 ):
		user_products_read = user_products_read.split(';')
		del user_products_read[6]
		user_products_r.close()

		user_products_w = open(self.login_user + '_list_basket.txt', 'w')
		user_products_w.write(user_products_read[0] + ';' + user_products_read[1] + ';' + user_products_read[2] + ';' + user_products_read[3] + ';' + user_products_read[4] + ';' + user_products_read[5] + ';' + user_products_read[6] + ';')
		user_products_w.close()
	elif ( user_products_read.count(';') == 9 ):
		user_products_read = user_products_read.split(';')
		del user_products_read[6]
		user_products_r.close()

		user_products_w = open(self.login_user + '_list_basket.txt', 'w')
		user_products_w.write(user_products_read[0] + ';' + user_products_read[1] + ';' + user_products_read[2] + ';' + user_products_read[3] + ';' + user_products_read[4] + ';' + user_products_read[5] + ';' + user_products_read[6] + ';' + user_products_read[7] + ';')
		user_products_w.close()
	elif ( user_products_read.count(';') == 10 ):
		user_products_read = user_products_read.split(';')
		del user_products_read[6]
		user_products_r.close()

		user_products_w = open(self.login_user + '_list_basket.txt', 'w')
		user_products_w.write(user_products_read[0] + ';' + user_products_read[1] + ';' + user_products_read[2] + ';' + user_products_read[3] + ';' + user_products_read[4] + ';' + user_products_read[5] + ';' + user_products_read[6] + ';' + user_products_read[7] + ';' + user_products_read[8] + ';')
		user_products_w.close()
	self.basket_big_window()


def func_basket_product_8_del(self):
	''' Функция Удаление товара №8 '''
	user_products_r = open(self.login_user + '_list_basket.txt', 'r')
	user_products_read = user_products_r.read()
	if ( user_products_read.count(';') == 1 ):
		user_products_read = user_products_read.split(';')
		del user_products_read[7]
		user_products_r.close()

		user_products_w = open(self.login_user + '_list_basket.txt', 'w')
		user_products_w.write('')
		user_products_w.close()
	elif ( user_products_read.count(';') == 2 ):
		user_products_read = user_products_read.split(';')
		del user_products_read[7]
		user_products_r.close()

		user_products_w = open(self.login_user + '_list_basket.txt', 'w')
		user_products_w.write(user_products_read[0] + ';')
		user_products_w.close()
	elif ( user_products_read.count(';') == 3 ):
		user_products_read = user_products_read.split(';')
		del user_products_read[7]
		user_products_r.close()

		user_products_w = open(self.login_user + '_list_basket.txt', 'w')
		user_products_w.write(user_products_read[0] + ';' + user_products_read[1] + ';')
		user_products_w.close()
	elif ( user_products_read.count(';') == 4 ):
		user_products_read = user_products_read.split(';')
		del user_products_read[7]
		user_products_r.close()

		user_products_w = open(self.login_user + '_list_basket.txt', 'w')
		user_products_w.write(user_products_read[0] + ';' + user_products_read[1] + ';' + user_products_read[2] + ';')
		user_products_w.close()
	elif ( user_products_read.count(';') == 5 ):
		user_products_read = user_products_read.split(';')
		del user_products_read[7]
		user_products_r.close()

		user_products_w = open(self.login_user + '_list_basket.txt', 'w')
		user_products_w.write(user_products_read[0] + ';' + user_products_read[1] + ';' + user_products_read[2] + ';' + user_products_read[3] + ';')
		user_products_w.close()
	elif ( user_products_read.count(';') == 6 ):
		user_products_read = user_products_read.split(';')
		del user_products_read[7]
		user_products_r.close()

		user_products_w = open(self.login_user + '_list_basket.txt', 'w')
		user_products_w.write(user_products_read[0] + ';' + user_products_read[1] + ';' + user_products_read[2] + ';' + user_products_read[3] + ';' + user_products_read[4] + ';')
		user_products_w.close()
	elif ( user_products_read.count(';') == 7 ):
		user_products_read = user_products_read.split(';')
		del user_products_read[7]
		user_products_r.close()

		user_products_w = open(self.login_user + '_list_basket.txt', 'w')
		user_products_w.write(user_products_read[0] + ';' + user_products_read[1] + ';' + user_products_read[2] + ';' + user_products_read[3] + ';' + user_products_read[4] + ';' + user_products_read[5] + ';')
		user_products_w.close()
	elif ( user_products_read.count(';') == 8 ):
		user_products_read = user_products_read.split(';')
		del user_products_read[7]
		user_products_r.close()

		user_products_w = open(self.login_user + '_list_basket.txt', 'w')
		user_products_w.write(user_products_read[0] + ';' + user_products_read[1] + ';' + user_products_read[2] + ';' + user_products_read[3] + ';' + user_products_read[4] + ';' + user_products_read[5] + ';' + user_products_read[6] + ';')
		user_products_w.close()
	elif ( user_products_read.count(';') == 9 ):
		user_products_read = user_products_read.split(';')
		del user_products_read[7]
		user_products_r.close()

		user_products_w = open(self.login_user + '_list_basket.txt', 'w')
		user_products_w.write(user_products_read[0] + ';' + user_products_read[1] + ';' + user_products_read[2] + ';' + user_products_read[3] + ';' + user_products_read[4] + ';' + user_products_read[5] + ';' + user_products_read[6] + ';' + user_products_read[7] + ';')
		user_products_w.close()
	elif ( user_products_read.count(';') == 10 ):
		user_products_read = user_products_read.split(';')
		del user_products_read[7]
		user_products_r.close()

		user_products_w = open(self.login_user + '_list_basket.txt', 'w')
		user_products_w.write(user_products_read[0] + ';' + user_products_read[1] + ';' + user_products_read[2] + ';' + user_products_read[3] + ';' + user_products_read[4] + ';' + user_products_read[5] + ';' + user_products_read[6] + ';' + user_products_read[7] + ';' + user_products_read[8] + ';')
		user_products_w.close()
	self.basket_big_window()


def func_basket_product_9_del(self):
	''' Функция Удаление товара №9 '''
	user_products_r = open(self.login_user + '_list_basket.txt', 'r')
	user_products_read = user_products_r.read()
	if ( user_products_read.count(';') == 1 ):
		user_products_read = user_products_read.split(';')
		del user_products_read[8]
		user_products_r.close()

		user_products_w = open(self.login_user + '_list_basket.txt', 'w')
		user_products_w.write('')
		user_products_w.close()
	elif ( user_products_read.count(';') == 2 ):
		user_products_read = user_products_read.split(';')
		del user_products_read[8]
		user_products_r.close()

		user_products_w = open(self.login_user + '_list_basket.txt', 'w')
		user_products_w.write(user_products_read[0] + ';')
		user_products_w.close()
	elif ( user_products_read.count(';') == 3 ):
		user_products_read = user_products_read.split(';')
		del user_products_read[8]
		user_products_r.close()

		user_products_w = open(self.login_user + '_list_basket.txt', 'w')
		user_products_w.write(user_products_read[0] + ';' + user_products_read[1] + ';')
		user_products_w.close()
	elif ( user_products_read.count(';') == 4 ):
		user_products_read = user_products_read.split(';')
		del user_products_read[8]
		user_products_r.close()

		user_products_w = open(self.login_user + '_list_basket.txt', 'w')
		user_products_w.write(user_products_read[0] + ';' + user_products_read[1] + ';' + user_products_read[2] + ';')
		user_products_w.close()
	elif ( user_products_read.count(';') == 5 ):
		user_products_read = user_products_read.split(';')
		del user_products_read[8]
		user_products_r.close()

		user_products_w = open(self.login_user + '_list_basket.txt', 'w')
		user_products_w.write(user_products_read[0] + ';' + user_products_read[1] + ';' + user_products_read[2] + ';' + user_products_read[3] + ';')
		user_products_w.close()
	elif ( user_products_read.count(';') == 6 ):
		user_products_read = user_products_read.split(';')
		del user_products_read[8]
		user_products_r.close()

		user_products_w = open(self.login_user + '_list_basket.txt', 'w')
		user_products_w.write(user_products_read[0] + ';' + user_products_read[1] + ';' + user_products_read[2] + ';' + user_products_read[3] + ';' + user_products_read[4] + ';')
		user_products_w.close()
	elif ( user_products_read.count(';') == 7 ):
		user_products_read = user_products_read.split(';')
		del user_products_read[8]
		user_products_r.close()

		user_products_w = open(self.login_user + '_list_basket.txt', 'w')
		user_products_w.write(user_products_read[0] + ';' + user_products_read[1] + ';' + user_products_read[2] + ';' + user_products_read[3] + ';' + user_products_read[4] + ';' + user_products_read[5] + ';')
		user_products_w.close()
	elif ( user_products_read.count(';') == 8 ):
		user_products_read = user_products_read.split(';')
		del user_products_read[8]
		user_products_r.close()

		user_products_w = open(self.login_user + '_list_basket.txt', 'w')
		user_products_w.write(user_products_read[0] + ';' + user_products_read[1] + ';' + user_products_read[2] + ';' + user_products_read[3] + ';' + user_products_read[4] + ';' + user_products_read[5] + ';' + user_products_read[6] + ';')
		user_products_w.close()
	elif ( user_products_read.count(';') == 9 ):
		user_products_read = user_products_read.split(';')
		del user_products_read[8]
		user_products_r.close()

		user_products_w = open(self.login_user + '_list_basket.txt', 'w')
		user_products_w.write(user_products_read[0] + ';' + user_products_read[1] + ';' + user_products_read[2] + ';' + user_products_read[3] + ';' + user_products_read[4] + ';' + user_products_read[5] + ';' + user_products_read[6] + ';' + user_products_read[7] + ';')
		user_products_w.close()
	elif ( user_products_read.count(';') == 10 ):
		user_products_read = user_products_read.split(';')
		del user_products_read[8]
		user_products_r.close()

		user_products_w = open(self.login_user + '_list_basket.txt', 'w')
		user_products_w.write(user_products_read[0] + ';' + user_products_read[1] + ';' + user_products_read[2] + ';' + user_products_read[3] + ';' + user_products_read[4] + ';' + user_products_read[5] + ';' + user_products_read[6] + ';' + user_products_read[7] + ';' + user_products_read[8] + ';')
		user_products_w.close()
	self.basket_big_window()


def func_basket_product_10_del(self):
	''' Функция Удаление товара №10 '''
	user_products_r = open(self.login_user + '_list_basket.txt', 'r')
	user_products_read = user_products_r.read()
	if ( user_products_read.count(';') == 1 ):
		user_products_read = user_products_read.split(';')
		del user_products_read[9]
		user_products_r.close()

		user_products_w = open(self.login_user + '_list_basket.txt', 'w')
		user_products_w.write('')
		user_products_w.close()
	elif ( user_products_read.count(';') == 2 ):
		user_products_read = user_products_read.split(';')
		del user_products_read[9]
		user_products_r.close()

		user_products_w = open(self.login_user + '_list_basket.txt', 'w')
		user_products_w.write(user_products_read[0] + ';')
		user_products_w.close()
	elif ( user_products_read.count(';') == 3 ):
		user_products_read = user_products_read.split(';')
		del user_products_read[9]
		user_products_r.close()

		user_products_w = open(self.login_user + '_list_basket.txt', 'w')
		user_products_w.write(user_products_read[0] + ';' + user_products_read[1] + ';')
		user_products_w.close()
	elif ( user_products_read.count(';') == 4 ):
		user_products_read = user_products_read.split(';')
		del user_products_read[9]
		user_products_r.close()

		user_products_w = open(self.login_user + '_list_basket.txt', 'w')
		user_products_w.write(user_products_read[0] + ';' + user_products_read[1] + ';' + user_products_read[2] + ';')
		user_products_w.close()
	elif ( user_products_read.count(';') == 5 ):
		user_products_read = user_products_read.split(';')
		del user_products_read[9]
		user_products_r.close()

		user_products_w = open(self.login_user + '_list_basket.txt', 'w')
		user_products_w.write(user_products_read[0] + ';' + user_products_read[1] + ';' + user_products_read[2] + ';' + user_products_read[3] + ';')
		user_products_w.close()
	elif ( user_products_read.count(';') == 6 ):
		user_products_read = user_products_read.split(';')
		del user_products_read[9]
		user_products_r.close()

		user_products_w = open(self.login_user + '_list_basket.txt', 'w')
		user_products_w.write(user_products_read[0] + ';' + user_products_read[1] + ';' + user_products_read[2] + ';' + user_products_read[3] + ';' + user_products_read[4] + ';')
		user_products_w.close()
	elif ( user_products_read.count(';') == 7 ):
		user_products_read = user_products_read.split(';')
		del user_products_read[9]
		user_products_r.close()

		user_products_w = open(self.login_user + '_list_basket.txt', 'w')
		user_products_w.write(user_products_read[0] + ';' + user_products_read[1] + ';' + user_products_read[2] + ';' + user_products_read[3] + ';' + user_products_read[4] + ';' + user_products_read[5] + ';')
		user_products_w.close()
	elif ( user_products_read.count(';') == 8 ):
		user_products_read = user_products_read.split(';')
		del user_products_read[9]
		user_products_r.close()

		user_products_w = open(self.login_user + '_list_basket.txt', 'w')
		user_products_w.write(user_products_read[0] + ';' + user_products_read[1] + ';' + user_products_read[2] + ';' + user_products_read[3] + ';' + user_products_read[4] + ';' + user_products_read[5] + ';' + user_products_read[6] + ';')
		user_products_w.close()
	elif ( user_products_read.count(';') == 9 ):
		user_products_read = user_products_read.split(';')
		del user_products_read[9]
		user_products_r.close()

		user_products_w = open(self.login_user + '_list_basket.txt', 'w')
		user_products_w.write(user_products_read[0] + ';' + user_products_read[1] + ';' + user_products_read[2] + ';' + user_products_read[3] + ';' + user_products_read[4] + ';' + user_products_read[5] + ';' + user_products_read[6] + ';' + user_products_read[7] + ';')
		user_products_w.close()
	elif ( user_products_read.count(';') == 10 ):
		user_products_read = user_products_read.split(';')
		del user_products_read[9]
		user_products_r.close()

		user_products_w = open(self.login_user + '_list_basket.txt', 'w')
		user_products_w.write(user_products_read[0] + ';' + user_products_read[1] + ';' + user_products_read[2] + ';' + user_products_read[3] + ';' + user_products_read[4] + ';' + user_products_read[5] + ';' + user_products_read[6] + ';' + user_products_read[7] + ';' + user_products_read[8] + ';')
		user_products_w.close()
	self.basket_big_window()


def func_basket_products_all_del(self):
	user_products_w = open(self.login_user + '_list_basket.txt', 'w')
	user_products_w.write('')
	user_products_w.close()
	self.basket_big_window()

def basket_product_1_count_del_buy_style(self):
	# Стили Количество
	self.basket_product_1_count = QLineEdit(self.basket_Window)
	self.basket_product_1_count.setStyleSheet('''QLineEdit {font-size: 12px; border: 1px solid #000000;}''')
	self.basket_product_1_count.resize(72, 18)
	self.basket_product_1_count.move(664, 152)
	self.basket_product_1_count_apply_btn = QPushButton('Применить', self.basket_Window)
	self.basket_product_1_count_apply_btn.clicked.connect(self.func_basket_product_1_count_apply_btn)
	self.basket_product_1_count_apply_btn.setStyleSheet('''QPushButton {font-size: 12px; color: #FFFFFF; border: 1px solid green; background-color: green;}''')
	self.basket_product_1_count_apply_btn.resize(72, 18)
	self.basket_product_1_count_apply_btn.move(664, 172)

	# Стили Удаление
	self.basket_product_1_del = QPushButton('', self.basket_Window)
	self.basket_product_1_del.clicked.connect(self.func_basket_product_1_del)
	self.basket_product_1_del.setStyleSheet('''QPushButton {border: 0; background-image: url(icons/close.png);}''')
	self.basket_product_1_del.resize(32, 32)
	self.basket_product_1_del.move(906, 155)

	# Стили Купить
	self.basket_product_1_buy = QPushButton('', self.basket_Window)
	# self.basket_product_1_buy.clicked.connect(self.func_basket_product_1_buy)
	self.basket_product_1_buy.setStyleSheet('''QPushButton {border: 0; background-image: url(icons/icon_basket_buy.png);}''')
	self.basket_product_1_buy.resize(32, 32)
	self.basket_product_1_buy.move(968, 155)


def basket_product_2_count_del_buy_style(self):
	# Стили Количество
	self.basket_product_2_count = QLineEdit(self.basket_Window)
	self.basket_product_2_count.setStyleSheet('''QLineEdit {font-size: 12px; border: 1px solid #000000;}''')
	self.basket_product_2_count.resize(72, 18)
	self.basket_product_2_count.move(664, 197)
	self.basket_product_2_count_apply_btn = QPushButton('Применить', self.basket_Window)
	self.basket_product_2_count_apply_btn.clicked.connect(self.func_basket_product_2_count_apply_btn)
	self.basket_product_2_count_apply_btn.setStyleSheet('''QPushButton {font-size: 12px; color: #FFFFFF; border: 1px solid green; background-color: green;}''')
	self.basket_product_2_count_apply_btn.resize(72, 18)
	self.basket_product_2_count_apply_btn.move(664, 217)

	# Стили Удаление
	self.basket_product_2_del = QPushButton('', self.basket_Window)
	self.basket_product_2_del.clicked.connect(self.func_basket_product_2_del)
	self.basket_product_2_del.setStyleSheet('''QPushButton {border: 0; background-image: url(icons/close.png);}''')
	self.basket_product_2_del.resize(32, 32)
	self.basket_product_2_del.move(906, 200)

	# Стили Купить
	self.basket_product_2_buy = QPushButton('', self.basket_Window)
	# self.basket_product_2_buy.clicked.connect(self.func_basket_product_2_buy)
	self.basket_product_2_buy.setStyleSheet('''QPushButton {border: 0; background-image: url(icons/icon_basket_buy.png);}''')
	self.basket_product_2_buy.resize(32, 32)
	self.basket_product_2_buy.move(968, 200)


def basket_product_3_count_del_buy_style(self):
	# Стили Количество
	self.basket_product_3_count = QLineEdit(self.basket_Window)
	self.basket_product_3_count.setStyleSheet('''QLineEdit {font-size: 12px; border: 1px solid #000000;}''')
	self.basket_product_3_count.resize(72, 18)
	self.basket_product_3_count.move(664, 242)
	self.basket_product_3_count_apply_btn = QPushButton('Применить', self.basket_Window)
	self.basket_product_3_count_apply_btn.clicked.connect(self.func_basket_product_3_count_apply_btn)
	self.basket_product_3_count_apply_btn.setStyleSheet('''QPushButton {font-size: 12px; color: #FFFFFF; border: 1px solid green; background-color: green;}''')
	self.basket_product_3_count_apply_btn.resize(72, 18)
	self.basket_product_3_count_apply_btn.move(664, 262)

	# Стили Удаление
	self.basket_product_3_del = QPushButton('', self.basket_Window)
	self.basket_product_3_del.clicked.connect(self.func_basket_product_3_del)
	self.basket_product_3_del.setStyleSheet('''QPushButton {border: 0; background-image: url(icons/close.png);}''')
	self.basket_product_3_del.resize(32, 32)
	self.basket_product_3_del.move(906, 245)

	# Стили Купить
	self.basket_product_3_buy = QPushButton('', self.basket_Window)
	# self.basket_product_3_buy.clicked.connect(self.func_basket_product_3_buy)
	self.basket_product_3_buy.setStyleSheet('''QPushButton {border: 0; background-image: url(icons/icon_basket_buy.png);}''')
	self.basket_product_3_buy.resize(32, 32)
	self.basket_product_3_buy.move(968, 245)


def basket_product_4_count_del_buy_style(self):
	# Стили Количество
	self.basket_product_4_count = QLineEdit(self.basket_Window)
	self.basket_product_4_count.setStyleSheet('''QLineEdit {font-size: 12px; border: 1px solid #000000;}''')
	self.basket_product_4_count.resize(72, 18)
	self.basket_product_4_count.move(664, 287)
	self.basket_product_4_count_apply_btn = QPushButton('Применить', self.basket_Window)
	self.basket_product_4_count_apply_btn.clicked.connect(self.func_basket_product_4_count_apply_btn)
	self.basket_product_4_count_apply_btn.setStyleSheet('''QPushButton {font-size: 12px; color: #FFFFFF; border: 1px solid green; background-color: green;}''')
	self.basket_product_4_count_apply_btn.resize(72, 18)
	self.basket_product_4_count_apply_btn.move(664, 307)

	# Стили Удаление
	self.basket_product_4_del = QPushButton('', self.basket_Window)
	self.basket_product_4_del.clicked.connect(self.func_basket_product_4_del)
	self.basket_product_4_del.setStyleSheet('''QPushButton {border: 0; background-image: url(icons/close.png);}''')
	self.basket_product_4_del.resize(32, 32)
	self.basket_product_4_del.move(906, 290)

	# Стили Купить
	self.basket_product_4_buy = QPushButton('', self.basket_Window)
	# self.basket_product_4_buy.clicked.connect(self.func_basket_product_4_buy)
	self.basket_product_4_buy.setStyleSheet('''QPushButton {border: 0; background-image: url(icons/icon_basket_buy.png);}''')
	self.basket_product_4_buy.resize(32, 32)
	self.basket_product_4_buy.move(968, 290)


def basket_product_5_count_del_buy_style(self):
	# Стили Количество
	self.basket_product_5_count = QLineEdit(self.basket_Window)
	self.basket_product_5_count.setStyleSheet('''QLineEdit {font-size: 12px; border: 1px solid #000000;}''')
	self.basket_product_5_count.resize(72, 18)
	self.basket_product_5_count.move(664, 332)
	self.basket_product_5_count_apply_btn = QPushButton('Применить', self.basket_Window)
	self.basket_product_5_count_apply_btn.clicked.connect(self.func_basket_product_5_count_apply_btn)
	self.basket_product_5_count_apply_btn.setStyleSheet('''QPushButton {font-size: 12px; color: #FFFFFF; border: 1px solid green; background-color: green;}''')
	self.basket_product_5_count_apply_btn.resize(72, 18)
	self.basket_product_5_count_apply_btn.move(664, 352)

	# Стили Удаление
	self.basket_product_5_del = QPushButton('', self.basket_Window)
	self.basket_product_5_del.clicked.connect(self.func_basket_product_5_del)
	self.basket_product_5_del.setStyleSheet('''QPushButton {border: 0; background-image: url(icons/close.png);}''')
	self.basket_product_5_del.resize(32, 32)
	self.basket_product_5_del.move(906, 335)

	# Стили Купить
	self.basket_product_5_buy = QPushButton('', self.basket_Window)
	# self.basket_product_5_buy.clicked.connect(self.func_basket_product_5_buy)
	self.basket_product_5_buy.setStyleSheet('''QPushButton {border: 0; background-image: url(icons/icon_basket_buy.png);}''')
	self.basket_product_5_buy.resize(32, 32)
	self.basket_product_5_buy.move(968, 335)


def basket_product_6_count_del_buy_style(self):
	# Стили Количество
	self.basket_product_6_count = QLineEdit(self.basket_Window)
	self.basket_product_6_count.setStyleSheet('''QLineEdit {font-size: 12px; border: 1px solid #000000;}''')
	self.basket_product_6_count.resize(72, 18)
	self.basket_product_6_count.move(664, 377)
	self.basket_product_6_count_apply_btn = QPushButton('Применить', self.basket_Window)
	self.basket_product_6_count_apply_btn.clicked.connect(self.func_basket_product_6_count_apply_btn)
	self.basket_product_6_count_apply_btn.setStyleSheet('''QPushButton {font-size: 12px; color: #FFFFFF; border: 1px solid green; background-color: green;}''')
	self.basket_product_6_count_apply_btn.resize(72, 18)
	self.basket_product_6_count_apply_btn.move(664, 397)

	# Стили Удаление
	self.basket_product_6_del = QPushButton('', self.basket_Window)
	self.basket_product_6_del.clicked.connect(self.func_basket_product_6_del)
	self.basket_product_6_del.setStyleSheet('''QPushButton {border: 0; background-image: url(icons/close.png);}''')
	self.basket_product_6_del.resize(32, 32)
	self.basket_product_6_del.move(906, 380)

	# Стили Купить
	self.basket_product_6_buy = QPushButton('', self.basket_Window)
	# self.basket_product_6_buy.clicked.connect(self.func_basket_product_6_buy)
	self.basket_product_6_buy.setStyleSheet('''QPushButton {border: 0; background-image: url(icons/icon_basket_buy.png);}''')
	self.basket_product_6_buy.resize(32, 32)
	self.basket_product_6_buy.move(968, 380)


def basket_product_7_count_del_buy_style(self):
	# Стили Количество
	self.basket_product_7_count = QLineEdit(self.basket_Window)
	self.basket_product_7_count.setStyleSheet('''QLineEdit {font-size: 12px; border: 1px solid #000000;}''')
	self.basket_product_7_count.resize(72, 18)
	self.basket_product_7_count.move(664, 422)
	self.basket_product_7_count_apply_btn = QPushButton('Применить', self.basket_Window)
	self.basket_product_7_count_apply_btn.clicked.connect(self.func_basket_product_7_count_apply_btn)
	self.basket_product_7_count_apply_btn.setStyleSheet('''QPushButton {font-size: 12px; color: #FFFFFF; border: 1px solid green; background-color: green;}''')
	self.basket_product_7_count_apply_btn.resize(72, 18)
	self.basket_product_7_count_apply_btn.move(664, 442)

	# Стили Удаление
	self.basket_product_7_del = QPushButton('', self.basket_Window)
	self.basket_product_7_del.clicked.connect(self.func_basket_product_7_del)
	self.basket_product_7_del.setStyleSheet('''QPushButton {border: 0; background-image: url(icons/close.png);}''')
	self.basket_product_7_del.resize(32, 32)
	self.basket_product_7_del.move(906, 425)

	# Стили Купить
	self.basket_product_7_buy = QPushButton('', self.basket_Window)
	# self.basket_product_7_buy.clicked.connect(self.func_basket_product_7_buy)
	self.basket_product_7_buy.setStyleSheet('''QPushButton {border: 0; background-image: url(icons/icon_basket_buy.png);}''')
	self.basket_product_7_buy.resize(32, 32)
	self.basket_product_7_buy.move(968, 425)


def basket_product_8_count_del_buy_style(self):
	# Стили Количество
	self.basket_product_8_count = QLineEdit(self.basket_Window)
	self.basket_product_8_count.setStyleSheet('''QLineEdit {font-size: 12px; border: 1px solid #000000;}''')
	self.basket_product_8_count.resize(72, 18)
	self.basket_product_8_count.move(664, 467)
	self.basket_product_8_count_apply_btn = QPushButton('Применить', self.basket_Window)
	self.basket_product_8_count_apply_btn.clicked.connect(self.func_basket_product_8_count_apply_btn)
	self.basket_product_8_count_apply_btn.setStyleSheet('''QPushButton {font-size: 12px; color: #FFFFFF; border: 1px solid green; background-color: green;}''')
	self.basket_product_8_count_apply_btn.resize(72, 18)
	self.basket_product_8_count_apply_btn.move(664, 487)

	# Стили Удаление
	self.basket_product_8_del = QPushButton('', self.basket_Window)
	self.basket_product_8_del.clicked.connect(self.func_basket_product_8_del)
	self.basket_product_8_del.setStyleSheet('''QPushButton {border: 0; background-image: url(icons/close.png);}''')
	self.basket_product_8_del.resize(32, 32)
	self.basket_product_8_del.move(906, 470)

	# Стили Купить
	self.basket_product_8_buy = QPushButton('', self.basket_Window)
	# self.basket_product_8_buy.clicked.connect(self.func_basket_product_8_buy)
	self.basket_product_8_buy.setStyleSheet('''QPushButton {border: 0; background-image: url(icons/icon_basket_buy.png);}''')
	self.basket_product_8_buy.resize(32, 32)
	self.basket_product_8_buy.move(968, 470)


def basket_product_9_count_del_buy_style(self):
	# Стили Количество
	self.basket_product_9_count = QLineEdit(self.basket_Window)
	self.basket_product_9_count.setStyleSheet('''QLineEdit {font-size: 12px; border: 1px solid #000000;}''')
	self.basket_product_9_count.resize(72, 18)
	self.basket_product_9_count.move(664, 512)
	self.basket_product_9_count_apply_btn = QPushButton('Применить', self.basket_Window)
	self.basket_product_9_count_apply_btn.clicked.connect(self.func_basket_product_9_count_apply_btn)
	self.basket_product_9_count_apply_btn.setStyleSheet('''QPushButton {font-size: 12px; color: #FFFFFF; border: 1px solid green; background-color: green;}''')
	self.basket_product_9_count_apply_btn.resize(72, 18)
	self.basket_product_9_count_apply_btn.move(664, 532)

	# Стили Удаление
	self.basket_product_9_del = QPushButton('', self.basket_Window)
	self.basket_product_9_del.clicked.connect(self.func_basket_product_9_del)
	self.basket_product_9_del.setStyleSheet('''QPushButton {border: 0; background-image: url(icons/close.png);}''')
	self.basket_product_9_del.resize(32, 32)
	self.basket_product_9_del.move(906, 515)

	# Стили Купить
	self.basket_product_9_buy = QPushButton('', self.basket_Window)
	# self.basket_product_9_buy.clicked.connect(self.func_basket_product_9_buy)
	self.basket_product_9_buy.setStyleSheet('''QPushButton {border: 0; background-image: url(icons/icon_basket_buy.png);}''')
	self.basket_product_9_buy.resize(32, 32)
	self.basket_product_9_buy.move(968, 515)


def basket_product_10_count_del_buy_style(self):
	# Стили Количество
	self.basket_product_10_count = QLineEdit(self.basket_Window)
	self.basket_product_10_count.setStyleSheet('''QLineEdit {font-size: 12px; border: 1px solid #000000;}''')
	self.basket_product_10_count.resize(72, 18)
	self.basket_product_10_count.move(664, 557)
	self.basket_product_10_count_apply_btn = QPushButton('Применить', self.basket_Window)
	self.basket_product_10_count_apply_btn.clicked.connect(self.func_basket_product_10_count_apply_btn)
	self.basket_product_10_count_apply_btn.setStyleSheet('''QPushButton {font-size: 12px; color: #FFFFFF; border: 1px solid green; background-color: green;}''')
	self.basket_product_10_count_apply_btn.resize(72, 18)
	self.basket_product_10_count_apply_btn.move(664, 577)

	# Стили Удаление
	self.basket_product_10_del = QPushButton('', self.basket_Window)
	self.basket_product_10_del.clicked.connect(self.func_basket_product_10_del)
	self.basket_product_10_del.setStyleSheet('''QPushButton {border: 0; background-image: url(icons/close.png);}''')
	self.basket_product_10_del.resize(32, 32)
	self.basket_product_10_del.move(906, 560)

	# Стили Купить
	self.basket_product_10_buy = QPushButton('', self.basket_Window)
	# self.basket_product_10_buy.clicked.connect(self.func_basket_product_10_buy)
	self.basket_product_10_buy.setStyleSheet('''QPushButton {border: 0; background-image: url(icons/icon_basket_buy.png);}''')
	self.basket_product_10_buy.resize(32, 32)
	self.basket_product_10_buy.move(968, 560)