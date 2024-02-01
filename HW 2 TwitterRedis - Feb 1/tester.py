import redis
import pprint as pp

def lr(redis, key):
    cmd = redis.lrange(key, 0, -1)

r = redis.Redis(host='localhost', port=6379, decode_responses=True)

r.lpush('Tweets', 123)
r.sadd('User', 1)
#
# print(lr(r, "Tweets"))


s = {0, 1, 2}

# for i in s:
#     print(i)

l = ['Ill post the complete test files shortly!', 'Hello World', 'Ill post the complete test files shortly!', 'Hello World']
pp.pprint(l)

