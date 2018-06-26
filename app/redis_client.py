
import redis

redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)


# Design
"""
session_storage_design = {
    'brittany@gmail.ca': {
        'sessionId': '1234',
        'timeout': '12',
        'information': 'bluh bluh'
    },
}
"""