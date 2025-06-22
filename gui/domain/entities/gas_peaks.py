from struct import unpack
from gui.domain.entities.entity import Entity


class GasPeaks(Entity):

    def __init__(self):
        super().__init__("i", 4, "Gas peaks")

    def unpack(self, d):
        return unpack(f"{self.window_length}{self.format_idenitfier}")