
class RhombusMapException(Exception):
    pass


class RhombusMap:
    def __init__(self, diagonal, default_factory=lambda: None, wrap_cw=True):
        self.check_diagonal(diagonal)
        self.diagonal = diagonal
        self.wrap_cw = wrap_cw
        self.data = [default_factory() for _ in range(self.get_size(diagonal))]

    @classmethod
    def check_diagonal(cls, diagonal):
        if not isinstance(diagonal, int):
            raise RhombusMapException("Parameter 'diagonal' has to be int; got %s" % diagonal)
        if diagonal < 3:
            raise RhombusMapException("Parameter 'diagonal' has to be 3 or greater; got %s" % diagonal)
        if diagonal % 2 == 0:
            raise RhombusMapException("Parameter 'diagonal' has to be an odd number; got %s" % diagonal)

    @classmethod
    def get_size(cls, diagonal):
        return (diagonal // 2) ** 2 + (diagonal // 2 + 1) ** 2

    def __getitem__(self, key):
        idx = self.tuple_to_index(key)
        return self.data[idx]

    def __setitem__(self, key, value):
        idx = self.tuple_to_index(key)
        self.data[idx] = value

    def tuple_to_index(self, tpl):
        x, y = tpl
        if self.wrap_cw:
            offset = y * self.diagonal
        else:
            offset = -y * self.diagonal
        return (x + offset) % len(self.data)
