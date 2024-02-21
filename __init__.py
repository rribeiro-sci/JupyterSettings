import pkgutil

__all__ = []
for loader, module_name, is_pkg in pkgutil.walk_packages(__path__):
    __all__.append(module_name)
    _module = loader.find_module(module_name).load_module(module_name)
    globals()[module_name] = _module


import sys, os, warnings
sys.path.insert(0, os.path.abspath(os.path.split(os.path.realpath(__file__))[0])) 
warnings.simplefilter(action='ignore')