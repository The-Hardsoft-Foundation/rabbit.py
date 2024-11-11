# transpile.py


class Row:
    # self.elements: list[str]
    def __init__(self, elements: list[str] | str = None):
        if elements:
            if type(elements) == str:
                self.elements = elements.split(",")
            else:
                self.elements = list(elements)
        else:
            self.elements = []

    def add(self, element):
        self.elements.append(element)

    def extend(self, elements):
        self.elements.extend(elements)

    # convert the row into a string that can be written into a csv
    def __str__(self) -> str:
        return ",".join(self.elements)


# base class for anything that can be transpiled into sheets
# must implement the transpile function
class Transpilable:
    def __init__(self):
        pass

    def transpile(self) -> list[Row]:
        return []


# # transpile the python code into the csvs
# class Transpiler:
#     def __init__(self):
#         pass

#     # this autogenerates the files needed in the specified folder
#     def transpile(self, obj: list[Transpilable], folder: str):
#         pass