class Explore(object):
    def __init__(self, columns):
        for attr in columns.key():
            setattr(self, attr, columns[attr])
