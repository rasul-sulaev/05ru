import sys
from os import listdir
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QLabel, QGridLayout, QMainWindow
from PyQt5 import QtGui
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize


class Multi(QMainWindow):
	# Мои функции
	import catalog_menu_btn
	import catalog_menu_btn_active
	import product_1_8_style

	def __init__(self):
		super().__init__()
		self.initUI()


	def initUI(self):
		self.autorization()
		self.setCentralWidget(self.logWindow) # отображение окна Входа
		self.list_basket = []
		self.login_user = ''
		self.basket_count = 0
		self.basket_price = 0
		self.required = QLabel('* :', self)
		self.required.setStyleSheet('QLabel {color: #FF0000}')


		# Настройки QWidget. Отрисовка окна
		self.setGeometry(140, 50, 1060, 700) # (margin-left, margin-top, width, height)
		self.show()


	def logo(self):
		# self.logo_img = QLabel(self.logWindow)
		self.pix = QtGui.QPixmap("icons/logo.png")
		self.logo_img.setPixmap(self.pix)
		self.logo_img.resize(220, 76)
		self.logo_img.move(430, 60)


	def logo_mini(self):
		# self.logo_img = QLabel(self.logWindow)
		self.pix = QtGui.QPixmap("icons/logo_mini.png")
		self.logo_img.setPixmap(self.pix)
		self.logo_img.resize(175, 42)
		self.logo_img.move(15, 15)


	def background_img_window(self):
		self.background_img_pix = QtGui.QPixmap("background_img_window.jpg")
		self.background_img.setPixmap(self.background_img_pix)
		self.background_img.resize(1920, 1080)
		self.background_img.move(0, 0)

	def name_categoriy_window(self):
		self.name_categoriy.setStyleSheet('QLabel {font-size: 24px}')
		self.name_categoriy.move(90, 70)


	def autorization(self):
		self.logWindow = QWidget(self)
		self.setCentralWidget(self.logWindow)
		self.setWindowTitle('App_Shop - Вход в личный кабинет')

		## Login
		self.logo_img = QLabel(self.logWindow)
		self.logo()

		## Autorization
		self.title_log = QLabel('Авторизация', self.logWindow)
		self.title_log.setStyleSheet('QLabel {font-size: 20px}')
		self.title_log.move(480, 180)

		# Поля ввода
		self.loginLabel_log = QLabel('Введите логин :', self.logWindow)
		self.loginInput_log = QLineEdit(self.logWindow)
		self.loginLabel_log.setStyleSheet('QLabel {padding: -2px 5px; color: #FFFFFF; font-size: 13px; border-left: 1.5px solid #6491A3; border-top: 1.5px solid #6491A3; border-top-left-radius: 4px; border-bottom-left-radius: 4px; background-color: #8AAFBF;}')
		self.loginInput_log.setStyleSheet('QLineEdit {padding: -2px 5px; font-size: 14px; border-top: 1.5px solid #979797; border-top-right-radius: 4px; border-bottom-right-radius: 4px; background-color: #C7C7C7;}')
		self.loginLabel_log.resize(152, 30)
		self.loginInput_log.resize(190, 30)
		self.loginLabel_log.move(369, 222)
		self.loginInput_log.move(521, 222)

		self.passwordText_log = QLabel('Введите пароль :', self.logWindow)
		self.passwordInput_log = QLineEdit(self.logWindow)
		self.passwordText_log.setStyleSheet('QLabel {padding: -2px 5px; color: #FFFFFF; font-size: 13px; border-left: 1.5px solid #6491A3; border-top: 1.5px solid #6491A3; border-top-left-radius: 4px; border-bottom-left-radius: 4px; background-color: #8AAFBF;}')
		self.passwordInput_log.setStyleSheet('QLineEdit {padding: -2px 5px; font-size: 14px; border-top: 1.5px solid #979797; border-top-right-radius: 4px; border-bottom-right-radius: 4px; background-color: #C7C7C7;}')
		self.passwordText_log.resize(152, 30)
		self.passwordInput_log.resize(190, 30)
		self.passwordText_log.move(369, 260)
		self.passwordInput_log.move(521, 260)

		# Результат (Ошибки)
		self.resultText_log = QLabel('', self.logWindow)
		self.resultText_log.setStyleSheet('QLabel {color: #FF0000; font-size: 14px;}')
		self.resultText_log.resize(400, 20)

		# Кнопка Вход
		self.btn_log = QPushButton('Войти', self.logWindow)
		self.btn_log.setStyleSheet('''QPushButton {font-size: 14px; color: #FFFFFF; background-color: #ee272d; border: 0; border-radius: 3px; padding: 10px 15px;}
		QPushButton:hover {font-size: 14px; color: #FFFFFF; background-color: #ff0008; padding: 10px 15px;}
		QPushButton:pressed {background-color: #a9070c;}''')
		self.btn_log.clicked.connect(self.form_log) # событие при нажатии
		self.btn_log.resize(160, 38)
		self.btn_log.move(460, 360)

		# Текст с кнопкой для Регистрации
		self.info_regLabel_1_log = QLabel('Если у Вас нет личного кабинета, то', self.logWindow)
		self.info_regLabel_2_log = QLabel('Вам необходимо', self.logWindow)
		self.info_regBtn_log = QPushButton('Зарегистрироваться', self.logWindow)
		self.info_regLabel_1_log.setStyleSheet('''QLabel {font-size: 13px;}''')
		self.info_regLabel_2_log.setStyleSheet('''QLabel {font-size: 13px;}''')
		self.info_regBtn_log.setStyleSheet('''QPushButton {padding-bottom: 0px; background-color: none; font-size: 13px; border: 0; border-bottom: 1px solid black;}
			QPushButton:hover {border-bottom: 1px solid transparent;}''')
		self.info_regBtn_log.clicked.connect(self.registration)
		self.info_regLabel_1_log.move(432, 420)
		self.info_regLabel_2_log.move(428, 438)
		self.info_regBtn_log.move(529, 438)


	def registration(self):
		self.regWindow = QWidget(self)
		self.setCentralWidget(self.regWindow)
		self.setWindowTitle('App_shop - Регистрация личного кабинета')

		## Login
		self.logo_img = QLabel(self.regWindow)
		self.logo()

		## Registration
		self.title_reg = QLabel('Регистрация', self.regWindow)
		self.title_reg.setStyleSheet('QLabel {font-size: 20px}')
		self.title_reg.move(483, 180)

		self.loginLabel_reg = QLabel('Придумайте логин* :', self.regWindow)
		self.loginInput_reg = QLineEdit(self.regWindow)
		self.loginLabel_reg.setStyleSheet('QLabel {padding: -2px 5px; color: #FFFFFF; font-size: 13px; border-left: 1.5px solid #6491A3; border-top: 1.5px solid #6491A3; border-top-left-radius: 4px; border-bottom-left-radius: 4px; background-color: #8AAFBF;}')
		self.loginInput_reg.setStyleSheet('QLineEdit {padding: -2px 5px; font-size: 14px; border-top: 1.5px solid #979797; border-top-right-radius: 4px; border-bottom-right-radius: 4px; background-color: #C7C7C7;}')
		self.loginLabel_reg.resize(152, 30)
		self.loginInput_reg.resize(190, 30)
		self.loginLabel_reg.move(369, 222)
		self.loginInput_reg.move(521, 222)

		self.passwordText_reg = QLabel('Введите пароль* :', self.regWindow)
		self.passwordInput_reg = QLineEdit(self.regWindow)
		self.passwordText_reg.setStyleSheet('QLabel {padding: -2px 5px; color: #FFFFFF; font-size: 13px; border-left: 1.5px solid #6491A3; border-top: 1.5px solid #6491A3; border-top-left-radius: 4px; border-bottom-left-radius: 4px; background-color: #8AAFBF;}')
		self.passwordInput_reg.setStyleSheet('QLineEdit {padding: -2px 5px; font-size: 14px; border-top: 1.5px solid #979797; border-top-right-radius: 4px; border-bottom-right-radius: 4px; background-color: #C7C7C7;}')
		self.passwordText_reg.resize(152, 30)
		self.passwordInput_reg.resize(190, 30)
		self.passwordText_reg.move(369, 260)
		self.passwordInput_reg.move(521, 260)

		self.password2Text_reg = QLabel('Подтвердите пароль* :', self.regWindow)
		self.password2Input_reg = QLineEdit(self.regWindow)
		self.password2Text_reg.setStyleSheet('QLabel {padding: -2px 5px; color: #FFFFFF; font-size: 13px; border-left: 1.5px solid #6491A3; border-top: 1.5px solid #6491A3; border-top-left-radius: 4px; border-bottom-left-radius: 4px; background-color: #8AAFBF;}')
		self.password2Input_reg.setStyleSheet('QLineEdit {padding: -2px 5px; font-size: 14px; border-top: 1.5px solid #979797; border-top-right-radius: 4px; border-bottom-right-radius: 4px; background-color: #C7C7C7;}')
		self.password2Text_reg.resize(152, 30)
		self.password2Input_reg.resize(190, 30)
		self.password2Text_reg.move(369, 298)
		self.password2Input_reg.move(521, 298)

		# Результат (Ошибки)
		self.resultText_reg = QLabel('', self.regWindow)
		self.resultText_reg.setStyleSheet('QLabel {color: #FF0000; font-size: 14px;}')
		self.resultText_reg.resize(400, 20)

		# Кнопка регистрации
		self.btn_reg = QPushButton('Зарегистрироваться', self.regWindow)
		self.btn_reg.setStyleSheet('''QPushButton {font-size: 14px; color: #FFFFFF; background-color: #ee272d; border: 0; border-radius: 3px; padding: 10px 15px;}
		QPushButton:hover {font-size: 14px; color: #FFFFFF; background-color: #ff0008; padding: 10px 15px;}
		QPushButton:pressed {background-color: #a9070c;}''')
		self.btn_reg.clicked.connect(self.form_reg) # событие при нажатии
		self.btn_reg.resize(160, 38)
		self.btn_reg.move(460, 398)

		# Текст с кнопкой для Регистрации
		self.info_regLabel_1_log = QLabel('Если у Вас есть личный кабинет, то', self.regWindow)
		self.info_regLabel_2_log = QLabel('Вам необходимо', self.regWindow)
		self.info_logBtn_reg = QPushButton('Войти', self.regWindow)
		self.info_regLabel_1_log.setStyleSheet('QLabel {font-size: 13px;}')
		self.info_regLabel_2_log.setStyleSheet('QLabel {font-size: 13px;}')
		self.info_logBtn_reg.setStyleSheet('''QPushButton {padding-bottom: 0px; background-color: none; font-size: 13px; border: 0; border-bottom: 1px solid black;}
			QPushButton:hover {border-bottom: 1px solid transparent;}''')
		self.info_logBtn_reg.clicked.connect(self.autorization)
		self.info_regLabel_1_log.move(436, 458)
		self.info_regLabel_2_log.move(472, 476)
		self.info_logBtn_reg.move(574, 476)


	def search_products(self):
		## Поиск
		# self.search_Input_shop = QLineEdit('Быстрый поиск', self)
		# self.search_Btn_shop = QPushButton('Найти', self)
		self.search_Btn_shop.setIcon(QIcon('icons/icon_search.png'))
		self.search_Btn_shop.setIconSize(QSize(20, 20))
		self.search_Input_shop.setStyleSheet('QLineEdit {font-size: 14px; padding-left: 8px; padding-right: 8px;}')
		self.search_Input_shop.resize(350, 40)
		self.search_Btn_shop.resize(46, 42)
		self.search_Input_shop.move(248, 15)
		self.search_Btn_shop.move(596, 14)


	def add_to_basket(self):
		'''Функция для отрисовки мини корзины, а так же для добавления суммы и кол-ва товаров в мини корзину'''
		#  Если у данного пользователия нет файла с корзиной, то создает
		if ((self.login_user + '_list_basket.txt') not in listdir()):
			new_user = open(self.login_user + '_list_basket.txt', 'w')
			new_user.close()

		# Сетчик суммы и кол-ва товаров в Корзине пользователя
		list_of_produtcs_backet_user = open(self.login_user + '_list_basket.txt', 'r')
		list_of_produtcs_backet = list_of_produtcs_backet_user.read()
		if (list_of_produtcs_backet.count(';') > 0):
			list_of_produtcs_backet = list_of_produtcs_backet.split(';')

			basket_count_user = 0 # Количество товаров пользователя в корзине
			basket_price_sum_user = 0 # Общая сумма на все товары в корзине

			i = 0
			while True:
				basket_count_user += int(list_of_produtcs_backet[i].split(':')[3])
				basket_price_sum_user += int(list_of_produtcs_backet[i].split(':')[4])

				i += 1
				if (i >= len(list_of_produtcs_backet) - 1):
					break

			if (basket_price_sum_user > 0):
				self.basket_price_label.setText( str(basket_price_sum_user)  + ' руб')
			if (basket_count_user == 0):
				self.basket_count_label.setText('Нет товаров')
				self.basket_price_label.setText('')
			elif (basket_count_user == 1):
				self.basket_count_label.setText( str(basket_count_user) + ' товар')
			elif (basket_count_user < 5):
				self.basket_count_label.setText( str(basket_count_user) + ' товара')
			elif (basket_count_user >= 5):
				self.basket_count_label.setText( str(basket_count_user) + ' товаров')

		# Стиллизация для мини Корзины
			self.basket_count_label.setStyleSheet('QLabel {font-size: 12px}')
			self.basket_price_label.setStyleSheet('QLabel {font-size: 15px; text-decoration: underline;}')
			self.basket_count_label.move(914, 16)
			self.basket_price_label.move(914, 33)

		elif (list_of_produtcs_backet.count('')):
			self.basket_count_label.setStyleSheet('QLabel {font-size: 16px}')
			self.basket_price_label.setStyleSheet('QLabel {font-size: 14px}')
			self.basket_count_label.move(914, 12)
			self.basket_price_label.move(914, 34)

		# self.basket_Btn = QPushButton('', self)
		# self.basket_Btn.clicked.connect(self...)
		self.basket_Btn.setIcon(QIcon('icons/icon_basket.png'))
		self.basket_Btn.setIconSize(QSize(25, 25))
		self.basket_count_label.resize(460, 22)
		self.basket_price_label.resize(460, 22)
		self.basket_Btn.resize(46, 42)
		self.basket_Btn.move(860, 12)

		list_of_produtcs_backet_user.close()


	def catalog_shop(self):
		self.shopWindow = QWidget(self)
		self.setCentralWidget(self.shopWindow)
		self.setWindowTitle('App_Shop - Добро пожаловать в Интернет-магазин!')

		# Белый фон
		self.background_img = QLabel(self.shopWindow)
		self.background_img_window()

		# Лого мини
		self.logo_img = QLabel(self.shopWindow)
		self.logo_mini()

		# Корзина
		self.basket_Btn = QPushButton('', self.shopWindow)
		self.basket_Btn.clicked.connect(self.basket_big_window)
		if (self.basket_price > 0):
			self.basket_price_label = QLabel(str(self.basket_price) + ' руб', self.shopWindow)
		if (self.basket_count == 0):
			self.basket_count_label = QLabel('В корзине', self.shopWindow)
			self.basket_price_label = QLabel('нет товаров', self.shopWindow)
		elif (self.basket_count == 1):
			self.basket_count_label = QLabel(str(self.basket_count) + ' товар', self.shopWindow)
		elif (self.basket_count < 5):
			self.basket_count_label = QLabel(str(self.basket_count) + ' товара', self.shopWindow)
		elif (self.basket_count >= 5):
			self.basket_count_label = QLabel(str(self.basket_count) + ' товаров', self.shopWindow)
		self.add_to_basket()

		# Поиск
		self.search_Input_shop = QLineEdit('Быстрый поиск', self.shopWindow)
		self.search_Btn_shop = QPushButton('', self.shopWindow)
		self.search_products()

		# Название категории
		self.name_categoriy = QLabel('Добро пожаловать в Интернет-магазин - App_Shop', self.shopWindow)
		self.name_categoriy_window()

		# Левый sidebar-catalog_menu
		self.btn_catalog_auto = QPushButton(self.shopWindow)
		self.btn_catalog_games = QPushButton(self.shopWindow)
		self.btn_catalog_beauty = QPushButton(self.shopWindow)
		self.btn_catalog_remont = QPushButton(self.shopWindow)
		self.btn_catalog_network = QPushButton(self.shopWindow)
		self.btn_catalog_forHome = QPushButton(self.shopWindow)
		self.btn_catalog_cameras = QPushButton(self.shopWindow)
		self.btn_catalog_portativ = QPushButton(self.shopWindow)
		self.btn_catalog_computers = QPushButton(self.shopWindow)
		self.btn_catalog_audioVideo = QPushButton(self.shopWindow)
		self.btn_catalog_climateControl = QPushButton(self.shopWindow)
		self.btn_catalog_ucenennyeTovary = QPushButton(self.shopWindow)
		self.catalog_menu_btn.menu_btn(self)

		# Каталог магазина


	def basket_product_1(self):
		list_basket_array = open(self.login_user + '_list_basket.txt', 'r')
		list_of_data_basket = list_basket_array.read()

		# Работает если в корзине есть хоть один товар
		if (list_of_data_basket.count(';') > 0	):
			list_of_data_basket_a = list_of_data_basket.split(';')
			print( list_of_data_basket_a )

			i = 0
			while True:
				list_of_data_basket_b = list_of_data_basket_a[i]
				list_of_data_basket_w = list_of_data_basket_b.split(':')

				# Если в корзине 10 товаров, то выводит "Корзина переполнена"
				if (list_of_data_basket.count(';') == 10):
					print('Корзина переполнена!!!')
					break
				# Если в корзине есть Данный товар, то к товару добавляются Кол-во и Цена
				elif (list_of_data_basket.count(self.product_1_name.text()) > 0):
					print('Такой товар есть в корзине')
					break
				# Если в корзине нет Данного товара, то в конец корзины добавится товар
				elif (list_of_data_basket.count(self.product_1_name.text()) == 0):
					list_of_produtcs_basket = open(self.login_user + '_list_basket.txt', 'a')
					list_of_produtcs_basket.write(self.product_1_img + ':' + self.product_1_name.text() + ':' + self.product_1_price_int + ':' + self.product_1_count.text() + ':' + self.product_1_price_sum + ';')
					list_of_produtcs_basket.close()
					break

				i += 1
				if (i >= len(list_of_data_basket_a) ):
					break

		# Если в корзине нет товаров, то добавляется первый товар методом -w
		elif (list_of_data_basket.count(';') == 0):
			list_of_produtcs_basket = open(self.login_user + '_list_basket.txt', 'w')
			list_of_produtcs_basket.write(self.product_1_img + ':' + self.product_1_name.text() + ':' + self.product_1_price_int + ':' + self.product_1_count.text() + ':' + self.product_1_price_sum + ';')
			list_of_produtcs_basket.close()

		list_basket_array.close()
		self.add_to_basket()


	def basket_product_2(self):
		list_basket_array = open(self.login_user + '_list_basket.txt', 'r')
		list_of_data_basket = list_basket_array.read()

		# Работает если в корзине есть хоть один товар
		if (list_of_data_basket.count(';') > 0	):
			list_of_data_basket_a = list_of_data_basket.split(';')
			print( list_of_data_basket_a )

			i = 0
			while True:
				list_of_data_basket_b = list_of_data_basket_a[i]
				list_of_data_basket_w = list_of_data_basket_b.split(':')

				# Если в корзине 10 товаров, то выводит "Корзина переполнена"
				if (list_of_data_basket.count(';') == 10):
					print('Корзина переполнена!!!')
					break
				# Если в корзине есть Данный товар, то к товару добавляются Кол-во и Цена
				elif (list_of_data_basket.count(self.product_2_name.text()) > 0):
					print('Такой товар есть в корзине')
					break
				# Если в корзине нет Данного товара, то в конец корзины добавится товар
				elif (list_of_data_basket.count(self.product_2_name.text()) == 0):
					list_of_produtcs_basket = open(self.login_user + '_list_basket.txt', 'a')
					list_of_produtcs_basket.write(self.product_2_img + ':' + self.product_2_name.text() + ':' + self.product_2_price_int + ':' + self.product_2_count.text() + ':' + self.product_2_price_sum + ';')
					list_of_produtcs_basket.close()
					break

				i += 1
				if (i >= len(list_of_data_basket_a) ):
					break

		# Если в корзине нет товаров, то добавляется первый товар методом -w
		elif (list_of_data_basket.count(';') == 0):
			list_of_produtcs_basket = open(self.login_user + '_list_basket.txt', 'w')
			list_of_produtcs_basket.write(self.product_2_img + ':' + self.product_2_name.text() + ':' + self.product_2_price_int + ':' + self.product_2_count.text() + ':' + self.product_2_price_sum + ';')
			list_of_produtcs_basket.close()

		list_basket_array.close()
		self.add_to_basket()


	def basket_product_3(self):
		list_basket_array = open(self.login_user + '_list_basket.txt', 'r')
		list_of_data_basket = list_basket_array.read()

		# Работает если в корзине есть хоть один товар
		if (list_of_data_basket.count(';') > 0	):
			list_of_data_basket_a = list_of_data_basket.split(';')
			print( list_of_data_basket_a )

			i = 0
			while True:
				list_of_data_basket_b = list_of_data_basket_a[i]
				list_of_data_basket_w = list_of_data_basket_b.split(':')

				# Если в корзине 10 товаров, то выводит "Корзина переполнена"
				if (list_of_data_basket.count(';') == 10):
					print('Корзина переполнена!!!')
					break
				# Если в корзине есть Данный товар, то к товару добавляются Кол-во и Цена
				elif (list_of_data_basket.count(self.product_3_name.text()) > 0):
					print('Такой товар есть в корзине')
					break
				# Если в корзине нет Данного товара, то в конец корзины добавится товар
				elif (list_of_data_basket.count(self.product_3_name.text()) == 0):
					list_of_produtcs_basket = open(self.login_user + '_list_basket.txt', 'a')
					list_of_produtcs_basket.write(self.product_3_img + ':' + self.product_3_name.text() + ':' + self.product_3_price_int + ':' + self.product_3_count.text() + ':' + self.product_3_price_sum + ';')
					list_of_produtcs_basket.close()
					break

				i += 1
				if (i >= len(list_of_data_basket_a) ):
					break

		# Если в корзине нет товаров, то добавляется первый товар методом -w
		elif (list_of_data_basket.count(';') == 0):
			list_of_produtcs_basket = open(self.login_user + '_list_basket.txt', 'w')
			list_of_produtcs_basket.write(self.product_3_img + ':' + self.product_3_name.text() + ':' + self.product_3_price_int + ':' + self.product_3_count.text() + ':' + self.product_3_price_sum + ';')
			list_of_produtcs_basket.close()

		list_basket_array.close()
		self.add_to_basket()

	def basket_product_4(self):
		list_basket_array = open(self.login_user + '_list_basket.txt', 'r')
		list_of_data_basket = list_basket_array.read()

		# Работает если в корзине есть хоть один товар
		if (list_of_data_basket.count(';') > 0	):
			list_of_data_basket_a = list_of_data_basket.split(';')
			print( list_of_data_basket_a )

			i = 0
			while True:
				list_of_data_basket_b = list_of_data_basket_a[i]
				list_of_data_basket_w = list_of_data_basket_b.split(':')

				# Если в корзине 10 товаров, то выводит "Корзина переполнена"
				if (list_of_data_basket.count(';') == 10):
					print('Корзина переполнена!!!')
					break
				# Если в корзине есть Данный товар, то к товару добавляются Кол-во и Цена
				elif (list_of_data_basket.count(self.product_4_name.text()) > 0):
					print('Такой товар есть в корзине')
					break
				# Если в корзине нет Данного товара, то в конец корзины добавится товар
				elif (list_of_data_basket.count(self.product_4_name.text()) == 0):
					list_of_produtcs_basket = open(self.login_user + '_list_basket.txt', 'a')
					list_of_produtcs_basket.write(self.product_4_img + ':' + self.product_4_name.text() + ':' + self.product_4_price_int + ':' + self.product_4_count.text() + ':' + self.product_4_price_sum + ';')
					list_of_produtcs_basket.close()
					break

				i += 1
				if (i >= len(list_of_data_basket_a) ):
					break

		# Если в корзине нет товаров, то добавляется первый товар методом -w
		elif (list_of_data_basket.count(';') == 0):
			list_of_produtcs_basket = open(self.login_user + '_list_basket.txt', 'w')
			list_of_produtcs_basket.write(self.product_4_img + ':' + self.product_4_name.text() + ':' + self.product_4_price_int + ':' + self.product_4_count.text() + ':' + self.product_4_price_sum + ';')
			list_of_produtcs_basket.close()

		list_basket_array.close()
		self.add_to_basket()

	def basket_product_5(self):
		list_basket_array = open(self.login_user + '_list_basket.txt', 'r')
		list_of_data_basket = list_basket_array.read()

		# Работает если в корзине есть хоть один товар
		if (list_of_data_basket.count(';') > 0	):
			list_of_data_basket_a = list_of_data_basket.split(';')
			print( list_of_data_basket_a )

			i = 0
			while True:
				list_of_data_basket_b = list_of_data_basket_a[i]
				list_of_data_basket_w = list_of_data_basket_b.split(':')

				# Если в корзине 10 товаров, то выводит "Корзина переполнена"
				if (list_of_data_basket.count(';') == 10):
					print('Корзина переполнена!!!')
					break
				# Если в корзине есть Данный товар, то к товару добавляются Кол-во и Цена
				elif (list_of_data_basket.count(self.product_5_name.text()) > 0):
					print('Такой товар есть в корзине')
					break
				# Если в корзине нет Данного товара, то в конец корзины добавится товар
				elif (list_of_data_basket.count(self.product_5_name.text()) == 0):
					list_of_produtcs_basket = open(self.login_user + '_list_basket.txt', 'a')
					list_of_produtcs_basket.write(self.product_5_img + ':' + self.product_5_name.text() + ':' + self.product_5_price_int + ':' + self.product_5_count.text() + ':' + self.product_5_price_sum + ';')
					list_of_produtcs_basket.close()
					break

				i += 1
				if (i >= len(list_of_data_basket_a) ):
					break

		# Если в корзине нет товаров, то добавляется первый товар методом -w
		elif (list_of_data_basket.count(';') == 0):
			list_of_produtcs_basket = open(self.login_user + '_list_basket.txt', 'w')
			list_of_produtcs_basket.write(self.product_5_img + ':' + self.product_5_name.text() + ':' + self.product_5_price_int + ':' + self.product_5_count.text() + ':' + self.product_5_price_sum + ';')
			list_of_produtcs_basket.close()

		list_basket_array.close()
		self.add_to_basket()

	def basket_product_6(self):
		list_basket_array = open(self.login_user + '_list_basket.txt', 'r')
		list_of_data_basket = list_basket_array.read()

		# Работает если в корзине есть хоть один товар
		if (list_of_data_basket.count(';') > 0	):
			list_of_data_basket_a = list_of_data_basket.split(';')
			print( list_of_data_basket_a )

			i = 0
			while True:
				list_of_data_basket_b = list_of_data_basket_a[i]
				list_of_data_basket_w = list_of_data_basket_b.split(':')

				# Если в корзине 10 товаров, то выводит "Корзина переполнена"
				if (list_of_data_basket.count(';') == 10):
					print('Корзина переполнена!!!')
					break
				# Если в корзине есть Данный товар, то к товару добавляются Кол-во и Цена
				elif (list_of_data_basket.count(self.product_6_name.text()) > 0):
					print('Такой товар есть в корзине')
					break
				# Если в корзине нет Данного товара, то в конец корзины добавится товар
				elif (list_of_data_basket.count(self.product_6_name.text()) == 0):
					list_of_produtcs_basket = open(self.login_user + '_list_basket.txt', 'a')
					list_of_produtcs_basket.write(self.product_6_img + ':' + self.product_6_name.text() + ':' + self.product_6_price_int + ':' + self.product_6_count.text() + ':' + self.product_6_price_sum + ';')
					list_of_produtcs_basket.close()
					break

				i += 1
				if (i >= len(list_of_data_basket_a) ):
					break

		# Если в корзине нет товаров, то добавляется первый товар методом -w
		elif (list_of_data_basket.count(';') == 0):
			list_of_produtcs_basket = open(self.login_user + '_list_basket.txt', 'w')
			list_of_produtcs_basket.write(self.product_6_img + ':' + self.product_6_name.text() + ':' + self.product_6_price_int + ':' + self.product_6_count.text() + ':' + self.product_6_price_sum + ';')
			list_of_produtcs_basket.close()

		list_basket_array.close()
		self.add_to_basket()

	def basket_product_7(self):
		list_basket_array = open(self.login_user + '_list_basket.txt', 'r')
		list_of_data_basket = list_basket_array.read()

		# Работает если в корзине есть хоть один товар
		if (list_of_data_basket.count(';') > 0	):
			list_of_data_basket_a = list_of_data_basket.split(';')
			print( list_of_data_basket_a )

			i = 0
			while True:
				list_of_data_basket_b = list_of_data_basket_a[i]
				list_of_data_basket_w = list_of_data_basket_b.split(':')

				# Если в корзине 10 товаров, то выводит "Корзина переполнена"
				if (list_of_data_basket.count(';') == 10):
					print('Корзина переполнена!!!')
					break
				# Если в корзине есть Данный товар, то к товару добавляются Кол-во и Цена
				elif (list_of_data_basket.count(self.product_7_name.text()) > 0):
					print('Такой товар есть в корзине')
					break
				# Если в корзине нет Данного товара, то в конец корзины добавится товар
				elif (list_of_data_basket.count(self.product_7_name.text()) == 0):
					list_of_produtcs_basket = open(self.login_user + '_list_basket.txt', 'a')
					list_of_produtcs_basket.write(self.product_7_img + ':' + self.product_7_name.text() + ':' + self.product_7_price_int + ':' + self.product_7_count.text() + ':' + self.product_7_price_sum + ';')
					list_of_produtcs_basket.close()
					break

				i += 1
				if (i >= len(list_of_data_basket_a) ):
					break

		# Если в корзине нет товаров, то добавляется первый товар методом -w
		elif (list_of_data_basket.count(';') == 0):
			list_of_produtcs_basket = open(self.login_user + '_list_basket.txt', 'w')
			list_of_produtcs_basket.write(self.product_7_img + ':' + self.product_7_name.text() + ':' + self.product_7_price_int + ':' + self.product_7_count.text() + ':' + self.product_7_price_sum + ';')
			list_of_produtcs_basket.close()

		list_basket_array.close()
		self.add_to_basket()

	def basket_product_8(self):
		list_basket_array = open(self.login_user + '_list_basket.txt', 'r')
		list_of_data_basket = list_basket_array.read()

		# Работает если в корзине есть хоть один товар
		if (list_of_data_basket.count(';') > 0	):
			list_of_data_basket_a = list_of_data_basket.split(';')
			print( list_of_data_basket_a )

			i = 0
			while True:
				list_of_data_basket_b = list_of_data_basket_a[i]
				list_of_data_basket_w = list_of_data_basket_b.split(':')

				# Если в корзине 10 товаров, то выводит "Корзина переполнена"
				if (list_of_data_basket.count(';') == 10):
					print('Корзина переполнена!!!')
					break
				# Если в корзине есть Данный товар, то к товару добавляются Кол-во и Цена
				elif (list_of_data_basket.count(self.product_8_name.text()) > 0):
					print('Такой товар есть в корзине')
					break
				# Если в корзине нет Данного товара, то в конец корзины добавится товар
				elif (list_of_data_basket.count(self.product_8_name.text()) == 0):
					list_of_produtcs_basket = open(self.login_user + '_list_basket.txt', 'a')
					list_of_produtcs_basket.write(self.product_8_img + ':' + self.product_8_name.text() + ':' + self.product_8_price_int + ':' + self.product_8_count.text() + ':' + self.product_8_price_sum + ';')
					list_of_produtcs_basket.close()
					break

				i += 1
				if (i >= len(list_of_data_basket_a) ):
					break

		# Если в корзине нет товаров, то добавляется первый товар методом -w
		elif (list_of_data_basket.count(';') == 0):
			list_of_produtcs_basket = open(self.login_user + '_list_basket.txt', 'w')
			list_of_produtcs_basket.write(self.product_8_img + ':' + self.product_8_name.text() + ':' + self.product_8_price_int + ':' + self.product_8_count.text() + ':' + self.product_8_price_sum + ';')
			list_of_produtcs_basket.close()

		list_basket_array.close()
		self.add_to_basket()


	def product(self):
		# Фоновая белая картинка для продукта
		# self.product_bg_img = QLabel(self)
		self.product_bg_pix = QtGui.QPixmap("product_bg_img.jpg")
		self.product_bg_img.setPixmap(self.product_bg_pix)
		self.product_bg_img.resize(200, 263)

		# Картинка продукта
		# self.product_img = QLabel(self)
		# self.product_pix = QtGui.QPixmap("product_1.jpg")
		self.product_img.setPixmap(self.product_pix)
		self.product_img.resize(180, 150)


	def basket_big_window(self):
		self.basket_Window = QWidget(self)
		self.setCentralWidget(self.basket_Window)

		# Белый фон
		self.background_img = QLabel(self.basket_Window)
		self.background_img_window()

		# Лого мини
		self.logo_img = QLabel(self.basket_Window)
		self.logo_mini()

		# Поиск
		self.search_Input_shop = QLineEdit('Быстрый поиск', self.basket_Window)
		self.search_Btn_shop = QPushButton('', self.basket_Window)
		self.search_products()

		# Название категории
		self.name_categoriy = QLabel('В корзине нет товаров', self.basket_Window)
		self.name_categoriy_window()

		# Левый sidebar-catalog_menu_btn
		self.btn_catalog_auto = QPushButton(self.basket_Window)
		self.btn_catalog_games = QPushButton(self.basket_Window)
		self.btn_catalog_beauty = QPushButton(self.basket_Window)
		self.btn_catalog_remont = QPushButton(self.basket_Window)
		self.btn_catalog_network = QPushButton(self.basket_Window)
		self.btn_catalog_forHome = QPushButton(self.basket_Window)
		self.btn_catalog_cameras = QPushButton(self.basket_Window)
		self.btn_catalog_portativ = QPushButton(self.basket_Window)
		self.btn_catalog_computers = QPushButton(self.basket_Window)
		self.btn_catalog_audioVideo = QPushButton(self.basket_Window)
		self.btn_catalog_climateControl = QPushButton(self.basket_Window)
		self.btn_catalog_ucenennyeTovary = QPushButton(self.basket_Window)
		self.catalog_menu_btn.menu_btn(self)

		# Таблица Корзины
		self.basket_product_num = QLabel('№', self.basket_Window)
		self.basket_product_num.setStyleSheet('''QLabel {font-size: 14px; color: #FFFFFF; border: 1px solid #000000; border-top-left-radius: 4px; background-color: #EE272D;}''')
		self.basket_product_num.resize(40, 34)
		self.basket_product_num.move(90, 115)

		self.basket_product_img = QLabel('Картинка', self.basket_Window)
		self.basket_product_img.setStyleSheet('''QLabel {font-size: 14px; color: #FFFFFF; border: 1px solid #000000; background-color: #EE272D;}''')
		self.basket_product_img.resize(80, 34)
		self.basket_product_img.move(130, 115)

		self.basket_product_name = QLabel('Название товара', self.basket_Window)
		self.basket_product_name.setStyleSheet('''QLabel {font-size: 14px; color: #FFFFFF; border: 1px solid #000000; background-color: #EE272D;}''')
		self.basket_product_name.resize(350, 34)
		self.basket_product_name.move(210, 115)

		self.basket_product_price = QLabel('Цена', self.basket_Window)
		self.basket_product_price.setStyleSheet('''QLabel {font-size: 14px; color: #FFFFFF; border: 1px solid #000000; background-color: #EE272D;}''')
		self.basket_product_price.resize(100, 34)
		self.basket_product_price.move(560, 115)

		self.basket_product_count = QLabel('Кол-во', self.basket_Window)
		self.basket_product_count.setStyleSheet('''QLabel {font-size: 14px; color: #FFFFFF; border: 1px solid #000000; background-color: #EE272D;}''')
		self.basket_product_count.resize(80, 34)
		self.basket_product_count.move(660, 115)

		self.basket_product_price_sum = QLabel('Сумма', self.basket_Window)
		self.basket_product_price_sum.setStyleSheet('''QLabel {font-size: 14px; color: #FFFFFF; border: 1px solid #000000; background-color: #EE272D;}''')
		self.basket_product_price_sum.resize(150, 34)
		self.basket_product_price_sum.move(740, 115)

		self.basket_product_del_block = QLabel('Удалить', self.basket_Window)
		self.basket_product_del_block.setStyleSheet('''QLabel {font-size: 14px; color: #FFFFFF; border: 1px solid #000000; background-color: #EE272D;}''')
		self.basket_product_del_block.resize(64, 34)
		self.basket_product_del_block.move(890, 115)

		self.basket_product_buy = QLabel('Купить', self.basket_Window)
		self.basket_product_buy.setStyleSheet('''QLabel {font-size: 14px; color: #FFFFFF; border: 1px solid #000000; border-top-right-radius: 4px; background-color: #EE272D;}''')
		self.basket_product_buy.resize(60, 34)
		self.basket_product_buy.move(954, 115)


		self.basket_product_1_num = QLabel('1', self.basket_Window)
		self.basket_product_1_num.setStyleSheet('''QLabel {font-size: 14px; border: 1px solid #000000;}''')
		self.basket_product_1_num.resize(40, 46)
		self.basket_product_1_num.move(90, 148)

		self.basket_product_1_img_block = QLabel('', self.basket_Window)
		self.basket_product_1_img_block.setStyleSheet('''QLabel {font-size: 14px; border: 1px solid #000000;}''')
		self.basket_product_1_img_block.resize(80, 46)
		self.basket_product_1_img_block.move(130, 148)
		self.basket_product_1_img = QLabel(self.basket_Window)
		# self.basket_product_1_img_pix = QtGui.QPixmap("img/portativ/apple_iphone_x_64gb_silver.jpg")
		# self.basket_product_1_img.setPixmap(self.basket_product_1_img_pix)
		self.basket_product_1_img.resize(70, 40)
		self.basket_product_1_img.move(135, 151)

		self.basket_product_1_name = QLabel('', self.basket_Window)
		self.basket_product_1_name.setStyleSheet('''QLabel {font-size: 14px; border: 1px solid #000000;}''')
		self.basket_product_1_name.resize(350, 46)
		self.basket_product_1_name.move(210, 148)

		self.basket_product_1_price = QLabel('', self.basket_Window)
		self.basket_product_1_price.setStyleSheet('''QLabel {font-size: 14px; border: 1px solid #000000;}''')
		self.basket_product_1_price.resize(100, 46)
		self.basket_product_1_price.move(560, 148)

		self.basket_product_1_count_block = QLabel('', self.basket_Window)
		self.basket_product_1_count_block.setStyleSheet('''QLabel {font-size: 14px; border: 1px solid #000000;}''')
		self.basket_product_1_count_block.resize(80, 46)
		self.basket_product_1_count_block.move(660, 148)

		self.basket_product_1_price_sum = QLabel('', self.basket_Window)
		self.basket_product_1_price_sum.setStyleSheet('''QLabel {font-size: 14px; border: 1px solid #000000;}''')
		self.basket_product_1_price_sum.resize(150, 46)
		self.basket_product_1_price_sum.move(740, 148)

		self.basket_product_1_del_block = QLabel('', self.basket_Window)
		self.basket_product_1_del_block.setStyleSheet('''QLabel {font-size: 14px; border: 1px solid #000000;}''')
		self.basket_product_1_del_block.resize(64, 46)
		self.basket_product_1_del_block.move(890, 148)

		self.basket_product_1_buy_block = QLabel('', self.basket_Window)
		self.basket_product_1_buy_block.setStyleSheet('''QLabel {font-size: 14px; border: 1px solid #000000;}''')
		self.basket_product_1_buy_block.resize(60, 46)
		self.basket_product_1_buy_block.move(954, 148)


		self.basket_product_2_num = QLabel('2', self.basket_Window)
		self.basket_product_2_num.setStyleSheet('''QLabel {font-size: 14px; border: 1px solid #000000;}''')
		self.basket_product_2_num.resize(40, 46)
		self.basket_product_2_num.move(90, 193)

		self.basket_product_2_img_block = QLabel('', self.basket_Window)
		self.basket_product_2_img_block.setStyleSheet('''QLabel {font-size: 14px; border: 1px solid #000000;}''')
		self.basket_product_2_img_block.resize(80, 46)
		self.basket_product_2_img_block.move(130, 193)
		self.basket_product_2_img = QLabel(self.basket_Window)
		self.basket_product_2_img.resize(70, 40)
		self.basket_product_2_img.move(135, 196)

		self.basket_product_2_name = QLabel('', self.basket_Window)
		self.basket_product_2_name.setStyleSheet('''QLabel {font-size: 14px; border: 1px solid #000000;}''')
		self.basket_product_2_name.resize(350, 46)
		self.basket_product_2_name.move(210, 193)

		self.basket_product_2_price = QLabel('', self.basket_Window)
		self.basket_product_2_price.setStyleSheet('''QLabel {font-size: 14px; border: 1px solid #000000;}''')
		self.basket_product_2_price.resize(100, 46)
		self.basket_product_2_price.move(560, 193)

		self.basket_product_2_count_block = QLabel('', self.basket_Window)
		self.basket_product_2_count_block.setStyleSheet('''QLabel {font-size: 14px; border: 1px solid #000000;}''')
		self.basket_product_2_count_block.resize(80, 46)
		self.basket_product_2_count_block.move(660, 193)

		self.basket_product_2_price_sum = QLabel('', self.basket_Window)
		self.basket_product_2_price_sum.setStyleSheet('''QLabel {font-size: 14px; border: 1px solid #000000;}''')
		self.basket_product_2_price_sum.resize(150, 46)
		self.basket_product_2_price_sum.move(740, 193)

		self.basket_product_2_del_block = QLabel('', self.basket_Window)
		self.basket_product_2_del_block.setStyleSheet('''QLabel {font-size: 14px; border: 1px solid #000000;}''')
		self.basket_product_2_del_block.resize(64, 46)
		self.basket_product_2_del_block.move(890, 193)

		self.basket_product_2_buy_block = QLabel('', self.basket_Window)
		self.basket_product_2_buy_block.setStyleSheet('''QLabel {font-size: 14px; border: 1px solid #000000;}''')
		self.basket_product_2_buy_block.resize(60, 46)
		self.basket_product_2_buy_block.move(954, 193)


		self.basket_product_3_num = QLabel('3', self.basket_Window)
		self.basket_product_3_num.setStyleSheet('''QLabel {font-size: 14px; border: 1px solid #000000;}''')
		self.basket_product_3_num.resize(40, 46)
		self.basket_product_3_num.move(90, 238)

		self.basket_product_3_img_block = QLabel('', self.basket_Window)
		self.basket_product_3_img_block.setStyleSheet('''QLabel {font-size: 14px; border: 1px solid #000000;}''')
		self.basket_product_3_img_block.resize(80, 46)
		self.basket_product_3_img_block.move(130, 238)
		self.basket_product_3_img = QLabel(self.basket_Window)
		self.basket_product_3_img.resize(70, 40)
		self.basket_product_3_img.move(135, 241)

		self.basket_product_3_name = QLabel('', self.basket_Window)
		self.basket_product_3_name.setStyleSheet('''QLabel {font-size: 14px; border: 1px solid #000000;}''')
		self.basket_product_3_name.resize(350, 46)
		self.basket_product_3_name.move(210, 238)

		self.basket_product_3_price = QLabel('', self.basket_Window)
		self.basket_product_3_price.setStyleSheet('''QLabel {font-size: 14px; border: 1px solid #000000;}''')
		self.basket_product_3_price.resize(100, 46)
		self.basket_product_3_price.move(560, 238)

		self.basket_product_3_count_block = QLabel('', self.basket_Window)
		self.basket_product_3_count_block.setStyleSheet('''QLabel {font-size: 14px; border: 1px solid #000000;}''')
		self.basket_product_3_count_block.resize(80, 46)
		self.basket_product_3_count_block.move(660, 238)

		self.basket_product_3_price_sum = QLabel('', self.basket_Window)
		self.basket_product_3_price_sum.setStyleSheet('''QLabel {font-size: 14px; border: 1px solid #000000;}''')
		self.basket_product_3_price_sum.resize(150, 46)
		self.basket_product_3_price_sum.move(740, 238)

		self.basket_product_3_del_block = QLabel('', self.basket_Window)
		self.basket_product_3_del_block.setStyleSheet('''QLabel {font-size: 14px; border: 1px solid #000000;}''')
		self.basket_product_3_del_block.resize(64, 46)
		self.basket_product_3_del_block.move(890, 238)

		self.basket_product_3_buy_block = QLabel('', self.basket_Window)
		self.basket_product_3_buy_block.setStyleSheet('''QLabel {font-size: 14px; border: 1px solid #000000;}''')
		self.basket_product_3_buy_block.resize(60, 46)
		self.basket_product_3_buy_block.move(954, 238)


		self.basket_product_4_num = QLabel('4', self.basket_Window)
		self.basket_product_4_num.setStyleSheet('''QLabel {font-size: 14px; border: 1px solid #000000;}''')
		self.basket_product_4_num.resize(40, 46)
		self.basket_product_4_num.move(90, 283)

		self.basket_product_4_img_block = QLabel('', self.basket_Window)
		self.basket_product_4_img_block.setStyleSheet('''QLabel {font-size: 14px; border: 1px solid #000000;}''')
		self.basket_product_4_img_block.resize(80, 46)
		self.basket_product_4_img_block.move(130, 283)
		self.basket_product_4_img = QLabel(self.basket_Window)
		self.basket_product_4_img.resize(70, 40)
		self.basket_product_4_img.move(135, 286)

		self.basket_product_4_name = QLabel('', self.basket_Window)
		self.basket_product_4_name.setStyleSheet('''QLabel {font-size: 14px; border: 1px solid #000000;}''')
		self.basket_product_4_name.resize(350, 46)
		self.basket_product_4_name.move(210, 283)

		self.basket_product_4_price = QLabel('', self.basket_Window)
		self.basket_product_4_price.setStyleSheet('''QLabel {font-size: 14px; border: 1px solid #000000;}''')
		self.basket_product_4_price.resize(100, 46)
		self.basket_product_4_price.move(560, 283)

		self.basket_product_4_count_block = QLabel('', self.basket_Window)
		self.basket_product_4_count_block.setStyleSheet('''QLabel {font-size: 14px; border: 1px solid #000000;}''')
		self.basket_product_4_count_block.resize(80, 46)
		self.basket_product_4_count_block.move(660, 283)

		self.basket_product_4_price_sum = QLabel('', self.basket_Window)
		self.basket_product_4_price_sum.setStyleSheet('''QLabel {font-size: 14px; border: 1px solid #000000;}''')
		self.basket_product_4_price_sum.resize(150, 46)
		self.basket_product_4_price_sum.move(740, 283)

		self.basket_product_4_del_block = QLabel('', self.basket_Window)
		self.basket_product_4_del_block.setStyleSheet('''QLabel {font-size: 14px; border: 1px solid #000000;}''')
		self.basket_product_4_del_block.resize(64, 46)
		self.basket_product_4_del_block.move(890, 283)

		self.basket_product_4_buy_block = QLabel('', self.basket_Window)
		self.basket_product_4_buy_block.setStyleSheet('''QLabel {font-size: 14px; border: 1px solid #000000;}''')
		self.basket_product_4_buy_block.resize(60, 46)
		self.basket_product_4_buy_block.move(954, 283)


		self.basket_product_5_num = QLabel('5', self.basket_Window)
		self.basket_product_5_num.setStyleSheet('''QLabel {font-size: 14px; border: 1px solid #000000;}''')
		self.basket_product_5_num.resize(40, 46)
		self.basket_product_5_num.move(90, 328)

		self.basket_product_5_img_block = QLabel('', self.basket_Window)
		self.basket_product_5_img_block.setStyleSheet('''QLabel {font-size: 14px; border: 1px solid #000000;}''')
		self.basket_product_5_img_block.resize(80, 46)
		self.basket_product_5_img_block.move(130, 328)
		self.basket_product_5_img = QLabel(self.basket_Window)
		self.basket_product_5_img.resize(70, 40)
		self.basket_product_5_img.move(135, 331)

		self.basket_product_5_name = QLabel('', self.basket_Window)
		self.basket_product_5_name.setStyleSheet('''QLabel {font-size: 14px; border: 1px solid #000000;}''')
		self.basket_product_5_name.resize(350, 46)
		self.basket_product_5_name.move(210, 328)

		self.basket_product_5_price = QLabel('', self.basket_Window)
		self.basket_product_5_price.setStyleSheet('''QLabel {font-size: 14px; border: 1px solid #000000;}''')
		self.basket_product_5_price.resize(100, 46)
		self.basket_product_5_price.move(560, 328)

		self.basket_product_5_count_block = QLabel('', self.basket_Window)
		self.basket_product_5_count_block.setStyleSheet('''QLabel {font-size: 14px; border: 1px solid #000000;}''')
		self.basket_product_5_count_block.resize(80, 46)
		self.basket_product_5_count_block.move(660, 328)

		self.basket_product_5_price_sum = QLabel('', self.basket_Window)
		self.basket_product_5_price_sum.setStyleSheet('''QLabel {font-size: 14px; border: 1px solid #000000;}''')
		self.basket_product_5_price_sum.resize(150, 46)
		self.basket_product_5_price_sum.move(740, 328)

		self.basket_product_5_del_block = QLabel('', self.basket_Window)
		self.basket_product_5_del_block.setStyleSheet('''QLabel {font-size: 14px; border: 1px solid #000000;}''')
		self.basket_product_5_del_block.resize(64, 46)
		self.basket_product_5_del_block.move(890, 328)

		self.basket_product_5_buy_block = QLabel('', self.basket_Window)
		self.basket_product_5_buy_block.setStyleSheet('''QLabel {font-size: 14px; border: 1px solid #000000;}''')
		self.basket_product_5_buy_block.resize(60, 46)
		self.basket_product_5_buy_block.move(954, 328)


		self.basket_product_6_num = QLabel('6', self.basket_Window)
		self.basket_product_6_num.setStyleSheet('''QLabel {font-size: 14px; border: 1px solid #000000;}''')
		self.basket_product_6_num.resize(40, 46)
		self.basket_product_6_num.move(90, 373)

		self.basket_product_6_img_block = QLabel('', self.basket_Window)
		self.basket_product_6_img_block.setStyleSheet('''QLabel {font-size: 14px; border: 1px solid #000000;}''')
		self.basket_product_6_img_block.resize(80, 46)
		self.basket_product_6_img_block.move(130, 373)
		self.basket_product_6_img = QLabel(self.basket_Window)
		self.basket_product_6_img.resize(70, 40)
		self.basket_product_6_img.move(135, 376)

		self.basket_product_6_name = QLabel('', self.basket_Window)
		self.basket_product_6_name.setStyleSheet('''QLabel {font-size: 14px; border: 1px solid #000000;}''')
		self.basket_product_6_name.resize(350, 46)
		self.basket_product_6_name.move(210, 373)

		self.basket_product_6_price = QLabel('', self.basket_Window)
		self.basket_product_6_price.setStyleSheet('''QLabel {font-size: 14px; border: 1px solid #000000;}''')
		self.basket_product_6_price.resize(100, 46)
		self.basket_product_6_price.move(560, 373)

		self.basket_product_6_count_block = QLabel('', self.basket_Window)
		self.basket_product_6_count_block.setStyleSheet('''QLabel {font-size: 14px; border: 1px solid #000000;}''')
		self.basket_product_6_count_block.resize(80, 46)
		self.basket_product_6_count_block.move(660, 373)

		self.basket_product_6_price_sum = QLabel('', self.basket_Window)
		self.basket_product_6_price_sum.setStyleSheet('''QLabel {font-size: 14px; border: 1px solid #000000;}''')
		self.basket_product_6_price_sum.resize(150, 46)
		self.basket_product_6_price_sum.move(740, 373)

		self.basket_product_6_del_block = QLabel('', self.basket_Window)
		self.basket_product_6_del_block.setStyleSheet('''QLabel {font-size: 14px; border: 1px solid #000000;}''')
		self.basket_product_6_del_block.resize(64, 46)
		self.basket_product_6_del_block.move(890, 373)

		self.basket_product_6_buy_block = QLabel('', self.basket_Window)
		self.basket_product_6_buy_block.setStyleSheet('''QLabel {font-size: 14px; border: 1px solid #000000;}''')
		self.basket_product_6_buy_block.resize(60, 46)
		self.basket_product_6_buy_block.move(954, 373)


		self.basket_product_7_num = QLabel('7', self.basket_Window)
		self.basket_product_7_num.setStyleSheet('''QLabel {font-size: 14px; border: 1px solid #000000;}''')
		self.basket_product_7_num.resize(40, 46)
		self.basket_product_7_num.move(90, 418)

		self.basket_product_7_img_block = QLabel('', self.basket_Window)
		self.basket_product_7_img_block.setStyleSheet('''QLabel {font-size: 14px; border: 1px solid #000000;}''')
		self.basket_product_7_img_block.resize(80, 46)
		self.basket_product_7_img_block.move(130, 418)
		self.basket_product_7_img = QLabel(self.basket_Window)
		self.basket_product_7_img.resize(70, 40)
		self.basket_product_7_img.move(135, 421)

		self.basket_product_7_name = QLabel('', self.basket_Window)
		self.basket_product_7_name.setStyleSheet('''QLabel {font-size: 14px; border: 1px solid #000000;}''')
		self.basket_product_7_name.resize(350, 46)
		self.basket_product_7_name.move(210, 418)

		self.basket_product_7_price = QLabel('', self.basket_Window)
		self.basket_product_7_price.setStyleSheet('''QLabel {font-size: 14px; border: 1px solid #000000;}''')
		self.basket_product_7_price.resize(100, 46)
		self.basket_product_7_price.move(560, 418)

		self.basket_product_7_count_block = QLabel('', self.basket_Window)
		self.basket_product_7_count_block.setStyleSheet('''QLabel {font-size: 14px; border: 1px solid #000000;}''')
		self.basket_product_7_count_block.resize(80, 46)
		self.basket_product_7_count_block.move(660, 418)

		self.basket_product_7_price_sum = QLabel('', self.basket_Window)
		self.basket_product_7_price_sum.setStyleSheet('''QLabel {font-size: 14px; border: 1px solid #000000;}''')
		self.basket_product_7_price_sum.resize(150, 46)
		self.basket_product_7_price_sum.move(740, 418)

		self.basket_product_7_del_block = QLabel('', self.basket_Window)
		self.basket_product_7_del_block.setStyleSheet('''QLabel {font-size: 14px; border: 1px solid #000000;}''')
		self.basket_product_7_del_block.resize(64, 46)
		self.basket_product_7_del_block.move(890, 418)

		self.basket_product_7_buy_block = QLabel('', self.basket_Window)
		self.basket_product_7_buy_block.setStyleSheet('''QLabel {font-size: 14px; border: 1px solid #000000;}''')
		self.basket_product_7_buy_block.resize(60, 46)
		self.basket_product_7_buy_block.move(954, 418)


		self.basket_product_8_num = QLabel('8', self.basket_Window)
		self.basket_product_8_num.setStyleSheet('''QLabel {font-size: 14px; border: 1px solid #000000;}''')
		self.basket_product_8_num.resize(40, 46)
		self.basket_product_8_num.move(90, 463)

		self.basket_product_8_img_block = QLabel('', self.basket_Window)
		self.basket_product_8_img_block.setStyleSheet('''QLabel {font-size: 14px; border: 1px solid #000000;}''')
		self.basket_product_8_img_block.resize(80, 46)
		self.basket_product_8_img_block.move(130, 463)
		self.basket_product_8_img = QLabel(self.basket_Window)
		self.basket_product_8_img.resize(70, 40)
		self.basket_product_8_img.move(135, 466)

		self.basket_product_8_name = QLabel('', self.basket_Window)
		self.basket_product_8_name.setStyleSheet('''QLabel {font-size: 14px; border: 1px solid #000000;}''')
		self.basket_product_8_name.resize(350, 46)
		self.basket_product_8_name.move(210, 463)

		self.basket_product_8_price = QLabel('', self.basket_Window)
		self.basket_product_8_price.setStyleSheet('''QLabel {font-size: 14px; border: 1px solid #000000;}''')
		self.basket_product_8_price.resize(100, 46)
		self.basket_product_8_price.move(560, 463)

		self.basket_product_8_count_block = QLabel('', self.basket_Window)
		self.basket_product_8_count_block.setStyleSheet('''QLabel {font-size: 14px; border: 1px solid #000000;}''')
		self.basket_product_8_count_block.resize(80, 46)
		self.basket_product_8_count_block.move(660, 463)

		self.basket_product_8_price_sum = QLabel('', self.basket_Window)
		self.basket_product_8_price_sum.setStyleSheet('''QLabel {font-size: 14px; border: 1px solid #000000;}''')
		self.basket_product_8_price_sum.resize(150, 46)
		self.basket_product_8_price_sum.move(740, 463)

		self.basket_product_8_del_block = QLabel('', self.basket_Window)
		self.basket_product_8_del_block.setStyleSheet('''QLabel {font-size: 14px; border: 1px solid #000000;}''')
		self.basket_product_8_del_block.resize(64, 46)
		self.basket_product_8_del_block.move(890, 463)

		self.basket_product_8_buy_block = QLabel('', self.basket_Window)
		self.basket_product_8_buy_block.setStyleSheet('''QLabel {font-size: 14px; border: 1px solid #000000;}''')
		self.basket_product_8_buy_block.resize(60, 46)
		self.basket_product_8_buy_block.move(954, 463)


		self.basket_product_9_num = QLabel('9', self.basket_Window)
		self.basket_product_9_num.setStyleSheet('''QLabel {font-size: 14px; border: 1px solid #000000;}''')
		self.basket_product_9_num.resize(40, 46)
		self.basket_product_9_num.move(90, 508)

		self.basket_product_9_img_block = QLabel('', self.basket_Window)
		self.basket_product_9_img_block.setStyleSheet('''QLabel {font-size: 14px; border: 1px solid #000000;}''')
		self.basket_product_9_img_block.resize(80, 46)
		self.basket_product_9_img_block.move(130, 508)
		self.basket_product_9_img = QLabel(self.basket_Window)
		self.basket_product_9_img.resize(70, 40)
		self.basket_product_9_img.move(135, 511)

		self.basket_product_9_name = QLabel('', self.basket_Window)
		self.basket_product_9_name.setStyleSheet('''QLabel {font-size: 14px; border: 1px solid #000000;}''')
		self.basket_product_9_name.resize(350, 46)
		self.basket_product_9_name.move(210, 508)

		self.basket_product_9_price = QLabel('', self.basket_Window)
		self.basket_product_9_price.setStyleSheet('''QLabel {font-size: 14px; border: 1px solid #000000;}''')
		self.basket_product_9_price.resize(100, 46)
		self.basket_product_9_price.move(560, 508)

		self.basket_product_9_count_block = QLabel('', self.basket_Window)
		self.basket_product_9_count_block.setStyleSheet('''QLabel {font-size: 14px; border: 1px solid #000000;}''')
		self.basket_product_9_count_block.resize(80, 46)
		self.basket_product_9_count_block.move(660, 508)

		self.basket_product_9_price_sum = QLabel('', self.basket_Window)
		self.basket_product_9_price_sum.setStyleSheet('''QLabel {font-size: 14px; border: 1px solid #000000;}''')
		self.basket_product_9_price_sum.resize(150, 46)
		self.basket_product_9_price_sum.move(740, 508)

		self.basket_product_9_del_block = QLabel('', self.basket_Window)
		self.basket_product_9_del_block.setStyleSheet('''QLabel {font-size: 14px; border: 1px solid #000000;}''')
		self.basket_product_9_del_block.resize(64, 46)
		self.basket_product_9_del_block.move(890, 508)

		self.basket_product_9_buy_block = QLabel('', self.basket_Window)
		self.basket_product_9_buy_block.setStyleSheet('''QLabel {font-size: 14px; border: 1px solid #000000;}''')
		self.basket_product_9_buy_block.resize(60, 46)
		self.basket_product_9_buy_block.move(954, 508)


		self.basket_product_10_num = QLabel('10', self.basket_Window)
		self.basket_product_10_num.setStyleSheet('''QLabel {font-size: 14px; border: 1px solid #000000;}''')
		self.basket_product_10_num.resize(40, 46)
		self.basket_product_10_num.move(90, 553)

		self.basket_product_10_img_block = QLabel('', self.basket_Window)
		self.basket_product_10_img_block.setStyleSheet('''QLabel {font-size: 14px; border: 1px solid #000000;}''')
		self.basket_product_10_img_block.resize(80, 46)
		self.basket_product_10_img_block.move(130, 553)
		self.basket_product_10_img = QLabel(self.basket_Window)
		self.basket_product_10_img.resize(70, 40)
		self.basket_product_10_img.move(135, 556)

		self.basket_product_10_name = QLabel('', self.basket_Window)
		self.basket_product_10_name.setStyleSheet('''QLabel {font-size: 14px; border: 1px solid #000000;}''')
		self.basket_product_10_name.resize(350, 46)
		self.basket_product_10_name.move(210, 553)

		self.basket_product_10_price = QLabel('', self.basket_Window)
		self.basket_product_10_price.setStyleSheet('''QLabel {font-size: 14px; border: 1px solid #000000;}''')
		self.basket_product_10_price.resize(100, 46)
		self.basket_product_10_price.move(560, 553)

		self.basket_product_10_count_block = QLabel('', self.basket_Window)
		self.basket_product_10_count_block.setStyleSheet('''QLabel {font-size: 14px; border: 1px solid #000000;}''')
		self.basket_product_10_count_block.resize(80, 46)
		self.basket_product_10_count_block.move(660, 553)

		self.basket_product_10_price_sum = QLabel('', self.basket_Window)
		self.basket_product_10_price_sum.setStyleSheet('''QLabel {font-size: 14px; border: 1px solid #000000;}''')
		self.basket_product_10_price_sum.resize(150, 46)
		self.basket_product_10_price_sum.move(740, 553)

		self.basket_product_10_del_block = QLabel('', self.basket_Window)
		self.basket_product_10_del_block.setStyleSheet('''QLabel {font-size: 14px; border: 1px solid #000000;}''')
		self.basket_product_10_del_block.resize(64, 46)
		self.basket_product_10_del_block.move(890, 553)

		self.basket_product_10_buy_block = QLabel('', self.basket_Window)
		self.basket_product_10_buy_block.setStyleSheet('''QLabel {font-size: 14px; border: 1px solid #000000;}''')
		self.basket_product_10_buy_block.resize(60, 46)
		self.basket_product_10_buy_block.move(954, 553)


		self.basket_hr = QLabel('', self.basket_Window)
		self.basket_hr.setStyleSheet('''QLabel {border-top: 1.5px dashed #EE272D;}''')
		self.basket_hr.resize(924, 2)
		self.basket_hr.move(90, 610)


		self.basket_products_all_result = QLabel('Итог:', self.basket_Window)
		self.basket_products_all_result.setStyleSheet('''QLabel {font-size: 18px; border: 1px solid #000000; border-bottom-left-radius: 4px;}''')
		self.basket_products_all_result.resize(570, 46)
		self.basket_products_all_result.move(90, 623)

		self.basket_products_all_count = QLabel('', self.basket_Window)
		self.basket_products_all_count.setStyleSheet('''QLabel {font-size: 14px; border: 1px solid #000000;}''')
		self.basket_products_all_count.resize(80, 46)
		self.basket_products_all_count.move(660, 623)

		self.basket_products_all_price_sum = QLabel('', self.basket_Window)
		self.basket_products_all_price_sum.setStyleSheet('''QLabel {font-size: 14px; border: 1px solid #000000;}''')
		self.basket_products_all_price_sum.resize(150, 46)
		self.basket_products_all_price_sum.move(740, 623)

		self.basket_products_all_del_block = QLabel('', self.basket_Window)
		self.basket_products_all_del_block.setStyleSheet('''QLabel {font-size: 14px; border: 1px solid #000000;}''')
		self.basket_products_all_del_block.resize(64, 46)
		self.basket_products_all_del_block.move(890, 623)

		self.basket_products_all_buy_block = QLabel('', self.basket_Window)
		self.basket_products_all_buy_block.setStyleSheet('''QLabel {font-size: 14px; border: 1px solid #000000; border-bottom-right-radius: 4px;}''')
		self.basket_products_all_buy_block.resize(60, 46)
		self.basket_products_all_buy_block.move(954, 623)


		user_products = open(self.login_user + '_list_basket.txt', 'r')
		user_products_read = user_products.read()
		if (user_products_read.count(';') > 0 ):
			self.basket_products_all_del = QPushButton('', self.basket_Window)
			self.basket_products_all_del.clicked.connect(self.func_basket_products_all_del)
			self.basket_products_all_del.setStyleSheet('''QPushButton {border: 0; background-image: url(icons/icon_close_all.png);}''')
			self.basket_products_all_del.resize(32, 32)
			self.basket_products_all_del.move(906, 630)

			self.basket_products_all_buy = QPushButton('', self.basket_Window)
			# self.basket_products_all_buy.clicked.connect(self.func_basket_products_all_buy)
			self.basket_products_all_buy.setStyleSheet('''QPushButton {border: 0; background-image: url(icons/icon_basket_buy_all.png);}''')
			self.basket_products_all_buy.resize(32, 32)
			self.basket_products_all_buy.move(968, 630)
		if (user_products_read.count(';') == 1 ):
			user_products_read = user_products_read.split(';')
			self.name_categoriy.setText('В корзине 1 товар')
			self.basket_product_1_count_del_buy_style()
			self.basket_product_1_img_pix = QtGui.QPixmap(user_products_read[0].split(':')[0])
			self.basket_product_1_img.setPixmap(self.basket_product_1_img_pix)
			self.basket_product_1_name.setText(user_products_read[0].split(':')[1])
			self.basket_product_1_price.setText(user_products_read[0].split(':')[2] + ' руб.')
			self.basket_product_1_count.setText(user_products_read[0].split(':')[3])
			self.basket_product_1_price_sum.setText(user_products_read[0].split(':')[4] + ' руб.')
			self.basket_products_all_count.setText(user_products_read[0].split(':')[3] + ' шт.')
			self.basket_products_all_price_sum.setText(str( int(user_products_read[0].split(':')[4]) ) + ' руб.')
		elif (user_products_read.count(';') == 2 ):
			user_products_read = user_products_read.split(';')
			self.name_categoriy.setText('В корзине 2 товара')
			self.basket_product_1_count_del_buy_style()
			self.basket_product_1_img_pix = QtGui.QPixmap(user_products_read[0].split(':')[0])
			self.basket_product_1_img.setPixmap(self.basket_product_1_img_pix)
			self.basket_product_1_name.setText(user_products_read[0].split(':')[1])
			self.basket_product_1_price.setText(user_products_read[0].split(':')[2] + ' руб.')
			self.basket_product_1_count.setText(user_products_read[0].split(':')[3])
			self.basket_product_1_price_sum.setText(user_products_read[0].split(':')[4] + ' руб.')
			self.basket_product_2_count_del_buy_style()
			self.basket_product_2_img_pix = QtGui.QPixmap(user_products_read[1].split(':')[0])
			self.basket_product_2_img.setPixmap(self.basket_product_2_img_pix)
			self.basket_product_2_name.setText(user_products_read[1].split(':')[1])
			self.basket_product_2_price.setText(user_products_read[1].split(':')[2] + ' руб.')
			self.basket_product_2_count.setText(user_products_read[1].split(':')[3])
			self.basket_product_2_price_sum.setText(user_products_read[1].split(':')[4] + ' руб.')
			self.basket_products_all_count.setText(str( int(user_products_read[0].split(':')[3]) + int(user_products_read[1].split(':')[3])) + ' шт.')
			self.basket_products_all_price_sum.setText(str( int(user_products_read[0].split(':')[4]) + int(user_products_read[1].split(':')[4]) ) + ' руб.')
		elif (user_products_read.count(';') == 3 ):
			user_products_read = user_products_read.split(';')
			self.name_categoriy.setText('В корзине 3 товара')
			self.basket_product_1_count_del_buy_style()
			self.basket_product_1_img_pix = QtGui.QPixmap(user_products_read[0].split(':')[0])
			self.basket_product_1_img.setPixmap(self.basket_product_1_img_pix)
			self.basket_product_1_name.setText(user_products_read[0].split(':')[1])
			self.basket_product_1_price.setText(user_products_read[0].split(':')[2] + ' руб.')
			self.basket_product_1_count.setText(user_products_read[0].split(':')[3])
			self.basket_product_1_price_sum.setText(user_products_read[0].split(':')[4] + ' руб.')
			self.basket_product_2_count_del_buy_style()
			self.basket_product_2_img_pix = QtGui.QPixmap(user_products_read[1].split(':')[0])
			self.basket_product_2_img.setPixmap(self.basket_product_2_img_pix)
			self.basket_product_2_name.setText(user_products_read[1].split(':')[1])
			self.basket_product_2_price.setText(user_products_read[1].split(':')[2] + ' руб.')
			self.basket_product_2_count.setText(user_products_read[1].split(':')[3])
			self.basket_product_2_price_sum.setText(user_products_read[1].split(':')[4] + ' руб.')
			self.basket_product_3_count_del_buy_style()
			self.basket_product_3_img_pix = QtGui.QPixmap(user_products_read[2].split(':')[0])
			self.basket_product_3_img.setPixmap(self.basket_product_3_img_pix)
			self.basket_product_3_name.setText(user_products_read[2].split(':')[1])
			self.basket_product_3_price.setText(user_products_read[2].split(':')[2] + ' руб.')
			self.basket_product_3_count.setText(user_products_read[2].split(':')[3])
			self.basket_product_3_price_sum.setText(user_products_read[2].split(':')[4] + ' руб.')
			self.basket_products_all_count.setText(str( int(user_products_read[0].split(':')[3]) + int(user_products_read[1].split(':')[3]) + int(user_products_read[2].split(':')[3])) + ' шт.')
			self.basket_products_all_price_sum.setText(str( int(user_products_read[0].split(':')[4]) + int(user_products_read[1].split(':')[4]) + int(user_products_read[2].split(':')[4]) ) + ' руб.')
		elif (user_products_read.count(';') == 4 ):
			user_products_read = user_products_read.split(';')
			self.name_categoriy.setText('В корзине 4 товара')
			self.basket_product_1_count_del_buy_style()
			self.basket_product_1_img_pix = QtGui.QPixmap(user_products_read[0].split(':')[0])
			self.basket_product_1_img.setPixmap(self.basket_product_1_img_pix)
			self.basket_product_1_name.setText(user_products_read[0].split(':')[1])
			self.basket_product_1_price.setText(user_products_read[0].split(':')[2] + ' руб.')
			self.basket_product_1_count.setText(user_products_read[0].split(':')[3])
			self.basket_product_1_price_sum.setText(user_products_read[0].split(':')[4] + ' руб.')
			self.basket_product_2_count_del_buy_style()
			self.basket_product_2_img_pix = QtGui.QPixmap(user_products_read[1].split(':')[0])
			self.basket_product_2_img.setPixmap(self.basket_product_2_img_pix)
			self.basket_product_2_name.setText(user_products_read[1].split(':')[1])
			self.basket_product_2_price.setText(user_products_read[1].split(':')[2] + ' руб.')
			self.basket_product_2_count.setText(user_products_read[1].split(':')[3])
			self.basket_product_2_price_sum.setText(user_products_read[1].split(':')[4] + ' руб.')
			self.basket_product_3_count_del_buy_style()
			self.basket_product_3_img_pix = QtGui.QPixmap(user_products_read[2].split(':')[0])
			self.basket_product_3_img.setPixmap(self.basket_product_3_img_pix)
			self.basket_product_3_name.setText(user_products_read[2].split(':')[1])
			self.basket_product_3_price.setText(user_products_read[2].split(':')[2] + ' руб.')
			self.basket_product_3_count.setText(user_products_read[2].split(':')[3])
			self.basket_product_3_price_sum.setText(user_products_read[2].split(':')[4] + ' руб.')
			self.basket_product_4_count_del_buy_style()
			self.basket_product_4_img_pix = QtGui.QPixmap(user_products_read[3].split(':')[0])
			self.basket_product_4_img.setPixmap(self.basket_product_4_img_pix)
			self.basket_product_4_name.setText(user_products_read[3].split(':')[1])
			self.basket_product_4_price.setText(user_products_read[3].split(':')[2] + ' руб.')
			self.basket_product_4_count.setText(user_products_read[3].split(':')[3])
			self.basket_product_4_price_sum.setText(user_products_read[3].split(':')[4] + ' руб.')
			self.basket_products_all_count.setText(str( int(user_products_read[0].split(':')[3]) + int(user_products_read[1].split(':')[3]) + int(user_products_read[2].split(':')[3]) + int(user_products_read[3].split(':')[3]) ) + ' шт.')
			self.basket_products_all_price_sum.setText(str( int(user_products_read[0].split(':')[4]) + int(user_products_read[1].split(':')[4]) + int(user_products_read[2].split(':')[4]) + int(user_products_read[3].split(':')[4]) ) + ' руб.')
		elif (user_products_read.count(';') == 5 ):
			user_products_read = user_products_read.split(';')
			self.name_categoriy.setText('В корзине 5 товаров')
			self.basket_product_1_count_del_buy_style()
			self.basket_product_1_img_pix = QtGui.QPixmap(user_products_read[0].split(':')[0])
			self.basket_product_1_img.setPixmap(self.basket_product_1_img_pix)
			self.basket_product_1_name.setText(user_products_read[0].split(':')[1])
			self.basket_product_1_price.setText(user_products_read[0].split(':')[2] + ' руб.')
			self.basket_product_1_count.setText(user_products_read[0].split(':')[3])
			self.basket_product_1_price_sum.setText(user_products_read[0].split(':')[4] + ' руб.')
			self.basket_product_2_count_del_buy_style()
			self.basket_product_2_img_pix = QtGui.QPixmap(user_products_read[1].split(':')[0])
			self.basket_product_2_img.setPixmap(self.basket_product_2_img_pix)
			self.basket_product_2_name.setText(user_products_read[1].split(':')[1])
			self.basket_product_2_price.setText(user_products_read[1].split(':')[2] + ' руб.')
			self.basket_product_2_count.setText(user_products_read[1].split(':')[3])
			self.basket_product_2_price_sum.setText(user_products_read[1].split(':')[4] + ' руб.')
			self.basket_product_3_count_del_buy_style()
			self.basket_product_3_img_pix = QtGui.QPixmap(user_products_read[2].split(':')[0])
			self.basket_product_3_img.setPixmap(self.basket_product_3_img_pix)
			self.basket_product_3_name.setText(user_products_read[2].split(':')[1])
			self.basket_product_3_price.setText(user_products_read[2].split(':')[2] + ' руб.')
			self.basket_product_3_count.setText(user_products_read[2].split(':')[3])
			self.basket_product_3_price_sum.setText(user_products_read[2].split(':')[4] + ' руб.')
			self.basket_product_4_count_del_buy_style()
			self.basket_product_4_img_pix = QtGui.QPixmap(user_products_read[3].split(':')[0])
			self.basket_product_4_img.setPixmap(self.basket_product_4_img_pix)
			self.basket_product_4_name.setText(user_products_read[3].split(':')[1])
			self.basket_product_4_price.setText(user_products_read[3].split(':')[2] + ' руб.')
			self.basket_product_4_count.setText(user_products_read[3].split(':')[3])
			self.basket_product_4_price_sum.setText(user_products_read[3].split(':')[4] + ' руб.')
			self.basket_product_5_count_del_buy_style()
			self.basket_product_5_img_pix = QtGui.QPixmap(user_products_read[4].split(':')[0])
			self.basket_product_5_img.setPixmap(self.basket_product_5_img_pix)
			self.basket_product_5_name.setText(user_products_read[4].split(':')[1])
			self.basket_product_5_price.setText(user_products_read[4].split(':')[2] + ' руб.')
			self.basket_product_5_count.setText(user_products_read[4].split(':')[3])
			self.basket_product_5_price_sum.setText(user_products_read[4].split(':')[4] + ' руб.')
			self.basket_products_all_count.setText(str( int(user_products_read[0].split(':')[3]) + int(user_products_read[1].split(':')[3]) + int(user_products_read[2].split(':')[3]) + int(user_products_read[3].split(':')[3]) + int(user_products_read[4].split(':')[3]) ) + ' шт.')
			self.basket_products_all_price_sum.setText(str( int(user_products_read[0].split(':')[4]) + int(user_products_read[1].split(':')[4]) + int(user_products_read[2].split(':')[4]) + int(user_products_read[3].split(':')[4]) + int(user_products_read[4].split(':')[4]) ) + ' руб.')
		elif (user_products_read.count(';') == 6 ):
			user_products_read = user_products_read.split(';')
			self.name_categoriy.setText('В корзине 6 товаров')
			self.basket_product_1_count_del_buy_style()
			self.basket_product_1_img_pix = QtGui.QPixmap(user_products_read[0].split(':')[0])
			self.basket_product_1_img.setPixmap(self.basket_product_1_img_pix)
			self.basket_product_1_name.setText(user_products_read[0].split(':')[1])
			self.basket_product_1_price.setText(user_products_read[0].split(':')[2] + ' руб.')
			self.basket_product_1_count.setText(user_products_read[0].split(':')[3])
			self.basket_product_1_price_sum.setText(user_products_read[0].split(':')[4] + ' руб.')
			self.basket_product_2_count_del_buy_style()
			self.basket_product_2_img_pix = QtGui.QPixmap(user_products_read[1].split(':')[0])
			self.basket_product_2_img.setPixmap(self.basket_product_2_img_pix)
			self.basket_product_2_name.setText(user_products_read[1].split(':')[1])
			self.basket_product_2_price.setText(user_products_read[1].split(':')[2] + ' руб.')
			self.basket_product_2_count.setText(user_products_read[1].split(':')[3])
			self.basket_product_2_price_sum.setText(user_products_read[1].split(':')[4] + ' руб.')
			self.basket_product_3_count_del_buy_style()
			self.basket_product_3_img_pix = QtGui.QPixmap(user_products_read[2].split(':')[0])
			self.basket_product_3_img.setPixmap(self.basket_product_3_img_pix)
			self.basket_product_3_name.setText(user_products_read[2].split(':')[1])
			self.basket_product_3_price.setText(user_products_read[2].split(':')[2] + ' руб.')
			self.basket_product_3_count.setText(user_products_read[2].split(':')[3])
			self.basket_product_3_price_sum.setText(user_products_read[2].split(':')[4] + ' руб.')
			self.basket_product_4_count_del_buy_style()
			self.basket_product_4_img_pix = QtGui.QPixmap(user_products_read[3].split(':')[0])
			self.basket_product_4_img.setPixmap(self.basket_product_4_img_pix)
			self.basket_product_4_name.setText(user_products_read[3].split(':')[1])
			self.basket_product_4_price.setText(user_products_read[3].split(':')[2] + ' руб.')
			self.basket_product_4_count.setText(user_products_read[3].split(':')[3])
			self.basket_product_4_price_sum.setText(user_products_read[3].split(':')[4] + ' руб.')
			self.basket_product_5_count_del_buy_style()
			self.basket_product_5_img_pix = QtGui.QPixmap(user_products_read[4].split(':')[0])
			self.basket_product_5_img.setPixmap(self.basket_product_5_img_pix)
			self.basket_product_5_name.setText(user_products_read[4].split(':')[1])
			self.basket_product_5_price.setText(user_products_read[4].split(':')[2] + ' руб.')
			self.basket_product_5_count.setText(user_products_read[4].split(':')[3])
			self.basket_product_5_price_sum.setText(user_products_read[4].split(':')[4] + ' руб.')
			self.basket_product_6_count_del_buy_style()
			self.basket_product_6_img_pix = QtGui.QPixmap(user_products_read[5].split(':')[0])
			self.basket_product_6_img.setPixmap(self.basket_product_6_img_pix)
			self.basket_product_6_name.setText(user_products_read[5].split(':')[1])
			self.basket_product_6_price.setText(user_products_read[5].split(':')[2] + ' руб.')
			self.basket_product_6_count.setText(user_products_read[5].split(':')[3])
			self.basket_product_6_price_sum.setText(user_products_read[5].split(':')[4] + ' руб.')
			self.basket_products_all_count.setText(str( int(user_products_read[0].split(':')[3]) + int(user_products_read[1].split(':')[3]) + int(user_products_read[2].split(':')[3]) + int(user_products_read[3].split(':')[3]) + int(user_products_read[4].split(':')[3]) + int(user_products_read[5].split(':')[3]) ) + ' шт.')
			self.basket_products_all_price_sum.setText(str( int(user_products_read[0].split(':')[4]) + int(user_products_read[1].split(':')[4]) + int(user_products_read[2].split(':')[4]) + int(user_products_read[3].split(':')[4]) + int(user_products_read[4].split(':')[4]) + int(user_products_read[5].split(':')[4]) ) + ' руб.')
		elif (user_products_read.count(';') == 7 ):
			user_products_read = user_products_read.split(';')
			self.name_categoriy.setText('В корзине 7 товаров')
			self.basket_product_1_count_del_buy_style()
			self.basket_product_1_img_pix = QtGui.QPixmap(user_products_read[0].split(':')[0])
			self.basket_product_1_img.setPixmap(self.basket_product_1_img_pix)
			self.basket_product_1_name.setText(user_products_read[0].split(':')[1])
			self.basket_product_1_price.setText(user_products_read[0].split(':')[2] + ' руб.')
			self.basket_product_1_count.setText(user_products_read[0].split(':')[3])
			self.basket_product_1_price_sum.setText(user_products_read[0].split(':')[4] + ' руб.')
			self.basket_product_2_count_del_buy_style()
			self.basket_product_2_img_pix = QtGui.QPixmap(user_products_read[1].split(':')[0])
			self.basket_product_2_img.setPixmap(self.basket_product_2_img_pix)
			self.basket_product_2_name.setText(user_products_read[1].split(':')[1])
			self.basket_product_2_price.setText(user_products_read[1].split(':')[2] + ' руб.')
			self.basket_product_2_count.setText(user_products_read[1].split(':')[3])
			self.basket_product_2_price_sum.setText(user_products_read[1].split(':')[4] + ' руб.')
			self.basket_product_3_count_del_buy_style()
			self.basket_product_3_img_pix = QtGui.QPixmap(user_products_read[2].split(':')[0])
			self.basket_product_3_img.setPixmap(self.basket_product_3_img_pix)
			self.basket_product_3_name.setText(user_products_read[2].split(':')[1])
			self.basket_product_3_price.setText(user_products_read[2].split(':')[2] + ' руб.')
			self.basket_product_3_count.setText(user_products_read[2].split(':')[3])
			self.basket_product_3_price_sum.setText(user_products_read[2].split(':')[4] + ' руб.')
			self.basket_product_4_count_del_buy_style()
			self.basket_product_4_img_pix = QtGui.QPixmap(user_products_read[3].split(':')[0])
			self.basket_product_4_img.setPixmap(self.basket_product_4_img_pix)
			self.basket_product_4_name.setText(user_products_read[3].split(':')[1])
			self.basket_product_4_price.setText(user_products_read[3].split(':')[2] + ' руб.')
			self.basket_product_4_count.setText(user_products_read[3].split(':')[3])
			self.basket_product_4_price_sum.setText(user_products_read[3].split(':')[4] + ' руб.')
			self.basket_product_5_count_del_buy_style()
			self.basket_product_5_img_pix = QtGui.QPixmap(user_products_read[4].split(':')[0])
			self.basket_product_5_img.setPixmap(self.basket_product_5_img_pix)
			self.basket_product_5_name.setText(user_products_read[4].split(':')[1])
			self.basket_product_5_price.setText(user_products_read[4].split(':')[2] + ' руб.')
			self.basket_product_5_count.setText(user_products_read[4].split(':')[3])
			self.basket_product_5_price_sum.setText(user_products_read[4].split(':')[4] + ' руб.')
			self.basket_product_6_count_del_buy_style()
			self.basket_product_6_img_pix = QtGui.QPixmap(user_products_read[5].split(':')[0])
			self.basket_product_6_img.setPixmap(self.basket_product_6_img_pix)
			self.basket_product_6_name.setText(user_products_read[5].split(':')[1])
			self.basket_product_6_price.setText(user_products_read[5].split(':')[2] + ' руб.')
			self.basket_product_6_count.setText(user_products_read[5].split(':')[3])
			self.basket_product_6_price_sum.setText(user_products_read[5].split(':')[4] + ' руб.')
			self.basket_product_7_count_del_buy_style()
			self.basket_product_7_img_pix = QtGui.QPixmap(user_products_read[6].split(':')[0])
			self.basket_product_7_img.setPixmap(self.basket_product_7_img_pix)
			self.basket_product_7_name.setText(user_products_read[6].split(':')[1])
			self.basket_product_7_price.setText(user_products_read[6].split(':')[2] + ' руб.')
			self.basket_product_7_count.setText(user_products_read[6].split(':')[3])
			self.basket_product_7_price_sum.setText(user_products_read[6].split(':')[4] + ' руб.')
			self.basket_products_all_count.setText(str( int(user_products_read[0].split(':')[3]) + int(user_products_read[1].split(':')[3]) + int(user_products_read[2].split(':')[3]) + int(user_products_read[3].split(':')[3]) + int(user_products_read[4].split(':')[3]) + int(user_products_read[5].split(':')[3]) + int(user_products_read[6].split(':')[3]) ) + ' шт.')
			self.basket_products_all_price_sum.setText(str( int(user_products_read[0].split(':')[4]) + int(user_products_read[1].split(':')[4]) + int(user_products_read[2].split(':')[4]) + int(user_products_read[3].split(':')[4]) + int(user_products_read[4].split(':')[4]) + int(user_products_read[5].split(':')[4]) + int(user_products_read[6].split(':')[4]) ) + ' руб.')
		elif (user_products_read.count(';') == 8 ):
			user_products_read = user_products_read.split(';')
			self.name_categoriy.setText('В корзине 8 товаров')
			self.basket_product_1_count_del_buy_style()
			self.basket_product_1_img_pix = QtGui.QPixmap(user_products_read[0].split(':')[0])
			self.basket_product_1_img.setPixmap(self.basket_product_1_img_pix)
			self.basket_product_1_name.setText(user_products_read[0].split(':')[1])
			self.basket_product_1_price.setText(user_products_read[0].split(':')[2] + ' руб.')
			self.basket_product_1_count.setText(user_products_read[0].split(':')[3])
			self.basket_product_1_price_sum.setText(user_products_read[0].split(':')[4] + ' руб.')
			self.basket_product_2_count_del_buy_style()
			self.basket_product_2_img_pix = QtGui.QPixmap(user_products_read[1].split(':')[0])
			self.basket_product_2_img.setPixmap(self.basket_product_2_img_pix)
			self.basket_product_2_name.setText(user_products_read[1].split(':')[1])
			self.basket_product_2_price.setText(user_products_read[1].split(':')[2] + ' руб.')
			self.basket_product_2_count.setText(user_products_read[1].split(':')[3])
			self.basket_product_2_price_sum.setText(user_products_read[1].split(':')[4] + ' руб.')
			self.basket_product_3_count_del_buy_style()
			self.basket_product_3_img_pix = QtGui.QPixmap(user_products_read[2].split(':')[0])
			self.basket_product_3_img.setPixmap(self.basket_product_3_img_pix)
			self.basket_product_3_name.setText(user_products_read[2].split(':')[1])
			self.basket_product_3_price.setText(user_products_read[2].split(':')[2] + ' руб.')
			self.basket_product_3_count.setText(user_products_read[2].split(':')[3])
			self.basket_product_3_price_sum.setText(user_products_read[2].split(':')[4] + ' руб.')
			self.basket_product_4_count_del_buy_style()
			self.basket_product_4_img_pix = QtGui.QPixmap(user_products_read[3].split(':')[0])
			self.basket_product_4_img.setPixmap(self.basket_product_4_img_pix)
			self.basket_product_4_name.setText(user_products_read[3].split(':')[1])
			self.basket_product_4_price.setText(user_products_read[3].split(':')[2] + ' руб.')
			self.basket_product_4_count.setText(user_products_read[3].split(':')[3])
			self.basket_product_4_price_sum.setText(user_products_read[3].split(':')[4] + ' руб.')
			self.basket_product_5_count_del_buy_style()
			self.basket_product_5_img_pix = QtGui.QPixmap(user_products_read[4].split(':')[0])
			self.basket_product_5_img.setPixmap(self.basket_product_5_img_pix)
			self.basket_product_5_name.setText(user_products_read[4].split(':')[1])
			self.basket_product_5_price.setText(user_products_read[4].split(':')[2] + ' руб.')
			self.basket_product_5_count.setText(user_products_read[4].split(':')[3])
			self.basket_product_5_price_sum.setText(user_products_read[4].split(':')[4] + ' руб.')
			self.basket_product_6_count_del_buy_style()
			self.basket_product_6_img_pix = QtGui.QPixmap(user_products_read[5].split(':')[0])
			self.basket_product_6_img.setPixmap(self.basket_product_6_img_pix)
			self.basket_product_6_name.setText(user_products_read[5].split(':')[1])
			self.basket_product_6_price.setText(user_products_read[5].split(':')[2] + ' руб.')
			self.basket_product_6_count.setText(user_products_read[5].split(':')[3])
			self.basket_product_6_price_sum.setText(user_products_read[5].split(':')[4] + ' руб.')
			self.basket_product_7_count_del_buy_style()
			self.basket_product_7_img_pix = QtGui.QPixmap(user_products_read[6].split(':')[0])
			self.basket_product_7_img.setPixmap(self.basket_product_7_img_pix)
			self.basket_product_7_name.setText(user_products_read[6].split(':')[1])
			self.basket_product_7_price.setText(user_products_read[6].split(':')[2] + ' руб.')
			self.basket_product_7_count.setText(user_products_read[6].split(':')[3])
			self.basket_product_7_price_sum.setText(user_products_read[6].split(':')[4] + ' руб.')
			self.basket_product_8_count_del_buy_style()
			self.basket_product_8_img_pix = QtGui.QPixmap(user_products_read[7].split(':')[0])
			self.basket_product_8_img.setPixmap(self.basket_product_8_img_pix)
			self.basket_product_8_name.setText(user_products_read[7].split(':')[1])
			self.basket_product_8_price.setText(user_products_read[7].split(':')[2] + ' руб.')
			self.basket_product_8_count.setText(user_products_read[7].split(':')[3])
			self.basket_product_8_price_sum.setText(user_products_read[7].split(':')[4] + ' руб.')
			self.basket_products_all_count.setText(str( int(user_products_read[0].split(':')[3]) + int(user_products_read[1].split(':')[3]) + int(user_products_read[2].split(':')[3]) + int(user_products_read[3].split(':')[3]) + int(user_products_read[4].split(':')[3]) + int(user_products_read[5].split(':')[3]) + int(user_products_read[6].split(':')[3]) + int(user_products_read[7].split(':')[3]) ) + ' шт.')
			self.basket_products_all_price_sum.setText(str( int(user_products_read[0].split(':')[4]) + int(user_products_read[1].split(':')[4]) + int(user_products_read[2].split(':')[4]) + int(user_products_read[3].split(':')[4]) + int(user_products_read[4].split(':')[4]) + int(user_products_read[5].split(':')[4]) + int(user_products_read[6].split(':')[4]) + int(user_products_read[7].split(':')[4]) ) + ' руб.')
		elif (user_products_read.count(';') == 9 ):
			user_products_read = user_products_read.split(';')
			self.name_categoriy.setText('В корзине 9 товаров')
			self.basket_product_1_count_del_buy_style()
			self.basket_product_1_img_pix = QtGui.QPixmap(user_products_read[0].split(':')[0])
			self.basket_product_1_img.setPixmap(self.basket_product_1_img_pix)
			self.basket_product_1_name.setText(user_products_read[0].split(':')[1])
			self.basket_product_1_price.setText(user_products_read[0].split(':')[2] + ' руб.')
			self.basket_product_1_count.setText(user_products_read[0].split(':')[3])
			self.basket_product_1_price_sum.setText(user_products_read[0].split(':')[4] + ' руб.')
			self.basket_product_2_count_del_buy_style()
			self.basket_product_2_img_pix = QtGui.QPixmap(user_products_read[1].split(':')[0])
			self.basket_product_2_img.setPixmap(self.basket_product_2_img_pix)
			self.basket_product_2_name.setText(user_products_read[1].split(':')[1])
			self.basket_product_2_price.setText(user_products_read[1].split(':')[2] + ' руб.')
			self.basket_product_2_count.setText(user_products_read[1].split(':')[3])
			self.basket_product_2_price_sum.setText(user_products_read[1].split(':')[4] + ' руб.')
			self.basket_product_3_count_del_buy_style()
			self.basket_product_3_img_pix = QtGui.QPixmap(user_products_read[2].split(':')[0])
			self.basket_product_3_img.setPixmap(self.basket_product_3_img_pix)
			self.basket_product_3_name.setText(user_products_read[2].split(':')[1])
			self.basket_product_3_price.setText(user_products_read[2].split(':')[2] + ' руб.')
			self.basket_product_3_count.setText(user_products_read[2].split(':')[3])
			self.basket_product_3_price_sum.setText(user_products_read[2].split(':')[4] + ' руб.')
			self.basket_product_4_count_del_buy_style()
			self.basket_product_4_img_pix = QtGui.QPixmap(user_products_read[3].split(':')[0])
			self.basket_product_4_img.setPixmap(self.basket_product_4_img_pix)
			self.basket_product_4_name.setText(user_products_read[3].split(':')[1])
			self.basket_product_4_price.setText(user_products_read[3].split(':')[2] + ' руб.')
			self.basket_product_4_count.setText(user_products_read[3].split(':')[3])
			self.basket_product_4_price_sum.setText(user_products_read[3].split(':')[4] + ' руб.')
			self.basket_product_5_count_del_buy_style()
			self.basket_product_5_img_pix = QtGui.QPixmap(user_products_read[4].split(':')[0])
			self.basket_product_5_img.setPixmap(self.basket_product_5_img_pix)
			self.basket_product_5_name.setText(user_products_read[4].split(':')[1])
			self.basket_product_5_price.setText(user_products_read[4].split(':')[2] + ' руб.')
			self.basket_product_5_count.setText(user_products_read[4].split(':')[3])
			self.basket_product_5_price_sum.setText(user_products_read[4].split(':')[4] + ' руб.')
			self.basket_product_6_count_del_buy_style()
			self.basket_product_6_img_pix = QtGui.QPixmap(user_products_read[5].split(':')[0])
			self.basket_product_6_img.setPixmap(self.basket_product_6_img_pix)
			self.basket_product_6_name.setText(user_products_read[5].split(':')[1])
			self.basket_product_6_price.setText(user_products_read[5].split(':')[2] + ' руб.')
			self.basket_product_6_count.setText(user_products_read[5].split(':')[3])
			self.basket_product_6_price_sum.setText(user_products_read[5].split(':')[4] + ' руб.')
			self.basket_product_7_count_del_buy_style()
			self.basket_product_7_img_pix = QtGui.QPixmap(user_products_read[6].split(':')[0])
			self.basket_product_7_img.setPixmap(self.basket_product_7_img_pix)
			self.basket_product_7_name.setText(user_products_read[6].split(':')[1])
			self.basket_product_7_price.setText(user_products_read[6].split(':')[2] + ' руб.')
			self.basket_product_7_count.setText(user_products_read[6].split(':')[3])
			self.basket_product_7_price_sum.setText(user_products_read[6].split(':')[4] + ' руб.')
			self.basket_product_8_count_del_buy_style()
			self.basket_product_8_img_pix = QtGui.QPixmap(user_products_read[7].split(':')[0])
			self.basket_product_8_img.setPixmap(self.basket_product_8_img_pix)
			self.basket_product_8_name.setText(user_products_read[7].split(':')[1])
			self.basket_product_8_price.setText(user_products_read[7].split(':')[2] + ' руб.')
			self.basket_product_8_count.setText(user_products_read[7].split(':')[3])
			self.basket_product_8_price_sum.setText(user_products_read[7].split(':')[4] + ' руб.')
			self.basket_product_9_count_del_buy_style()
			self.basket_product_9_img_pix = QtGui.QPixmap(user_products_read[8].split(':')[0])
			self.basket_product_9_img.setPixmap(self.basket_product_9_img_pix)
			self.basket_product_9_name.setText(user_products_read[8].split(':')[1])
			self.basket_product_9_price.setText(user_products_read[8].split(':')[2] + ' руб.')
			self.basket_product_9_count.setText(user_products_read[8].split(':')[3])
			self.basket_product_9_price_sum.setText(user_products_read[8].split(':')[4] + ' руб.')
			self.basket_products_all_count.setText(str( int(user_products_read[0].split(':')[3]) + int(user_products_read[1].split(':')[3]) + int(user_products_read[2].split(':')[3]) + int(user_products_read[3].split(':')[3]) + int(user_products_read[4].split(':')[3]) + int(user_products_read[5].split(':')[3]) + int(user_products_read[6].split(':')[3]) + int(user_products_read[7].split(':')[3]) + int(user_products_read[8].split(':')[3]) ) + ' шт.')
			self.basket_products_all_price_sum.setText(str( int(user_products_read[0].split(':')[4]) + int(user_products_read[1].split(':')[4]) + int(user_products_read[2].split(':')[4]) + int(user_products_read[3].split(':')[4]) + int(user_products_read[4].split(':')[4]) + int(user_products_read[5].split(':')[4]) + int(user_products_read[6].split(':')[4]) + int(user_products_read[7].split(':')[4]) + int(user_products_read[8].split(':')[4]) ) + ' руб.')
		elif (user_products_read.count(';') == 10 ):
			user_products_read = user_products_read.split(';')
			self.name_categoriy.setText('В корзине 10 товаров')
			self.basket_product_1_count_del_buy_style()
			self.basket_product_1_img_pix = QtGui.QPixmap(user_products_read[0].split(':')[0])
			self.basket_product_1_img.setPixmap(self.basket_product_1_img_pix)
			self.basket_product_1_name.setText(user_products_read[0].split(':')[1])
			self.basket_product_1_price.setText(user_products_read[0].split(':')[2] + ' руб.')
			self.basket_product_1_count.setText(user_products_read[0].split(':')[3])
			self.basket_product_1_price_sum.setText(user_products_read[0].split(':')[4] + ' руб.')
			self.basket_product_2_count_del_buy_style()
			self.basket_product_2_img_pix = QtGui.QPixmap(user_products_read[1].split(':')[0])
			self.basket_product_2_img.setPixmap(self.basket_product_2_img_pix)
			self.basket_product_2_name.setText(user_products_read[1].split(':')[1])
			self.basket_product_2_price.setText(user_products_read[1].split(':')[2] + ' руб.')
			self.basket_product_2_count.setText(user_products_read[1].split(':')[3])
			self.basket_product_2_price_sum.setText(user_products_read[1].split(':')[4] + ' руб.')
			self.basket_product_3_count_del_buy_style()
			self.basket_product_3_img_pix = QtGui.QPixmap(user_products_read[2].split(':')[0])
			self.basket_product_3_img.setPixmap(self.basket_product_3_img_pix)
			self.basket_product_3_name.setText(user_products_read[2].split(':')[1])
			self.basket_product_3_price.setText(user_products_read[2].split(':')[2] + ' руб.')
			self.basket_product_3_count.setText(user_products_read[2].split(':')[3])
			self.basket_product_3_price_sum.setText(user_products_read[2].split(':')[4] + ' руб.')
			self.basket_product_4_count_del_buy_style()
			self.basket_product_4_img_pix = QtGui.QPixmap(user_products_read[3].split(':')[0])
			self.basket_product_4_img.setPixmap(self.basket_product_4_img_pix)
			self.basket_product_4_name.setText(user_products_read[3].split(':')[1])
			self.basket_product_4_price.setText(user_products_read[3].split(':')[2] + ' руб.')
			self.basket_product_4_count.setText(user_products_read[3].split(':')[3])
			self.basket_product_4_price_sum.setText(user_products_read[3].split(':')[4] + ' руб.')
			self.basket_product_5_count_del_buy_style()
			self.basket_product_5_img_pix = QtGui.QPixmap(user_products_read[4].split(':')[0])
			self.basket_product_5_img.setPixmap(self.basket_product_5_img_pix)
			self.basket_product_5_name.setText(user_products_read[4].split(':')[1])
			self.basket_product_5_price.setText(user_products_read[4].split(':')[2] + ' руб.')
			self.basket_product_5_count.setText(user_products_read[4].split(':')[3])
			self.basket_product_5_price_sum.setText(user_products_read[4].split(':')[4] + ' руб.')
			self.basket_product_6_count_del_buy_style()
			self.basket_product_6_img_pix = QtGui.QPixmap(user_products_read[5].split(':')[0])
			self.basket_product_6_img.setPixmap(self.basket_product_6_img_pix)
			self.basket_product_6_name.setText(user_products_read[5].split(':')[1])
			self.basket_product_6_price.setText(user_products_read[5].split(':')[2] + ' руб.')
			self.basket_product_6_count.setText(user_products_read[5].split(':')[3])
			self.basket_product_6_price_sum.setText(user_products_read[5].split(':')[4] + ' руб.')
			self.basket_product_7_count_del_buy_style()
			self.basket_product_7_img_pix = QtGui.QPixmap(user_products_read[6].split(':')[0])
			self.basket_product_7_img.setPixmap(self.basket_product_7_img_pix)
			self.basket_product_7_name.setText(user_products_read[6].split(':')[1])
			self.basket_product_7_price.setText(user_products_read[6].split(':')[2] + ' руб.')
			self.basket_product_7_count.setText(user_products_read[6].split(':')[3])
			self.basket_product_7_price_sum.setText(user_products_read[6].split(':')[4] + ' руб.')
			self.basket_product_8_count_del_buy_style()
			self.basket_product_8_img_pix = QtGui.QPixmap(user_products_read[7].split(':')[0])
			self.basket_product_8_img.setPixmap(self.basket_product_8_img_pix)
			self.basket_product_8_name.setText(user_products_read[7].split(':')[1])
			self.basket_product_8_price.setText(user_products_read[7].split(':')[2] + ' руб.')
			self.basket_product_8_count.setText(user_products_read[7].split(':')[3])
			self.basket_product_8_price_sum.setText(user_products_read[7].split(':')[4] + ' руб.')
			self.basket_product_9_count_del_buy_style()
			self.basket_product_9_img_pix = QtGui.QPixmap(user_products_read[8].split(':')[0])
			self.basket_product_9_img.setPixmap(self.basket_product_9_img_pix)
			self.basket_product_9_name.setText(user_products_read[8].split(':')[1])
			self.basket_product_9_price.setText(user_products_read[8].split(':')[2] + ' руб.')
			self.basket_product_9_count.setText(user_products_read[8].split(':')[3])
			self.basket_product_9_price_sum.setText(user_products_read[8].split(':')[4] + ' руб.')
			self.basket_product_10_count_del_buy_style()
			self.basket_product_10_img_pix = QtGui.QPixmap(user_products_read[9].split(':')[0])
			self.basket_product_10_img.setPixmap(self.basket_product_10_img_pix)
			self.basket_product_10_name.setText(user_products_read[9].split(':')[1])
			self.basket_product_10_price.setText(user_products_read[9].split(':')[2] + ' руб.')
			self.basket_product_10_count.setText(user_products_read[9].split(':')[3])
			self.basket_product_10_price_sum.setText(user_products_read[9].split(':')[4] + ' руб.')
			self.basket_products_all_count.setText(str( int(user_products_read[0].split(':')[3]) + int(user_products_read[1].split(':')[3]) + int(user_products_read[2].split(':')[3]) + int(user_products_read[3].split(':')[3]) + int(user_products_read[4].split(':')[3]) + int(user_products_read[5].split(':')[3]) + int(user_products_read[6].split(':')[3]) + int(user_products_read[7].split(':')[3]) + int(user_products_read[8].split(':')[3]) + int(user_products_read[9].split(':')[3]) ) + ' шт.')
			self.basket_products_all_price_sum.setText(str( int(user_products_read[0].split(':')[4]) + int(user_products_read[1].split(':')[4]) + int(user_products_read[2].split(':')[4]) + int(user_products_read[3].split(':')[4]) + int(user_products_read[4].split(':')[4]) + int(user_products_read[5].split(':')[4]) + int(user_products_read[6].split(':')[4]) + int(user_products_read[7].split(':')[4]) + int(user_products_read[8].split(':')[4]) + int(user_products_read[9].split(':')[4]) ) + ' руб.')
		user_products.close()

		self.setWindowTitle('App_Shop - Корзина')


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




	def catalog_portativ(self): # Каталог - Телефоны и гаджеты
		self.catalog_portativ_Window = QWidget(self)
		self.setCentralWidget(self.catalog_portativ_Window)

		# Белый фон
		self.background_img = QLabel(self.catalog_portativ_Window)
		self.background_img_window()

		# Лого мини
		self.logo_img = QLabel(self.catalog_portativ_Window)
		self.logo_mini()

		# Поиск
		self.search_Input_shop = QLineEdit('Быстрый поиск', self.catalog_portativ_Window)
		self.search_Btn_shop = QPushButton('', self.catalog_portativ_Window)
		self.search_products()

		# Название категории
		self.name_categoriy = QLabel('Мобильные телефоны', self.catalog_portativ_Window)
		self.name_categoriy_window()

		# Корзина
		self.basket_Btn = QPushButton('', self.catalog_portativ_Window)
		self.basket_Btn.clicked.connect(self.basket_big_window)
		if (self.basket_price > 0):
			self.basket_price_label = QLabel(str(self.basket_price) + ' руб', self.catalog_portativ_Window)
		if (self.basket_count == 0):
			self.basket_count_label = QLabel('В корзине', self.catalog_portativ_Window)
			self.basket_price_label = QLabel('нет товаров', self.catalog_portativ_Window)
		elif (self.basket_count == 1):
			self.basket_count_label = QLabel(str(self.basket_count) + ' товар', self.catalog_portativ_Window)
		elif (self.basket_count < 5):
			self.basket_count_label = QLabel(str(self.basket_count) + ' товара', self.catalog_portativ_Window)
		elif (self.basket_count >= 5):
			self.basket_count_label = QLabel(str(self.basket_count) + ' товаров', self.catalog_portativ_Window)
		self.basket_price_label.resize(200, 12)
		self.basket_count_label.resize(120, 12)
		self.add_to_basket()

		# Левый sidebar-catalog_menu_btn (active)
		self.btn_catalog_portativ_active = QPushButton(self.catalog_portativ_Window)
		self.catalog_menu_btn_active.catalog_menu_btn_portativ_active(self)

		# Левый sidebar-catalog_menu_btn
		self.btn_catalog_auto = QPushButton(self.catalog_portativ_Window)
		self.btn_catalog_games = QPushButton(self.catalog_portativ_Window)
		self.btn_catalog_beauty = QPushButton(self.catalog_portativ_Window)
		self.btn_catalog_remont = QPushButton(self.catalog_portativ_Window)
		self.btn_catalog_network = QPushButton(self.catalog_portativ_Window)
		self.btn_catalog_forHome = QPushButton(self.catalog_portativ_Window)
		self.btn_catalog_cameras = QPushButton(self.catalog_portativ_Window)
		self.btn_catalog_computers = QPushButton(self.catalog_portativ_Window)
		self.btn_catalog_audioVideo = QPushButton(self.catalog_portativ_Window)
		self.btn_catalog_climateControl = QPushButton(self.catalog_portativ_Window)
		self.btn_catalog_ucenennyeTovary = QPushButton(self.catalog_portativ_Window)
		self.catalog_menu_btn.menu_btn(self)

		# Продукты (Телефоны и гаджеты)
		# Продукт 1
		self.product_bg_img = QLabel(self.catalog_portativ_Window)
		self.product_bg_img.move(90, 115)
		self.product_img = QLabel(self.catalog_portativ_Window)
		self.product_pix = QtGui.QPixmap("img/portativ/galaxy_s9+_64gb.jpg")
		self.product_img.move(100, 125)
		self.product()
		self.product_1_img = 'img/portativ/basket_galaxy_s9+_64gb.jpg'
		self.product_1_name = QLabel('Samsung Galaxy S9+ 64GB', self.catalog_portativ_Window)
		self.product_1_count = QLabel('1', self.catalog_portativ_Window)
		self.product_1_price = QLabel('Цена: 55350 руб', self.catalog_portativ_Window)
		self.product_1_price_int = self.product_1_price.text()[6:-4]
		self.product_1_price_sum = self.product_1_price.text()[6:-4]
		self.product_1_add_basket = QPushButton('В корзину', self.catalog_portativ_Window)
		self.product_1_add_basket.clicked.connect(self.basket_product_1)
		self.product_1_8_style.product_1_style(self)

		# Продукт 2
		self.product_bg_img = QLabel(self.catalog_portativ_Window)
		self.product_bg_img.move(330, 115)
		self.product_img = QLabel(self.catalog_portativ_Window)
		self.product_pix = QtGui.QPixmap("img/portativ/apple_iphone_7_32gb.jpg")
		self.product_img.move(340, 125)
		self.product()
		self.product_2_img = 'img/portativ/basket_apple_iphone_7_32gb.jpg'
		self.product_2_name = QLabel('Apple iPhone 7 32Gb silver', self.catalog_portativ_Window)
		self.product_2_count = QLabel('1', self.catalog_portativ_Window)
		self.product_2_price = QLabel('Цена: 38490 руб', self.catalog_portativ_Window)
		self.product_2_price_int = self.product_2_price.text()[6:-4]
		self.product_2_price_sum = self.product_2_price.text()[6:-4]
		self.product_2_add_basket = QPushButton('В корзину', self.catalog_portativ_Window)
		self.product_2_add_basket.clicked.connect(self.basket_product_2)
		self.product_1_8_style.product_2_style(self)

		# Продукт 3
		self.product_bg_img = QLabel(self.catalog_portativ_Window)
		self.product_bg_img.move(570, 115)
		self.product_img = QLabel(self.catalog_portativ_Window)
		self.product_pix = QtGui.QPixmap("img/portativ/apple_iphone_x_64gb_silver.jpg")
		self.product_img.move(580, 125)
		self.product()
		self.product_3_img = 'img/portativ/basket_apple_iphone_x_64gb_silver.jpg'
		self.product_3_name = QLabel('Apple iPhone X 64GB Silver', self.catalog_portativ_Window)
		self.product_3_count = QLabel('1', self.catalog_portativ_Window)
		self.product_3_price = QLabel('Цена: 67990 руб', self.catalog_portativ_Window)
		self.product_3_price_int = self.product_3_price.text()[6:-4]
		self.product_3_price_sum = self.product_3_price.text()[6:-4]
		self.product_3_add_basket = QPushButton('В корзину', self.catalog_portativ_Window)
		self.product_3_add_basket.clicked.connect(self.basket_product_3)
		self.product_1_8_style.product_3_style(self)

		# Продукт 4
		self.product_bg_img = QLabel(self.catalog_portativ_Window)
		self.product_bg_img.move(810, 115)
		self.product_img = QLabel(self.catalog_portativ_Window)
		self.product_pix = QtGui.QPixmap("img/portativ/sony_xperia_xa_f5122_16_gb.jpg")
		self.product_img.move(820, 125)
		self.product()
		self.product_4_img = 'img/portativ/basket_sony_xperia_xa_f5122_16_gb.jpg'
		self.product_4_name = QLabel('Sony Xperia XA F5122 16GB Black', self.catalog_portativ_Window)
		self.product_4_count = QLabel('1', self.catalog_portativ_Window)
		self.product_4_price = QLabel('Цена: 12990 руб', self.catalog_portativ_Window)
		self.product_4_price_int = self.product_4_price.text()[6:-4]
		self.product_4_price_sum = self.product_4_price.text()[6:-4]
		self.product_4_add_basket = QPushButton('В корзину', self.catalog_portativ_Window)
		self.product_4_add_basket.clicked.connect(self.basket_product_4)
		self.product_1_8_style.product_4_style(self)

		# Продукт 5
		self.product_bg_img = QLabel(self.catalog_portativ_Window)
		self.product_bg_img.move(90, 405)
		self.product_img = QLabel(self.catalog_portativ_Window)
		self.product_pix = QtGui.QPixmap("img/portativ/xiaomi_redmi_note_4X_32gb_blue.jpg")
		self.product_img.move(100, 415)
		self.product()
		self.product_5_img = 'img/portativ/basket_xiaomi_redmi_note_4X_32gb_blue.jpg'
		self.product_5_name = QLabel('Xiaomi Redmi Note 4X 32GB Blue', self.catalog_portativ_Window)
		self.product_5_count = QLabel('1', self.catalog_portativ_Window)
		self.product_5_price = QLabel('Цена: 9650 руб', self.catalog_portativ_Window)
		self.product_5_price_int = self.product_5_price.text()[6:-4]
		self.product_5_price_sum = self.product_5_price.text()[6:-4]
		self.product_5_add_basket = QPushButton('В корзину', self.catalog_portativ_Window)
		self.product_5_add_basket.clicked.connect(self.basket_product_5)
		self.product_1_8_style.product_5_style(self)

		# Продукт 6
		self.product_bg_img = QLabel(self.catalog_portativ_Window)
		self.product_bg_img.move(330, 405)
		self.product_img = QLabel(self.catalog_portativ_Window)
		self.product_pix = QtGui.QPixmap("img/portativ/huawei_honor_8_lite_32gb_blue.jpg")
		self.product_img.move(340, 415)
		self.product()
		self.product_6_img = 'img/portativ/basket_huawei_honor_8_lite_32gb_blue.jpg'
		self.product_6_name = QLabel('Huawei Honor 8 Lite 32GB Blue', self.catalog_portativ_Window)
		self.product_6_count = QLabel('1', self.catalog_portativ_Window)
		self.product_6_price = QLabel('Цена: 12990 руб', self.catalog_portativ_Window)
		self.product_6_price_int = self.product_6_price.text()[6:-4]
		self.product_6_price_sum = self.product_6_price.text()[6:-4]
		self.product_6_add_basket = QPushButton('В корзину', self.catalog_portativ_Window)
		self.product_6_add_basket.clicked.connect(self.basket_product_6)
		self.product_1_8_style.product_6_style(self)

		# Продукт 7
		self.product_bg_img = QLabel(self.catalog_portativ_Window)
		self.product_bg_img.move(570, 405)
		self.product_img = QLabel(self.catalog_portativ_Window)
		self.product_pix = QtGui.QPixmap("img/portativ/meizu_pro_6s_64gb.jpg")
		self.product_img.move(580, 415)
		self.product()
		self.product_7_img = 'img/portativ/basket_meizu_pro_6s_64gb.jpg'
		self.product_7_name = QLabel('Meizu Pro 6s 64GB Gold', self.catalog_portativ_Window)
		self.product_7_count = QLabel('1', self.catalog_portativ_Window)
		self.product_7_price = QLabel('Цена: 14350 руб', self.catalog_portativ_Window)
		self.product_7_price_int = self.product_7_price.text()[6:-4]
		self.product_7_price_sum = self.product_7_price.text()[6:-4]
		self.product_7_add_basket = QPushButton('В корзину', self.catalog_portativ_Window)
		self.product_7_add_basket.clicked.connect(self.basket_product_7)
		self.product_1_8_style.product_7_style(self)

		# Продукт 8
		self.product_bg_img = QLabel(self.catalog_portativ_Window)
		self.product_bg_img.move(810, 405)
		self.product_img = QLabel(self.catalog_portativ_Window)
		self.product_pix = QtGui.QPixmap("img/portativ/asus_zenfone_max_16gb_black.jpg")
		self.product_img.move(820, 415)
		self.product()
		self.product_8_img = 'img/portativ/basket_asus_zenfone_max_16gb_black.jpg'
		self.product_8_name = QLabel('Asus ZenFone Max 16GB Black', self.catalog_portativ_Window)
		self.product_8_count = QLabel('1', self.catalog_portativ_Window)
		self.product_8_price = QLabel('Цена: 7990 руб', self.catalog_portativ_Window)
		self.product_8_price_int = self.product_8_price.text()[6:-4]
		self.product_8_price_sum = self.product_8_price.text()[6:-4]
		self.product_8_add_basket = QPushButton('В корзину', self.catalog_portativ_Window)
		self.product_8_add_basket.clicked.connect(self.basket_product_8)
		self.product_1_8_style.product_8_style(self)

		self.setWindowTitle('App_Shop - Телефоны и гаджеты')

	def catalog_computers(self): # Каталог - Компьютеры и ноутбуки
		self.catalog_computers_Window = QWidget(self)
		self.setCentralWidget(self.catalog_computers_Window)

		# Белый фон
		self.background_img = QLabel(self.catalog_computers_Window)
		self.background_img_window()

		# Левый sidebar-catalog_menu_btn (active)
		self.btn_catalog_computers_active = QPushButton(self.catalog_computers_Window)
		self.catalog_menu_btn_active.catalog_menu_btn_computers_active(self)

		# Лого мини
		self.logo_img = QLabel(self.catalog_computers_Window)
		self.logo_mini()

		# Поиск
		self.search_Input_shop = QLineEdit('Быстрый поиск', self.catalog_computers_Window)
		self.search_Btn_shop = QPushButton('', self.catalog_computers_Window)
		self.search_products()

		# Название категории
		self.name_categoriy = QLabel('Компьютеры и ноутбуки', self.catalog_computers_Window)
		self.name_categoriy_window()

		# Корзина
		self.basket_Btn = QPushButton('', self.catalog_computers_Window)
		self.basket_Btn.clicked.connect(self.basket_big_window)
		if (self.basket_price > 0):
			self.basket_price_label = QLabel(str(self.basket_price) + ' руб', self.catalog_computers_Window)
		if (self.basket_count == 0):
			self.basket_count_label = QLabel('В корзине', self.catalog_computers_Window)
			self.basket_price_label = QLabel('нет товаров', self.catalog_computers_Window)
		elif (self.basket_count == 1):
			self.basket_count_label = QLabel(str(self.basket_count) + ' товар', self.catalog_computers_Window)
		elif (self.basket_count < 5):
			self.basket_count_label = QLabel(str(self.basket_count) + ' товара', self.catalog_computers_Window)
		elif (self.basket_count >= 5):
			self.basket_count_label = QLabel(str(self.basket_count) + ' товаров', self.catalog_computers_Window)
		self.basket_price_label.resize(200, 12)
		self.basket_count_label.resize(120, 12)
		self.add_to_basket()

		# Левый sidebar-catalog_menu_btn
		self.btn_catalog_auto = QPushButton(self.catalog_computers_Window)
		self.btn_catalog_games = QPushButton(self.catalog_computers_Window)
		self.btn_catalog_beauty = QPushButton(self.catalog_computers_Window)
		self.btn_catalog_remont = QPushButton(self.catalog_computers_Window)
		self.btn_catalog_forHome = QPushButton(self.catalog_computers_Window)
		self.btn_catalog_network = QPushButton(self.catalog_computers_Window)
		self.btn_catalog_cameras = QPushButton(self.catalog_computers_Window)
		self.btn_catalog_portativ = QPushButton(self.catalog_computers_Window)
		self.btn_catalog_audioVideo = QPushButton(self.catalog_computers_Window)
		self.btn_catalog_climateControl = QPushButton(self.catalog_computers_Window)
		self.btn_catalog_ucenennyeTovary = QPushButton(self.catalog_computers_Window)
		self.catalog_menu_btn.menu_btn(self)


		# Продукты (Компьютеры и ноутбуки)
		# Продукт 1
		self.product_bg_img = QLabel(self.catalog_computers_Window)
		self.product_bg_img.move(90, 115)
		self.product_img = QLabel(self.catalog_computers_Window)
		self.product_pix = QtGui.QPixmap("img/computers/pc_of_base_corei7_7700k.jpg")
		self.product_img.move(100, 125)
		self.product()
		self.product_1_img = 'img/computers/basket_pc_of_base_corei7_7700k.jpg'
		self.product_1_name = QLabel('i7-7700k/GTX 1080ti/DDR4 16GB', self.catalog_computers_Window)
		self.product_1_count = QLabel('1', self.catalog_computers_Window)
		self.product_1_price = QLabel('Цена: 185000 руб', self.catalog_computers_Window)
		self.product_1_price_int = self.product_1_price.text()[6:-4]
		self.product_1_price_sum = self.product_1_price.text()[6:-4]
		self.product_1_add_basket = QPushButton('В корзину', self.catalog_computers_Window)
		self.product_1_add_basket.clicked.connect(self.basket_product_1)
		self.product_1_8_style.product_1_style(self)

		# Продукт 2
		self.product_bg_img = QLabel(self.catalog_computers_Window)
		self.product_bg_img.move(330, 115)
		self.product_img = QLabel(self.catalog_computers_Window)
		self.product_pix = QtGui.QPixmap("img/computers/pc_of_base_corei3_7100.jpg")
		self.product_img.move(340, 125)
		self.product()
		self.product_2_img = 'img/computers/basket_pc_of_base_corei3_7100.jpg'
		self.product_2_name = QLabel('i3-7100/GTX 1050/DDR4 4GB', self.catalog_computers_Window)
		self.product_2_count = QLabel('1', self.catalog_computers_Window)
		self.product_2_price = QLabel('Цена: 37400 руб', self.catalog_computers_Window)
		self.product_2_price_int = self.product_2_price.text()[6:-4]
		self.product_2_price_sum = self.product_2_price.text()[6:-4]
		self.product_2_add_basket = QPushButton('В корзину', self.catalog_computers_Window)
		self.product_2_add_basket.clicked.connect(self.basket_product_2)
		self.product_1_8_style.product_2_style(self)

		# Продукт 3
		self.product_bg_img = QLabel(self.catalog_computers_Window)
		self.product_bg_img.move(570, 115)
		self.product_img = QLabel(self.catalog_computers_Window)
		self.product_pix = QtGui.QPixmap("img/computers/pc_of_base_core-7_7800k.jpg")
		self.product_img.move(580, 125)
		self.product()
		self.product_3_img = 'img/computers/basket_pc_of_base_core-7_7800k.jpg'
		self.product_3_name = QLabel('i7-7800k/GTX 1070/DDR4 16GB', self.catalog_computers_Window)
		self.product_3_count = QLabel('1', self.catalog_computers_Window)
		self.product_3_price = QLabel('Цена: 134500 руб', self.catalog_computers_Window)
		self.product_3_price_int = self.product_3_price.text()[6:-4]
		self.product_3_price_sum = self.product_3_price.text()[6:-4]
		self.product_3_add_basket = QPushButton('В корзину', self.catalog_computers_Window)
		self.product_3_add_basket.clicked.connect(self.basket_product_3)
		self.product_1_8_style.product_3_style(self)

		# Продукт 4
		self.product_bg_img = QLabel(self.catalog_computers_Window)
		self.product_bg_img.move(810, 115)
		self.product_img = QLabel(self.catalog_computers_Window)
		self.product_pix = QtGui.QPixmap("img/computers/pc_of_base_pentium_g4560.jpg")
		self.product_img.move(820, 125)
		self.product()
		self.product_4_img = 'img/computers/basket_pc_of_base_pentium_g4560.jpg'
		self.product_4_name = QLabel('Ptm G4560/GTX 1050/DDR4 8GB', self.catalog_computers_Window)
		self.product_4_count = QLabel('1', self.catalog_computers_Window)
		self.product_4_price = QLabel('Цена: 31940 руб', self.catalog_computers_Window)
		self.product_4_price_int = self.product_4_price.text()[6:-4]
		self.product_4_price_sum = self.product_4_price.text()[6:-4]
		self.product_4_add_basket = QPushButton('В корзину', self.catalog_computers_Window)
		self.product_4_add_basket.clicked.connect(self.basket_product_4)
		self.product_1_8_style.product_4_style(self)

		# Продукт 5
		self.product_bg_img = QLabel(self.catalog_computers_Window)
		self.product_bg_img.move(90, 405)
		self.product_img = QLabel(self.catalog_computers_Window)
		self.product_pix = QtGui.QPixmap("img/computers/notebook_asus_x541nc_gq081t.jpg")
		self.product_img.move(100, 415)
		self.product()
		self.product_5_img = 'img/computers/basket_notebook_asus_x541nc_gq081t.jpg'
		self.product_5_name = QLabel('Asus X541NC-GQ081T', self.catalog_computers_Window)
		self.product_5_count = QLabel('1', self.catalog_computers_Window)
		self.product_5_price = QLabel('Цена: 24690 руб', self.catalog_computers_Window)
		self.product_5_price_int = self.product_5_price.text()[6:-4]
		self.product_5_price_sum = self.product_5_price.text()[6:-4]
		self.product_5_add_basket = QPushButton('В корзину', self.catalog_computers_Window)
		self.product_5_add_basket.clicked.connect(self.basket_product_5)
		self.product_1_8_style.product_5_style(self)

		# Продукт 6
		self.product_bg_img = QLabel(self.catalog_computers_Window)
		self.product_bg_img.move(330, 405)
		self.product_img = QLabel(self.catalog_computers_Window)
		self.product_pix = QtGui.QPixmap("img/computers/notebook_lenovo_520_15ikb.jpg")
		self.product_img.move(340, 415)
		self.product()
		self.product_6_img = 'img/computers/basket_notebook_lenovo_520_15ikb.jpg'
		self.product_6_name = QLabel('Lenovo 520-15IKB', self.catalog_computers_Window)
		self.product_6_count = QLabel('1', self.catalog_computers_Window)
		self.product_6_price = QLabel('Цена: 38990 руб', self.catalog_computers_Window)
		self.product_6_price_int = self.product_6_price.text()[6:-4]
		self.product_6_price_sum = self.product_6_price.text()[6:-4]
		self.product_6_add_basket = QPushButton('В корзину', self.catalog_computers_Window)
		self.product_6_add_basket.clicked.connect(self.basket_product_6)
		self.product_1_8_style.product_6_style(self)

		# Продукт 7
		self.product_bg_img = QLabel(self.catalog_computers_Window)
		self.product_bg_img.move(570, 405)
		self.product_img = QLabel(self.catalog_computers_Window)
		self.product_pix = QtGui.QPixmap("img/computers/notebook_asus_rog_gl502vm.jpg")
		self.product_img.move(580, 415)
		self.product()
		self.product_7_img = 'img/computers/basket_notebook_asus_rog_gl502vm.jpg'
		self.product_7_name = QLabel('Asus ROG GL502VM', self.catalog_computers_Window)
		self.product_7_count = QLabel('1', self.catalog_computers_Window)
		self.product_7_price = QLabel('Цена: 84690 руб', self.catalog_computers_Window)
		self.product_7_price_int = self.product_7_price.text()[6:-4]
		self.product_7_price_sum = self.product_7_price.text()[6:-4]
		self.product_7_add_basket = QPushButton('В корзину', self.catalog_computers_Window)
		self.product_7_add_basket.clicked.connect(self.basket_product_7)
		self.product_1_8_style.product_7_style(self)

		# Продукт 8
		self.product_bg_img = QLabel(self.catalog_computers_Window)
		self.product_bg_img.move(810, 405)
		self.product_img = QLabel(self.catalog_computers_Window)
		self.product_pix = QtGui.QPixmap("img/computers/notebook_apple_macbook_pro_15.jpg")
		self.product_img.move(820, 415)
		self.product()
		self.product_8_img = 'img/computers/basket_notebook_apple_macbook_pro_15.jpg'
		self.product_8_name = QLabel('Apple MacBook Pro 15\"', self.catalog_computers_Window)
		self.product_8_count = QLabel('1', self.catalog_computers_Window)
		self.product_8_price = QLabel('Цена: 158990 руб', self.catalog_computers_Window)
		self.product_8_price_int = self.product_8_price.text()[6:-4]
		self.product_8_price_sum = self.product_8_price.text()[6:-4]
		self.product_8_add_basket = QPushButton('В корзину', self.catalog_computers_Window)
		self.product_8_add_basket.clicked.connect(self.basket_product_8)
		self.product_1_8_style.product_8_style(self)

		self.setWindowTitle('App_Shop - Компьютеры и ноутбуки')

	def catalog_network(self): # Каталог - Сети, Оргтехника
		self.catalog_network_Window = QWidget(self)
		self.setCentralWidget(self.catalog_network_Window)

		# Белый фон
		self.background_img = QLabel(self.catalog_network_Window)
		self.background_img_window()

		# Левый sidebar-catalog_menu_btn (active)
		self.btn_catalog_network_active = QPushButton(self.catalog_network_Window)
		self.catalog_menu_btn_active.catalog_menu_btn_network_active(self)

		# Лого мини
		self.logo_img = QLabel(self.catalog_network_Window)
		self.logo_mini()

		# Поиск
		self.search_Input_shop = QLineEdit('Быстрый поиск', self.catalog_network_Window)
		self.search_Btn_shop = QPushButton('', self.catalog_network_Window)
		self.search_products()

		# Название категории
		self.name_categoriy = QLabel('Сети, оргтехника, ПО', self.catalog_network_Window)
		self.name_categoriy_window()

		# Корзина
		self.basket_Btn = QPushButton('', self.catalog_network_Window)
		self.basket_Btn.clicked.connect(self.basket_big_window)
		if (self.basket_price > 0):
			self.basket_price_label = QLabel(str(self.basket_price) + ' руб', self.catalog_network_Window)
		if (self.basket_count == 0):
			self.basket_count_label = QLabel('В корзине', self.catalog_network_Window)
			self.basket_price_label = QLabel('нет товаров', self.catalog_network_Window)
		elif (self.basket_count == 1):
			self.basket_count_label = QLabel(str(self.basket_count) + ' товар', self.catalog_network_Window)
		elif (self.basket_count < 5):
			self.basket_count_label = QLabel(str(self.basket_count) + ' товара', self.catalog_network_Window)
		elif (self.basket_count >= 5):
			self.basket_count_label = QLabel(str(self.basket_count) + ' товаров', self.catalog_network_Window)
		self.basket_price_label.resize(200, 12)
		self.basket_count_label.resize(120, 12)
		self.add_to_basket()


		# Левый sidebar-catalog_menu
		self.btn_catalog_portativ = QPushButton(self.catalog_network_Window)
		self.btn_catalog_computers = QPushButton(self.catalog_network_Window)
		self.btn_catalog_audioVideo = QPushButton(self.catalog_network_Window)
		self.btn_catalog_climateControl = QPushButton(self.catalog_network_Window)
		self.btn_catalog_forHome = QPushButton(self.catalog_network_Window)
		self.btn_catalog_beauty = QPushButton(self.catalog_network_Window)
		self.btn_catalog_cameras = QPushButton(self.catalog_network_Window)
		self.btn_catalog_games = QPushButton(self.catalog_network_Window)
		self.btn_catalog_remont = QPushButton(self.catalog_network_Window)
		self.btn_catalog_auto = QPushButton(self.catalog_network_Window)
		self.btn_catalog_ucenennyeTovary = QPushButton(self.catalog_network_Window)
		self.catalog_menu_btn.menu_btn(self)


		# Продукты (Сети, Оргтехника, ПО)
		# Продукт 1
		self.product_bg_img = QLabel(self.catalog_network_Window)
		self.product_bg_img.move(90, 115)
		self.product_img = QLabel(self.catalog_network_Window)
		self.product_pix = QtGui.QPixmap("img/network/mfu_epson_l3050.jpg")
		self.product_img.move(100, 125)
		self.product()
		self.product_1_img = 'img/network/basket_mfu_epson_l3050.jpg'
		self.product_1_name = QLabel('МФУ Epson L3050', self.catalog_network_Window)
		self.product_1_count = QLabel('1', self.catalog_network_Window)
		self.product_1_price = QLabel('Цена: 13850 руб', self.catalog_network_Window)
		self.product_1_price_int = self.product_1_price.text()[6:-4]
		self.product_1_price_sum = self.product_1_price.text()[6:-4]
		self.product_1_add_basket = QPushButton('В корзину', self.catalog_network_Window)
		self.product_1_add_basket.clicked.connect(self.basket_product_1)
		self.product_1_8_style.product_1_style(self)

		# Продукт 2
		self.product_bg_img = QLabel(self.catalog_network_Window)
		self.product_bg_img.move(330, 115)
		self.product_img = QLabel(self.catalog_network_Window)
		self.product_pix = QtGui.QPixmap("img/network/ip_camera_orient_yc-52b.jpg")
		self.product_img.move(340, 125)
		self.product()	
		self.product_2_img = 'img/network/basket_ip_camera_orient_yc-52b.jpg'
		self.product_2_name = QLabel('IP-камера Orient YC-52B', self.catalog_network_Window)
		self.product_2_count = QLabel('1', self.catalog_network_Window)
		self.product_2_price = QLabel('Цена: 2800 руб', self.catalog_network_Window)
		self.product_2_price_int = self.product_2_price.text()[6:-4]
		self.product_2_price_sum = self.product_2_price.text()[6:-4]
		self.product_2_add_basket = QPushButton('В корзину', self.catalog_network_Window)
		self.product_2_add_basket.clicked.connect(self.basket_product_2)
		self.product_1_8_style.product_2_style(self)

		# Продукт 3
		self.product_bg_img = QLabel(self.catalog_network_Window)
		self.product_bg_img.move(570, 115)
		self.product_img = QLabel(self.catalog_network_Window)
		self.product_pix = QtGui.QPixmap("img/network/wi-fi_router_asus_rt-ac53.jpg")
		self.product_img.move(580, 125)
		self.product()
		self.product_3_img = 'img/network/basket_wi-fi_router_asus_rt-ac53.jpg'
		self.product_3_name = QLabel('Wi-Fi роутер Asus RT-AC53', self.catalog_network_Window)
		self.product_3_count = QLabel('1', self.catalog_network_Window)
		self.product_3_price = QLabel('Цена: 2950 руб', self.catalog_network_Window)
		self.product_3_price_int = self.product_3_price.text()[6:-4]
		self.product_3_price_sum = self.product_3_price.text()[6:-4]
		self.product_3_add_basket = QPushButton('В корзину', self.catalog_network_Window)
		self.product_3_add_basket.clicked.connect(self.basket_product_3)
		self.product_1_8_style.product_3_style(self)

		# Продукт 4
		self.product_bg_img = QLabel(self.catalog_network_Window)
		self.product_bg_img.move(810, 115)
		self.product_img = QLabel(self.catalog_network_Window)
		self.product_pix = QtGui.QPixmap("img/network/kaspersky_internet_security_1x1.jpg")
		self.product_img.move(820, 125)
		self.product()
		self.product_4_img = 'img/network/basket_kaspersky_internet_security_1x1.jpg'
		self.product_4_name = QLabel('Kaspersky Internet Security 1x1', self.catalog_network_Window)
		self.product_4_count = QLabel('1', self.catalog_network_Window)
		self.product_4_price = QLabel('Цена: 550 руб', self.catalog_network_Window)
		self.product_4_price_int = self.product_4_price.text()[6:-4]
		self.product_4_price_sum = self.product_4_price.text()[6:-4]
		self.product_4_add_basket = QPushButton('В корзину', self.catalog_network_Window)
		self.product_4_add_basket.clicked.connect(self.basket_product_4)
		self.product_1_8_style.product_4_style(self)


		# Продукт 5
		self.product_bg_img = QLabel(self.catalog_network_Window)
		self.product_bg_img.move(90, 405)
		self.product_img = QLabel(self.catalog_network_Window)
		self.product_pix = QtGui.QPixmap("img/network/ibp_eaton_5s_1000i.jpg")
		self.product_img.move(100, 415)
		self.product()
		self.product_5_img = 'img/network/basket_ibp_eaton_5s_1000i.jpg'
		self.product_5_name = QLabel('ИБП EATON 5S 1000i', self.catalog_network_Window)
		self.product_5_count = QLabel('1', self.catalog_network_Window)
		self.product_5_price = QLabel('Цена: 12260 руб', self.catalog_network_Window)
		self.product_5_price_int = self.product_5_price.text()[6:-4]
		self.product_5_price_sum = self.product_5_price.text()[6:-4]
		self.product_5_add_basket = QPushButton('В корзину', self.catalog_network_Window)
		self.product_5_add_basket.clicked.connect(self.basket_product_5)
		self.product_1_8_style.product_5_style(self)

		# Продукт 6
		self.product_bg_img = QLabel(self.catalog_network_Window)
		self.product_bg_img.move(330, 405)
		self.product_img = QLabel(self.catalog_network_Window)
		self.product_pix = QtGui.QPixmap("img/network/disk_bd-re_verbatim_2x25gb.jpg")
		self.product_img.move(340, 415)
		self.product()
		self.product_6_img = 'img/network/basket_disk_bd-re_verbatim_2x25gb.jpg'
		self.product_6_name = QLabel('Диск BD-RE Verbatim 2x25GB', self.catalog_network_Window)
		self.product_6_count = QLabel('1', self.catalog_network_Window)
		self.product_6_price = QLabel('Цена: 110 руб', self.catalog_network_Window)
		self.product_6_price_int = self.product_6_price.text()[6:-4]
		self.product_6_price_sum = self.product_6_price.text()[6:-4]
		self.product_6_add_basket = QPushButton('В корзину', self.catalog_network_Window)
		self.product_6_add_basket.clicked.connect(self.basket_product_6)
		self.product_1_8_style.product_6_style(self)

		# Продукт 7
		self.product_bg_img = QLabel(self.catalog_network_Window)
		self.product_bg_img.move(570, 405)
		self.product_img = QLabel(self.catalog_network_Window)
		self.product_pix = QtGui.QPixmap("img/network/kartridzh_hi-black_hb_cf218a.jpg")
		self.product_img.move(580, 415)
		self.product()
		self.product_7_img = 'img/network/basket_kartridzh_hi-black_hb_cf218a.jpg'
		self.product_7_name = QLabel('Картридж Hi-Black HB-CF218A', self.catalog_network_Window)
		self.product_7_count = QLabel('1', self.catalog_network_Window)
		self.product_7_price = QLabel('Цена: 1550 руб', self.catalog_network_Window)
		self.product_7_price_int = self.product_7_price.text()[6:-4]
		self.product_7_price_sum = self.product_7_price.text()[6:-4]
		self.product_7_add_basket = QPushButton('В корзину', self.catalog_network_Window)
		self.product_7_add_basket.clicked.connect(self.basket_product_7)
		self.product_1_8_style.product_7_style(self)

		# Продукт 8
		self.product_bg_img = QLabel(self.catalog_network_Window)
		self.product_bg_img.move(810, 405)
		self.product_img = QLabel(self.catalog_network_Window)
		self.product_pix = QtGui.QPixmap("img/network/proector_acer_p5227.jpg")
		self.product_img.move(820, 415)
		self.product()
		self.product_8_img = 'img/network/basket_proector_acer_p5227.jpg'
		self.product_8_name = QLabel('Проектор Acer P5227', self.catalog_network_Window)
		self.product_8_count = QLabel('1', self.catalog_network_Window)
		self.product_8_price = QLabel('Цена: 54820 руб', self.catalog_network_Window)
		self.product_8_price_int = self.product_8_price.text()[6:-4]
		self.product_8_price_sum = self.product_8_price.text()[6:-4]
		self.product_8_add_basket = QPushButton('В корзину', self.catalog_network_Window)
		self.product_8_add_basket.clicked.connect(self.basket_product_8)
		self.product_1_8_style.product_8_style(self)

		self.setWindowTitle('App_Shop - Сети, оргтехника, ПО')

	def catalog_audioVideo(self): # Каталог - ТВ, аудио, видео
		self.catalog_audioVideo_Window = QWidget(self)
		self.setCentralWidget(self.catalog_audioVideo_Window)

		# Белый фон
		self.background_img = QLabel(self.catalog_audioVideo_Window)
		self.background_img_window()

		# Левый sidebar-catalog_menu_btn (active)
		self.btn_catalog_audioVideo_active = QPushButton(self.catalog_audioVideo_Window)
		self.catalog_menu_btn_active.catalog_menu_btn_audioVideo_active(self)

		# Лого мини
		self.logo_img = QLabel(self.catalog_audioVideo_Window)
		self.logo_mini()

		# Поиск
		self.search_Input_shop = QLineEdit('Быстрый поиск', self.catalog_audioVideo_Window)
		self.search_Btn_shop = QPushButton('', self.catalog_audioVideo_Window)
		self.search_products()

		# Название категории
		self.name_categoriy = QLabel('ТВ, аудио, видео, приставки', self.catalog_audioVideo_Window)
		self.name_categoriy_window()

		# Корзина
		self.basket_Btn = QPushButton('', self.catalog_audioVideo_Window)
		self.basket_Btn.clicked.connect(self.basket_big_window)
		if (self.basket_price > 0):
			self.basket_price_label = QLabel(str(self.basket_price) + ' руб', self.catalog_audioVideo_Window)
		if (self.basket_count == 0):
			self.basket_count_label = QLabel('В корзине', self.catalog_audioVideo_Window)
			self.basket_price_label = QLabel('нет товаров', self.catalog_audioVideo_Window)
		elif (self.basket_count == 1):
			self.basket_count_label = QLabel(str(self.basket_count) + ' товар', self.catalog_audioVideo_Window)
		elif (self.basket_count < 5):
			self.basket_count_label = QLabel(str(self.basket_count) + ' товара', self.catalog_audioVideo_Window)
		elif (self.basket_count >= 5):
			self.basket_count_label = QLabel(str(self.basket_count) + ' товаров', self.catalog_audioVideo_Window)
		self.basket_price_label.resize(200, 12)
		self.basket_count_label.resize(120, 12)
		self.add_to_basket()

		# Левый sidebar-catalog_menu
		self.btn_catalog_portativ = QPushButton(self.catalog_audioVideo_Window)
		self.btn_catalog_computers = QPushButton(self.catalog_audioVideo_Window)
		self.btn_catalog_network = QPushButton(self.catalog_audioVideo_Window)
		self.btn_catalog_climateControl = QPushButton(self.catalog_audioVideo_Window)
		self.btn_catalog_forHome = QPushButton(self.catalog_audioVideo_Window)
		self.btn_catalog_beauty = QPushButton(self.catalog_audioVideo_Window)
		self.btn_catalog_cameras = QPushButton(self.catalog_audioVideo_Window)
		self.btn_catalog_games = QPushButton(self.catalog_audioVideo_Window)
		self.btn_catalog_remont = QPushButton(self.catalog_audioVideo_Window)
		self.btn_catalog_auto = QPushButton(self.catalog_audioVideo_Window)
		self.btn_catalog_ucenennyeTovary = QPushButton(self.catalog_audioVideo_Window)
		self.catalog_menu_btn.menu_btn(self)


		# Продукты (ТВ, аудио, видео, приставки)
		# Продукт 1
		self.product_bg_img = QLabel(self.catalog_audioVideo_Window)
		self.product_bg_img.move(90, 115)
		self.product_img = QLabel(self.catalog_audioVideo_Window)
		self.product_pix = QtGui.QPixmap("img/audioVideo/tv_lg_49lk5910.jpg")
		self.product_img.move(100, 125)
		self.product()
		self.product_1_img = 'img/audioVideo/basket_tv_lg_49lk5910.jpg'
		self.product_1_name = QLabel('Телевизор LG 49LK5910', self.catalog_audioVideo_Window)
		self.product_1_count = QLabel('1', self.catalog_audioVideo_Window)
		self.product_1_price = QLabel('Цена: 34950 руб', self.catalog_audioVideo_Window)
		self.product_1_price_int = self.product_1_price.text()[6:-4]
		self.product_1_price_sum = self.product_1_price.text()[6:-4]
		self.product_1_add_basket = QPushButton('В корзину', self.catalog_audioVideo_Window)
		self.product_1_add_basket.clicked.connect(self.basket_product_1)
		self.product_1_8_style.product_1_style(self)

		# Продукт 2
		self.product_bg_img = QLabel(self.catalog_audioVideo_Window)
		self.product_bg_img.move(330, 115)
		self.product_img = QLabel(self.catalog_audioVideo_Window)
		self.product_pix = QtGui.QPixmap("img/audioVideo/domashniy_kinoteatr_samsung_ht-j4550k.jpg")
		self.product_img.move(340, 125)
		self.product()
		self.product_2_img = 'img/audioVideo/basket_domashniy_kinoteatr_samsung_ht-j4550k.jpg'
		self.product_2_name = QLabel('Samsung HT-J4550K', self.catalog_audioVideo_Window)
		self.product_2_count = QLabel('1', self.catalog_audioVideo_Window)
		self.product_2_price = QLabel('Цена: 16750 руб', self.catalog_audioVideo_Window)
		self.product_2_price_int = self.product_2_price.text()[6:-4]
		self.product_2_price_sum = self.product_2_price.text()[6:-4]
		self.product_2_add_basket = QPushButton('В корзину', self.catalog_audioVideo_Window)
		self.product_2_add_basket.clicked.connect(self.basket_product_2)
		self.product_1_8_style.product_2_style(self)

		# Продукт 3
		self.product_bg_img = QLabel(self.catalog_audioVideo_Window)
		self.product_bg_img.move(570, 115)
		self.product_img = QLabel(self.catalog_audioVideo_Window)
		self.product_pix = QtGui.QPixmap("img/audioVideo/dvd-player_lg_dp132.jpg")
		self.product_img.move(580, 125)
		self.product()
		self.product_3_img = 'img/audioVideo/basket_dvd-player_lg_dp132.jpg'
		self.product_3_name = QLabel('DVD-плеер LG DP132', self.catalog_audioVideo_Window)
		self.product_3_count = QLabel('1', self.catalog_audioVideo_Window)
		self.product_3_price = QLabel('Цена: 2590 руб', self.catalog_audioVideo_Window)
		self.product_3_price_int = self.product_3_price.text()[6:-4]
		self.product_3_price_sum = self.product_3_price.text()[6:-4]
		self.product_3_add_basket = QPushButton('В корзину', self.catalog_audioVideo_Window)
		self.product_3_add_basket.clicked.connect(self.basket_product_3)
		self.product_1_8_style.product_3_style(self)

		# Продукт 4
		self.product_bg_img = QLabel(self.catalog_audioVideo_Window)
		self.product_bg_img.move(810, 115)
		self.product_img = QLabel(self.catalog_audioVideo_Window)
		self.product_pix = QtGui.QPixmap("img/audioVideo/game_console_microsoft_xbox_one_1tb.jpg")
		self.product_img.move(820, 125)
		self.product()
		self.product_4_img = 'img/audioVideo/basket_game_console_microsoft_xbox_one_1tb.jpg'
		self.product_4_name = QLabel('Microsoft Xbox One 1TB', self.catalog_audioVideo_Window)
		self.product_4_count = QLabel('1', self.catalog_audioVideo_Window)
		self.product_4_price = QLabel('Цена: 21990 руб', self.catalog_audioVideo_Window)
		self.product_4_price_int = self.product_4_price.text()[6:-4]
		self.product_4_price_sum = self.product_4_price.text()[6:-4]
		self.product_4_add_basket = QPushButton('В корзину', self.catalog_audioVideo_Window)
		self.product_4_add_basket.clicked.connect(self.basket_product_4)
		self.product_1_8_style.product_4_style(self)

		# Продукт 5
		self.product_bg_img = QLabel(self.catalog_audioVideo_Window)
		self.product_bg_img.move(90, 405)
		self.product_img = QLabel(self.catalog_audioVideo_Window)
		self.product_pix = QtGui.QPixmap("img/audioVideo/podstavka_tv_jk_126.jpg")
		self.product_img.move(100, 415)
		self.product()
		self.product_5_img = 'img/audioVideo/basket_podstavka_tv_jk_126.jpg'
		self.product_5_name = QLabel('Подставка под TV "ЖК 126 Б"', self.catalog_audioVideo_Window)
		self.product_5_count = QLabel('1', self.catalog_audioVideo_Window)
		self.product_5_price = QLabel('Цена: 7200 руб', self.catalog_audioVideo_Window)
		self.product_5_price_int = self.product_5_price.text()[6:-4]
		self.product_5_price_sum = self.product_5_price.text()[6:-4]
		self.product_5_add_basket = QPushButton('В корзину', self.catalog_audioVideo_Window)
		self.product_5_add_basket.clicked.connect(self.basket_product_5)
		self.product_1_8_style.product_5_style(self)

		# Продукт 6
		self.product_bg_img = QLabel(self.catalog_audioVideo_Window)
		self.product_bg_img.move(330, 405)
		self.product_img = QLabel(self.catalog_audioVideo_Window)
		self.product_pix = QtGui.QPixmap("img/audioVideo/komplekt_tricolor_s_modulem.jpg")
		self.product_img.move(340, 415)
		self.product()
		self.product_6_img = 'img/audioVideo/basket_komplekt_tricolor_s_modulem.jpg'
		self.product_6_name = QLabel('Комплект Триколор с модулем', self.catalog_audioVideo_Window)
		self.product_6_count = QLabel('1', self.catalog_audioVideo_Window)
		self.product_6_price = QLabel('Цена: 5500 руб', self.catalog_audioVideo_Window)
		self.product_6_price_int = self.product_6_price.text()[6:-4]
		self.product_6_price_sum = self.product_6_price.text()[6:-4]
		self.product_6_add_basket = QPushButton('В корзину', self.catalog_audioVideo_Window)
		self.product_6_add_basket.clicked.connect(self.basket_product_6)
		self.product_1_8_style.product_6_style(self)

		# Продукт 7
		self.product_bg_img = QLabel(self.catalog_audioVideo_Window)
		self.product_bg_img.move(570, 405)
		self.product_img = QLabel(self.catalog_audioVideo_Window)
		self.product_pix = QtGui.QPixmap("img/audioVideo/skype-camera_philips_pta317.jpg")
		self.product_img.move(580, 415)
		self.product()
		self.product_7_img = 'img/audioVideo/basket_skype-camera_philips_pta317.jpg'
		self.product_7_name = QLabel('Скайп-камера Philips PTA317', self.catalog_audioVideo_Window)
		self.product_7_count = QLabel('1', self.catalog_audioVideo_Window)
		self.product_7_price = QLabel('Цена: 1900 руб', self.catalog_audioVideo_Window)
		self.product_7_price_int = self.product_7_price.text()[6:-4]
		self.product_7_price_sum = self.product_7_price.text()[6:-4]
		self.product_7_add_basket = QPushButton('В корзину', self.catalog_audioVideo_Window)
		self.product_7_add_basket.clicked.connect(self.basket_product_7)
		self.product_1_8_style.product_7_style(self)

		# Продукт 8
		self.product_bg_img = QLabel(self.catalog_audioVideo_Window)
		self.product_bg_img.move(810, 405)
		self.product_img = QLabel(self.catalog_audioVideo_Window)
		self.product_pix = QtGui.QPixmap("img/audioVideo/3d_ochki_toshiba_fpt-ag02g.jpg")
		self.product_img.move(820, 415)
		self.product()
		self.product_8_img = 'img/audioVideo/basket_3d_ochki_toshiba_fpt-ag02g.jpg'
		self.product_8_name = QLabel('3D очки Toshiba FPT-AG02G', self.catalog_audioVideo_Window)
		self.product_8_count = QLabel('1', self.catalog_audioVideo_Window)
		self.product_8_price = QLabel('Цена: 990 руб', self.catalog_audioVideo_Window)
		self.product_8_price_int = self.product_8_price.text()[6:-4]
		self.product_8_price_sum = self.product_8_price.text()[6:-4]
		self.product_8_add_basket = QPushButton('В корзину', self.catalog_audioVideo_Window)
		self.product_8_add_basket.clicked.connect(self.basket_product_8)
		self.product_1_8_style.product_8_style(self)

		self.setWindowTitle('App_Shop - ТВ, аудио, видео, приставки')

	def catalog_climateControl(self): # Каталог - Климатическая техника
		self.catalog_climateControl_Window = QWidget(self)
		self.setCentralWidget(self.catalog_climateControl_Window)

		# Белый фон
		self.background_img = QLabel(self.catalog_climateControl_Window)
		self.background_img_window()

		# Левый sidebar-catalog_menu_btn (active)
		self.btn_catalog_climateControl_active = QPushButton(self.catalog_climateControl_Window)
		self.catalog_menu_btn_active.catalog_menu_btn_climateControl_active(self)

		# Лого мини
		self.logo_img = QLabel(self.catalog_climateControl_Window)
		self.logo_mini()

		# Поиск
		self.search_Input_shop = QLineEdit('Быстрый поиск', self.catalog_climateControl_Window)
		self.search_Btn_shop = QPushButton('', self.catalog_climateControl_Window)
		self.search_products()

		# Название категории
		self.name_categoriy = QLabel('Климатическая техника', self.catalog_climateControl_Window)
		self.name_categoriy_window()

		# Корзина
		self.basket_Btn = QPushButton('', self.catalog_climateControl_Window)
		self.basket_Btn.clicked.connect(self.basket_big_window)
		if (self.basket_price > 0):
			self.basket_price_label = QLabel(str(self.basket_price) + ' руб', self.catalog_climateControl_Window)
		if (self.basket_count == 0):
			self.basket_count_label = QLabel('В корзине', self.catalog_climateControl_Window)
			self.basket_price_label = QLabel('нет товаров', self.catalog_climateControl_Window)
		elif (self.basket_count == 1):
			self.basket_count_label = QLabel(str(self.basket_count) + ' товар', self.catalog_climateControl_Window)
		elif (self.basket_count < 5):
			self.basket_count_label = QLabel(str(self.basket_count) + ' товара', self.catalog_climateControl_Window)
		elif (self.basket_count >= 5):
			self.basket_count_label = QLabel(str(self.basket_count) + ' товаров', self.catalog_climateControl_Window)
		self.basket_price_label.resize(200, 12)
		self.basket_count_label.resize(120, 12)
		self.add_to_basket()

		# Левый sidebar-catalog_menu
		self.btn_catalog_portativ = QPushButton(self.catalog_climateControl_Window)
		self.btn_catalog_computers = QPushButton(self.catalog_climateControl_Window)
		self.btn_catalog_network = QPushButton(self.catalog_climateControl_Window)
		self.btn_catalog_audioVideo = QPushButton(self.catalog_climateControl_Window)
		self.btn_catalog_forHome = QPushButton(self.catalog_climateControl_Window)
		self.btn_catalog_beauty = QPushButton(self.catalog_climateControl_Window)
		self.btn_catalog_cameras = QPushButton(self.catalog_climateControl_Window)
		self.btn_catalog_games = QPushButton(self.catalog_climateControl_Window)
		self.btn_catalog_remont = QPushButton(self.catalog_climateControl_Window)
		self.btn_catalog_auto = QPushButton(self.catalog_climateControl_Window)
		self.btn_catalog_ucenennyeTovary = QPushButton(self.catalog_climateControl_Window)
		self.catalog_menu_btn.menu_btn(self)

		# Продукты (Климатическая техника)
		# Продукт 1
		self.product_bg_img = QLabel(self.catalog_climateControl_Window)
		self.product_bg_img.move(90, 115)
		self.product_img = QLabel(self.catalog_climateControl_Window)
		self.product_pix = QtGui.QPixmap("img/climateControl/konditioner_dantex_rk-18ent2.jpg")
		self.product_img.move(100, 125)
		self.product()
		self.product_1_img = 'img/climateControl/konditioner_dantex_rk-18ent2.jpg'
		self.product_1_name = QLabel('Кондиционер Dantex RK-18ENT2', self.catalog_climateControl_Window)
		self.product_1_count = QLabel('1', self.catalog_climateControl_Window)
		self.product_1_price = QLabel('Цена: 23990 руб', self.catalog_climateControl_Window)
		self.product_1_price_int = self.product_1_price.text()[6:-4]
		self.product_1_price_sum = self.product_1_price.text()[6:-4]
		self.product_1_add_basket = QPushButton('В корзину', self.catalog_climateControl_Window)
		self.product_1_add_basket.clicked.connect(self.basket_product_1)
		self.product_1_8_style.product_1_style(self)

		# Продукт 2
		self.product_bg_img = QLabel(self.catalog_climateControl_Window)
		self.product_bg_img.move(330, 115)
		self.product_img = QLabel(self.catalog_climateControl_Window)
		self.product_pix = QtGui.QPixmap("img/climateControl/ventilyator_vitek_vt-1936.jpg")
		self.product_img.move(340, 125)
		self.product()
		self.product_2_img = 'img/climateControl/ventilyator_vitek_vt-1936.jpg'
		self.product_2_name = QLabel('Вентилятор Vitek VT-1936', self.catalog_climateControl_Window)
		self.product_2_count = QLabel('1', self.catalog_climateControl_Window)
		self.product_2_price = QLabel('Цена: 5600 руб', self.catalog_climateControl_Window)
		self.product_2_price_int = self.product_2_price.text()[6:-4]
		self.product_2_price_sum = self.product_2_price.text()[6:-4]
		self.product_2_add_basket = QPushButton('В корзину', self.catalog_climateControl_Window)
		self.product_2_add_basket.clicked.connect(self.basket_product_2)
		self.product_1_8_style.product_2_style(self)

		# Продукт 3
		self.product_bg_img = QLabel(self.catalog_climateControl_Window)
		self.product_bg_img.move(570, 115)
		self.product_img = QLabel(self.catalog_climateControl_Window)
		self.product_pix = QtGui.QPixmap("img/climateControl/radiator_zanussi_zoh_lt-11.jpg")
		self.product_img.move(580, 125)
		self.product()
		self.product_3_img = 'img/climateControl/radiator_zanussi_zoh_lt-11.jpg'
		self.product_3_name = QLabel('Радиатор Zanussi ZOH/LT-11', self.catalog_climateControl_Window)
		self.product_3_count = QLabel('1', self.catalog_climateControl_Window)
		self.product_3_price = QLabel('Цена: 3950 руб', self.catalog_climateControl_Window)
		self.product_3_price_int = self.product_3_price.text()[6:-4]
		self.product_3_price_sum = self.product_3_price.text()[6:-4]
		self.product_3_add_basket = QPushButton('В корзину', self.catalog_climateControl_Window)
		self.product_3_add_basket.clicked.connect(self.basket_product_3)
		self.product_1_8_style.product_3_style(self)

		# Продукт 4
		self.product_bg_img = QLabel(self.catalog_climateControl_Window)
		self.product_bg_img.move(810, 115)
		self.product_img = QLabel(self.catalog_climateControl_Window)
		self.product_pix = QtGui.QPixmap("img/climateControl/vozduhoochistitel_dyson_pure.jpg")
		self.product_img.move(820, 125)
		self.product()
		self.product_4_img = 'img/climateControl/vozduhoochistitel_dyson_pure.jpg'
		self.product_4_name = QLabel('Воздухоочиститель Dyson Pure', self.catalog_climateControl_Window)
		self.product_4_count = QLabel('1', self.catalog_climateControl_Window)
		self.product_4_price = QLabel('Цена: 34990 руб', self.catalog_climateControl_Window)
		self.product_4_price_int = self.product_4_price.text()[6:-4]
		self.product_4_price_sum = self.product_4_price.text()[6:-4]
		self.product_4_add_basket = QPushButton('В корзину', self.catalog_climateControl_Window)
		self.product_4_add_basket.clicked.connect(self.basket_product_4)
		self.product_1_8_style.product_4_style(self)

		# Продукт 5
		self.product_bg_img = QLabel(self.catalog_climateControl_Window)
		self.product_bg_img.move(90, 405)
		self.product_img = QLabel(self.catalog_climateControl_Window)
		self.product_pix = QtGui.QPixmap("img/climateControl/uvlazhnitel_vozduha_boneco_s250.jpg")
		self.product_img.move(100, 415)
		self.product()
		self.product_5_img = 'img/climateControl/uvlazhnitel_vozduha_boneco_s250.jpg'
		self.product_5_name = QLabel('Увлажнит. воздуха Boneco S250', self.catalog_climateControl_Window)
		self.product_5_count = QLabel('1', self.catalog_climateControl_Window)
		self.product_5_price = QLabel('Цена: 9550 руб', self.catalog_climateControl_Window)
		self.product_5_price_int = self.product_5_price.text()[6:-4]
		self.product_5_price_sum = self.product_5_price.text()[6:-4]
		self.product_5_add_basket = QPushButton('В корзину', self.catalog_climateControl_Window)
		self.product_5_add_basket.clicked.connect(self.basket_product_5)
		self.product_1_8_style.product_5_style(self)

		# Продукт 6
		self.product_bg_img = QLabel(self.catalog_climateControl_Window)
		self.product_bg_img.move(330, 405)
		self.product_img = QLabel(self.catalog_climateControl_Window)
		self.product_pix = QtGui.QPixmap("img/climateControl/konvector_ballu_bep_ext-1000.jpg")
		self.product_img.move(340, 415)
		self.product()
		self.product_6_img = 'img/climateControl/konvector_ballu_bep_ext-1000.jpg'
		self.product_6_name = QLabel('Конвектор Ballu BEP/EXT-1000', self.catalog_climateControl_Window)
		self.product_6_count = QLabel('1', self.catalog_climateControl_Window)
		self.product_6_price = QLabel('Цена: 5900 руб', self.catalog_climateControl_Window)
		self.product_6_price_int = self.product_6_price.text()[6:-4]
		self.product_6_price_sum = self.product_6_price.text()[6:-4]
		self.product_6_add_basket = QPushButton('В корзину', self.catalog_climateControl_Window)
		self.product_6_add_basket.clicked.connect(self.basket_product_6)
		self.product_1_8_style.product_6_style(self)

		# Продукт 7
		self.product_bg_img = QLabel(self.catalog_climateControl_Window)
		self.product_bg_img.move(570, 405)
		self.product_img = QLabel(self.catalog_climateControl_Window)
		self.product_pix = QtGui.QPixmap("img/climateControl/konditioner_ballu_bse-24hn1.jpg")
		self.product_img.move(580, 415)
		self.product()
		self.product_7_img = 'img/climateControl/konditioner_ballu_bse-24hn1.jpg'
		self.product_7_name = QLabel('Кондиционер Ballu BSE-24HN1', self.catalog_climateControl_Window)
		self.product_7_count = QLabel('1', self.catalog_climateControl_Window)
		self.product_7_price = QLabel('Цена: 36450 руб', self.catalog_climateControl_Window)
		self.product_7_price_int = self.product_7_price.text()[6:-4]
		self.product_7_price_sum = self.product_7_price.text()[6:-4]
		self.product_7_add_basket = QPushButton('В корзину', self.catalog_climateControl_Window)
		self.product_7_add_basket.clicked.connect(self.basket_product_7)
		self.product_1_8_style.product_7_style(self)

		# Продукт 8
		self.product_bg_img = QLabel(self.catalog_climateControl_Window)
		self.product_bg_img.move(810, 405)
		self.product_img = QLabel(self.catalog_climateControl_Window)
		self.product_pix = QtGui.QPixmap("img/climateControl/ventilyator_vitek_vt-1922_ch.jpg")
		self.product_img.move(820, 415)
		self.product()
		self.product_8_img = 'img/climateControl/ventilyator_vitek_vt-1922_ch.jpg'
		self.product_8_name = QLabel('Вентилятор Vitek VT-1922 CH', self.catalog_climateControl_Window)
		self.product_8_count = QLabel('1', self.catalog_climateControl_Window)
		self.product_8_price = QLabel('Цена: 4850 руб', self.catalog_climateControl_Window)
		self.product_8_price_int = self.product_8_price.text()[6:-4]
		self.product_8_price_sum = self.product_8_price.text()[6:-4]
		self.product_8_add_basket = QPushButton('В корзину', self.catalog_climateControl_Window)
		self.product_8_add_basket.clicked.connect(self.basket_product_8)
		self.product_1_8_style.product_8_style(self)

		self.setWindowTitle('App_Shop - Климатическая техника')

	def catalog_forHome(self): # Каталог - Бытовая техника
		self.catalog_forHome_Window = QWidget(self)
		self.setCentralWidget(self.catalog_forHome_Window)

		# Белый фон
		self.background_img = QLabel(self.catalog_forHome_Window)
		self.background_img_window()

		# Левый sidebar-catalog_menu_btn (active)
		self.btn_catalog_forHome_active = QPushButton(self.catalog_forHome_Window)
		self.catalog_menu_btn_active.catalog_menu_btn_forHome_active(self)

		# Лого мини
		self.logo_img = QLabel(self.catalog_forHome_Window)
		self.logo_mini()

		# Поиск
		self.search_Input_shop = QLineEdit('Быстрый поиск', self.catalog_forHome_Window)
		self.search_Btn_shop = QPushButton('', self.catalog_forHome_Window)
		self.search_products()

		# Название категории
		self.name_categoriy = QLabel('Бытовая техника', self.catalog_forHome_Window)
		self.name_categoriy_window()

		# Корзина
		self.basket_Btn = QPushButton('', self.catalog_forHome_Window)
		self.basket_Btn.clicked.connect(self.basket_big_window)
		if (self.basket_price > 0):
			self.basket_price_label = QLabel(str(self.basket_price) + ' руб', self.catalog_forHome_Window)
		if (self.basket_count == 0):
			self.basket_count_label = QLabel('В корзине', self.catalog_forHome_Window)
			self.basket_price_label = QLabel('нет товаров', self.catalog_forHome_Window)
		elif (self.basket_count == 1):
			self.basket_count_label = QLabel(str(self.basket_count) + ' товар', self.catalog_forHome_Window)
		elif (self.basket_count < 5):
			self.basket_count_label = QLabel(str(self.basket_count) + ' товара', self.catalog_forHome_Window)
		elif (self.basket_count >= 5):
			self.basket_count_label = QLabel(str(self.basket_count) + ' товаров', self.catalog_forHome_Window)
		self.basket_count_label.resize(200, 12)
		self.basket_count_label.resize(120, 12)
		self.add_to_basket()

		# Левый sidebar-catalog_menu
		self.btn_catalog_portativ = QPushButton(self.catalog_forHome_Window)
		self.btn_catalog_computers = QPushButton(self.catalog_forHome_Window)
		self.btn_catalog_network = QPushButton(self.catalog_forHome_Window)
		self.btn_catalog_audioVideo = QPushButton(self.catalog_forHome_Window)
		self.btn_catalog_climateControl = QPushButton(self.catalog_forHome_Window)
		self.btn_catalog_beauty = QPushButton(self.catalog_forHome_Window)
		self.btn_catalog_cameras = QPushButton(self.catalog_forHome_Window)
		self.btn_catalog_games = QPushButton(self.catalog_forHome_Window)
		self.btn_catalog_remont = QPushButton(self.catalog_forHome_Window)
		self.btn_catalog_auto = QPushButton(self.catalog_forHome_Window)
		self.btn_catalog_ucenennyeTovary = QPushButton(self.catalog_forHome_Window)
		self.catalog_menu_btn.menu_btn(self)

		# Продукты (Бытовая техника)
		# Продукт 1
		self.product_bg_img = QLabel(self.catalog_forHome_Window)
		self.product_bg_img.move(90, 115)
		self.product_img = QLabel(self.catalog_forHome_Window)
		self.product_pix = QtGui.QPixmap("img/forHome/stiralnayz_mashina_bosch_wan_20160.jpg")
		self.product_img.move(100, 125)
		self.product()
		self.product_1_img = 'img/forHome/stiralnayz_mashina_bosch_wan_20160.jpg'
		self.product_1_name = QLabel('Стир. машина Bosch WAN 20160', self.catalog_forHome_Window)
		self.product_1_count = QLabel('1', self.catalog_forHome_Window)
		self.product_1_price = QLabel('Цена: 29750 руб', self.catalog_forHome_Window)
		self.product_1_price_int = self.product_1_price.text()[6:-4]
		self.product_1_price_sum = self.product_1_price.text()[6:-4]
		self.product_1_add_basket = QPushButton('В корзину', self.catalog_forHome_Window)
		self.product_1_add_basket.clicked.connect(self.basket_product_1)
		self.product_1_8_style.product_1_style(self)

		# Продукт 2
		self.product_bg_img = QLabel(self.catalog_forHome_Window)
		self.product_bg_img.move(330, 115)
		self.product_img = QLabel(self.catalog_forHome_Window)
		self.product_pix = QtGui.QPixmap("img/forHome/holodilnik_sharp_sj-xe59pmsl.jpg")
		self.product_img.move(340, 125)
		self.product()
		self.product_2_img = 'img/forHome/holodilnik_sharp_sj-xe59pmsl.jpg'
		self.product_2_name = QLabel('Холодильник Sharp SJ-XE59PMSL', self.catalog_forHome_Window)
		self.product_2_count = QLabel('1', self.catalog_forHome_Window)
		self.product_2_price = QLabel('Цена: 72450 руб', self.catalog_forHome_Window)
		self.product_2_price_int = self.product_2_price.text()[6:-4]
		self.product_2_price_sum = self.product_2_price.text()[6:-4]
		self.product_2_add_basket = QPushButton('В корзину', self.catalog_forHome_Window)
		self.product_2_add_basket.clicked.connect(self.basket_product_2)
		self.product_1_8_style.product_2_style(self)

		# Продукт 3
		self.product_bg_img = QLabel(self.catalog_forHome_Window)
		self.product_bg_img.move(570, 115)
		self.product_img = QLabel(self.catalog_forHome_Window)
		self.product_pix = QtGui.QPixmap("img/forHome/pilesos_philips_fc_8767.jpg")
		self.product_img.move(580, 125)
		self.product()
		self.product_3_img = 'img/forHome/pilesos_philips_fc_8767.jpg'
		self.product_3_name = QLabel('Пылесос Philips FC 8767', self.catalog_forHome_Window)
		self.product_3_count = QLabel('1', self.catalog_forHome_Window)
		self.product_3_price = QLabel('Цена: 11890 руб', self.catalog_forHome_Window)
		self.product_3_price_int = self.product_3_price.text()[6:-4]
		self.product_3_price_sum = self.product_3_price.text()[6:-4]
		self.product_3_add_basket = QPushButton('В корзину', self.catalog_forHome_Window)
		self.product_3_add_basket.clicked.connect(self.basket_product_3)
		self.product_1_8_style.product_3_style(self)

		# Продукт 4
		self.product_bg_img = QLabel(self.catalog_forHome_Window)
		self.product_bg_img.move(810, 115)
		self.product_img = QLabel(self.catalog_forHome_Window)
		self.product_pix = QtGui.QPixmap("img/forHome/kofevarka_philips_hd_8825.jpg")
		self.product_img.move(820, 125)
		self.product()
		self.product_4_img = 'img/forHome/kofevarka_philips_hd_8825.jpg'
		self.product_4_name = QLabel('Кофеварка Philips HD 8825', self.catalog_forHome_Window)
		self.product_4_count = QLabel('1', self.catalog_forHome_Window)
		self.product_4_price = QLabel('Цена: 21990 руб', self.catalog_forHome_Window)
		self.product_4_price_int = self.product_4_price.text()[6:-4]
		self.product_4_price_sum = self.product_4_price.text()[6:-4]
		self.product_4_add_basket = QPushButton('В корзину', self.catalog_forHome_Window)
		self.product_4_add_basket.clicked.connect(self.basket_product_4)
		self.product_1_8_style.product_4_style(self)

		# Продукт 5
		self.product_bg_img = QLabel(self.catalog_forHome_Window)
		self.product_bg_img.move(90, 405)
		self.product_img = QLabel(self.catalog_forHome_Window)
		self.product_pix = QtGui.QPixmap("img/forHome/mikrovolnovaya_pech_samsung_me83xr.jpg")
		self.product_img.move(100, 415)
		self.product()
		self.product_5_img = 'img/forHome/mikrovolnovaya_pech_samsung_me83xr.jpg'
		self.product_5_name = QLabel('Микров. печь Samsung ME83XR', self.catalog_forHome_Window)
		self.product_5_count = QLabel('1', self.catalog_forHome_Window)
		self.product_5_price = QLabel('Цена: 7750 руб', self.catalog_forHome_Window)
		self.product_5_price_int = self.product_5_price.text()[6:-4]
		self.product_5_price_sum = self.product_5_price.text()[6:-4]
		self.product_5_add_basket = QPushButton('В корзину', self.catalog_forHome_Window)
		self.product_5_add_basket.clicked.connect(self.basket_product_5)
		self.product_1_8_style.product_5_style(self)

		# Продукт 6
		self.product_bg_img = QLabel(self.catalog_forHome_Window)
		self.product_bg_img.move(330, 405)
		self.product_img = QLabel(self.catalog_forHome_Window)
		self.product_pix = QtGui.QPixmap("img/forHome/kombain_Bosch_MCM_64085.jpg")
		self.product_img.move(340, 415)
		self.product()
		self.product_6_img = 'img/forHome/kombain_Bosch_MCM_64085.jpg'
		self.product_6_name = QLabel('Комбайн Bosch MCM 64085', self.catalog_forHome_Window)
		self.product_6_count = QLabel('1', self.catalog_forHome_Window)
		self.product_6_price = QLabel('Цена: 10650 руб', self.catalog_forHome_Window)
		self.product_6_price_int = self.product_6_price.text()[6:-4]
		self.product_6_price_sum = self.product_6_price.text()[6:-4]
		self.product_6_add_basket = QPushButton('В корзину', self.catalog_forHome_Window)
		self.product_6_add_basket.clicked.connect(self.basket_product_6)
		self.product_1_8_style.product_6_style(self)

		# Продукт 7
		self.product_bg_img = QLabel(self.catalog_forHome_Window)
		self.product_bg_img.move(570, 405)
		self.product_img = QLabel(self.catalog_forHome_Window)
		self.product_pix = QtGui.QPixmap("img/climateControl/konditioner_ballu_bse-24hn1.jpg")
		self.product_img.move(580, 415)
		self.product()
		self.product_7_img = 'img/climateControl/konditioner_ballu_bse-24hn1.jpg'
		self.product_7_name = QLabel('Кондиционер Ballu BSE-24HN1', self.catalog_forHome_Window)
		self.product_7_count = QLabel('1', self.catalog_forHome_Window)
		self.product_7_price = QLabel('Цена: 36450 руб', self.catalog_forHome_Window)
		self.product_7_price_int = self.product_7_price.text()[6:-4]
		self.product_7_price_sum = self.product_7_price.text()[6:-4]
		self.product_7_add_basket = QPushButton('В корзину', self.catalog_forHome_Window)
		self.product_7_add_basket.clicked.connect(self.basket_product_7)
		self.product_1_8_style.product_7_style(self)

		# Продукт 8
		self.product_bg_img = QLabel(self.catalog_forHome_Window)
		self.product_bg_img.move(810, 405)
		self.product_img = QLabel(self.catalog_forHome_Window)
		self.product_pix = QtGui.QPixmap("img/climateControl/ventilyator_vitek_vt-1922_ch.jpg")
		self.product_img.move(820, 415)
		self.product()
		self.product_8_img = 'img/climateControl/ventilyator_vitek_vt-1922_ch.jpg'
		self.product_8_name = QLabel('Вентилятор Vitek VT-1922 CH', self.catalog_forHome_Window)
		self.product_8_count = QLabel('1', self.catalog_forHome_Window)
		self.product_8_price = QLabel('Цена: 4850 руб', self.catalog_forHome_Window)
		self.product_8_price_int = self.product_8_price.text()[6:-4]
		self.product_8_price_sum = self.product_8_price.text()[6:-4]
		self.product_8_add_basket = QPushButton('В корзину', self.catalog_forHome_Window)
		self.product_8_add_basket.clicked.connect(self.basket_product_8)
		self.product_1_8_style.product_8_style(self)

		self.setWindowTitle('App_Shop - Бытовая техника')

	def catalog_beauty(self): # Каталог - Красота и здоровье
		self.catalog_beauty_Window = QWidget(self)
		self.setCentralWidget(self.catalog_beauty_Window)

		# Белый фон
		self.background_img = QLabel(self.catalog_beauty_Window)
		self.background_img_window()

		# Левый sidebar-catalog_menu_btn (active)
		self.btn_catalog_beauty_active = QPushButton(self.catalog_beauty_Window)
		self.catalog_menu_btn_active.catalog_menu_btn_beauty_active(self)

		# Лого мини
		self.logo_img = QLabel(self.catalog_beauty_Window)
		self.logo_mini()

		# Поиск
		self.search_Input_shop = QLineEdit('Быстрый поиск', self.catalog_beauty_Window)
		self.search_Btn_shop = QPushButton('', self.catalog_beauty_Window)
		self.search_products()

		# Название категории
		self.name_categoriy = QLabel('Красота и здоровье', self.catalog_beauty_Window)
		self.name_categoriy_window()

		# Корзина
		self.basket_Btn = QPushButton('', self.catalog_beauty_Window)
		self.basket_Btn.clicked.connect(self.basket_big_window)
		if (self.basket_price > 0):
			self.basket_price_label = QLabel(str(self.basket_price) + ' руб', self.catalog_beauty_Window)
		if (self.basket_count == 0):
			self.basket_count_label = QLabel('В корзине', self.catalog_beauty_Window)
			self.basket_price_label = QLabel('нет товаров', self.catalog_beauty_Window)
		elif (self.basket_count == 1):
			self.basket_count_label = QLabel(str(self.basket_count) + ' товар', self.catalog_beauty_Window)
		elif (self.basket_count < 5):
			self.basket_count_label = QLabel(str(self.basket_count) + ' товара', self.catalog_beauty_Window)
		elif (self.basket_count >= 5):
			self.basket_count_label = QLabel(str(self.basket_count) + ' товаров', self.catalog_beauty_Window)
		self.basket_count_label.resize(200, 12)
		self.basket_count_label.resize(120, 12)
		self.add_to_basket()

		# Левый sidebar-catalog_menu
		self.btn_catalog_portativ = QPushButton(self.catalog_beauty_Window)
		self.btn_catalog_computers = QPushButton(self.catalog_beauty_Window)
		self.btn_catalog_network = QPushButton(self.catalog_beauty_Window)
		self.btn_catalog_audioVideo = QPushButton(self.catalog_beauty_Window)
		self.btn_catalog_climateControl = QPushButton(self.catalog_beauty_Window)
		self.btn_catalog_forHome = QPushButton(self.catalog_beauty_Window)
		self.btn_catalog_cameras = QPushButton(self.catalog_beauty_Window)
		self.btn_catalog_games = QPushButton(self.catalog_beauty_Window)
		self.btn_catalog_remont = QPushButton(self.catalog_beauty_Window)
		self.btn_catalog_auto = QPushButton(self.catalog_beauty_Window)
		self.btn_catalog_ucenennyeTovary = QPushButton(self.catalog_beauty_Window)
		self.catalog_menu_btn.menu_btn(self)

		self.setWindowTitle('App_Shop - Красота и здоровье')


	def catalog_cameras(self): # Каталог - Фото и ведиеокамеры
		self.catalog_cameras_Window = QWidget(self)
		self.setCentralWidget(self.catalog_cameras_Window)

		# Белый фон
		self.background_img = QLabel(self.catalog_cameras_Window)
		self.background_img_window()

		# Левый sidebar-catalog_menu_btn (active)
		self.btn_catalog_cameras_active = QPushButton(self.catalog_cameras_Window)
		self.catalog_menu_btn_active.catalog_menu_btn_cameras_active(self)

		# Лого мини
		self.logo_img = QLabel(self.catalog_cameras_Window)
		self.logo_mini()

		# Поиск
		self.search_Input_shop = QLineEdit('Быстрый поиск', self.catalog_cameras_Window)
		self.search_Btn_shop = QPushButton('', self.catalog_cameras_Window)
		self.search_products()

		# Название категории
		self.name_categoriy = QLabel('Фото и видеокамеры', self.catalog_cameras_Window)
		self.name_categoriy_window()

		# Корзина
		self.basket_Btn = QPushButton('', self.catalog_cameras_Window)
		self.basket_Btn.clicked.connect(self.basket_big_window)
		if (self.basket_price > 0):
			self.basket_price_label = QLabel(str(self.basket_price) + ' руб', self.catalog_cameras_Window)
		if (self.basket_count == 0):
			self.basket_count_label = QLabel('В корзине', self.catalog_cameras_Window)
			self.basket_price_label = QLabel('нет товаров', self.catalog_cameras_Window)
		elif (self.basket_count == 1):
			self.basket_count_label = QLabel(str(self.basket_count) + ' товар', self.catalog_cameras_Window)
		elif (self.basket_count < 5):
			self.basket_count_label = QLabel(str(self.basket_count) + ' товара', self.catalog_cameras_Window)
		elif (self.basket_count >= 5):
			self.basket_count_label = QLabel(str(self.basket_count) + ' товаров', self.catalog_cameras_Window)
		self.basket_count_label.resize(200, 12)
		self.basket_count_label.resize(120, 12)
		self.add_to_basket()

		# Левый sidebar-catalog_menu
		self.btn_catalog_portativ = QPushButton(self.catalog_cameras_Window)
		self.btn_catalog_computers = QPushButton(self.catalog_cameras_Window)
		self.btn_catalog_network = QPushButton(self.catalog_cameras_Window)
		self.btn_catalog_audioVideo = QPushButton(self.catalog_cameras_Window)
		self.btn_catalog_climateControl = QPushButton(self.catalog_cameras_Window)
		self.btn_catalog_forHome = QPushButton(self.catalog_cameras_Window)
		self.btn_catalog_beauty = QPushButton(self.catalog_cameras_Window)
		self.btn_catalog_games = QPushButton(self.catalog_cameras_Window)
		self.btn_catalog_remont = QPushButton(self.catalog_cameras_Window)
		self.btn_catalog_auto = QPushButton(self.catalog_cameras_Window)
		self.btn_catalog_ucenennyeTovary = QPushButton(self.catalog_cameras_Window)
		self.catalog_menu_btn.menu_btn(self)

		self.setWindowTitle('App_Shop - Фото и видеокамеры')


	def catalog_games(self): # Каталог - Игры и развлечения
		self.catalog_games_Window = QWidget(self)
		self.setCentralWidget(self.catalog_games_Window)

		# Белый фон
		self.background_img = QLabel(self.catalog_games_Window)
		self.background_img_window()

		# Левый sidebar-catalog_menu_btn (active)
		self.btn_catalog_games_active = QPushButton(self.catalog_games_Window)
		self.catalog_menu_btn_active.catalog_menu_btn_games_active(self)

		# Лого мини
		self.logo_img = QLabel(self.catalog_games_Window)
		self.logo_mini()

		# Поиск
		self.search_Input_shop = QLineEdit('Быстрый поиск', self.catalog_games_Window)
		self.search_Btn_shop = QPushButton('', self.catalog_games_Window)
		self.search_products()

		# Название категории
		self.name_categoriy = QLabel('Игрушки и развлечения', self.catalog_games_Window)
		self.name_categoriy_window()

		# Корзина
		self.basket_Btn = QPushButton('', self.catalog_games_Window)
		self.basket_Btn.clicked.connect(self.basket_big_window)
		if (self.basket_price > 0):
			self.basket_price_label = QLabel(str(self.basket_price) + ' руб', self.catalog_games_Window)
		if (self.basket_count == 0):
			self.basket_count_label = QLabel('В корзине', self.catalog_games_Window)
			self.basket_price_label = QLabel('нет товаров', self.catalog_games_Window)
		elif (self.basket_count == 1):
			self.basket_count_label = QLabel(str(self.basket_count) + ' товар', self.catalog_games_Window)
		elif (self.basket_count < 5):
			self.basket_count_label = QLabel(str(self.basket_count) + ' товара', self.catalog_games_Window)
		elif (self.basket_count >= 5):
			self.basket_count_label = QLabel(str(self.basket_count) + ' товаров', self.catalog_games_Window)
		self.basket_count_label.resize(200, 12)
		self.basket_count_label.resize(120, 12)
		self.add_to_basket()

		# Левый sidebar-catalog_menu
		self.btn_catalog_portativ = QPushButton(self.catalog_games_Window)
		self.btn_catalog_computers = QPushButton(self.catalog_games_Window)
		self.btn_catalog_network = QPushButton(self.catalog_games_Window)
		self.btn_catalog_audioVideo = QPushButton(self.catalog_games_Window)
		self.btn_catalog_climateControl = QPushButton(self.catalog_games_Window)
		self.btn_catalog_forHome = QPushButton(self.catalog_games_Window)
		self.btn_catalog_beauty = QPushButton(self.catalog_games_Window)
		self.btn_catalog_cameras = QPushButton(self.catalog_games_Window)
		self.btn_catalog_remont = QPushButton(self.catalog_games_Window)
		self.btn_catalog_auto = QPushButton(self.catalog_games_Window)
		self.btn_catalog_ucenennyeTovary = QPushButton(self.catalog_games_Window)
		self.catalog_menu_btn.menu_btn(self)

		self.setWindowTitle('App_Shop - Игрушки и развлечения')


	def catalog_remont(self): # Каталог - Дом, дача, ремонт
		self.catalog_remont_Window = QWidget(self)
		self.setCentralWidget(self.catalog_remont_Window)

		# Белый фон
		self.background_img = QLabel(self.catalog_remont_Window)
		self.background_img_window()

		# Левый sidebar-catalog_menu_btn (active)
		self.btn_catalog_remont_active = QPushButton(self.catalog_remont_Window)
		self.catalog_menu_btn_active.catalog_menu_btn_remont_active(self)

		# Лого мини
		self.logo_img = QLabel(self.catalog_remont_Window)
		self.logo_mini()

		# Поиск
		self.search_Input_shop = QLineEdit('Быстрый поиск', self.catalog_remont_Window)
		self.search_Btn_shop = QPushButton('', self.catalog_remont_Window)
		self.search_products()

		# Название категории
		self.name_categoriy = QLabel('Дом, дача, ремонт', self.catalog_remont_Window)
		self.name_categoriy_window()

		# Корзина
		self.basket_Btn = QPushButton('', self.catalog_remont_Window)
		self.basket_Btn.clicked.connect(self.basket_big_window)
		if (self.basket_price > 0):
			self.basket_price_label = QLabel(str(self.basket_price) + ' руб', self.catalog_remont_Window)
		if (self.basket_count == 0):
			self.basket_count_label = QLabel('В корзине', self.catalog_remont_Window)
			self.basket_price_label = QLabel('нет товаров', self.catalog_remont_Window)
		elif (self.basket_count == 1):
			self.basket_count_label = QLabel(str(self.basket_count) + ' товар', self.catalog_remont_Window)
		elif (self.basket_count < 5):
			self.basket_count_label = QLabel(str(self.basket_count) + ' товара', self.catalog_remont_Window)
		elif (self.basket_count >= 5):
			self.basket_count_label = QLabel(str(self.basket_count) + ' товаров', self.catalog_remont_Window)
		self.basket_count_label.resize(200, 12)
		self.basket_count_label.resize(120, 12)
		self.add_to_basket()

		# Левый sidebar-catalog_menu
		self.btn_catalog_portativ = QPushButton(self.catalog_remont_Window)
		self.btn_catalog_computers = QPushButton(self.catalog_remont_Window)
		self.btn_catalog_network = QPushButton(self.catalog_remont_Window)
		self.btn_catalog_audioVideo = QPushButton(self.catalog_remont_Window)
		self.btn_catalog_climateControl = QPushButton(self.catalog_remont_Window)
		self.btn_catalog_forHome = QPushButton(self.catalog_remont_Window)
		self.btn_catalog_beauty = QPushButton(self.catalog_remont_Window)
		self.btn_catalog_cameras = QPushButton(self.catalog_remont_Window)
		self.btn_catalog_games = QPushButton(self.catalog_remont_Window)
		self.btn_catalog_auto = QPushButton(self.catalog_remont_Window)
		self.btn_catalog_ucenennyeTovary = QPushButton(self.catalog_remont_Window)
		self.catalog_menu_btn.menu_btn(self)

		self.setWindowTitle('App_Shop - Дом, дача, ремонт')


	def catalog_auto(self): # Каталог - Автотехника
		self.catalog_auto_Window = QWidget(self)
		self.setCentralWidget(self.catalog_auto_Window)

		# Белый фон
		self.background_img = QLabel(self.catalog_auto_Window)
		self.background_img_window()

		# Левый sidebar-catalog_menu_btn (active)
		self.btn_catalog_auto_active = QPushButton(self.catalog_auto_Window)
		self.catalog_menu_btn_active.catalog_menu_btn_auto_active(self)

		# Лого мини
		self.logo_img = QLabel(self.catalog_auto_Window)
		self.logo_mini()

		# Поиск
		self.search_Input_shop = QLineEdit('Быстрый поиск', self.catalog_auto_Window)
		self.search_Btn_shop = QPushButton('', self.catalog_auto_Window)
		self.search_products()

		# Название категории
		self.name_categoriy = QLabel('Автотехника', self.catalog_auto_Window)
		self.name_categoriy_window()


		# Корзина
		self.basket_Btn = QPushButton('', self.catalog_auto_Window)
		self.basket_Btn.clicked.connect(self.basket_big_window)
		if (self.basket_price > 0):
			self.basket_price_label = QLabel(str(self.basket_price) + ' руб', self.catalog_auto_Window)
		if (self.basket_count == 0):
			self.basket_count_label = QLabel('В корзине', self.catalog_auto_Window)
			self.basket_price_label = QLabel('нет товаров', self.catalog_auto_Window)
		elif (self.basket_count == 1):
			self.basket_count_label = QLabel(str(self.basket_count) + ' товар', self.catalog_auto_Window)
		elif (self.basket_count < 5):
			self.basket_count_label = QLabel(str(self.basket_count) + ' товара', self.catalog_auto_Window)
		elif (self.basket_count >= 5):
			self.basket_count_label = QLabel(str(self.basket_count) + ' товаров', self.catalog_auto_Window)
		self.basket_count_label.resize(200, 12)
		self.basket_count_label.resize(120, 12)
		self.add_to_basket()

		# Левый sidebar-catalog_menu
		self.btn_catalog_portativ = QPushButton(self.catalog_auto_Window)
		self.btn_catalog_computers = QPushButton(self.catalog_auto_Window)
		self.btn_catalog_network = QPushButton(self.catalog_auto_Window)
		self.btn_catalog_audioVideo = QPushButton(self.catalog_auto_Window)
		self.btn_catalog_climateControl = QPushButton(self.catalog_auto_Window)
		self.btn_catalog_forHome = QPushButton(self.catalog_auto_Window)
		self.btn_catalog_beauty = QPushButton(self.catalog_auto_Window)
		self.btn_catalog_cameras = QPushButton(self.catalog_auto_Window)
		self.btn_catalog_games = QPushButton(self.catalog_auto_Window)
		self.btn_catalog_remont = QPushButton(self.catalog_auto_Window)
		self.btn_catalog_ucenennyeTovary = QPushButton(self.catalog_auto_Window)
		self.catalog_menu_btn.menu_btn(self)

		self.setWindowTitle('App_Shop - Автотехника')


	def catalog_ucenennyeTovary(self): # Каталог - Уцененные товары
		self.catalog_ucenennyeTovary_Window = QWidget(self)
		self.setCentralWidget(self.catalog_ucenennyeTovary_Window)

		# Белый фон
		self.background_img = QLabel(self.catalog_ucenennyeTovary_Window)
		self.background_img_window()

		# Левый sidebar-catalog_menu_btn (active)
		self.btn_catalog_ucenennyeTovary_active = QPushButton(self.catalog_ucenennyeTovary_Window)
		self.catalog_menu_btn_active.catalog_menu_btn_ucenennyeTovary_active(self)

		# Лого мини
		self.logo_img = QLabel(self.catalog_ucenennyeTovary_Window)
		self.logo_mini()

		# Поиск
		self.search_Input_shop = QLineEdit('Быстрый поиск', self.catalog_ucenennyeTovary_Window)
		self.search_Btn_shop = QPushButton('', self.catalog_ucenennyeTovary_Window)
		self.search_products()

		# Название категории
		self.name_categoriy = QLabel('Уцененные товары', self.catalog_ucenennyeTovary_Window)
		self.name_categoriy_window()

		# Корзина
		self.basket_Btn = QPushButton('', self.catalog_ucenennyeTovary_Window)
		self.basket_Btn.clicked.connect(self.basket_big_window)
		if (self.basket_price > 0):
			self.basket_price_label = QLabel(str(self.basket_price) + ' руб', self.catalog_ucenennyeTovary_Window)
		if (self.basket_count == 0):
			self.basket_count_label = QLabel('В корзине', self.catalog_ucenennyeTovary_Window)
			self.basket_price_label = QLabel('нет товаров', self.catalog_ucenennyeTovary_Window)
		elif (self.basket_count == 1):
			self.basket_count_label = QLabel(str(self.basket_count) + ' товар', self.catalog_ucenennyeTovary_Window)
		elif (self.basket_count < 5):
			self.basket_count_label = QLabel(str(self.basket_count) + ' товара', self.catalog_ucenennyeTovary_Window)
		elif (self.basket_count >= 5):
			self.basket_count_label = QLabel(str(self.basket_count) + ' товаров', self.catalog_ucenennyeTovary_Window)
		self.basket_count_label.resize(200, 12)
		self.basket_count_label.resize(120, 12)
		self.add_to_basket()

		# Левый sidebar-catalog_menu
		self.btn_catalog_portativ = QPushButton(self.catalog_ucenennyeTovary_Window)
		self.btn_catalog_computers = QPushButton(self.catalog_ucenennyeTovary_Window)
		self.btn_catalog_network = QPushButton(self.catalog_ucenennyeTovary_Window)
		self.btn_catalog_audioVideo = QPushButton(self.catalog_ucenennyeTovary_Window)
		self.btn_catalog_climateControl = QPushButton(self.catalog_ucenennyeTovary_Window)
		self.btn_catalog_forHome = QPushButton(self.catalog_ucenennyeTovary_Window)
		self.btn_catalog_beauty = QPushButton(self.catalog_ucenennyeTovary_Window)
		self.btn_catalog_cameras = QPushButton(self.catalog_ucenennyeTovary_Window)
		self.btn_catalog_games = QPushButton(self.catalog_ucenennyeTovary_Window)
		self.btn_catalog_remont = QPushButton(self.catalog_ucenennyeTovary_Window)
		self.btn_catalog_auto = QPushButton(self.catalog_ucenennyeTovary_Window)
		self.catalog_menu_btn.menu_btn(self)

		self.setWindowTitle('App_Shop - Уцененные товары')

	def form_log(self):
		# если поля пустые
		if ( self.passwordInput_log.text() == '' ):
			self.resultText_log.setText('Введите пароль!')
			self.resultText_log.move(485, 318)
		if ( self.loginInput_log.text() == '' ):
			self.resultText_log.setText('Введите логин!')
			self.resultText_log.move(490, 318)

		# если поля не пустые
		if ( self.loginInput_log.text() != '' and self.passwordInput_log.text() != '' ):
			list_users_read = open('users_data.txt', 'r')
			list_users = list_users_read.read()

			# Если данные есть в Базе
			if (list_users.count(self.loginInput_log.text()) > 0):
				list_users_array = list_users.split(';')
				del list_users_array[-1] # Удаляет последний элемент (Пустая ячейка*)
				i = 0
				while True:
					user_data = list_users_array[i].split(':')
					if (self.loginInput_log.text() == user_data[0] and self.passwordInput_log.text() == user_data[1]):
						self.login_user = self.loginInput_log.text()
						self.catalog_shop()

					elif (self.loginInput_log.text() == user_data[0] and self.passwordInput_log.text() != user_data[1]):
						self.resultText_log.setText('Не верный пароль!')
						self.resultText_log.move(480, 318)

					i += 1
					if (i >= len(list_users_array)):
						break

			# Если данного Логина нет в Базе
			elif (self.loginInput_log.text() not in list_users):
				self.resultText_log.setText('Такой пользователь не зарегистрирован!')
				self.resultText_log.move(402, 318)

			list_users_read.close()
		self.passwordInput_log.setText('') # очищает поле пароля


	def form_reg(self):
		# если поля пустые
		if ( self.passwordInput_reg.text() == '' ):
			self.resultText_reg.setText('Заполните пароль!')
			self.resultText_reg.move(478, 356)
		if ( self.passwordInput_reg.text() != self.password2Input_reg.text() ):
			self.resultText_reg.setText('Пароли не совпадают!')
			self.resultText_reg.move(468, 356)

		# если поле Логин пустое
		if ( self.loginInput_reg.text() == '' ):
			self.resultText_reg.setText('Заполните логин!')
			self.resultText_reg.move(483, 356)

		# проверка (занят ли логин)
		if ( self.loginInput_reg.text() != '' and self.passwordInput_reg.text() != '' and self.passwordInput_reg.text() == self.password2Input_reg.text() ):
			db_logins = []
			db_read = open('users_data.txt', 'r')
			list_of_data_users = db_read.read()
			list_of_data_users = list_of_data_users.split(';')

			# Собираем логины в массив db_logins
			k = 0
			while True:
				user_data = list_of_data_users[k].split(':')
				db_logins.append(user_data[0])

				k += 1
				if (k >= len(list_of_data_users)):
					break

			# Если данный логин есть в Базе, то выдает Ошибку
			if (db_logins.count(self.loginInput_reg.text()) > 0):
				self.resultText_reg.setText('Этот логин занят!')
				self.resultText_reg.move(481, 356)

			# Если данного логина нет в Базе, то регистрируется
			else:
				db_write = open('users_data.txt', 'a')
				db_write.write(self.loginInput_reg.text() + ':' + self.passwordInput_reg.text() + ';')
				self.resultText_reg.setText('Вы зарегистировались!')
				self.resultText_reg.setStyleSheet('QLabel {color: #009A33; font-size: 14px; font-weight: bold;}')
				self.resultText_reg.move(454, 356)
				db_write.close()

			db_read.close()
		self.passwordInput_reg.setText('') # Очищает поле 
		self.password2Input_reg.setText('')	# Очищает поле


app = QApplication(sys.argv)
my_window = Multi() # экземпляр класса Multi
sys.exit(app.exec_()) # исполняемый файл