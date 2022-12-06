class Class(object):
    def __init__(self, name, id):
        self._name = name
        self._id = id
        self._lables = None
        self._entry = None

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        self._name = value
    @property
    def id(self):
        return self._id
    @id.setter
    def id(self, *values):
        self._id = values
    @property
    def entry(self):
        return self._entry
    @entry.setter
    def entry(self, *values):
        self._entry = values