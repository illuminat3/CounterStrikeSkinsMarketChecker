from abc import ABC, abstractmethod
from Datatypes.WeaponSkin import WeaponSkin

class IScraperService(ABC):
    def __init__(self):
        self.weapon = WeaponSkin() 
    
    @abstractmethod
    def set_weapon(weapon: WeaponSkin):
        pass
    