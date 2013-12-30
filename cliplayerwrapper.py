import pty
import subprocess
import os, tempfile

class Player(object):
  def __init__(self):
    self.tmpdir = tempfile.mkdtemp()
    print 'saving fifo in ' + self.tmpdir
    self.fifo = os.path.join(self.tmpdir, 'piplayer' + str(os.getpid()))
    try:
      os.mkfifo(self.fifo)
    except:
      print(self.fifo + 'already exists')
    self.pause()
    self.pause()
  def play(self):
    self.p = subprocess.Popen('/usr/bin/mplayer /home/ldiamond/tmp/v.avi <' + self.fifo, shell=True)
  
  def pause(self):
    self._write(' ')
  def _write(self, cmd):
    with open(self.fifo, 'w') as f:
      f.write(cmd)

  def __del__(self):
    os.remove(self.fifo)
    os.rmdir(self.tmpdir)
