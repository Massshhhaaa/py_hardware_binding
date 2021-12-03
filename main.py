import os

def authenticate(func):
    def wrapper():
        from src.check_license import checkLicense
        
        WORKDIR = os.path.dirname(__file__)
        path_to_license = os.path.join(WORKDIR, 'store/license.txt')

        if checkLicense(path_to_license):
            func()
            
    return wrapper
