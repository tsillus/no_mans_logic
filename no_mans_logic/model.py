from dataclasses import dataclass

from no_mans_logic.editor.model.vector import Vector


@dataclass
class Model:
    topleft: Vector
    bottomright: Vector = None
    size: Vector = None

    def __post_init__(self):
        if not self.size:
            self.size = self.bottomright - self.topleft
        elif not self.bottomright:
            self.bottomright = self.topleft + self.size
