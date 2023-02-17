"""
Dependency Inversion: high-level modules should depend on abstractions rather than concrete implementations

In other words: 
- avoid multiple inheritance
- rely on stable abstractions
- don't refer to volatile concrete classes - refer to abstract interfaces instead
"""


class LightBulb:
    """Simple light bulb. Can be turned ON or OFF"""

    def turn_on(self):
        pass

    def turn_off(self):
        pass


class ElectricPowerSwitcher:
    """One button power switcher.

    Changes the state of controlled device after pressing the button
    """

    # do you see it? We rely on a concrete class (LightBulb) and violate DIP
    # what if we want to use other device? There might some issues
    def __init__(self, connected_device: LightBulb) -> None:
        self.connected_device = connected_device
        self.turned_on = False

    def press_btn(self):
        if self.turned_on:
            self.connected_device.turn_off()
            self.turned_on = False
        else:
            self.connected_device.turn_on()
            self.turned_on = True
