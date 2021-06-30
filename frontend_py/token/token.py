class Token():
    def __init__(self, type, string):
        self.type = type
        self.string = string

    def __repr__(self):
        return self.type + "\t" + self.string
