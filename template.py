class Category:
    def __init__(self):
        self.name = ""
        self.elements = []

    def set_name(self, name):
        self.name = name

    def add(self, element):
        self.elements.append(element)

    def save(self):
        return {"name": self.name,
                "elements": self.elements}

    def load(self, dict_file):
        self.name = dict_file["name"]
        for element in dict_file["elements"]:
            self.add(element)
        return self


class TempList:
    def __init__(self):
        self.name = ""
        self.categories = []

    def set_name(self, name):
        self.name = name

    def add(self, element):
        self.categories.append(element)

    def save(self):
        return {"name": self.name,
                "categories": [i.save() for i in self.categories]}

    def load(self, dict_file):
        self.name = dict_file["name"]
        for category in dict_file["categories"]:
            self.add(Category().load(category))
        return self


class Template:
    def __init__(self):
        self.name = ""
        self.description = ""
        self.lists = []

    def set_name_description(self, name, description):
        self.name = name
        self.description = description

    def add(self, element):
        self.lists.append(element)

    def save(self):
        return {"name": self.name,
                "description": self.description,
                "lists": [i.save() for i in self.lists]}

    def load(self, dict_file):
        self.name = dict_file["name"]
        self.description = dict_file["description"]
        for element in dict_file["lists"]:
            self.add(TempList().load(element))
        return self
