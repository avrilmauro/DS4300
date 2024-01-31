import redis

def lr(redis, key):
    cmd = redis.lrange(key, 0, -1)

r = redis.Redis(host='localhost', port=6379, decode_responses=True)

r.lpush('Tweets', 123)
r.sadd('User', 1)
#
# print(lr(r, "Tweets"))

s = {0, 1 , 2}

# for i in s:
#     print(i)

user_key = 'Tweets:' + str(1)
r.lpush(user_key, 55)

print(r.lrange(user_key, 0, -1))
