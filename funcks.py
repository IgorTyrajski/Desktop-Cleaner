import os
import globals as glb

def IsCorrect(file):
    if file.is_file():
        name, ext = os.path.splitext(file.name)
        ext = ext.lower().lstrip('.')
        return ext in glb.typesToRemove