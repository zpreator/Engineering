from math import *

class DrawCommand:

    def __init__(self, command, **kwargs):

        self.command = command
        self.text = kwargs.get('text')
        self.color = kwargs.get('color')
        self.color2 = kwargs.get('color2')
        self.x1 = kwargs.get('x1')
        self.x2 = kwargs.get('x2')
        self.x3 = kwargs.get('x3')
        self.x4 = kwargs.get('x4')
        self.x5 = kwargs.get('x5')
        self.x6 = kwargs.get('x6')
        self.x7 = kwargs.get('x7')
        self.x8 = kwargs.get('x8')
        self.points = kwargs.get('points')

class RaylockDrawing:

    def __init__(self):
        self.commands = []

    def SetSize(self, size, sizey):
        self.commands.append(DrawCommand("size", x1=size, x2=sizey))

    def SetBoundaries(self, size, sizey):
        self.commands.append(DrawCommand("boundary_size", x1=size, x2=sizey))

    def ChangePen(self, color):
        self.commands.append(DrawCommand("pen", color=color))

    def ChangeBrush(self, color):
        self.commands.append(DrawCommand("brush", color=color))

    def ChangeText(self, color):
        self.commands.append(DrawCommand("text_color", color=color))

    def ChangePenStyle(self, color):
        self.commands.append(DrawCommand("pen_style", color=color))

    def ChangeBrushStyle(self, color):
        self.commands.append(DrawCommand("brush_style", color=color))

    def DrawText(self, text, x, y, **kwargs):
        if 'pen' in kwargs:
            self.ChangePen(kwargs['pen'])
        if 'brush' in kwargs:
            self.ChangeBrush(kwargs['brush'])
        if 'textcolor' in kwargs:
            self.ChangeText(kwargs['textcolor'])
        if 'penstyle' in kwargs:
            self.ChangePenStyle(kwargs['penstyle'])
        self.commands.append(DrawCommand("text", text=text, x1=x, x2=y))

    def DrawRotatedText(self, text, x, y, angle, **kwargs):
        if 'pen' in kwargs:
            self.ChangePen(kwargs['pen'])
        if 'brush' in kwargs:
            self.ChangeBrush(kwargs['brush'])
        if 'textcolor' in kwargs:
            self.ChangeText(kwargs['textcolor'])
        if 'penstyle' in kwargs:
            self.ChangePenStyle(kwargs['penstyle'])
        self.commands.append(DrawCommand("rotatedtext", text=text, x1=x, x2=y, x3=angle))

    def DrawPic(self, text):
        self.commands.append(DrawCommand("picture", text=text))

    def DrawCircle(self, x, y, radius,**kwargs):
        if 'pen' in kwargs:
            self.ChangePen(kwargs['pen'])
        if 'brush' in kwargs:
            self.ChangeBrush(kwargs['brush'])
        if 'textcolor' in kwargs:
            self.ChangeText(kwargs['textcolor'])
        if 'penstyle' in kwargs:
            self.ChangePenStyle(kwargs['penstyle'])
        self.commands.append(DrawCommand("circle", x1=x, x2=y, x3=radius))

    def DrawEllipse(self, x, y, width, height, **kwargs):
        if 'pen' in kwargs:
            self.ChangePen(kwargs['pen'])
        if 'brush' in kwargs:
            self.ChangeBrush(kwargs['brush'])
        if 'textcolor' in kwargs:
            self.ChangeText(kwargs['textcolor'])
        if 'penstyle' in kwargs:
            self.ChangePenStyle(kwargs['penstyle'])
        self.commands.append(DrawCommand("ellipse", x1=x, x2=y, x3=width, x4=height))

    def DrawEllipticalArc(self, x, y, width, height, start, end, **kwargs):
        if 'pen' in kwargs:
            self.ChangePen(kwargs['pen'])
        if 'brush' in kwargs:
            self.ChangeBrush(kwargs['brush'])
        if 'textcolor' in kwargs:
            self.ChangeText(kwargs['textcolor'])
        if 'penstyle' in kwargs:
            self.ChangePenStyle(kwargs['penstyle'])
        self.commands.append(DrawCommand("ellipticalarc", x1=x, x2=y, x3=width, x4=height, x5=start, x6=end))

    def DrawArc(self, xs, ys, xe, ye, xc, yc, **kwargs):
        if 'pen' in kwargs:
            self.ChangePen(kwargs['pen'])
        if 'brush' in kwargs:
            self.ChangeBrush(kwargs['brush'])
        if 'textcolor' in kwargs:
            self.ChangeText(kwargs['textcolor'])
        if 'penstyle' in kwargs:
            self.ChangePenStyle(kwargs['penstyle'])
        self.commands.append(DrawCommand("arc", x1=xs, x2=ys, x3=xe, x4=ye, x5=xc, x6=yc))

    def DrawLine(self, x1, y1, x2, y2, **kwargs):
        if 'pen' in kwargs:
            self.ChangePen(kwargs['pen'])
        if 'brush' in kwargs:
            self.ChangeBrush(kwargs['brush'])
        if 'textcolor' in kwargs:
            self.ChangeText(kwargs['textcolor'])
        if 'penstyle' in kwargs:
            self.ChangePenStyle(kwargs['penstyle'])
        self.commands.append(DrawCommand("line", x1=x1, x2=y1, x3=x2, x4=y2))

    def DrawRectangle(self, x, y, width, height, **kwargs):
        if 'pen' in kwargs:
            self.ChangePen(kwargs['pen'])
        if 'brush' in kwargs:
            self.ChangeBrush(kwargs['brush'])
        if 'textcolor' in kwargs:
            self.ChangeText(kwargs['textcolor'])
        if 'penstyle' in kwargs:
            self.ChangePenStyle(kwargs['penstyle'])
        self.commands.append(DrawCommand("rectangle", x1=x, x2=y, x3=width, x4=height))

    def DrawRoundedRectangle(self, x, y, width, height, radius, **kwargs):
        if 'pen' in kwargs:
            self.ChangePen(kwargs['pen'])
        if 'brush' in kwargs:
            self.ChangeBrush(kwargs['brush'])
        if 'textcolor' in kwargs:
            self.ChangeText(kwargs['textcolor'])
        if 'penstyle' in kwargs:
            self.ChangePenStyle(kwargs['penstyle'])
        self.commands.append(DrawCommand("roundedrectangle", x1=x, x2=y, x3=width, x4=height, x5=radius))

    def DrawPolygon(self, points, **kwargs):
        if 'pen' in kwargs:
            self.ChangePen(kwargs['pen'])
        if 'brush' in kwargs:
            self.ChangeBrush(kwargs['brush'])
        if 'textcolor' in kwargs:
            self.ChangeText(kwargs['textcolor'])
        if 'penstyle' in kwargs:
            self.ChangePenStyle(kwargs['penstyle'])
        self.commands.append(DrawCommand("polygon", points=points))

    def DrawSpline(self, points, **kwargs):
        if 'pen' in kwargs:
            self.ChangePen(kwargs['pen'])
        if 'brush' in kwargs:
            self.ChangeBrush(kwargs['brush'])
        if 'textcolor' in kwargs:
            self.ChangeText(kwargs['textcolor'])
        if 'penstyle' in kwargs:
            self.ChangePenStyle(kwargs['penstyle'])
        self.commands.append(DrawCommand("spline", points=points))

    def DimensionRadius(self, letter, x, y, radius, angle, **kwargs):
        if 'pen' in kwargs:
            self.ChangePen(kwargs['pen'])
        if 'brush' in kwargs:
            self.ChangeBrush(kwargs['brush'])
        if 'textcolor' in kwargs:
            self.ChangeText(kwargs['textcolor'])
        if 'penstyle' in kwargs:
            self.ChangePenStyle(kwargs['penstyle'])
        x5 = 0
        x6 = 0
        if 'wigglex' in kwargs:
            x5 = kwargs['wigglex']
        if 'wiggley' in kwargs:
            x6 = kwargs['wiggley']
        self.commands.append(DrawCommand("radial_dimension", text=letter, x1=x, x2=y, x3=radius, x4=angle, x5=x5,
                                         x6=x6))

    def DrawVRDimension(self, letter, x0, y0, x1, y1, **kwargs):
        if 'pen' in kwargs:
            self.ChangePen(kwargs['pen'])
        if 'brush' in kwargs:
            self.ChangeBrush(kwargs['brush'])
        if 'textcolor' in kwargs:
            self.ChangeText(kwargs['textcolor'])
        if 'penstyle' in kwargs:
            self.ChangePenStyle(kwargs['penstyle'])
        x5 = 0
        x6 = 0
        x7 = 20
        if 'wigglex' in kwargs:
            x5 = kwargs['wigglex']
        if 'wiggley' in kwargs:
            x6 = kwargs['wiggley']
        if 'length' in kwargs:
            x7 = kwargs['length']
        self.commands.append(DrawCommand("vertical_right_dimension", text=letter, x1=x0, x2=y0, x3=x1, x4=y1,
                                         x5=x5, x6=x6, x7=x7))

    def DrawVLDimension(self, letter, x0, y0, x1, y1, **kwargs):
        if 'pen' in kwargs:
            self.ChangePen(kwargs['pen'])
        if 'brush' in kwargs:
            self.ChangeBrush(kwargs['brush'])
        if 'textcolor' in kwargs:
            self.ChangeText(kwargs['textcolor'])
        if 'penstyle' in kwargs:
            self.ChangePenStyle(kwargs['penstyle'])
        x5 = 0
        x6 = 0
        x7 = 20
        if 'wigglex' in kwargs:
            x5 = kwargs['wigglex']
        if 'wiggley' in kwargs:
            x6 = kwargs['wiggley']
        if 'length' in kwargs:
            x7 = kwargs['length']
        self.commands.append(DrawCommand("vertical_left_dimension", text=letter, x1=x0, x2=y0, x3=x1, x4=y1,
                                         x5=x5, x6=x6, x7=x7))

    def DrawHTDimension(self, letter, x0, y0, x1, y1, **kwargs):
        if 'pen' in kwargs:
            self.ChangePen(kwargs['pen'])
        if 'brush' in kwargs:
            self.ChangeBrush(kwargs['brush'])
        if 'textcolor' in kwargs:
            self.ChangeText(kwargs['textcolor'])
        if 'penstyle' in kwargs:
            self.ChangePenStyle(kwargs['penstyle'])
        x5 = 0
        x6 = 0
        x7 = 20
        if 'wigglex' in kwargs:
            x5 = kwargs['wigglex']
        if 'wiggley' in kwargs:
            x6 = kwargs['wiggley']
        if 'length' in kwargs:
            x7 = kwargs['length']
        self.commands.append(DrawCommand("horizontal_top_dimension", text=letter, x1=x0, x2=y0, x3=x1, x4=y1,
                                         x5=x5, x6=x6, x7=x7))

    def DrawHBDimension(self, letter, x0, y0, x1, y1, **kwargs):
        if 'pen' in kwargs:
            self.ChangePen(kwargs['pen'])
        if 'brush' in kwargs:
            self.ChangeBrush(kwargs['brush'])
        if 'textcolor' in kwargs:
            self.ChangeText(kwargs['textcolor'])
        if 'penstyle' in kwargs:
            self.ChangePenStyle(kwargs['penstyle'])
        x5 = 0
        x6 = 0
        x7 = 20
        if 'wigglex' in kwargs:
            x5 = kwargs['wigglex']
        if 'wiggley' in kwargs:
            x6 = kwargs['wiggley']
        if 'length' in kwargs:
            x7 = kwargs['length']
        self.commands.append(DrawCommand("horizontal_bottom_dimension", text=letter, x1=x0, x2=y0, x3=x1, x4=y1,
                                         x5=x5, x6=x6, x7=x7))

    def DrawArrow(self, xs, ys, xf, yf, size, **kwargs):
        if 'pen' in kwargs:
            self.ChangePen(kwargs['pen'])
        if 'brush' in kwargs:
            self.ChangeBrush(kwargs['brush'])
        if 'textcolor' in kwargs:
            self.ChangeText(kwargs['textcolor'])
        if 'penstyle' in kwargs:
            self.ChangePenStyle(kwargs['penstyle'])
        self.commands.append(DrawCommand("arrow", x1=xs, x2=ys, x3=xf, x4=yf, x5=size))

    def DrawInternalPressure(self, letter, x, y, radius, **kwargs):
        if 'pen' in kwargs:
            self.ChangePen(kwargs['pen'])
        if 'brush' in kwargs:
            self.ChangeBrush(kwargs['brush'])
        if 'textcolor' in kwargs:
            self.ChangeText(kwargs['textcolor'])
        if 'penstyle' in kwargs:
            self.ChangePenStyle(kwargs['penstyle'])
        x4 = 10
        x5 = 0.0
        x6 = 360
        x7 = 0
        x8 = 0
        if 'length' in kwargs:
            x4 = kwargs['length']
        if 'startAngle' in kwargs:
            x5 = kwargs['startAngle']
        if 'endAngle' in kwargs:
            x6 = kwargs['endAngle']
        if 'xt' in kwargs:
            x7 = kwargs['xt']
        if 'yt' in kwargs:
            x8 = kwargs['yt']
        self.commands.append(DrawCommand("internal_pressure", text=letter, x1=x, x2=y, x3=radius, x4=x4,
                                         x5=x5, x6=x6, x7=x7, x8=x8))

    def DrawExternalPressure(self, letter, x, y, radius, **kwargs):
        if 'pen' in kwargs:
            self.ChangePen(kwargs['pen'])
        if 'brush' in kwargs:
            self.ChangeBrush(kwargs['brush'])
        if 'textcolor' in kwargs:
            self.ChangeText(kwargs['textcolor'])
        if 'penstyle' in kwargs:
            self.ChangePenStyle(kwargs['penstyle'])
        x4 = 10
        x5 = 0.0
        x6 = 360
        x7 = 0
        x8 = 0
        if 'length' in kwargs:
            x4 = kwargs['length']
        if 'startAngle' in kwargs:
            x5 = kwargs['startAngle']
        if 'endAngle' in kwargs:
            x6 = kwargs['endAngle']
        if 'xt' in kwargs:
            x7 = kwargs['xt']
        if 'yt' in kwargs:
            x8 = kwargs['yt']
        self.commands.append(DrawCommand("external_pressure", text=letter, x1=x, x2=y, x3=radius, x4=x4,
                                         x5=x5, x6=x6, x7=x7, x8=x8))