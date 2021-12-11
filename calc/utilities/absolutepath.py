from pathlib import Path

def absolutepath(filepath):
    """for absolute path"""
    relative = Path(filepath)
    return relative.absolute()
