from SandboxLibrary.RaylockWidgets import *
from SandboxLibrary.RaylockDrawing import *
from SandboxLibrary.RaylockPlot import *
import shelve
from winreg import *
from os import path

class AppUtility:

    def __init__(self, **kwargs):
    
    
        if "database" in kwargs:
            self.database = kwargs["database"]
        else:
            self.database = None

        if "owned" in kwargs:
            if kwargs["owned"]:
                self.owned = "True"
            else:
                self.owned = "False"
        else:
            self.owned = "True"

        self.UseConfig = "False"
        self.row = 0
        self.orow = 0
        self.togglerow = 0
        self.d_row = 0
        self.d_column=0
        self.dynamicrows = {}
        self.dynamicoutputrows = {}
        self.inputs = []
        self.returnedinputs = {}
        self.setinputs = {}
        self.returnvariables = {}
        self.returnedoutputs = {}
        self.outputs = []
        self.dynamicoutputs = []
        self.drawings = []
        self.drawingsmap = {}
        self.tables = []
        self.tablesmap = {}
        self.dynamicdrawings = []
        self.dynamicdrawingsmap ={}
        self.plots = []
        self.plotsmap = {}
        self.pics = []
        self.picsalignment = []
        self.plotsalignment = []
        self.P = {}
        self.staticinputlocation = "East"
        self.dynamicinputlocation = "East"
        self.staticoutputlocation = "South"
        self.dynamicoutputlocation = "South"
        self.togglelocation = "West"
        
        self.SavedInputs = {}
        self.givendatabase = None
        self.appname = None

    def SetStaticInputLocation(self, location):
        self.staticinputlocation = location.capitalize()

    def SetDynamicInputLocation(self, location):
        self.dynamicinputlocation = location.capitalize()

    def SetStaticOutputLocation(self, location):
        self.staticoutputlocation = location.capitalize()

    def SetDynamicOutputLocation(self, location):
        self.dynamicoutputlocation = location.capitalize()

    def AddPicture(self, pic, **kwargs):
        row = self.d_row-1
        col = 0
        if 'row' in kwargs:
            row = kwargs["row"]
        if 'column' in kwargs:
            col = kwargs["column"]
        if not "column" in kwargs and not "row" in kwargs:
            row = self.d_row
            col = self.d_column
            self.d_row = self.d_row + 1
        self.pics.append(pic)
        self.picsalignment.append([row,col])

    def SetToggleLocation(self, location):
        self.togglelocation = location.capitalize()

    def AddInputSpace(self, **kwargs):

        if 'id' in kwargs:
            id = kwargs["id"]
            if id in self.dynamicrows:
                self.dynamicrows[id] = self.dynamicrows[id] + 1
            else:
                self.dynamicrows[id] = 1

        else:
            self.row = self.row+1

    def AddOutputSpace(self, **kwargs):

        if 'id' in kwargs:
            id = kwargs["id"]
            if id in self.dynamicrows:
                self.dynamicoutputrows[id] = self.dynamicoutputrows[id] + 1
            else:
                self.dynamicoutputrows[id] = 1

        else:
            self.orow = self.orow+1

    def AddAppLauncher(self, name, filename, classname, **kwargs):

        aReg = ConnectRegistry(None, HKEY_CURRENT_USER)
        aKey = OpenKey(aReg, r"Software\Raylock LLC\Sandbox")
        location = QueryValueEx(aKey, "Home")[0]
    
        dbase = shelve.open(location+"/Config/" + filename + classname)
        dbase.close()
        
        dbase = shelve.open(location+"/Config/" + classname + "forwarding")
        dbase.close()
        

        if 'id' in kwargs:
            id = kwargs["id"]
            if id in self.dynamicrows:
                row = self.dynamicrows[id]
            else:
                row = 0
                self.dynamicrows[id] = row
            self.inputs.append(DynamicAppLauncher(name, filename, classname, row,id,**kwargs))
            self.dynamicrows[id] = self.dynamicrows[id] + 1
            if 'location' in kwargs:
                self.dynamicinputlocation = kwargs["location"].capitalize()

        else:
            self.inputs.append(AppLauncher(name, filename, classname, self.row, **kwargs))
            self.row = self.row+1
            if 'location' in kwargs:
                self.staticinputlocation = kwargs["location"].capitalize()

    def AddInput(self, name, **kwargs):

        # check for forwarding
        aReg = ConnectRegistry(None, HKEY_CURRENT_USER)
        aKey = OpenKey(aReg, r"Software\Raylock LLC\Sandbox")
        location = QueryValueEx(aKey, "Home")[0]
        if path.exists(location + "Config/" + self.appname+"forwarding.dir"):
            dbase = shelve.open(location+"Config/" + self.appname + "forwarding")

            if name in dbase:
                kwargs['default'] = dbase[name]
                
            dbase.close()
            
        if 'id' in kwargs:
            id = kwargs["id"]
            if id in self.dynamicrows:
                row = self.dynamicrows[id]
            else:
                row = 0
                self.dynamicrows[id] = row
            self.inputs.append(DynamicInput(name, row, id, **kwargs))
            self.dynamicrows[id] = self.dynamicrows[id] + 1
            if 'location' in kwargs:
                self.dynamicinputlocation = kwargs["location"].capitalize()

        else:
            self.inputs.append(Input(name, self.row, **kwargs))
            self.row = self.row+1
            if 'location' in kwargs:
                self.staticinputlocation = kwargs["location"].capitalize()
                


    def AddFilePicker(self, name, **kwargs):

        # check for forwarding
        aReg = ConnectRegistry(None, HKEY_CURRENT_USER)
        aKey = OpenKey(aReg, r"Software\Raylock LLC\Sandbox")
        location = QueryValueEx(aKey, "Home")[0]
        if path.exists(location + "Config/" + self.appname+"forwarding.dir"):
            dbase = shelve.open(location+"Config/" + self.appname + "forwarding")

            if name in dbase:
                kwargs['default'] = dbase[name]
                
            dbase.close()
                            
        if 'id' in kwargs:
            id = kwargs["id"]
            if id in self.dynamicrows:
                row = self.dynamicrows[id]
            else:
                row = 0
                self.dynamicrows[id] = row
            self.inputs.append(DynamicFilePicker(name, row, id, **kwargs))
            self.dynamicrows[id] = self.dynamicrows[id] + 1
            if 'location' in kwargs:
                self.dynamicinputlocation = kwargs["location"].capitalize()

        else:
            self.inputs.append(FilePicker(name, self.row, **kwargs))
            self.row = self.row+1
            if 'location' in kwargs:
                self.staticinputlocation = kwargs["location"].capitalize()

    def AddDirectoryPicker(self, name, **kwargs):

        # check for forwarding
        aReg = ConnectRegistry(None, HKEY_CURRENT_USER)
        aKey = OpenKey(aReg, r"Software\Raylock LLC\Sandbox")
        location = QueryValueEx(aKey, "Home")[0]
        if path.exists(location + "Config/" + self.appname+"forwarding.dir"):
            dbase = shelve.open(location+"Config/" + self.appname + "forwarding")

            if name in dbase:
                kwargs['default'] = dbase[name]
                
            dbase.close()

        if 'id' in kwargs:
            id = kwargs["id"]
            if id in self.dynamicrows:
                row = self.dynamicrows[id]
            else:
                row = 0
                self.dynamicrows[id] = row
            self.inputs.append(DynamicDirectoryPicker(name, row, id, **kwargs))
            self.dynamicrows[id] = self.dynamicrows[id] + 1
            if 'location' in kwargs:
                self.dynamicinputlocation = kwargs["location"].capitalize()

        else:
            self.inputs.append(DirectoryPicker(name, self.row, **kwargs))
            self.row = self.row+1
            if 'location' in kwargs:
                self.staticinputlocation = kwargs["location"].capitalize()

    def AddOutput(self, name, **kwargs):

        if 'id' in kwargs:
            id = kwargs["id"]
            if id in self.dynamicoutputrows:
                row = self.dynamicoutputrows[id]
            else:
                row = 0
                self.dynamicoutputrows[id] = row
            self.dynamicoutputs.append(DynamicOutput(name, row, id, **kwargs))
            self.dynamicoutputrows[id] = self.dynamicoutputrows[id] + 1
            if 'location' in kwargs:
                self.dynamicoutputlocation = kwargs["location"].capitalize()
        else:
            self.outputs.append(Output(name, self.orow,**kwargs))
            self.orow = self.orow+1
            if 'location' in kwargs:
                self.staticoutputlocation = kwargs["location"].capitalize()

    def AddCheckBox(self, name, **kwargs):

        # check for forwarding
        aReg = ConnectRegistry(None, HKEY_CURRENT_USER)
        aKey = OpenKey(aReg, r"Software\Raylock LLC\Sandbox")
        location = QueryValueEx(aKey, "Home")[0]
        if path.exists(location + "Config/" + self.appname+"forwarding.dir"):
            dbase = shelve.open(location+"Config/" + self.appname + "forwarding")

            if name in dbase:
                kwargs['default'] = dbase[name]
                
            dbase.close()
            

        if 'id' in kwargs:
            id = kwargs["id"]
            if id in self.dynamicrows:
                row = self.dynamicrows[id]
            else:
                row = 0
                self.dynamicrows[id] = row
            self.inputs.append(DynamicCheckBox(name, row, id, **kwargs))
            self.dynamicrows[id] = self.dynamicrows[id] + 1
            if 'location' in kwargs:
                self.dynamicinputlocation = kwargs["location"].capitalize()

        else:
            self.inputs.append(CheckBox(name, self.row, **kwargs))
            self.row = self.row+1
            if 'location' in kwargs:
                self.staticinputlocation = kwargs["location"].capitalize()

    def AddRadioSet(self, name, *args, **kwargs):


        # check for forwarding
        aReg = ConnectRegistry(None, HKEY_CURRENT_USER)
        aKey = OpenKey(aReg, r"Software\Raylock LLC\Sandbox")
        location = QueryValueEx(aKey, "Home")[0]
        if path.exists(location + "Config/" + self.appname+"forwarding.dir"):
            dbase = shelve.open(location+"Config/" + self.appname + "forwarding")

            if name in dbase:
                for i in range(0, len(args)):
                    if args[i] == dbase[name]:
                        kwargs['default'] = i
                
            dbase.close()


        if 'id' in kwargs:
            id = kwargs["id"]
            if id in self.dynamicrows:
                row = self.dynamicrows[id]
            else:
                row = 0
                self.dynamicrows[id] = row
            self.inputs.append(DynamicRadioSet(name, row, list(args), id, **kwargs))
            self.dynamicrows[id] = self.dynamicrows[id] + len(args)+1
            if 'location' in kwargs:
                self.dynamicinputlocation = kwargs["location"].capitalize()

        else:

            self.inputs.append(RadioSet(name, self.row, list(args), **kwargs))
            self.row = self.row+len(args)+1
            if 'location' in kwargs:
                self.staticinputlocation = kwargs["location"].capitalize()

    def AddChoice(self, name, *args, **kwargs):

        # check for forwarding
        aReg = ConnectRegistry(None, HKEY_CURRENT_USER)
        aKey = OpenKey(aReg, r"Software\Raylock LLC\Sandbox")
        location = QueryValueEx(aKey, "Home")[0]
        if path.exists(location + "Config/" + self.appname+"forwarding.dir"):
            dbase = shelve.open(location+"Config/" + self.appname + "forwarding")

            if name in dbase:
                kwargs['default'] = dbase[name]
                
            dbase.close()

        if 'id' in kwargs:
            id = kwargs["id"]
            if id in self.dynamicrows:
                row = self.dynamicrows[id]
            else:
                row = 0
                self.dynamicrows[id] = row
            self.inputs.append(DynamicChoice(name, row, list(args), id, **kwargs))
            self.dynamicrows[id] = self.dynamicrows[id] +1
            if 'location' in kwargs:
                self.dynamicinputlocation = kwargs["location"].capitalize()

        else:

            self.inputs.append(Choice(name, self.row, list(args), **kwargs))
            self.row = self.row+1
            if 'location' in kwargs:
                self.staticinputlocation = kwargs["location"].capitalize()

    def AddToggleSet(self, name, *args, **kwargs):
    
        self.inputs.append(ToggleSet(name, self.togglerow, list(args), **kwargs))
        self.togglerow = self.togglerow+len(args)+1
        if 'location' in kwargs:
            self.togglelocation = kwargs["location"].capitalize()

    def AddToggleBox(self, name, *args, **kwargs):
        
        self.inputs.append(ToggleBox(name, self.togglerow, list(args), **kwargs))
        self.togglerow = self.togglerow+1
        if 'location' in kwargs:
            self.togglelocation = kwargs["location"].capitalize()

    def AddDrawing(self, name, drawing, **kwargs):

        if "method" in kwargs:
            method = kwargs["method"]
            row = self.d_row-1
            col = 0
            if 'row' in kwargs:
                row = kwargs["row"]
            if 'column' in kwargs:
                col = kwargs["column"]
            if not "column" in kwargs and not "row" in kwargs:
                row = self.d_row
                col = self.d_column
                self.d_row = self.d_row + 1
            self.dynamicdrawings.append([method,drawing,row,col])
            self.dynamicdrawingsmap[name] = len(self.dynamicdrawings)-1


        else:
            row = self.d_row-1
            col = 0
            if 'row' in kwargs:
                row = kwargs["row"]
            if 'column' in kwargs:
                col = kwargs["column"]
            if not "column" in kwargs and not "row" in kwargs:
                row = self.d_row
                col = self.d_column
                self.d_row = self.d_row + 1

            self.drawings.append([drawing,row,col])
            self.drawingsmap[name] = len(self.drawings)-1

    def AddEmptyTable(self, name, *args, **kwargs):
        table = [name]
        for arg in args:
            table.append(arg)
        self.tables.append([table])
        self.tablesmap[name] = len(self.tables)-1

    def AddTable(self, name, data, **kwargs):
        table = []
        tableheader = [name]
        for header in data[0]:
            tableheader.append(header)
        table.append(tableheader)
        for i in range(1,len(data)):
            line = []
            for j in range(0,len(data[i])):
                line.append(str(data[i][j]))
            table.append(line)
        self.tables.append(table)
        self.tablesmap[name] = len(self.tables)-1

    def AddLineToTable(self, name, data, **kwargs):

        line = []
        for i in data:
            line.append(str(i))
        self.tables[self.tablesmap[name]].append(line)

    def AddTableData(self, name, data, **kwargs):
        table = []
        tableheader = self.tables[self.tablesmap[name]][0]
        table.append(tableheader)
        for i in range(0,len(data)):
            line = []
            for j in range(0,len(data[i])):
                line.append(str(data[i][j]))
            table.append(line)
        self.tables[self.tablesmap[name]] = table
        self.tablesmap[name] = len(self.tables)-1

    def ClearTable(self, name):
        table = []
        tableheader = self.tables[self.tablesmap[name]][0]
        table.append(tableheader)
        self.tables[self.tablesmap[name]] = table

    def AddPlot(self, name, plot, **kwargs):
        row = self.d_row-1
        col = 0
        if 'row' in kwargs:
            row = kwargs["row"]
        if 'column' in kwargs:
            col = kwargs["column"]
        if not "column" in kwargs and not "row" in kwargs:
            row = self.d_row
            col = self.d_column
            self.d_row = self.d_row + 1
        self.plots.append(plot)
        self.plotsmap[name] = len(self.plots)-1
        self.plotsalignment.append([row,col])
        if 'name' in kwargs:
            self.P[kwargs["name"]] = len(self.plots)-1

    def GetInput(self, input, **kwargs):

        aReg = ConnectRegistry(None, HKEY_CURRENT_USER)
        aKey = OpenKey(aReg, r"Software\Raylock LLC\Sandbox")
        location = QueryValueEx(aKey, "Home")[0]

        # storing for communication if child app
        if self.givendatabase != None:
            answer = self.returnedinputs.get(input, 0)
                
            try:
                answer = float(answer)
                intanswer = int(answer)
                if answer-intanswer == 0:
                    answer = intanswer
            except ValueError:
                answer = answer
        


            dbase = shelve.open(location+"/Config/" + self.givendatabase)
            dbase[input] = answer
            dbase.close()

        if 'child' not in kwargs:

            answer = self.returnedinputs.get(input, 0)
                
            try:
                answer = float(answer)
                intanswer = int(answer)
                if answer-intanswer == 0:
                    answer = intanswer
            except ValueError:
                answer = answer
                
            # check if input should be saved
            if input in self.SavedInputs:
                if self.SavedInputs[input] == True:
                    self.StoreData(input, answer)
                    
            
            
        
        else:
            # find shared database
            for item in self.inputs:
                if item.type == "AppLauncher" or item.type == "DynamicAppLauncer":
                
                    if item.classname == kwargs["child"]:
                    
                        aReg = ConnectRegistry(None, HKEY_CURRENT_USER)
                        aKey = OpenKey(aReg, r"Software\Raylock LLC\Sandbox")
                        location = QueryValueEx(aKey, "Home")[0]
            
                        dbase = shelve.open(location+"/Config/" + item.filename + item.classname)
                        answer = dbase[input]
                        dbase.close()
                        dbase = shelve.open(location+"/Config/" + item.classname + "forwarding")
                        dbase[input] = answer
                        dbase.close()
                        
                        if self.database != None:
                            dbase = shelve.open(location+"/Config/" + self.database)
                            dbase[input] = answer
                            dbase.close()
                    #return answer
                    
                
        if path.exists(location+"Config/" + self.appname + "forwarding.dat"):
            dbase = shelve.open(location+"Config/" + self.appname + "forwarding")
            dbase[input] = answer
            dbase.close()
            
            
        return answer
                    
        
            
                    
        
    def SetOutput(self, output, value, **kwargs):

        self.returnedoutputs[output] = value
        
    def SetParentInput(self, input, value, **kwargs):
        self.setinputs[input] = value
        

    def StoreData(self, name, data, **kwargs):
    
        if not self.database == None:
            aReg = ConnectRegistry(None, HKEY_CURRENT_USER)
            aKey = OpenKey(aReg, r"Software\Raylock LLC\Sandbox")
            location = QueryValueEx(aKey, "Home")[0]
        
            dbase = shelve.open(location+"/Config/" + self.database)
            dbase[name] = data

            dbase.close()
            
            
            
            
            
    def SetChildDefault(self, child, name, data, **kwargs):
    
        aReg = ConnectRegistry(None, HKEY_CURRENT_USER)
        aKey = OpenKey(aReg, r"Software\Raylock LLC\Sandbox")
        location = QueryValueEx(aKey, "Home")[0]
        
        
        childclass = None
        filename = None
        
        # prefill forwarding
        for input in self.inputs:
            if input.type == "AppLauncher" or input.type == "DynamicAppLauncer":
                if input.classname == child:
                    childclass = input.classname
                    filename = input.filename
    
        if childclass != None:
            dbase = shelve.open(location+"Config/" + childclass + "forwarding")
            dbase[name] = data
            dbase.close()
        
        # just for first run
        dbase = shelve.open(location+"Config/" + filename + childclass)
        if name not in dbase:
            dbase[name] = data
        dbase.close()

    
        
    def RetrieveData(self, name, default=None, **kwargs):

        if self.database != None:
            aReg = ConnectRegistry(None, HKEY_CURRENT_USER)
            aKey = OpenKey(aReg, r"Software\Raylock LLC\Sandbox")
            location = QueryValueEx(aKey, "Home")[0]

            dbase = shelve.open(location+"Config/" + self.database)
            
            if name in dbase:
                data = dbase[name]
            else:
                data = default
                
            if "store_default" in kwargs and data == None and default != None:
                if kwargs['store_default'] == True:
                    self.StoreData(name, default)
            
            dbase.close()
            return data
        
        return default
        
    def StoreAllInputs(self, **kwargs):
        for input in self.inputs:
            self.StoreData(input.name, self.GetInput(input.name))
            
    def GetAllInputs(self, **kwargs):
        for input in self.inputs:
            self.GetInput(input.name)
            