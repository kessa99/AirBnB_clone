#!/usr/bin/python3
"""
initializes the models folder.
"""
from models.engine.FileStorage import FileStorage


storage = FileStorage()
storage.reload()
