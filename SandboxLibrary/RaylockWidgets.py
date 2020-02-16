
class Vector:
    def __init__(self, input):
        input = input.rstrip()
        input = input.lstrip()
        input = input.split(",")

        for i in range(0,len(input)):
            input[i] = float(input[i])

        self.x = input[0]
        self.y = input[1]
        if len(input) == 3:
            self.z = input[2]
        else:
            self.z = 0

    def DotProduct(self, vector):

        return self.x*vector.x + self.y*vector.y + self.z*vector.z

    def CrossProduct(self, vector):

        CP = Vector("0,0,0")

        CP.x = self.y*vector.z - self.z*vector.y
        CP.y = -self.x*vector.z + self.z*vector.x
        CP.z = self.x*vector.y - self.y*vector.x

        return CP

    def Normalize(self):

        CP = Vector("0,0,0")

        mag = (self.x**2 + self.y**2 + self.z**2)**0.5

        CP.x = self.x/mag
        CP.y = self.y/mag
        CP.z = self.z/mag

        return CP

    def GetString(self):
        answer = "< " + str(round(self.x,5)) + ", "+str(round(self.y,5))+", " +str(round(self.z,5))+">"
        return answer

class ColumnHeader:

    def __init__(self, text, row, column, rowspan=1, colspan=1):

        self.text = text
        self.row = row
        self.column = column
        self.rowspan = rowspan
        self.colspan = colspan

class Column:

    def __init__(self, title, group=False, width=30):

        self.title = title
        self.group = group
        self.width = width

class Table:

    def __init__(self):
        self.columns = []
        self.column_headers = []

    def AddColumn(self, title, group=False, width=100):
        self.columns.append(Column(title, group, width))

    def AddColumnHeader(self, text, row, column, rowspan=1, colspan=1):
        self.column_headers.append(ColumnHeader(text, row, column, rowspan, colspan))

class FilePicker:
    def __init__(self, name, row, **kwargs):
        self.name = name
        self.row = row
        self.tip = "Select a File"
        self.default = "Select File"
        self.type = "FilePicker"
        self.extension = "default"
        self.wildcard = "default"

        if 'extension' in kwargs:
            self.extension = kwargs["extension"]

        if 'wildcard' in kwargs:
            self.wildcard = kwargs["wildcard"]

        if 'tip' in kwargs:
            self.tip = kwargs["tip"]

        if 'default' in kwargs:
            self.default = kwargs["default"]

class DynamicFilePicker:
    def __init__(self, name, row, id0,**kwargs):
        self.name = name
        self.row = row
        self.id = id0
        self.tip = "Select a File"
        self.default = "Select File"
        self.type = "DynamicFilePicker"
        self.extension = "default"
        self.wildcard = "default"

        if 'extension' in kwargs:
            self.extension = kwargs["extension"]

        if 'wildcard' in kwargs:
            self.wildcard = kwargs["wildcard"]

        if 'tip' in kwargs:
            self.tip = kwargs["tip"]

        if 'default' in kwargs:
            self.default = kwargs["default"]

class DirectoryPicker:
    def __init__(self, name, row, **kwargs):
        self.name = name
        self.row = row
        self.tip = "Select a Directory"
        self.default = "C:\\Raylock\\"
        self.type = "DirectoryPicker"
        self.extension = "directory"
        self.wildcard = "directory"

        if 'tip' in kwargs:
            self.tip = kwargs["tip"]

        if 'default' in kwargs:
            self.default = kwargs["default"]

class DynamicDirectoryPicker:
    def __init__(self, name, row, id0, **kwargs):
        self.name = name
        self.row = row
        self.id = id0
        self.tip = "Select a File"
        self.default = "Select File"
        self.type = "DynamicDirectoryPicker"
        self.extension = "directory"
        self.wildcard = "directory"

        if 'tip' in kwargs:
            self.tip = kwargs["tip"]

        if 'default' in kwargs:
            self.default = kwargs["default"]

class Variable:
    def __init__(self, name):
        self.name = name
        self.value = ""
        self.type = "Variable"

class Input:
    def __init__(self, name, row, **kwargs):
        self.name = name
        self.row = row
        self.tip = ""
        self.unit = ""
        self.default = ""
        self.numbers = True
        self.type = "Input"

        if 'tip' in kwargs:
            self.tip = kwargs["tip"]

        if 'numbers' in kwargs:
            self.numbers = kwargs["numbers"]

        if 'unit' in kwargs:
            self.unit = kwargs["unit"]

        if 'default' in kwargs:
            self.default = kwargs["default"]

        if 'label' in kwargs:
            self.label = kwargs["label"]
        else:
            self.label = name

class DynamicInput:
    def __init__(self, name, row, id0, **kwargs):
        self.name = name
        self.row = row
        self.id = id0
        self.numbers = True
        self.tip = ""
        self.unit = ""
        self.default = ""
        self.type = "DynamicInput"

        if 'tip' in kwargs:
            self.tip = kwargs["tip"]

        if 'numbers' in kwargs:
            self.numbers = kwargs["numbers"]

        if 'unit' in kwargs:
            self.unit = kwargs["unit"]

        if 'default' in kwargs:
            self.default = kwargs["default"]

        if 'label' in kwargs:
            self.label = kwargs["label"]
        else:
            self.label = name

class Output:
    def __init__(self, name, row, **kwargs):
        self.name = name
        self.row = row
        self.tip = ""
        self.unit = ""
        self.default = "Not Calculated"
        self.format = "%.3f"
        self.type = "output"

        if 'tip' in kwargs:
            self.tip = kwargs["tip"]

        if 'unit' in kwargs:
            self.unit = kwargs["unit"]

        if 'default' in kwargs:
            self.default = kwargs["default"]

        if 'format' in kwargs:
            self.format = kwargs["format"]

        if 'label' in kwargs:
            self.label = kwargs["label"]
        else:
            self.label = name

class DynamicOutput:
    def __init__(self, name, row, id0, **kwargs):
        self.name = name
        self.id = id0
        self.row = row
        self.tip = ""
        self.unit = ""
        self.default = "Not Calculated"
        self.format = "%.3f"
        self.type = "dynamicoutput"

        if 'tip' in kwargs:
            self.tip = kwargs["tip"]

        if 'unit' in kwargs:
            self.unit = kwargs["unit"]

        if 'default' in kwargs:
            self.default = kwargs["default"]

        if 'format' in kwargs:
            self.format = kwargs["format"]

        if 'label' in kwargs:
            self.label = kwargs["label"]
        else:
            self.label = name

class CheckBox:
    def __init__(self, name, row, **kwargs):
        self.name = name
        self.row = row
        self.tip = ""
        self.default = False
        self.type = "CheckBox"

        if 'tip' in kwargs:
            self.tip = kwargs["tip"]

        if 'default' in kwargs:
            self.default = kwargs["default"]

        if 'label' in kwargs:
            self.label = kwargs["label"]
        else:
            self.label = name

class DynamicCheckBox:
    def __init__(self, name, row, id0,**kwargs):
        self.name = name
        self.row = row
        self.id = id0
        self.tip = ""
        self.default = False
        self.type = "DynamicCheckBox"

        if 'tip' in kwargs:
            self.tip = kwargs["tip"]

        if 'default' in kwargs:
            self.default = kwargs["default"]

        if 'label' in kwargs:
            self.label = kwargs["label"]
        else:
            self.label = name

class RadioSet:
    def __init__(self, name, row, items, **kwargs):
        self.name = name
        self.row = row
        self.tip = ""
        self.default = 0
        self.type = "RadioSet"
        self.items = items
        self.ShowStaticBox = True

        if 'tip' in kwargs:
            self.tip = kwargs["tip"]

        if 'default' in kwargs:
            self.default = kwargs["default"]

        if 'label' in kwargs:
            self.label = kwargs["label"]

        else:
            self.label = name

        if 'outline' in kwargs:
            self.ShowStaticBox = kwargs["outline"]

class Choice:
    def __init__(self, name, row, items, **kwargs):
        self.name = name
        self.row = row
        self.tip = ""
        self.default = 0
        self.type = "Choice"
        self.items = items
        self.edit = False

        if 'tip' in kwargs:
            self.tip = kwargs["tip"]

        if 'default' in kwargs:
            self.default = kwargs["default"]

        if 'label' in kwargs:
            self.label = kwargs["label"]

        else:
            self.label = name

        if 'edit' in kwargs:
            self.edit = kwargs["edit"]

class DynamicRadioSet:
    def __init__(self, name, row, items, id0,**kwargs):
        self.name = name
        self.row = row
        self.id = id0
        self.tip = ""
        self.default = 0
        self.type = "DynamicRadioSet"
        self.items = items
        self.ShowStaticBox = True

        if 'tip' in kwargs:
            self.tip = kwargs["tip"]

        if 'default' in kwargs:
            self.default = kwargs["default"]

        if 'label' in kwargs:
            self.label = kwargs["label"]

        else:
            self.label = name

        if 'outline' in kwargs:
            self.ShowStaticBox = kwargs["outline"]

class DynamicChoice:
    def __init__(self, name, row, items, id0,**kwargs):
        self.name = name
        self.row = row
        self.id = id0
        self.tip = ""
        self.default = 0
        self.type = "DynamicChoice"
        self.items = items
        self.edit = False

        if 'tip' in kwargs:
            self.tip = kwargs["tip"]

        if 'default' in kwargs:
            self.default = kwargs["default"]

        if 'label' in kwargs:
            self.label = kwargs["label"]

        else:
            self.label = name

        if 'edit' in kwargs:
            self.edit = kwargs["edit"]

class ToggleSet:
    def __init__(self, name, row, items, **kwargs):
        self.name = name
        self.row = row
        self.tip = ""
        self.default = 0
        self.type = "ToggleSet"
        self.items = items
        self.ShowStaticBox = True

        if 'tip' in kwargs:
            self.tip = kwargs["tip"]

        if 'default' in kwargs:
            self.default = kwargs["default"]

        if 'label' in kwargs:
            self.label = kwargs["label"]

        else:
            self.label = name

        if 'outline' in kwargs:
            self.ShowStaticBox = kwargs["outline"]

class ToggleBox:
    def __init__(self, name, row, items, **kwargs):
        self.name = name
        self.row = row
        self.tip = ""
        self.default = 0
        self.type = "ToggleBox"
        self.items = items

        if 'tip' in kwargs:
            self.tip = kwargs["tip"]

        if 'default' in kwargs:
            self.default = kwargs["default"]

        if 'label' in kwargs:
            self.label = kwargs["label"]
        else:
            self.label = name

class AppLauncher:
    def __init__(self, name, filename, classname, row, **kwargs):
        self.name = name
        self.filename = filename
        self.classname = classname
        self.row = row
        self.tip = ""
        self.type = "AppLauncher"

        if 'tip' in kwargs:
            self.tip = kwargs["tip"]
            
class DynamicAppLauncher:
    def __init__(self, name, filename, classname, row, id0, **kwargs):
        self.name = name
        self.id = id0
        self.filename = filename
        self.classname = classname
        self.row = row
        self.tip = ""
        self.type = "DynamicAppLauncher"

        if 'tip' in kwargs:
            self.tip = kwargs["tip"]