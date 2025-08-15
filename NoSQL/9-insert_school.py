#!/usr/bin/env python3
"""
9-insert_school.py
Module containing the function insert_school.
"""


def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document in a collection.
    """
    items = {key: value for key, value in kwargs.items()}
    new = mongo_collection.insert_one(items)
    return new.inserted_id
