Pm = 140000 # Pa
Dp = 44 # Cm
Dm = 7 # cm
wp = 71 # rad/s
wm = 112 # rad/s
Vdotp = 2.23 #m^3/s
Vdotm = 8.89 # m^3/s
Pp = Pm*(Dp/Dm)**2*(wp/wm)**2
print(Pp)

Vp = 48
num = 1.29
nup = 1.64
lp = 4
lm = 1
Vm = Vp*(num/nup)*(lp/lm)
print(Vm)