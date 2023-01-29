"""import requests
from flask import *
from flask_cors import CORS
app=Flask(__name__)
CORS(app)
@app.route('/',methods=['POST'])
def get():
    parameters={'clear_authorized':'Yes'}
    r=requests.post('http://localhost:8080/echo',data=parameters)
    print(r.text)
    return {"answer":"hello there"}"""

"""
from flask import *
#from flask_socketio import SocketIO, emit
from flask_cors import CORS
import asyncio
import websockets



app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
#socketio = SocketIO(app,cors_allowed_origins='*')
CORS(app)

@app.route('/')
def index():
    async def hello():
        async with websockets.connect("ws://localhost:8765") as websocket:
            await websocket.send("Hello world!")
            await websocket.recv()

    asyncio.run(hello())
    return render_template('base.html')

@socketio.on('my event3')
def do(data):
    emit('connect1','Hello world23')

@socketio.on('connect')
def test_connect(data):
    print("connected")
    emit('my response', {'data': 'Connected'})
@socketio.on('my event')
def test_connect1(data):
    print(data)
    emit('connect1','Hello world')

if __name__ == '__main__':
    socketio.run(app,host='0.0.0.0',allow_unsafe_werkzeug=True)
import asyncio
import websockets

async def echo(websocket):
    async for message in websocket:
        print(message)
        await websocket.send(message)

async def main():
    async with websockets.serve(echo, "localhost", 8765):
        await asyncio.Future()  # run forever

asyncio.run(main())"""

"""from flask import *
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
from kafka import KafkaConsumer
my_consumer = KafkaConsumer(
    'qe1',
     bootstrap_servers = ['192.168.0.100:9092'],
     auto_offset_reset = 'earliest',
     enable_auto_commit = True,
     group_id = 'my-group',
     consumer_timeout_ms=10000,
     value_deserializer = lambda x : x.decode('utf-8'))




Coffee_steps = ["turn on the stove", "pour milk", "boil it generously",
                "throw a handful of sugar crystals" "Meanwhile, whisk coffee in a mug", "turn off the stove"
                                                                                        "let the hot milk into the cup while constantly stirring it",
                "serve hot", "slurp before it cools down to become Not_so_ColdCoffee",
                "The output is pretty good, leave comments below! "]


# the homE_pagE

@app.route('/')
def homE_pagE():
    return render_template("base.html", len=len(Coffee_steps), Coffee_steps=Coffee_steps,com=my_consumer)"""

from datetime import datetime
from flask import *
from flask_cors import CORS

app=Flask(__name__)
CORS(app)
@app.context_processor
def utility_processor():
    def format_price(filename):
        with open(filename,'r') as f:
            return f.read()
    return dict(format_price=format_price)

@app.context_processor
def utility_processor():
    def format_price1(filename):
        with open(filename,'r') as f:
            return f.readlines()
    return dict(format_price1=format_price1)

@app.context_processor
def utility_processor():
    def format_price2(filename):
        with open(filename,'a') as f:
             f.write('Hello there')
             return ['1']
    return dict(format_price2=format_price2)

@app.context_processor
def inject_time():
    x=datetime.now().second
    return dict(time=x)

@app.context_processor
def inject_user1():
    return dict(time1=datetime.now().day)


@app.route('/')
def homE_pagE():
    return render_template("base1.html")

@app.route('/data',methods=['POST'])
def homE_pagE1():
    x=request.values.items()
    with open('data.txt', 'a') as f:
        for i in x:
            f.write(str(i))
    return make_response("inserted")


