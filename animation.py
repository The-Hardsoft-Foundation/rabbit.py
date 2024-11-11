# animation.py 

from transpile import Transpilable, Row


# TODO: make this real
class Animation(Transpilable):
    def __init__(self, key: str, filepath: str, filepath_lq: str):
        self.key = key
        self.filepath = filepath
        self.filepath_lq = filepath_lq

    def transpile(self) -> list[Row]:
        row = Row([self.key, self.filepath, self.filepath_lq])
        row.extend("14 250 280 0 -180 0-1 2-3 4-5 6 6 7-8-9 10 11-12-13 7-8-9 10 11-12-13 7-8-9 10 11-12-13 7-8-9 10 11-12-13".split(" "))
        return [row]