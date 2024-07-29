# __init__.py
import importlib
import pkgutil

# Import the functions directly into the package namespace
for loader, module_name, is_pkg in pkgutil.walk_packages(__path__):
    _module = importlib.import_module(f"{__name__}.{module_name}")
   #_module = loader.find_module(module_name).load_module(module_name)
    for name in dir(_module):
        if not name.startswith('__'):
            globals()[name] = getattr(_module, name)


import sys, os, warnings
sys.path.insert(0, os.path.abspath(os.path.split(os.path.realpath(__file__))[0])) 
warnings.simplefilter(action='ignore')
