class Category:
    def __init__(self, name):
        self.name = name
        self.elements = []

    def add(self, element):
        self.elements.append(element)