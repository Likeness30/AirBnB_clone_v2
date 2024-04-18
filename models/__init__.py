#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from models.engine.file_storage import FileStorage
from lib import get_model, model


storage = FileStorage()
get_model()
storage.reload()
