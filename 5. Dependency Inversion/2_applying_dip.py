"""
DIP sugggests us to refer to abstract interfaces instead. 
Let's do a necessary changees and see which posibilities it opens for us
"""
from abc import ABC, abstractmethod


# CHANGE: we created an abstract class which will represent basic device controlled by switcher
class SwitchableDevice(ABC):
    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass


# LightBulb is a switchable device, so let's make it obvios in the code by inheriting base class
# As you can see in this example, we can now add more devices of the Switchable type
class LightBulb(SwitchableDevice):
    """Simple light bulb. Can be turned ON or OFF"""

    def turn_on(self):
        print("Lumos! LightBulb is on")

    def turn_off(self):
        print("Ah, it's dark again. LightBulb is off")


class SelfieRingLight(SwitchableDevice):
    def turn_on(self):
        print("ON: We're now read to take some selfies")

    def turn_off(self):
        print("OFF: Enough for today. Bye")


class ElectricPowerSwitcher:

    # CHANGE: we can now specify that this class controls only SwitchableDevice type of devices
    # it allows us to pass any Switchable object and call same method thanks to Dependency Injection
    def __init__(self, connected_device: SwitchableDevice) -> None:
        self.connected_device = connected_device
        self.turned_on = False

    def press_btn(self):
        if self.turned_on:
            # We do not care whether connected_device is a LightBulb or not
            # We KNOW for sure that this object has turn_on/turn_off methods and can call them:
            self.connected_device.turn_off()
            self.turned_on = False
        else:
            self.connected_device.turn_on()
            self.turned_on = True
