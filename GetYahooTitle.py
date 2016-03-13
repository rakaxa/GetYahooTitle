# -*- coding: utf-8 -*-
import sys
import re
import datetime
import sqlite3
import feedparser

if __name__ == '__main__':
  if len(sys.argv) != 3:
    sys.exit("usage : > python GetYahooTitle.py [URLFileName]")
  dbname = sys.argv[1]
  urlfile = sys.argv[2]

  timestump = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")

  conn = sqlite3.connect(dbname)
  c = conn.cursor()

  with open(urlfile, 'r') as fh:
    for line in fh:
      if line[0] == '#':
        continue
      d = feedparser.parse(line)

      for entry in d['entries']:
#        print("title:", entry.title)
        query = "insert into YahooTitle values (\"" + timestump + "\",\"" +  entry.title + "\")"
        try:
          c.execute(query)
          conn.commit()
        except:
          print("Error!!" + entry.title + entry.link)
          continue
  c.close()
