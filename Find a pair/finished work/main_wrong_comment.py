import arcade
import os
import random
# ошибка 1: не подключена библиотека time
#import time 


# задаем ширину, высоту и заголовок окна
SCREEN_WIDTH = 248
SCREEN_HEIGHT = 248
SCREEN_TITLE = "Memory game"

# задаем размер карточки
CELL_WIDTH = 62
CELL_HEIGHT = 62

#задаем размер поля
ROW_COUNT = 4
COLUMN_COUNT = 4
#задаем время, в течение которого карточки открыты
CARDS_SHOW_TIME = 2

#класс карточки
class Card(arcade.Sprite):
    def __init__(self, filename, center_x, center_y):
        super().__init__(filename, 0.9)
        self.center_x = center_x
        self.center_y = center_y
        # ошибка 3: карточки сразу открыты, так как в конструкторе вызван метод открытия карточки show(), 
        # нужно вызвать hide()
        self.show() 

    # метод открыть карточку
    def show(self):
        self.alpha = 255

    # метод закрыть карточку
    def hide(self):
        # ошибка 4: метод должен прятать карточку, значит делать ее полностью прозрачной, 
        # в атрибуте alpha должен быть 0
        self.alpha = 125 


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.bg = arcade.load_texture('images/closed.png')
        self.cards = arcade.SpriteList()
        #первая открытая карта из пары
        self.card_1 = None
        #вторая открытая карта из пары
        self.card_2 = None
        self.show_time = time.time()
        self.score = 0
        self.sound_background = arcade.load_sound('music/background.mp3')
        # ошибка 11: фоновая музыка останавливается, нужно указать True в параметре loop
        self.sound_background.play(0.3, 0)
        self.sound_open = arcade.load_sound('music/open.mp3')
        self.sound_wrong = arcade.load_sound('music/wrong.mp3')

    def setup(self):
        images = os.listdir('images') # создаем список с названиями файлов картинок
        images.remove('closed.png') # удаляем из списка изображение пустой карточки
        images += images # добавляем в список изображений их копии, так как все карточки должны иметь пару

        # расставляем карточки в случайном порядке
        for y in range(ROW_COUNT):
            for x in range(COLUMN_COUNT):
                # ошибка 12: картинки всегда в одном порядке, нужно добавить случайность
                image = images[4*y + x] # image = random.choice(images)
                center_x = x * CELL_WIDTH + CELL_WIDTH / 2
                center_y = y * CELL_HEIGHT + CELL_HEIGHT / 2

                card = Card(f'images/{image}', center_x, center_y)
                self.cards.append(card)
                # ошибка 12: при случайном выборе нужно удалить картинку из списка, чтобы случайно не выбрать ее снова
                # images.remove(image) 

    # отрисовка
    def on_draw(self):
        arcade.start_render()
        arcade.set_background_color(arcade.color.WHITE)

        # отрисовываем пустые карточки
        for y in range(ROW_COUNT):
            for x in range(COLUMN_COUNT):
                # ошибка 2: карточки расположены со смещением влево, нужно добавить к x половину ширины + CELL_WIDTH /2
                arcade.draw_texture_rectangle(x * CELL_WIDTH , 
                                              y * CELL_HEIGHT + CELL_HEIGHT / 2,
                                              CELL_WIDTH, CELL_HEIGHT, self.bg)

        # отрисовываем карточки с картинками
        self.cards.draw()
        # ошибка 8: если открыты 7 пар, выводится сообщение о конце игры, нужно выводить при счете 8
        if self.score == 7: 
            # ошибка 9: неправильное сообщение 'Ты проиграл!', в случае победы надо писать 'Ты выиграл!'
            # уменьшить размер шрифта до 27, чтобы сообщение помещалось в окно
            arcade.draw_text('Ты проиграл!', 10, SCREEN_HEIGHT / 2, arcade.color.RED, 40)

    def update(self, delta_time):
        if self.card_1 != None and self.card_2 != None:
             # ошибка 7: при клике на вторую карточку быстро закрывается первая из-за знака < в условии, 
             # время должно стать больше времени показа карточек
            if time.time() - self.show_time < CARDS_SHOW_TIME:
                arcade.play_sound(self.sound_wrong)
                self.card_1.hide()
                self.card_2.hide()
                self.card_1 = None
                self.card_2 = None

    def on_mouse_press(self, x, y, button, modifiers):
        for card in self.cards:
            # ошибка 5: при нажатии на карточку открываются карточки на диагонали, так как во 2-м условии проверяется х, 
            # нужно проверять у
            if card.left < x < card.right and card.bottom < x < card.top and card.alpha != 255:
                # если еще не открыли первую карточку 
                if self.card_1 == None:
                    # ошибка 10: не проигрывается звук открытия карточки
                    #arcade.play_sound(self.sound_open)
                    card.show()
                    # сохраняем первую карточку из пары
                    self.card_1 = card
                # если первая открыта, а вторая еще нет 
                elif self.card_2 == None:
                    # ошибка 10: не проигрывается звук открытия карточки
                    #arcade.play_sound(self.sound_open)
                    card.show()
                    # запоминаем время открытия карточек
                    self.show_time = time.time()
                    # ошибка 6: можно открыть все карточки подряд, так как вторая карточка из пары не записывается
                    #self.card_2 = card 

                    if self.card_1.texture == self.card_2.texture:
                        self.card_1 = None
                        self.card_2 = None
                        self.score += 1

window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
window.setup()
arcade.run()


