from SandboxLibrary.Raylock import RaylockDialogs, RaylockDrawing, RaylockPlot, AppUtility
import xlsxwriter
import os
from winreg import *
import shelve

def GetInputFormats(workbook):

        formats = {}

        # Title format
        t1 = workbook.add_format()
        t1.set_bold()
        t1.set_align('center')
        t1.set_align('vcenter')
        t1.set_shrink()
        t1.set_border(5)
        t1.set_bg_color('#DA9694')

        # Title format
        t2 = workbook.add_format()
        t2.set_bold()
        t2.set_align('center')
        t2.set_align('vcenter')
        t2.set_shrink()
        t2.set_border(5)
        t2.set_bg_color('#95B3D7')

        # Title format
        t3 = workbook.add_format()
        t3.set_bold()
        t3.set_align('center')
        t3.set_align('vcenter')
        t3.set_shrink()
        t3.set_border(5)
        t3.set_bg_color('#C4BD97')

        # Title format
        t4 = workbook.add_format()
        t4.set_bold()
        t4.set_align('center')
        t4.set_align('vcenter')
        t4.set_shrink()
        t4.set_border(5)
        t4.set_bg_color('#C4D79B')

        # Title format
        t5 = workbook.add_format()
        t5.set_bold()
        t5.set_align('center')
        t5.set_align('vcenter')
        t5.set_shrink()
        t5.set_border(5)
        t5.set_bg_color('#B1A0C7')

        # Title format
        t6 = workbook.add_format()
        t6.set_bold()
        t6.set_align('center')
        t6.set_align('vcenter')
        t6.set_shrink()
        t6.set_border(5)
        t6.set_bg_color('#92CDDC')

        # Input name 
        f1 = workbook.add_format()
        f1.set_align('left')
        f1.set_border(1)

        # Input name 
        f2 = workbook.add_format()
        f2.set_align('right')
        f2.set_border(1)
        f2.set_left(5)
        

        # Input value
        f3 = workbook.add_format()
        f3.set_align('right')
        f3.set_border(1)
        f3.set_bg_color('#E4DFEC')

        # Input unit 
        f4 = workbook.add_format()
        f4.set_align('left')
        f4.set_border(1)
        f4.set_right(5)

        # Input value
        f5 = workbook.add_format()
        f5.set_top(5)

        # Input value
        f6 = workbook.add_format()
        f6.set_align('left')
        f6.set_border(1)
        f6.set_right(5)
        f6.set_bg_color('#E4DFEC')


        formats['Title1'] = t1
        formats['Title2'] = t2
        formats['Title3'] = t3
        formats['Title4'] = t4
        formats['Title5'] = t5
        formats['Title6'] = t6
        formats['DUnit'] = f1
        formats['Label'] = f2
        formats['Value'] = f3
        formats['Unit'] = f4
        formats['Bottom'] = f5
        formats['TValue'] = f6

        return formats

def function1(parent, worksheet, title, type, ii, firstcolumn, inputformats, titleformat):
    
    found = False
    for i in range(0, len(parent.app.inputs)):
        if parent.app.inputs[i].type == type:
            found = True

    if found:
        worksheet.merge_range(ii+1,firstcolumn,ii+1,firstcolumn+2, title, inputformats[titleformat])

        i = 0
        while i < len(parent.app.inputs):

            if(parent.app.inputs[i].type == type):

                if hasattr(parent.app.inputs[i], "label"):
                    worksheet.write(ii+2,firstcolumn,parent.app.inputs[i].label, inputformats["Label"])
                else:
                    worksheet.write(ii+2,firstcolumn,parent.app.inputs[i].name, inputformats["Label"])

                worksheet.write(ii+2,firstcolumn+1,parent.app.returnedinputs[parent.app.inputs[i].name], inputformats["Value"])
                
                if hasattr(parent.app.inputs[i], "unit"):
                    worksheet.write(ii+2,firstcolumn+2,parent.app.inputs[i].unit, inputformats["Unit"])
                else:
                    worksheet.write(ii+2,firstcolumn+2,"", inputformats["Unit"])

                if hasattr(parent.app.inputs[i], "tip"):
                    if(parent.app.inputs[i].tip != ""):
                        worksheet.write_comment(ii+2,firstcolumn,parent.app.inputs[i].tip)

                ii+=1
            
            i+=1

        ii+=2
        worksheet.write(ii,firstcolumn,"", inputformats["Bottom"])
        worksheet.write(ii,firstcolumn+1,"", inputformats["Bottom"])
        worksheet.write(ii,firstcolumn+2,"", inputformats["Bottom"])

    return ii

def function2(parent, worksheet, title, type, ii, firstcolumn, inputformats, titleformat):
    
    found = False
    for i in range(0, len(parent.app.inputs)):
        if parent.app.inputs[i].type == type:
            found = True

    if found:
        worksheet.merge_range(ii+1,firstcolumn,ii+1,firstcolumn+3, title, inputformats[titleformat])

        i = 0
        while i < len(parent.app.inputs):

            if(parent.app.inputs[i].type == type):

                if hasattr(parent.app.inputs[i], "label"):
                    worksheet.write(ii+2,firstcolumn,parent.app.inputs[i].label, inputformats["Label"])
                else:
                    worksheet.write(ii+2,firstcolumn,parent.app.inputs[i].name, inputformats["Label"])

                worksheet.write(ii+2,firstcolumn+1,parent.app.returnedinputs[parent.app.inputs[i].name], inputformats["Value"])
                
                if hasattr(parent.app.inputs[i], "unit"):
                    worksheet.write(ii+2,firstcolumn+2,parent.app.inputs[i].unit, inputformats["DUnit"])
                else:
                    worksheet.write(ii+2,firstcolumn+2,"", inputformats["DUnit"])

                if hasattr(parent.app.inputs[i], "tip"):
                    if(parent.app.inputs[i].tip != ""):
                        worksheet.write_comment(ii+2,firstcolumn,parent.app.inputs[i].tip)

                worksheet.write(ii+2,firstcolumn+3,parent.app.inputs[i].id, inputformats["Unit"])
                
                ii+=1


            
            i+=1

        ii+=2
        worksheet.write(ii,firstcolumn,"", inputformats["Bottom"])
        worksheet.write(ii,firstcolumn+1,"", inputformats["Bottom"])
        worksheet.write(ii,firstcolumn+2,"", inputformats["Bottom"])
        worksheet.write(ii,firstcolumn+3,"", inputformats["Bottom"])

    return ii

def function3(parent, worksheet, title, type, ii, firstcolumn, inputformats, titleformat):
    
    found = False
    for i in range(0, len(parent.app.inputs)):
        if parent.app.inputs[i].type == type:
            found = True

    if found:
        worksheet.merge_range(ii+1,firstcolumn,ii+1,firstcolumn+1, title, inputformats[titleformat])

        i = 0
        while i < len(parent.app.inputs):

            if(parent.app.inputs[i].type == type):

                if hasattr(parent.app.inputs[i], "label"):
                    worksheet.write(ii+2,firstcolumn,parent.app.inputs[i].label, inputformats["Label"])
                else:
                    worksheet.write(ii+2,firstcolumn,parent.app.inputs[i].name, inputformats["Label"])

                worksheet.write(ii+2,firstcolumn+1,parent.app.returnedinputs[parent.app.inputs[i].name], inputformats["TValue"])
                

                if hasattr(parent.app.inputs[i], "tip"):
                    if(parent.app.inputs[i].tip != ""):
                        worksheet.write_comment(ii+2,firstcolumn,parent.app.inputs[i].tip)
                
                ii+=1


            
            i+=1

        ii+=2
        worksheet.write(ii,firstcolumn,"", inputformats["Bottom"])
        worksheet.write(ii,firstcolumn+1,"", inputformats["Bottom"])

    return ii

def function4(parent, worksheet, title, type, ii, firstcolumn, inputformats, titleformat):
    
    found = False
    for i in range(0, len(parent.app.outputs)):
        if parent.app.outputs[i].type == type:
            found = True

    if found:
        worksheet.merge_range(ii+1,firstcolumn,ii+1,firstcolumn+2, title, inputformats[titleformat])

        i = 0
        while i < len(parent.app.outputs):

            if(parent.app.outputs[i].type == type):

                if hasattr(parent.app.outputs[i], "label"):
                    worksheet.write(ii+2,firstcolumn,parent.app.outputs[i].label, inputformats["Label"])
                else:
                    worksheet.write(ii+2,firstcolumn,parent.app.outputs[i].name, inputformats["Label"])

                if parent.app.outputs[i].name in parent.app.returnedoutputs:
                    worksheet.write(ii+2,firstcolumn+1,parent.app.returnedoutputs[parent.app.outputs[i].name], inputformats["Value"])
                else:
                    worksheet.write(ii+2,firstcolumn+1,"", inputformats["Value"])
                
                if hasattr(parent.app.outputs[i], "unit"):
                    worksheet.write(ii+2,firstcolumn+2,parent.app.outputs[i].unit, inputformats["Unit"])
                else:
                    worksheet.write(ii+2,firstcolumn+2,"", inputformats["Unit"])

                if hasattr(parent.app.outputs[i], "tip"):
                    if(parent.app.outputs[i].tip != ""):
                        worksheet.write_comment(ii+2,firstcolumn,parent.app.outputs[i].tip)

                ii+=1
            
            i+=1

        ii+=2
        worksheet.write(ii,firstcolumn,"", inputformats["Bottom"])
        worksheet.write(ii,firstcolumn+1,"", inputformats["Bottom"])
        worksheet.write(ii,firstcolumn+2,"", inputformats["Bottom"])

    return ii

def function5(parent, worksheet, title, type, ii, firstcolumn, inputformats, titleformat):
    
    found = False
    for i in range(0, len(parent.app.dynamicoutputs)):
        if parent.app.dynamicoutputs[i].type == type:
            found = True

    if found:
        worksheet.merge_range(ii+1,firstcolumn,ii+1,firstcolumn+3, title, inputformats[titleformat])

        i = 0
        while i < len(parent.app.dynamicoutputs):

            if(parent.app.dynamicoutputs[i].type == type):

                if hasattr(parent.app.dynamicoutputs[i], "label"):
                    worksheet.write(ii+2,firstcolumn,parent.app.dynamicoutputs[i].label, inputformats["Label"])
                else:
                    worksheet.write(ii+2,firstcolumn,parent.app.dynamicoutputs[i].name, inputformats["Label"])

                if parent.app.dynamicoutputs[i].name in parent.app.returnedoutputs:
                    worksheet.write(ii+2,firstcolumn+1,parent.app.returnedoutputs[parent.app.dynamicoutputs[i].name], inputformats["Value"])
                else:
                    worksheet.write(ii+2,firstcolumn+1,"", inputformats["Value"])
                
                if hasattr(parent.app.dynamicoutputs[i], "unit"):
                    worksheet.write(ii+2,firstcolumn+2,parent.app.dynamicoutputs[i].unit, inputformats["DUnit"])
                else:
                    worksheet.write(ii+2,firstcolumn+2,"", inputformats["DUnit"])

                if hasattr(parent.app.dynamicoutputs[i], "tip"):
                    if(parent.app.dynamicoutputs[i].tip != ""):
                        worksheet.write_comment(ii+2,firstcolumn,parent.app.dynamicoutputs[i].tip)
                
                worksheet.write(ii+2,firstcolumn+3,parent.app.dynamicoutputs[i].id, inputformats["Unit"])

                ii+=1


            
            i+=1

        ii+=2
        worksheet.write(ii,firstcolumn,"", inputformats["Bottom"])
        worksheet.write(ii,firstcolumn+1,"", inputformats["Bottom"])
        worksheet.write(ii,firstcolumn+2,"", inputformats["Bottom"])
        worksheet.write(ii,firstcolumn+3,"", inputformats["Bottom"])

    return ii

def function6(parent, worksheet, title, ii, firstcolumn, inputformats, titleformat):
    
    if len(parent.app.returnvariables) > 0:
        worksheet.merge_range(ii+1,firstcolumn,ii+1,firstcolumn+1, title, inputformats[titleformat])
        
        i = 0
        for key in parent.app.returnvariables:
            worksheet.write(ii+2,firstcolumn,key, inputformats["Label"])
            worksheet.write(ii+2,firstcolumn+1,parent.app.returnvariables[key], inputformats["Unit"])
            ii+=1
        ii+=2
        worksheet.write(ii,firstcolumn,"", inputformats["Bottom"])
        worksheet.write(ii,firstcolumn+1,"", inputformats["Bottom"])
        return ii
        
    else:
        return ii

def function7(parent, worksheet, title, ii, firstcolumn, inputformats, titleformat):
    
    if parent.app.database != None:
        aReg = ConnectRegistry(None, HKEY_CURRENT_USER)
        aKey = OpenKey(aReg, r"Software\Raylock LLC\Sandbox")
        location = QueryValueEx(aKey, "Home")[0]
    
        dbase = shelve.open(location+"Config/" + parent.app.database)
        
        worksheet.merge_range(ii+1,firstcolumn,ii+1,firstcolumn+1, title, inputformats[titleformat])
        used = False
        for key in dbase:
            
            found = False
            for input in parent.app.inputs:
                if input.name == key:
                    found = True

            
            if found == False:
                used = True
                worksheet.write(ii+2,firstcolumn,key, inputformats["Label"])
                worksheet.write(ii+2,firstcolumn+1,dbase[key], inputformats["TValue"])
                ii+=1
        if used == True:
            ii+=2
            worksheet.write(ii,firstcolumn,"", inputformats["Bottom"])
            worksheet.write(ii,firstcolumn+1,"", inputformats["Bottom"])
        
        dbase.close()
        
    return ii

def documentplots(parent, workbook):

    for plot in parent.app.plots:
        if(len(plot.data) > 0):
            datasheet = workbook.add_worksheet(plot.title + "data")
            datasheet.protect()
            datasheet.hide()
            chartsheet = workbook.add_chartsheet(plot.title)
            chart = workbook.add_chart({'type': 'scatter', 'subtype':'straight_with_markers'})
            chart.set_style(2)
            chart.set_title ({'name': plot.title})
            if(plot.showLegend == "False"):
                chart.set_legend({'none': True})
            chart.set_x_axis({
                                'name': plot.xtitle, 
                                'major_gridlines': {'visible': True},
                                'label_position': "low",
                                'line' : {"width": 2},
                                #'max' : plot.xMaxValue,
                                #'min' : plot.xMinValue,

                            })
            chart.set_y_axis({
                                'name': plot.ytitle, 
                                'major_gridlines': {'visible': True},
                                'label_position': "low",
                                'line' : {"width": 2},
                                #'max' : plot.yMaxValue,
                                #'min' : plot.yMinValue,

                            })
            
            column = 0

            for series in plot.data:
                
                for i in range(0, len(series.data)):
                    
                    datasheet.write(i, column, series.data[i][0])
                    datasheet.write(i, column+1, series.data[i][1])

                if series.type == "line" or series.type == "area":
                    chart.add_series({
                        'name':       series.name,
                        'categories': [plot.title + "data", 0,column, len(series.data), column],
                        'values': [plot.title + "data", 0,column+1, len(series.data), column+1],
                        'line' : {'width': 1},
                        'marker' : {"type": 'none'}
                    })
                elif series.type == "scatter":
                    chart.add_series({
                        'name':       series.name,
                        'categories': [plot.title + "data", 0,column, len(series.data), column],
                        'values': [plot.title + "data", 0,column+1, len(series.data), column+1],
                        'line' : {'none': True},
                        'marker' : {"type": 'circle', 'size':5}
                    })

                elif series.type == "point":
                    chart.add_series({
                        'name':       series.name,
                        'categories': [plot.title + "data", 0,column, len(series.data), column],
                        'values': [plot.title + "data", 0,column+1, len(series.data), column+1],
                        'line' : {'none': True},
                        'marker' : {"type": 'circle', 'size':5},
                        'data_labels': {'series_name': True},
                    })

                elif series.type == "circle":
                    chart.add_series({
                        'name':       series.name,
                        'categories': [plot.title + "data", 0,column, len(series.data), column],
                        'values': [plot.title + "data", 0,column+1, len(series.data), column+1],
                        'line' : {'width': 2},
                        'marker' : {"type": 'none'}
                    })


                column+=2

            #chart.set_plotarea({'gradient': {'colors': ['#F2DCDB', 'white']}})
            chartsheet.set_tab_color("#307A17")
            chartsheet.set_chart(chart)

def documenttables(parent, workbook):

    firstrow = 2
    firstcolumn = 1

    # Title format
    t1 = workbook.add_format()
    t1.set_bold()
    t1.set_align('center')
    t1.set_align('vcenter')
    t1.set_shrink()
    t1.set_border(2)
    t1.set_bg_color("#538ED5")

    # Header format
    h1 = workbook.add_format()
    h1.set_bold()
    h1.set_align('center')
    h1.set_align('vcenter')
    h1.set_shrink()
    h1.set_border(2)
    h1.set_bottom(5)
    h1.set_bg_color("#DA9694")

    # regular 
    reg = workbook.add_format()
    reg.set_align('center')
    reg.set_border(1)

    # regular color
    regc = workbook.add_format()
    regc.set_align('center')
    regc.set_border(1)
    regc.set_bg_color("#C5D9F1")

    # left 
    left = workbook.add_format()
    left.set_align('center')
    left.set_border(1)
    left.set_left(2)

    # left color
    leftc = workbook.add_format()
    leftc.set_align('center')
    leftc.set_border(1)
    leftc.set_left(2)
    leftc.set_bg_color("#C5D9F1")

    # right 
    right = workbook.add_format()
    right.set_align('center')
    right.set_border(1)
    right.set_right(2)

    # right color
    rightc = workbook.add_format()
    rightc.set_align('center')
    rightc.set_border(1)
    rightc.set_right(2)
    rightc.set_bg_color("#C5D9F1")

    # bottom 
    bottom = workbook.add_format()
    bottom.set_align('center')
    bottom.set_top(2)
    
    for table in parent.app.tables:
        worksheet = workbook.add_worksheet(table[0][0])
        worksheet.set_tab_color("#538ED5")
        worksheet.merge_range(firstrow-1, firstcolumn, firstrow-1, firstcolumn + len(table[0])-2, table[0][0], t1)
        for i in range(0, len(table)+1):
            for j in range(0, len(table[0])-1):
                if i == 0:
                    worksheet.write(i+firstrow,j+firstcolumn,table[i][j+1], h1)
                elif i == len(table):
                    worksheet.write(i+firstrow,j+firstcolumn,"", bottom)
                else:
                    if i % 2 != 0:
                        if j == 0:
                            worksheet.write(i+firstrow,j+firstcolumn,table[i][j], left)
                        elif j == len(table[0])-2:
                            worksheet.write(i+firstrow,j+firstcolumn,table[i][j], right)
                        else:
                            worksheet.write(i+firstrow,j+firstcolumn,table[i][j], reg)
                    else:
                        if j == 0:
                            worksheet.write(i+firstrow,j+firstcolumn,table[i][j], leftc)
                        elif j == len(table[0])-2:
                            worksheet.write(i+firstrow,j+firstcolumn,table[i][j], rightc)
                        else:
                            worksheet.write(i+firstrow,j+firstcolumn,table[i][j], regc)

def documentfiguresplots(parent, workbook):
    
    aReg = ConnectRegistry(None, HKEY_CURRENT_USER)
    aKey = OpenKey(aReg, r"Software\Raylock LLC\Sandbox")
    home = QueryValueEx(aKey, "Home")[0]
    
    for key in parent.app.plotsmap:
        
        mapped = parent.app.plotsmap[key]
        file = home + "Output\\" +str(mapped) + "plot.png"
        
        file = str(file)
        
        worksheet = workbook.add_worksheet(key+"-sb")
        worksheet.set_tab_color("#16505C")
        worksheet.insert_image('B2', file)

def documentfigures(parent, workbook):
    
    aReg = ConnectRegistry(None, HKEY_CURRENT_USER)
    aKey = OpenKey(aReg, r"Software\Raylock LLC\Sandbox")
    home = QueryValueEx(aKey, "Home")[0]
    
    for key in parent.app.drawingsmap:
        
        file = home + "Output\\" + str(parent.app.drawingsmap[key]) + "stat.png"
        
        file = str(file)
        
        worksheet = workbook.add_worksheet(key)
        worksheet.set_tab_color("#16365C")
        worksheet.insert_image('B2', file)
        
    for key in parent.app.dynamicdrawingsmap:
        
        mapped = parent.app.dynamicdrawingsmap[key]
        file = home + "Output\\" + parent.app.dynamicdrawings[mapped][0] + "dyn.png"
        
        file = str(file)
        
        worksheet = workbook.add_worksheet(key)
        worksheet.set_tab_color("#3E165C")
        worksheet.insert_image('B2', file)
      
def cleanfigures(parent):
    
    aReg = ConnectRegistry(None, HKEY_CURRENT_USER)
    aKey = OpenKey(aReg, r"Software\Raylock LLC\Sandbox")
    home = QueryValueEx(aKey, "Home")[0]
    
    i = 0
    for key in parent.app.drawingsmap:
        
        file = home + "Output\\" + str(parent.app.drawingsmap[key]) + "stat.png"
        
        file = str(file)
        
        os.remove(file)
        
    for key in parent.app.dynamicdrawingsmap:
        
        mapped = parent.app.dynamicdrawingsmap[key]
        file = home + "Output\\" + parent.app.dynamicdrawings[mapped][0] + "dyn.png"
        
        file = str(file)
        
        os.remove(file)
        
    for key in parent.app.plotsmap:
        
        mapped = parent.app.plotsmap[key]
        file = home + "Output\\" +str(mapped) + "plot.png"
        
        file = str(file)
        
        os.remove(file)
        
def AddExcelPrinting(parent, **kwargs):

    #print(parent.app.returnvariables)
    if hasattr(parent, "solve"):
        solve = getattr(parent, "solve")
        if callable(solve):
            parent.solve()
    import tkinter as tk
    from tkinter import filedialog
    root = tk.Tk()
    root.iconbitmap(default='C:\\Program Files (x86)\\Raylock\\Sandbox\\py-components\\main_logo.ico')
    root.withdraw()
    f = filedialog.asksaveasfilename(initialdir='.', title='Save File', defaultextension=".xlsx", filetypes=[("Excel","*.xlsx")])
    if f is None:
        return
    aReg = ConnectRegistry(None, HKEY_CURRENT_USER)
    aKey = OpenKey(aReg, r"Software\Raylock LLC\Sandbox")
    First = QueryValueEx(aKey, "First_Name")[0]
    Last = QueryValueEx(aKey, "Last_Name")[0]

    #workbook = xlsxwriter.Workbook("C:/Users/jhoff/Desktop/test.xlsx", {"strings_to_numbers":True})
    workbook = xlsxwriter.Workbook(f, {"strings_to_numbers":True})

    workbook.set_properties({
        'title':    "Engineer's Sandbox Output",
        'subject':  'Calculation Output',
        'author':   First + " " + Last,
        'manager':  '',
        'company':  'Raylock LLC',
        'category': "Engineer's Sandbox Output",
        'keywords': 'Sandbox',
        #'created':  datetime.date(2019, 1, 1),
        'comments': "Created with Engineer's Sandbox and XlsxWriter"})
    workbook.set_custom_property('Checked by',       '')
    inputsheet = workbook.add_worksheet("Inputs")
    inputsheet.set_tab_color("#DA9694")
    outputsheet = workbook.add_worksheet("Outputs")
    outputsheet.set_tab_color("#B1A0C7")

    firstcolumn = 1
    ii = 0

    inputsheet.set_column(firstcolumn,firstcolumn, 20)
    inputsheet.set_column(firstcolumn+1,firstcolumn+1, 20)
    inputsheet.set_column(firstcolumn+4,firstcolumn+4, 20)
    inputsheet.set_column(firstcolumn+5,firstcolumn+5, 20)
    outputsheet.set_column(firstcolumn,firstcolumn, 20)
    outputsheet.set_column(firstcolumn+1,firstcolumn+1, 20)
    
    inputformats = GetInputFormats(workbook)

    ###############################################################################################################
    ## Static inputs
    ###############################################################################################################

    ii = function1(parent, inputsheet, "Inputs", "Input", ii, firstcolumn, inputformats, 'Title1')
    ii = function1(parent, inputsheet, "CheckBoxes", "CheckBox", ii, firstcolumn, inputformats, 'Title1')
    ii = function1(parent, inputsheet, "RadioSets", "RadioSet", ii, firstcolumn, inputformats, 'Title1')
    ii = function1(parent, inputsheet, "Choices", "Choice", ii, firstcolumn, inputformats, 'Title1')
    ii = function1(parent, inputsheet, "Files", "FilePicker", ii, firstcolumn, inputformats, 'Title1')
    ii = function1(parent, inputsheet, "Directories", "DirectoryPicker", ii, firstcolumn, inputformats, 'Title1')

    ###############################################################################################################
    ## Dynmic inputs
    ###############################################################################################################
    ii = function2(parent, inputsheet, "Dynamic Inputs", "DynamicInput", ii, firstcolumn, inputformats, 'Title4')
    ii = function2(parent, inputsheet, "Dynamic CheckBoxes", "DynamicCheckBox", ii, firstcolumn, inputformats, 'Title4')
    ii = function2(parent, inputsheet, "Dynamic RadioSets", "DynamicRadioSet", ii, firstcolumn, inputformats, 'Title4')
    ii = function2(parent, inputsheet, "Dynamic Choices", "DynamicChoice", ii, firstcolumn, inputformats, 'Title4')
    ii = function2(parent, inputsheet, "Dynamic Files", "DynamicFilePicker", ii, firstcolumn, inputformats, 'Title4')
    ii = function2(parent, inputsheet, "Dynamic Directories", "DynamicDirectoryPicker", ii, firstcolumn, inputformats, 'Title4')
    
    ii = function6(parent, inputsheet, "Variables", ii, firstcolumn, inputformats, 'Title5')

    ###############################################################################################################
    ## Toggle Sets
    ###############################################################################################################
    ii = function3(parent, inputsheet, "ToggleSets", "ToggleSet", 0, firstcolumn+4, inputformats, 'Title2')
    ii = function3(parent, inputsheet, "ToggleBoxes", "ToggleBox", ii, firstcolumn+4, inputformats, 'Title2')
    ii = function7(parent, inputsheet, "Database Items", ii, firstcolumn+4, inputformats, 'Title2')

    ###############################################################################################################
    ## Static Outputs
    ###############################################################################################################

    ii = function4(parent, outputsheet, "Outputs", "output", 0, firstcolumn, inputformats, 'Title5')

    ###############################################################################################################
    ## Dynamic Outputs
    ###############################################################################################################

    ii = function5(parent, outputsheet, "Dynamic Outputs", "dynamicoutput", ii, firstcolumn, inputformats, 'Title1')
    
    documentfigures(parent, workbook)
    documenttables(parent, workbook)
    documentplots(parent, workbook)
    documentfiguresplots(parent, workbook)

    workbook.close()  
    cleanfigures(parent)