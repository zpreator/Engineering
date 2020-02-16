from SandboxLibrary.AppUtility import *


def ClearDrawing(parent, drawing):
    HelperGetDrawing(parent, drawing).commands = []

def HelperGetDrawing(parent, drawing):
    if drawing in parent.app.drawingsmap:
        return parent.app.drawings[parent.app.drawingsmap[drawing]][0]
    elif drawing in parent.app.dynamicdrawingsmap:
        return parent.app.dynamicdrawings[parent.app.dynamicdrawingsmap[drawing]][1]

def ReturnDrawing(parent, drawing):
    return HelperGetDrawing(parent, drawing)   

def DrawCircle(parent, drawing, x, y, radius, **kwargs):
    HelperGetDrawing(parent, drawing).DrawCircle(x, y, radius, **kwargs)
 
 
def SetDrawingSize(parent, drawing, size, *args):
    if len(args) > 0:
        HelperGetDrawing(parent, drawing).SetSize(size, args[0])
    else:
        HelperGetDrawing(parent, drawing).SetSize(size, 0)
    
def SetBoundaries(parent, drawing, size, *args):
    if len(args) > 0:
        HelperGetDrawing(parent, drawing).SetBoundaries(size, args[0])
    else:
        HelperGetDrawing(parent, drawing).SetBoundaries(size, 0)
 
def ChangePen(parent, drawing, color):
    HelperGetDrawing(parent, drawing).ChangePen(color)
    
def ChangeBrush(parent, drawing, color):
    HelperGetDrawing(parent, drawing).ChangeBrush(color)
    
def ChangeText(parent, drawing, color):
    HelperGetDrawing(parent, drawing).ChangeText(color)
    
def ChangePenStyle(parent, drawing, style):
    HelperGetDrawing(parent, drawing).ChangePenStyle(style)
    
def ChangeBrushStyle(parent, drawing, style):
    HelperGetDrawing(parent, drawing).ChangeBrushStyle(style)
 
def DrawText(parent, drawing, text, x, y, **kwargs):
    HelperGetDrawing(parent, drawing).DrawText(text, x, y, **kwargs)

def DrawRotatedText(parent, drawing, text, x, y, angle, **kwargs):
    HelperGetDrawing(parent, drawing).DrawRotatedText(text, x, y, angle, **kwargs)
 
def DrawPic(parent, drawing, pic):
    HelperGetDrawing(parent, drawing).DrawPic(pic)
    
def DrawEllipse(parent, drawing, x, y, width, height, **kwargs):
    HelperGetDrawing(parent, drawing).DrawEllipse(x, y, width, height, **kwargs)

def DrawEllipticalArc(parent, drawing, x, y, width, height, start, end, **kwargs):
    HelperGetDrawing(parent, drawing).DrawEllipticalArc(x, y, width, height, start, end, **kwargs)
    
def DrawArc(parent, drawing, xs, ys, xe, ye, xc, yc, **kwargs):
    HelperGetDrawing(parent, drawing).DrawArc(xs, ys, xe, ye, xc, yc, **kwargs)

def DrawLine(parent, drawing, x1, y1, x2, y2, **kwargs):
    HelperGetDrawing(parent, drawing).DrawLine( x1, y1, x2, y2, **kwargs)

def DrawRectangle(parent, drawing, x, y, width, height, **kwargs):
    HelperGetDrawing(parent, drawing).DrawRectangle(x, y, width, height, **kwargs)

def DrawRoundedRectangle(parent, drawing, x, y, width, height, radius,  **kwargs):
    HelperGetDrawing(parent, drawing).DrawRoundedRectangle(x, y, width, height, radius, **kwargs)
    
def DrawPolygon(parent, drawing, points, **kwargs):
    HelperGetDrawing(parent, drawing).DrawPolygon(points, **kwargs)

def DrawSpline(parent, drawing, points, **kwargs):
    HelperGetDrawing(parent, drawing).DrawSpline(points, **kwargs)

def DimensionRadius(parent, drawing, letter, x, y, radius, angle, **kwargs):
    HelperGetDrawing(parent, drawing).DimensionRadius(letter, x, y, radius, angle, **kwargs)
 
def DrawVRDimension(parent, drawing, letter, x0, y0, x1, y1, **kwargs):
    HelperGetDrawing(parent, drawing).DrawVRDimension(letter, x0, y0, x1, y1, **kwargs)
 
def DrawVLDimension(parent, drawing, letter, x0, y0, x1, y1, **kwargs):
    HelperGetDrawing(parent, drawing).DrawVLDimension(letter, x0, y0, x1, y1, **kwargs)
    
def DrawHTDimension(parent, drawing, letter, x0, y0, x1, y1, **kwargs):
    HelperGetDrawing(parent, drawing).DrawHTDimension(letter, x0, y0, x1, y1, **kwargs)

def DrawHBDimension(parent, drawing, letter, x0, y0, x1, y1, **kwargs):
    HelperGetDrawing(parent, drawing).DrawHBDimension(letter, x0, y0, x1, y1, **kwargs)
    
def DrawArrow(parent, drawing, xs, ys, xf, yf, size, **kwargs):
    HelperGetDrawing(parent, drawing).DrawArrow(xs, ys, xf, yf, size, **kwargs)
    
def DrawInternalPressure(parent, drawing, letter, x, y, radius, **kwargs):
    HelperGetDrawing(parent, drawing).DrawInternalPressure(letter, x, y, radius, **kwargs)
    
def DrawExternalPressure(parent, drawing, letter, x, y, radius, **kwargs):
    HelperGetDrawing(parent, drawing).DrawExternalPressure(letter, x, y, radius, **kwargs)
 
 

def AddSeries(parent, plot, data, color, name=" ", type="line", **kwargs):
    plot = parent.app.plotsmap[plot]
    if type.lower()=="line":
        parent.app.plots[plot].AddLineSeries(data, color, name=name, **kwargs)
    elif type.lower()=="scatter":
        parent.app.plots[plot].AddScatterSeries(data, color, name=name, **kwargs)
    else:
        parent.app.plots[plot].AddAreaSeries(data, color, name=name, **kwargs)

def SetSize(parent, plot, width, height):
    plot = parent.app.plotsmap[plot]
    parent.app.plots[plot].SetSize(width, height)
    
def SetTitle(parent, plot, title):
    plot = parent.app.plotsmap[plot]
    parent.app.plots[plot].SetTitle(title)
    
def SetTitleSize(parent, plot, size):
    plot = parent.app.plotsmap[plot]
    parent.app.plots[plot].SetTitleSize(size)
    
def SetXDecimalPoints(parent, plot, num):
    plot = parent.app.plotsmap[plot]
    parent.app.plots[plot].SetXDecimalPoints(num)
    
def SetYDecimalPoints(parent, plot, num):
    plot = parent.app.plotsmap[plot]
    parent.app.plots[plot].SetYDecimalPoints(num)

def SetXAxisTitle(parent, plot, title):
    plot = parent.app.plotsmap[plot]
    parent.app.plots[plot].SetXAxisTitle(title)

def SetYAxisTitle(parent, plot, title):
    plot = parent.app.plotsmap[plot]
    parent.app.plots[plot].SetYAxisTitle(title)

def ShowBorder(parent, plot, show):
    plot = parent.app.plotsmap[plot]
    parent.app.plots[plot].ShowBorder(show)
    
def ShowLegend(parent, plot, show):
    plot = parent.app.plotsmap[plot]
    parent.app.plots[plot].ShowLegend(show)

def AddPoint(parent, plot, x, y, color, **kwargs):
    plot = parent.app.plotsmap[plot]
    parent.app.plots[plot].AddPoint(x, y, color, **kwargs)
    
def SetXScientific(parent, plot):
    plot = parent.app.plotsmap[plot]
    parent.app.plots[plot].SetXScientific()
    
def SetYScientific(parent, plot):
    plot = parent.app.plotsmap[plot]
    parent.app.plots[plot].SetYScientific()

def AddCircle(parent, plot, x, y, r, color, **kwargs):
    plot = parent.app.plotsmap[plot]
    parent.app.plots[plot].AddCircle(x, y, r, color, **kwargs)
    
def AddLine(parent, plot, x1, y1, x2, y2, color, **kwargs):
    plot = parent.app.plotsmap[plot]
    parent.app.plots[plot].AddLine(x1, y1, x2, y2, color, **kwargs)
    
def ClearData(parent, plot):
    plot = parent.app.plotsmap[plot]
    parent.app.plots[plot].ClearData()
    
def LockRatio(parent, plot, lock):
    plot = parent.app.plotsmap[plot]
    parent.app.plots[plot].LockRatio(lock)
    
def ShowXTitle(parent, plot, show):
    plot = parent.app.plotsmap[plot]
    parent.app.plots[plot].ShowXTitle(show)
    
def ShowYTitle(parent, plot, show):
    plot = parent.app.plotsmap[plot]
    parent.app.plots[plot].ShowYTitle(show)

def SetXAutoBoundaries(parent, plot):
    plot = parent.app.plotsmap[plot]
    parent.app.plots[plot].SetXAutoBoundaries()
    
def SetYAutoBoundaries(parent, plot):
    plot = parent.app.plotsmap[plot]
    parent.app.plots[plot].SetYAutoBoundaries()
    
def SetXBoundaries(parent, plot, mi, ma):
    plot = parent.app.plotsmap[plot]
    parent.app.plots[plot].SetXBoundaries(mi, ma)
    
def SetYBoundaries(parent, plot, mi, ma):
    plot = parent.app.plotsmap[plot]
    parent.app.plots[plot].SetYBoundaries(mi, ma)
    
def SetXSymmetry(parent, plot):
    plot = parent.app.plotsmap[plot]
    parent.app.plots[plot].SetXSymmetry()
    
def SetYSymmetry(parent, plot):
    plot = parent.app.plotsmap[plot]
    parent.app.plots[plot].SetYSymmetry()
    
def SetChartBackgroundColor(parent, plot, color):
    plot = parent.app.plotsmap[plot]
    parent.app.plots[plot].SetChartBackgroundColor(color)
    
def SetBackgroundColor(parent, plot, color):
    plot = parent.app.plotsmap[plot]
    parent.app.plots[plot].SetBackgroundColor(color)
    
def SetBorderColor(parent, plot, color):
    plot = parent.app.plotsmap[plot]
    parent.app.plots[plot].SetBorderColor(color)
    
def SetChartBorderColor(parent, plot, color):
    plot = parent.app.plotsmap[plot]
    parent.app.plots[plot].SetChartBorderColor(color)

def SetTextColor(parent, plot, color):
    plot = parent.app.plotsmap[plot]
    parent.app.plots[plot].SetTextColor(color)
    
def SetAxisColor(parent, plot, color):
    plot = parent.app.plotsmap[plot]
    parent.app.plots[plot].SetAxisColor(color)
    
def SetGridColor(parent, plot, color):
    plot = parent.app.plotsmap[plot]
    parent.app.plots[plot].SetGridColor(color)
    
def SetTickColor(parent, plot, color):
    plot = parent.app.plotsmap[plot]
    parent.app.plots[plot].SetTickColor(color)
    


def GetInput(parent, input,**kwargs):
    return parent.app.GetInput(input, **kwargs)

def StartAppUtility(parentclass, **kwargs):
    parentclass.app = AppUtility(**kwargs)
    parentclass.app.appname = parentclass.__class__.__name__

def AddInput(parent, name, **kwargs):
    parent.app.AddInput(name, **kwargs)
    
def AddInputSpace(parent, **kwargs):
    parent.app.AddInputSpace(**kwargs)
    
def AddPlot(parent, name, **kwargs):
    plot = RaylockPlot()
    plot.SetTitle(name)
    parent.app.AddPlot(name, plot, **kwargs)
    
def AddOutput(parent, name, **kwargs):
    parent.app.AddOutput(name, **kwargs)
    
def AddRadioSet(parent, name, *args, **kwargs):
    parent.app.AddRadioSet(name, *args, **kwargs)
    
def AddEmptyTable(parent, name, *args, **kwargs):
    parent.app.AddEmptyTable(name, *args, **kwargs)
    
def AddToggleSet(parent, name, *args, **kwargs):
    parent.app.AddToggleSet(name, *args, **kwargs)
    
def AddToggleBox(parent, name, *args, **kwargs):
    parent.app.AddToggleBox(name, *args, **kwargs)
    
def AddLineToTable(parent, name, data, **kwargs):
    parent.app.AddLineToTable(name, data, **kwargs)
    
def SetStaticInputLocation(parent, location):
    parent.app.SetStaticInputLocation(location)

def SetDynamicInputLocation(parent, location):
    parent.app.SetDynamicInputLocation(location)
    
def SetStaticOutputLocation(parent, location):
    parent.app.SetStaticOutputLocation(location)
    
def SetDynamicOutputLocation(parent, location):
    parent.app.SetDynamicOutputLocation(location)
    
def SetToggleLocation(parent, location):
    parent.app.SetToggleLocation(location)
    
def AddOutputSpace(parent, **kwargs):
    parent.app.AddOutputSpace(**kwargs)
    
def AddAppLauncher(parent, name, filename, classname, **kwargs):
    parent.app.AddAppLauncher(name, filename, classname, **kwargs)
    
def AddFilePicker(parent, name, **kwargs):
    parent.app.AddFilePicker(name, **kwargs)
    
def AddDirectoryPicker(parent, name, **kwargs):
    parent.app.AddDirectoryPicker(name, **kwargs)
    
def AddCheckBox(parent, name, **kwargs):
    parent.app.AddCheckBox(name, **kwargs)
    
def AddChoice(parent, name, *args, **kwargs):
    parent.app.AddChoice(name, *args, **kwargs)
    
def AddDrawing(parent, name, **kwargs):
    parent.app.AddDrawing(name, RaylockDrawing(), **kwargs)

def AddPicture(parent, name, **kwargs):
    parent.app.AddDrawing(name, RaylockDrawing(), **kwargs)
    DrawPic(parent, name, name)
    
def AddTable(parent, name, data, **kwargs):
    parent.app.AddTable(name, data, **kwargs)
    
def AddTableData(parent, name, data, **kwargs):
    parent.app.AddTableData(name, data, **kwargs)
    
def ClearTable(parent, name):
    parent.app.ClearTable(name)
    
def SetOutput(parent, output, value, **kwargs):
    parent.app.SetOutput(output, value, **kwargs)
    
def SetParentInput(parent, input, value, **kwargs):
    parent.app.SetParentInput(input, value, **kwargs)
    
def StoreData(parent, name, data, **kwargs):
    parent.app.StoreData(name, data, **kwargs)
    
def SetChildDefault(parent, child, name, data, **kwargs):
    parent.app.SetChildDefault(child, name, data, **kwargs)
 
def StoreGlobalData(database, name, data, **kwargs):

    aReg = ConnectRegistry(None, HKEY_CURRENT_USER)
    aKey = OpenKey(aReg, r"Software\Raylock LLC\Sandbox")
    location = QueryValueEx(aKey, "Home")[0]

    dbase = shelve.open(location+"/Config/" + database)
    dbase[name] = data
    dbase.close()
 
def GetAllInputs(parent, **kwargs):
    parent.app.GetAllInputs(**kwargs)
    
def StoreAllInputs(parent, **kwargs):
    parent.app.StoreAllInputs(**kwargs)
    
def RetrieveData(parent, name, default=None,**kwargs):
    return parent.app.RetrieveData(name, default, **kwargs)

def RetrieveGlobalData(database, name, default=None, **kwargs):

    aReg = ConnectRegistry(None, HKEY_CURRENT_USER)
    aKey = OpenKey(aReg, r"Software\Raylock LLC\Sandbox")
    location = QueryValueEx(aKey, "Home")[0]

    dbase = shelve.open(location+"/Config/" + database)
    if name in dbase:
        data = dbase[name]
    else:
        data = default
        dbase[name] = data
    dbase.close()
    
    return data
    

def GetTheme():

    aReg = ConnectRegistry(None, HKEY_CURRENT_USER)
    aKey = OpenKey(aReg, r"Software\Raylock LLC\Sandbox")
    theme = QueryValueEx(aKey, "Theme")[0]
    return theme

def GetHomeDirectory():

    aReg = ConnectRegistry(None, HKEY_CURRENT_USER)
    aKey = OpenKey(aReg, r"Software\Raylock LLC\Sandbox")
    location = QueryValueEx(aKey, "Home")[0]
    return location
    
def GetAppDirectory():

    location = GetHomeDirectory()
    return location + "Apps\\"
    
def GetOutputDirectory():

    location = GetHomeDirectory()
    return location + "Output\\"

def GetResourcesDirectory():

    location = GetHomeDirectory()
    return location + "Resources\\"