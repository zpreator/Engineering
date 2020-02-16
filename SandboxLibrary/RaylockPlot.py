from math import *

class Series:

    def __init__(self, data):

        self.data = data
        self.type = "line"
        self.name = " "
        self.color = ""
        self.fill = ""
        self.thickness = 2
        self.x1 = 0
        self.x2 = 0
        self.x3 = 0

class RaylockPlot:

    def __init__(self):

        self.data = []

        self.title = "plot"
        self.xtitle = "x axis"
        self.ytitle = "y axis"
        self.xformat = "decimal"
        self.yformat = "decimal"

        self.lockRatio = "False"
        self.showBorder = "True"
        self.showLegend = "True"
        self.showXTitle = "True"
        self.showYTitle = "True"
        self.xFixedBounds = "False"
        self.yFixedBounds = "False"

        self.xMinValue = -1
        self.xMaxValue = 1
        self.yMinValue = -1
        self.yMaxValue = 1
        self.xMax = 0
        self.xMin = 0
        self.yMax = 0
        self.yMin = 0
        self.width = 300
        self.height = 300

        self.xDecimalPoints = 2
        self.yDecimalPoints = 2

        self.chartBackgroundColor = "ChartBackground"
        self.backgroundColor = "PlotBackground"
        self.borderColor = "PlotBorder"
        self.chartBorderColor = "ChartBorder"
        self.textColor = "PlotText"
        self.axisColor = "Axis"
        self.gridColor = "Grid"
        self.tickColor = "Tick"

        self.titleSize = 20

    def SetXScientific(self):
        self.xformat = "scientific"

    def SetYScientific(self):
        self.yformat = "scientific"

    def SetSize(self, width, height):
        self.width = width
        self.height = height

    def AddLineSeries(self, data, color, name = " ", **kwargs):

        series = Series(data)
        series.type = "line"
        series.color = color
        series.name = name
        if "thickness" in kwargs:
            series.thickness = kwargs['thickness']
        else:
            series.thickness = 2
        self.data.append(series)

    def AddScatterSeries(self, data, color, name = " ", **kwargs):
        series = Series(data)
        series.type = "scatter"
        series.color = color
        series.name = name
        if "thickness" in kwargs:
            series.thickness = kwargs["thickness"]
        else:
            series.thickness = 5
        self.data.append(series)

    def AddAreaSeries(self, data, color, name = " "):
        series = Series(data)
        series.type = "area"
        series.color = color
        series.name = name
        self.data.append(series)

    def AddCircle(self, x, y, r, color, **kwargs):

        points = []
        size = 1000
        for i in range(0, size):
            X = -r + (i * 2 * r / size) + x
            Y = sqrt(r**2 - ((-r + (i * 2 * r / size))**2)) + y
            points.append([X, Y])

        for i in range(size, size*2):
            X = r - ((i-1000) * 2 * r / size) + x
            Y = -sqrt(r**2 - ((r - ((i-1000) * 2 * r / size))**2)) + y
            points.append([X, Y])

        series = Series(points)
        series.type = "circle"
        series.color = color
        if "fill_color" in kwargs:
            series.fill = kwargs["fill_color"]
        else:
            series.fill = "Transparent"
        series.x1 = x
        series.x2 = y
        series.x3 = r
        if "thickness" in kwargs:
            series.thickness = kwargs["thickness"]
        else:
            series.thickness = 1
        self.data.append(series)

    def AddLine(self, x1, y1, x2, y2, color, **kwargs):
        data = [[x1, y1], [x2, y2]]


        if "thickness" in kwargs:
            self.AddLineSeries(data, color, thickness=kwargs['thickness'])
        else:
            self.AddLineSeries(data, color, thickness=1)

    def AddPoint(self, x, y, color, **kwargs):
        data = [[x, y]]

        series = Series(data)
        series.type = "point"
        series.color = color
        if "label" in kwargs:
            series.name = kwargs['label']
        else:
            series.name = ""
        series.thickness = 3
        self.data.append(series)

    def ClearData(self):
        self.data = []

    def SetTitle(self, title):
        self.title = title

    def SetTitleSize(self, size):
        self.titleSize = size

    def LockRatio(self, lock):
        if lock == True:
            self.lockRatio = "True"
        else:
            self.lockRatio = "False"

    def ShowBorder(self, show):
        if show == True:
            self.showBorder = "True"
        else:
            self.showBorder = "False"

    def ShowLegend(self, show):
        if show == True:
            self.showLegend = "True"
        else:
            self.showLegend = "False"

    def ShowXTitle(self, show):
        if show == True:
            self.showXTitle = "True"
        else:
            self.showXTitle = "False"

    def ShowYTitle(self, show):
        if show == True:
            self.showYTitle = "True"
        else:
            self.showYTitle = "False"

    def SetXAutoBoundaries(self):
        self.xFixedBounds = "False"

    def SetYAutoBoundaries(self):
        self.yFixedBounds = "False"

    def SetXBoundaries(self, mi, ma):
        self.xMinValue = mi
        self.xMaxValue = ma
        self.xFixedBounds = "True"

    def SetYBoundaries(self, mi, ma):
        self.yMinValue = mi
        self.yMaxValue = ma
        self.yFixedBounds = "True"

    def SetXAxisTitle(self, title):
        self.xtitle = title

    def SetYAxisTitle(self, title):
        self.ytitle = title

    def SetXDecimalPoints(self, num):
        self.xDecimalPoints = num

    def SetYDecimalPoints(self, num):
        self.yDecimalPoints = num

    def SetXSymmetry(self):

        if abs(self.xMinValue) >= abs(self.xMaxValue):
            self.SetXBoundaries(self.xMinValue, abs(self.xMinValue))
        else:
            self.SetXBoundaries(-abs(self.xMaxValue), abs(self.xMaxValue))

    def SetYSymmetry(self):

        if abs(self.yMinValue) >= abs(self.yMaxValue):
            self.SetYBoundaries(self.yMinValue, abs(self.yMinValue))
        else:
            self.SetYBoundaries(-abs(self.yMaxValue), abs(self.yMaxValue))

    def SetChartBackgroundColor(self, color):
        self.chartBackgroundColor = color

    def SetBackgroundColor(self, color):
        self.backgroundColor = color

    def SetBorderColor(self, color):
        self.borderColor = color

    def SetChartBorderColor(self, color):
        self.chartBorderColor = color

    def SetTextColor(self, color):
        self.textColor = color

    def SetAxisColor(self, color):
        self.axisColor = color

    def SetGridColor(self, color):
        self.gridColor = color

    def SetTickColor(self, color):
        self.tickColor = color
