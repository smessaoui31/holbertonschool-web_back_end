#!/usr/bin/env python3
"""list all"""
from pymongo import MongoClient


def schools_by_topic(mongo_collection, topic):
    """return list of school having specific topic"""
    return list(mongo_collection.find({"topics": topic}))
