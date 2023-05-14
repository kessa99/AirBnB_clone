#!/usr/bin/python3
"""
initializes the models folder
"""
from models.engine.file_storage import file_storage


storage = file_storage()
storage.reload()
