# enemy.py

from transpile import Transpilable, Row
from animation import Animation


Color = tuple[int, int, int]

# converts a color into the hex string equivalent
def to_hex(color: Color) -> str:
    assert 0 <= color[0] <= 255, f"R value must be between 0 and 255: {color[0]}"
    assert 0 <= color[1] <= 255, f"G value must be between 0 and 255: {color[1]}"
    assert 0 <= color[2] <= 255, f"B value must be between 0 and 255: {color[2]}"

    return f"#{color[0]:02X}{color[1]:02X}{color[2]:02X}"


class Enemy(Transpilable):
    def __init__(self, key: str, anim: Animation, anim_transform: Animation, color: Color, color_sat: Color, radius: float, draw_scale: float, focus_scale: float, is_spawn: bool, spawn_draw_type: bool):
        self.key = key    
    
        self.anim = anim
        self.anim_transform = anim_transform
        self.color = color
        self.color_sat = color_sat

        self.radius = radius
        self.draw_scale = draw_scale
        self.focus_scale = focus_scale
        self.is_spawn = is_spawn
        self.spawn_draw_type = spawn_draw_type

    def transpile(self) -> list[Row]:
        row = Row([
            self.key, 
            self.anim.key, 
            self.anim_transform.key, 
            to_hex(self.color), 
            to_hex(self.color_sat), 
            str(self.radius), 
            str(self.draw_scale),
            str(self.focus_scale),
            "1" if self.is_spawn else "0",
            "1" if self.spawn_draw_type else "0",
        ])
        return [row]