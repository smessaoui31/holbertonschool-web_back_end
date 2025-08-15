#!/usr/bin/env python3
"""
8-all.py
Module containing the function list_all.
"""


def list_all(mongo_collection):
    """
    Lists all documents in a collection.
    """
    cursor = mongo_collection.find()
    return cursor
