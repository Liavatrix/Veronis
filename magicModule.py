class MagicList:
    def __init__(self, cls_type=int):
        self._next_index = 0
        self._items = []
        self._items_type = cls_type

    def __setitem__(self, key, value):
        if key == self._next_index:
            self._items.append(self._items_type())
            self._next_index += 1

        self._items[key] = value

    def __getitem__(self, key):
        if key == self._next_index:
            self[key] = self._items_type()

        return self._items[key]

    def __str__(self):
        return str(self._items)

    def __repr__(self):
        return repr(self._items)

