class Category:
    def __init__(self, name):
        self.name = name
        self.elements = []

    def add(self, element):
        self.elements.append(element)

    def save(self):
        return {"name": self.name,
                "elements": self.elements}


class TempList:
    def __init__(self, name):
        self.name = name
        self.categories = []

    def add(self, element):
        self.categories.append(element)

    def save(self):
        return {"name": self.name,
                "categories": [i.save() for i in self.categories]}


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
        template_dict = dict_file["template"]
        self.name = template_dict["name"]
        self.description = template_dict["description"]
