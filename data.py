import sqlite3

class sqliteData(object):
  def __init__(self, file, dirs):
    self.conn = sqlite3.connect(file)
    self.dir = dirs
    self.videos = ['/home/ldiamond/tmp/v.avi']

  def refresh(self):
    for d in dirs:
      pass

  def get_list(self):
    return self.videos


