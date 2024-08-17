from Enums.weapon_type import WeaponType
from Enums.weapon_wear import WeaponWear

class WeaponSkin:
    def __init__(self):
        pass

    def __init__(self, weapon_type: WeaponType = WeaponType.ANY, weapon_name: str = "", weapon_wear: WeaponWear = WeaponWear.ALL, pattern: int = 0):
        self.weapon_type = weapon_type
        self.weapon_name = weapon_name
        self.weapon_wear = weapon_wear
        self.pattern = pattern