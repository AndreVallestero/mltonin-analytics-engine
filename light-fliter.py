'''
getforegroudnd

create gammaManager
    set gamma
        create gama ramp
        nativemethods

    create gama ramp:
    3 arrays of 256 ushorts, each one a the specified color from 0 to 255
    
'''
from ctypes import windll, Structure, c_ushort

class Ramp(Structure):
    _fields_ = [("red", c_ushort * 256),
                ("green", c_ushort * 256),
                ("blue", c_ushort * 256)]

user32 = windll.user32
gdi32 = windll.gdi32

hWndFg = user32.GetForegroundWindow()
dcFg = user32.GetDC(hWndFg)
gammaRamp = Ramp()
for i in range(256):
    gammaRamp.red[i] = 255
    gammaRamp.green[i] = 127
    gammaRamp.blue[i] = 127
#gdi.SetDeviceGammaRamp(dcFg, 


