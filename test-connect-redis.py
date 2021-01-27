import sys
import redis
import time

failedRedisOps = 0
totalTestsToRun = 1000
host='localhost'
port=6379
ssl=False

if len(sys.argv) >= 3:
    host = sys.argv[1]
    port = int(sys.argv[2])
if len(sys.argv) >= 4:
    ssl = True if sys.argv[3].lower() == 'true' else False
totalTestsToRun = int(sys.argv[4]) if len(sys.argv) >= 5 else 1000
password = sys.argv[5] if len(sys.argv) == 6 else None

for testNumber in range(1, totalTestsToRun + 1):
    try:
        redisServer = redis.Redis(host=host, port=6379, ssl=ssl, password=password, socket_timeout=0.1)
        redisServer.set(testNumber, testNumber)
        redisServer.get(testNumber)
        redisServer.delete(testNumber)
        redisServer = None
    except:
        failedRedisOps += 1
        time.sleep(0.1)
    finally:
        redisServer = None

print(f'Number of Tests Ran: {totalTestsToRun}')
print(f'A total of: {failedRedisOps} failed connection to perform operation')