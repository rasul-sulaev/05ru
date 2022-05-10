from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize

def menu_btn(self):
	## Левый sidebar-catalog_menu
	# Раздел телефоны
	# self.btn_catalog_portativ = QPushButton(self)
	self.btn_catalog_portativ.setIcon(QIcon('icons/icon_portativ.png'))
	self.btn_catalog_portativ.setIconSize(QSize(150, 150))
	self.btn_catalog_portativ.clicked.connect(self.catalog_portativ)
	self.btn_catalog_portativ.resize(66, 48)
	self.btn_catalog_portativ.move(-2, 75)

	# Раздел Компьютеры и ноутбуки
	# self.btn_catalog_computers = QPushButton(self)
	self.btn_catalog_computers.setIcon(QIcon('icons/icon_computers.png'))
	self.btn_catalog_computers.setIconSize(QSize(150, 150))
	self.btn_catalog_computers.clicked.connect(self.catalog_computers)
	self.btn_catalog_computers.resize(66, 48)
	self.btn_catalog_computers.move(-2, 120)

	# Раздел Сети, Оргтехника
	# self.btn_catalog_network = QPushButton(self)
	self.btn_catalog_network.setIcon(QIcon('icons/icon_network.png'))
	self.btn_catalog_network.setIconSize(QSize(150, 150))
	self.btn_catalog_network.clicked.connect(self.catalog_network)
	self.btn_catalog_network.resize(66, 48)
	self.btn_catalog_network.move(-2, 165)

	# Раздел ТВ, аудио, видео
	# self.btn_catalog_audioVideo = QPushButton(self)
	self.btn_catalog_audioVideo.setIcon(QIcon('icons/icon_audio-video.png'))
	self.btn_catalog_audioVideo.setIconSize(QSize(150, 150))
	self.btn_catalog_audioVideo.clicked.connect(self.catalog_audioVideo)
	self.btn_catalog_audioVideo.resize(66, 48)
	self.btn_catalog_audioVideo.move(-2, 210)

	# # Раздел Климатическая техника
	# self.btn_catalog_climateControl = QPushButton(self)
	self.btn_catalog_climateControl.setIcon(QIcon('icons/icon_climate-control.png'))
	self.btn_catalog_climateControl.setIconSize(QSize(150, 150))
	self.btn_catalog_climateControl.clicked.connect(self.catalog_climateControl)
	self.btn_catalog_climateControl.resize(66, 48)
	self.btn_catalog_climateControl.move(-2, 255)

	# # Раздел Бытавая техника
	# self.btn_catalog_forHome = QPushButton(self)
	self.btn_catalog_forHome.setIcon(QIcon('icons/icon_for-home.png'))
	self.btn_catalog_forHome.setIconSize(QSize(150, 150))
	self.btn_catalog_forHome.clicked.connect(self.catalog_forHome)
	self.btn_catalog_forHome.resize(66, 48)
	self.btn_catalog_forHome.move(-2, 300)

	# # Раздел Красота и здоровье
	# self.btn_catalog_beauty = QPushButton(self)
	self.btn_catalog_beauty.setIcon(QIcon('icons/icon_beauty.png'))
	self.btn_catalog_beauty.setIconSize(QSize(150, 150))
	self.btn_catalog_beauty.clicked.connect(self.catalog_beauty)
	self.btn_catalog_beauty.resize(66, 48)
	self.btn_catalog_beauty.move(-2, 345)

	# # Раздел Фото и видеокамеры
	# self.btn_catalog_cameras = QPushButton(self)
	self.btn_catalog_cameras.setIcon(QIcon('icons/icon_cameras.png'))
	self.btn_catalog_cameras.setIconSize(QSize(150, 150))
	self.btn_catalog_cameras.clicked.connect(self.catalog_cameras)
	self.btn_catalog_cameras.resize(66, 48)
	self.btn_catalog_cameras.move(-2, 390)

	# # Раздел Игрушки и развлечения
	# self.btn_catalog_games = QPushButton(self)
	self.btn_catalog_games.setIcon(QIcon('icons/icon_games.png'))
	self.btn_catalog_games.setIconSize(QSize(150, 150))
	self.btn_catalog_games.clicked.connect(self.catalog_games)
	self.btn_catalog_games.resize(66, 48)
	self.btn_catalog_games.move(-2, 435)

	# # Раздел Дом, дача, ремонт
	# self.btn_catalog_remont = QPushButton(self)
	self.btn_catalog_remont.setIcon(QIcon('icons/icon_remont.png'))
	self.btn_catalog_remont.setIconSize(QSize(150, 150))
	self.btn_catalog_remont.clicked.connect(self.catalog_remont)
	self.btn_catalog_remont.resize(66, 48)
	self.btn_catalog_remont.move(-2, 480)

	# # Раздел Автотехника
	# self.btn_catalog_auto = QPushButton(self)
	self.btn_catalog_auto.setIcon(QIcon('icons/icon_auto.png'))
	self.btn_catalog_auto.setIconSize(QSize(150, 150))
	self.btn_catalog_auto.clicked.connect(self.catalog_auto)
	self.btn_catalog_auto.resize(66, 48)
	self.btn_catalog_auto.move(-2, 525)

	# # Раздел Уцененные товары
	# self.btn_catalog_ucenennyeTovary = QPushButton(self)
	self.btn_catalog_ucenennyeTovary.setIcon(QIcon('icons/icon_ucenennye-tovary.png'))
	self.btn_catalog_ucenennyeTovary.setIconSize(QSize(150, 150))
	self.btn_catalog_ucenennyeTovary.clicked.connect(self.catalog_ucenennyeTovary)
	self.btn_catalog_ucenennyeTovary.resize(66, 48)
	self.btn_catalog_ucenennyeTovary.move(-2, 570)