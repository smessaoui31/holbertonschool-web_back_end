#!/usr/bin/env python3
"""
12-log_stats.py
Script providing statistics about Nginx logs stored in MongoDB.
"""
from pymongo import MongoClient


def main():
    """
    Provides statistics about Nginx logs stored in MongoDB.
    """
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx

    cursor = nginx_collection.find({'method': 'GET'})
    get_count = len(list(cursor))

    cursor = nginx_collection.find({'method': 'POST'})
    post_count = len(list(cursor))

    cursor = nginx_collection.find({'method': 'PUT'})
    put_count = len(list(cursor))

    cursor = nginx_collection.find({'method': 'PATCH'})
    patch_count = len(list(cursor))

    cursor = nginx_collection.find({'method': 'DELETE'})
    delete_count = len(list(cursor))

    cursor = nginx_collection.find({'path': '/status'})
    status = len(list(cursor))

    cursor = nginx_collection.find()
    total = len(list(cursor))

    print('{} logs'.format(total))
    print('Methods:')
    print('\tmethod GET: {}'.format(get_count))
    print('\tmethod POST: {}'.format(post_count))
    print('\tmethod PUT: {}'.format(put_count))
    print('\tmethod PATCH: {}'.format(patch_count))
    print('\tmethod DELETE: {}'.format(delete_count))
    print('{} status check'.format(status))


if __name__ == "__main__":
    main()
