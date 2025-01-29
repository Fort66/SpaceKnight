from dataclasses import dataclass

@dataclass
class Colors:
    white: str | tuple[int, int, int] = 'white'
    yellow: str | tuple[int, int, int] = 'yellow'