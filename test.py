import vgamepad as vg
from time import sleep

gamepad = vg.VX360Gamepad()
xbtn = vg.XUSB_BUTTON
sleep(5)

def test():
    gamepad.press_button(xbtn.XUSB_GAMEPAD_A)
    gamepad.update()
    sleep(5)
    gamepad.release_button(xbtn.XUSB_GAMEPAD_A)
    gamepad.update()
    sleep(1)

def takeoff():
    pass

def land():
    pass

def idle():
    pass

def up():
    pass

def down():
    pass

def left():
    pass

def right():
    pass

def forward():
    pass

def backward():
    pass

def trothle():
    pass

print("Starting test")
test()
print("Test complete")
sleep(3)
print("Starting test")
test()
print("Test complete")
sleep(3)
