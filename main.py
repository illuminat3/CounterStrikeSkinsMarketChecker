# Imports
from Services.PackageService import *

# Global
packageService = PackageInstaller()



def main() -> None:
    packageService.install_all()



if __name__ == "__main__":
    main()