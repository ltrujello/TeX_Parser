class Token():
    def __init__(self, name, value):
        self.name = name
        self.value = value
        self.type = None
        self.sibling = None

    def __repr__(self):
        return self.name + "\t" + self.value




