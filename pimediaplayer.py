from flask import Flask
from data import sqliteData 
import json
from cliplayerwrapper import Player

app = Flask(__name__)

@app.route('/list')
def list():
  return json.dumps(data.get_list())

@app.route('/play')
def play():
  player.play()
  return str(player.p.pid)

@app.route('/pause')
def pause():
  player.pause()
  return 'success'

if __name__ == '__main__':
  data = sqliteData('db','test')
  player = Player()
  app.debug = True
  app.run(host='0.0.0.0')

