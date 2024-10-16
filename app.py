from flask import Flask
from flask_cors import CORS
from file import parse_excel
from authentication import token_required

app = Flask(__name__)
CORS(app)

file_grid = 'Grid Demand Data.xlsx'
date_column = 'RUN_TIME'

@app.get('/runtime')
@token_required
def get_grid():
  return parse_excel('RUN_TIME', 'LUZ_MKT_REQT', 'VIS_MKT_REQT', 'MIN_MKT_REQT', file=file_grid, date_col=date_column)