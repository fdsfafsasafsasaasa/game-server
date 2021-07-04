import pickle
import uuid

class Player:
    def __init__(self, x: int, y: int, color: tuple, _uuid = uuid.uuid4()) -> None:
        self.x = x
        self.y = y
        self.color = color
        self.uuid = str(_uuid)

    def encode(self) -> bytes:
        return pickle.dumps({"x": self.x, "y": self.y, "uuid": self.uuid, "color": self.color})