# Import dataframe and functions
# from Helper import *
from main import *

# Import packages
import base64
import pandas as pd
import numpy as np
import dash
import dash_table
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
from dash.exceptions import PreventUpdate
from dash.dependencies import Input, Output, State
from tkinter import *

# Initialise empty 2D board
board  = []
for row in range(9):
    board += [["","","","","","","","",""]]
# board = [["1","","","","","","","",""],
#          ["","2","","","","","","",""],
#          ["","","3","","","","","",""],
#          ["","","","4","","","","",""],
#          ["","","","","5","","","",""],
#          ["","","","","","6","","",""],
#          ["","","","","","","7","",""],
#          ["","","","","","","","8",""],
#          ["","","","","","","","","9"]]
#
# board  = setZero(board)
#
# print(np.matrix(board))

# Setup app with stylesheets
app = dash.Dash(external_stylesheets=[dbc.themes.SANDSTONE])

# Create layout
app.layout = dbc.Container(
    [
        dbc.Row(
            html.H3("Sudoku Solver", style = {"margin-bottom": "Opx"}),
            justify = 'center'
        ),
        dbc.Row(
            dash_table.DataTable(
                id='sudoku',
                columns=[{
                    'name': 'Column {}'.format(i),
                    'id': 'column-{}'.format(i),
                } for i in range(9)],
                data=[
                    {'column-{}'.format(i): '' for i in range(9)}
                    for j in range(9)
                ],
                editable=True,
                style_header={'display': 'none'},
                # style_table = {'overflowX':'scroll'},
                style_cell={
                    'height': 'auto',
                    'minWidth': '30px', 'width': '30px', 'maxWidth': '30px',
                    'whiteSpace': 'normal',
                    'fontSize':20,
                    'font-family':'sans-serif'
                }
                # style={'vertical-align': 'center', 'horizontal-align': 'center', 'width': '100vh'},
            ),
            justify="center",
        ),
        dbc.Row(
            [
            dbc.Button("solve", id = "solve", outline=True, color="primary", className="mr-1"),
            dbc.Button("clear", id = "clear", outline=True, color="primary", className="mr-1"),
            ],
            justify="center",
        ),
    ],
    id="main-container",
    style={"display": "flex", "flex-direction": "column"},
    fluid=True
)

@app.callback(
    Output('sudoku', 'data'),
    [Input('solve','n_clicks')],
    state = [State('sudoku', 'data'),
             State('sudoku', 'columns')])
def sudoku_solve(n_clicks,rows,columns):
    if rows[0]['column-0'] == '' and n_clicks is None:
        raise PreventUpdate
    else:
        print(rows[0]['column-0'])
        # print(type(rows))
        df = pd.DataFrame(rows)
        board = df.values.tolist()
        board = setZero(board)
        main(board)
        for i in range(9):
            for j in range(9):
                board[i][j] = str(board[i][j])
        print(board)
        key_list = ['column-0','column-1','column-2','column-3','column-4','column-5','column-6','column-7','column-8']
        n = len(board)
        rows = []
        for idx in range(9):
            rows.append({key_list[0]: board[idx][0], key_list[1]: board[idx][1], key_list[2]: board[idx][2],
                         key_list[3]: board[idx][3], key_list[4]: board[idx][4], key_list[5]: board[idx][5],
                         key_list[6]: board[idx][6], key_list[7]: board[idx][7], key_list[8]: board[idx][8]})
        print(rows)
        return rows

# Main
if __name__ == "__main__":
    app.run_server(debug=True)