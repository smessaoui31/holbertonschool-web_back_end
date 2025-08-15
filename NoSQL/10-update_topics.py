#!/usr/bin/env python3
"""list all"""
from pymongo import MongoClient

def update_topics(mongo_collection, name, topics):
    """update topic"""
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
