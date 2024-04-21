from os.path import abspath, dirname
import sys

sys.path.insert(0, abspath(dirname(dirname(abspath(__file__)))))

from src import *

bd = DataBase()

data = bd.execute(get_all_registers()).fetchone()

print(data)

print("\n\nestou conectado? ->",bd.disconnect())