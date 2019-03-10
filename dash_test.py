# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd

#print(df.head())

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

df = pd.read_csv('data_fifa.csv', header=0)

colors = {
    'background': '#3f3f3f',
    'text': '#ffffff'
}

app.layout = html.Div([
    html.Label('Dropdown'),
    dcc.Dropdown(
        id='nationality-picker',
        options=[
            {'label': nationality, 'value': nationality} for nationality in df[df['Overall'] > 80].Nationality.unique()
        ],
        placeholder ='Select Players Nationality...',
        multi = True
    ),
    html.H1("Players Overall vs. Age"),
    dcc.Graph(id = 'test-graph')
])

@app.callback(

    dash.dependencies.Output('test-graph', 'figure'),
    [dash.dependencies.Input('nationality-picker','value')])

def update_players(picked_nations):
    filtered_df = df[(df['Nationality'].isin(picked_nations)) & (df['Overall'] > 80)]
    
    return{
        'data': [
            go.Scatter(
                x = filtered_df['Age'],
                y = filtered_df['Overall'],
                text=filtered_df['Name'],
                mode='markers',
                opacity=0.8,
                marker={
                    'size' : df['Overall']/10,
                    'line': {'width': 0.5, 'color': 'white'}
                }
            )
        ],
        'layout': go.Layout(
            xaxis={'title': 'Overall Rating'},
            yaxis={'title': 'Players Age'},
        )
    }
# test
if __name__ == '__main__':
    app.run_server(debug=True)