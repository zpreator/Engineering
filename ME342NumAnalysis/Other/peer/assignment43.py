from scipy.interpolate import RegularGridInterpolator
def f(x, y, z):
    return 2 * x**3 + 3 * y**2 - z
x = np.linspace(1, 4, 11)
y = np.linspace(4, 7, 22)
z = np.linspace(7, 9, 33)
data = f(*np.meshgrid(x, y, z, indexing='ij', sparse=True))
my_interpolating_function = RegularGridInterpolator((x, y, z), data)
(x,y,z) = (2.1, 6.2, 8.3) and (3.3, 5.2, 7.1):
pts = np.array([[2.1, 6.2, 8.3], [3.3, 5.2, 7.1]])
my_interpolating_function(pts)
array([ 125.80469388,  146.30069388])
[f(2.1, 6.2, 8.3), f(3.3, 5.2, 7.1)].