from ctypes import cdll
import ctypes
import os

lib = cdll.LoadLibrary('./shared/greet.so')

lib.greet.argtypes = [ctypes.c_char_p]
lib.greet.restype = ctypes.c_char_p

def greet(name: str):
    return lib.greet(name.encode()).decode()

print(greet("Hishmana"))