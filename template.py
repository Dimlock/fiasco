class Category:
    def __init__(self, name):
        self.name = name
        self.elements = []

    def add(self, element):
        self.elements.append(element)


class TempList:
    def __init__(self, name):
        self.name = name
        self.categories = []

    def add(self, element):
        self.categories.append(element)


class Template:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.lists = []

    def add(self, element):
        self.lists.append(element)
