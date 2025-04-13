from typing import List
from template import Template


class TemplatesHandler:
    def __init__(self):
        self.templates: List[Template] = []

    def add(self, template: Template):
        if not template in self.templates:
            self.templates.append(template)

    def delete(self, template: Template):
        if template in self.templates:
            self.templates.remove(template)
