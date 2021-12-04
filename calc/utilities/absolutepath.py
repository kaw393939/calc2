"""Absolute path code"""
from pathlib import Path
#This is how we get the correct path"
def absolutepath(filepath):
    """absolute path reference"""
    relative = Path(filepath)
    return relative.absolute()
