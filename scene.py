from manim import *

class createCircle(Scene):
    def construct(self):
        circle = Circle() #create a circle
        square = Square()
        square.rotate(PI / 4)
        circle.set_fill(PINK, opacity=0.5)
        self.play(Create(square))
        self.play(Transform(square, circle))
        self.play(FadeOut(square))


        



