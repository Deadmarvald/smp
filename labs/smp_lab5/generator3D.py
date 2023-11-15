from abc import ABC, abstractmethod
import colorama
from colorama import Fore

colorama.init(autoreset=True)

palette = {index: color for index, color in enumerate(sorted(Fore.__dict__.keys())) if not color.startswith('_')}

def show_palette() -> None:
    for index, color in palette.items():
        print(f"{index}. {color}")

class AbstractShape(ABC):
    def __init__(self, mark: str, color_code: int):
        if color_code not in palette:
            raise ValueError("Color code should be within the palette range")
        elif not self.valid_mark(mark):
            raise ValueError("Only a single mark is acceptable")
        self._mark = mark
        self._color_code = color_code

    @abstractmethod
    def draw_2d(self) -> list:
        pass

    @abstractmethod
    def draw_3d(self) -> str:
        pass

    @staticmethod
    def valid_mark(mark: str) -> bool:
        return len(mark) == 1

class Square(AbstractShape):
    def __init__(self, edge: int, mark: str, color_code: int):
        if edge <= 0:
            raise ValueError("Edge length must be positive")
        super().__init__(mark, color_code)
        self._edge = edge
        self._midpoint = int(edge / 2 + 1)

    def draw_2d(self) -> list:
        sketch = ""
        for i in range(self._edge):
            for j in range(self._edge):
                if i in [0, self._edge - 1] or j in [0, self._edge - 1]:
                    sketch += f"{self._mark}  "
                else:
                    sketch += "   "
            sketch += "\n"

        return [(Fore.__getattribute__(palette[self._color_code]) + "\n" + sketch) for _ in range(6)]

    def draw_3d(self, scaling: float = 1.0) -> str:
        new_edge = int(self._edge * scaling) if self._edge * scaling >= 2 else self._edge
        new_midpoint = int(new_edge / 2 + 1)
        sketch = ""

        for row in range(new_midpoint - 1):
            for col in range(new_edge + new_midpoint - 1):
                if (row + col == new_midpoint - 1) or (row == 0 and col > new_midpoint - 1):
                    sketch += f"{self._mark}" + (
                        "" if col == new_edge + new_midpoint - 2 and row == 0 else "  ")
                elif new_edge + new_midpoint - row == col + 2:
                    sketch += f"{self._mark}"
                elif col == new_edge + new_midpoint - 2:
                    sketch += f"  {self._mark}"
                else:
                    sketch += "   "
            sketch += "\n"

        for row in range(new_edge):
            for col in range(new_edge + new_midpoint):
                if ((row == 0 or row == new_edge - 1) and col < new_edge or (
                        col == 0 or col == new_edge - 1) and row < new_edge and col < new_edge):
                    sketch += f"{self._mark}" + (
                        "" if row == new_edge - 1 and col == new_edge - 1 else "  ")
                elif row + col == (new_edge - 1) * 2 and col < new_edge + new_midpoint - 1:
                    sketch += "   " * (new_edge - row - 2) + f"{self._mark}"
                elif col < new_edge and row < new_edge:
                    sketch += "   "
                elif row < new_edge - new_midpoint and col > new_edge:
                    if col == new_midpoint + new_edge - 1:
                        sketch += f"{self._mark}"
                    else:
                        sketch += "   "

            sketch += "\n"

        return Fore.__getattribute__(palette[self._color_code]) + "\n" + sketch
