import arcade
import os
import random
import time


# set the width, height and title of the window
SCREEN_WIDTH = 248
SCREEN_HEIGHT = 248
SCREEN_TITLE = "Memory game"

# set the card size
CELL_WIDTH = 62
CELL_HEIGHT = 62

#set the field size
ROW_COUNT = 4
COLUMN_COUNT = 4
#set the time during which the cards are open
CARDS_SHOW_TIME = 2

#card class
class Card(arcade.Sprite):
    def __init__(self, filename, center_x, center_y):
        super().__init__(filename, 0.9)
        self.center_x = center_x
        self.center_y = center_y
        self.hide()

    # method to open a card
    def show(self):
        self.alpha = 255

    # method to close a card
    def hide(self):
        self.alpha = 0


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.bg = arcade.load_texture('images/closed.png')
        self.cards = arcade.SpriteList()
        #first face-up card of a pair
        self.card_1 = None
        #second face-up card of the pair
        self.card_2 = None
        self.show_time = time.time()
        self.score = 0
        self.sound_background = arcade.load_sound('music/background.mp3')
        self.sound_background.play(0.3, 0)
        self.sound_open = arcade.load_sound('music/open.mp3')
        self.sound_wrong = arcade.load_sound('music/wrong.mp3')

    def setup(self):
        images = os.listdir('images') # create a list with the names of image files
        images.remove('closed.png') # remove the empty card image from the list
        images += images # add their copies to the list of images, since all cards must have a pair

        # arrange the cards in random order
        for y in range(ROW_COUNT):
            for x in range(COLUMN_COUNT):
                image = images[4*y + x]
                center_x = x * CELL_WIDTH + CELL_WIDTH / 2
                center_y = y * CELL_HEIGHT + CELL_HEIGHT / 2

                card = Card(f'images/{image}', center_x, center_y)
                self.cards.append(card)

    # rendering
    def on_draw(self):
        arcade.start_render()
        arcade.set_background_color(arcade.color.WHITE)

        # draw empty cards
        for y in range(ROW_COUNT):
            for x in range(COLUMN_COUNT):
                arcade.draw_texture_rectangle(x * CELL_WIDTH + CELL_WIDTH/2 ,
                                              y * CELL_HEIGHT + CELL_HEIGHT / 2,
                                              CELL_WIDTH, CELL_HEIGHT, self.bg)

        # draw cards with pictures
        self.cards.draw()
        if self.score == 7:
            arcade.draw_text('You lose!', 10, SCREEN_HEIGHT / 2, arcade.color.RED, 40)

    def update(self, delta_time):
        if self.card_1 != None and self.card_2 != None:
            if time.time() - self.show_time < CARDS_SHOW_TIME:
                arcade.play_sound(self.sound_wrong)
                self.card_1.hide()
                self.card_2.hide()
                self.card_1 = None
                self.card_2 = None

    def on_mouse_press(self, x, y, button, modifiers):
        # determine which card was clicked 
        for card in self.cards:
            if card.left < x < card.right and card.bottom < x < card.top and card.alpha != 255:
                # if you haven't opened the first card yet
                if self.card_1 == None:
                    card.show()
                    # save the first card of the pair
                    self.card_1 = card
                # if the first one is open, but the second one is not yet
                elif self.card_2 == None:
                    card.show()
                    # save the second card of the pair
                    self.card_2 = card
                    # remember the time the cards were opened
                    self.show_time = time.time()

                    if self.card_1.texture == self.card_2.texture:
                        self.card_1 = None
                        self.card_2 = None
                        self.score += 1

window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
window.setup()
arcade.run()


