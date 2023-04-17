from flask import Flask
from redis import Redis
import socket

app = Flask(__name__)
redis = Redis(host='redis',port=6379)
@app.route('/')
def hello():
  count = redis.incr('hitpoints')
  return "Hello from host.<p>HOstname is: " + socket.gethostname() + '\n I count {} times'.format(count)
if __name__ == "__main__":
  app.run(host="0.0.0.0", port=8000, debug=True)
