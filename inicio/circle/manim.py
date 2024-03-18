import manim as mn
# from manim import *

class CreateCircle(mn.Scene):
    
    def construct(self):
        
        circle = mn.Circle()                    # create a circle
        circle.set_fill(mn.RED, opacity=0.1)    # set the color and transparency
        self.play(mn.Create(circle))            # show the circle on screen


