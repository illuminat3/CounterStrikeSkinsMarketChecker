import subprocess
import sys

class PackageInstaller:
    def __init__(self):
        self.libraries = [
            
        ]

    def install_all(self):
        for library in self.libraries:
            self.install_specific(library)

    def install_specific(self, library_name):
        try:
            __import__(library_name)
            print(f"'{library_name}' is already installed.")
        except ImportError:
            print(f"Installing '{library_name}'...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", library_name])
