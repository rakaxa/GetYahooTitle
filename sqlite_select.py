# -*- coding: utf-8 -*-
import sys
import sqlite3

#
# �f�[�^���o��
#

if __name__ == '__main__':
  #
  # ��1���� : �f�[�^�x�[�X�ւ̃p�X
  #
  if len(sys.argv) != 2:
    sys.exit("usage : > python sqlite_select.py [DatabaseName]")
  db_path = sys.argv[1]

  conn = sqlite3.connect(db_path)
  c = conn.cursor()
  c.execute('''select * from YahooTitle''')
  for row in c:
    print(row)
