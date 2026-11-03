"""The paper look for Manim CE scenes (Build: Kit, Manim). A scene file starts with `from manim_paper import *`.
Colours are hfkit's tokens; lines are thick (6 px at 1080 wide is about stroke_width 9 in Manim units at this frame);
the background is transparent, so the clip sits on hfkit's paper inside a video's world."""
from manim import *  # noqa: F401,F403

PAPER, INK, MUTED, WHITE = "#F4EFE4", "#121212", "#6B665C", "#FFFFFF"
YELLOW_, BLUE_, RED_, GREEN_ = "#FFD23F", "#2C5BEA", "#D7392B", "#13965A"
STROKE = 9

config.background_opacity = 0.0           # transparent webm: hfkit's paper shows through
config.transparent = True
config.movie_file_extension = ".webm"
config.frame_rate = 30
for cls in (Line, Arrow, Circle, Square, Rectangle, Polygon, VMobject):
    cls.set_default(stroke_color=INK, stroke_width=STROKE)
Text.set_default(color=INK, font="Inter")
MathTex.set_default(color=INK)


def ink_axes(x=(-4, 4, 1), y=(-4, 4, 1), size=6):
    """Axes in the paper look: thick ink, no tips, muted ticks."""
    return Axes(x_range=x, y_range=y, x_length=size, y_length=size, tips=False,
                axis_config={"stroke_color": MUTED, "stroke_width": STROKE - 2, "include_ticks": False})
