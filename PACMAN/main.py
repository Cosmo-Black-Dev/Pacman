from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ObjectProperty
from kivy.clock import Clock
from kivy.vector import Vector
from kivy.core.window import Window
import random

class PacMan(Widget):
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)

    def move(self):
        self.pos = Vector(self.velocity_x, self.velocity_y) + self.pos

class Ghost(Widget):
    pass

class Point(Widget):
    pass

class PacManGame(Widget):
    pacman = ObjectProperty(None)
    ghosts = []
    points = []
    score = NumericProperty(0)

    def start(self):
        self.ghosts = [Ghost() for _ in range(4)]
        for ghost in self.ghosts:
            self.add_widget(ghost)
            ghost.pos = (random.randint(0, Window.width - ghost.width), random.randint(0, Window.height - ghost.height))

        self.points = [Point() for _ in range(10)]
        for point in self.points:
            self.add_widget(point)
            point.pos = (random.randint(0, Window.width - point.width), random.randint(0, Window.height - point.height))

        Clock.schedule_interval(self.update, 1.0 / 60.0)

    def update(self, dt):
        self.pacman.move()

        for ghost in self.ghosts:
            if self.pacman.collide_widget(ghost):
                self.game_over()

        for point in self.points:
            if self.pacman.collide_widget(point):
                self.points.remove(point)
                self.remove_widget(point)
                self.score += 1

    def game_over(self):
        Clock.unschedule(self.update)
        self.pacman.velocity_x = 0
        self.pacman.velocity_y = 0
        print("Game Over! Your score: {}".format(self.score))

class PacManApp(App):
    def build(self):
        game = PacManGame()
        game.start()
        return game

if __name__ == '__main__':
    PacManApp().run()
