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
    dcc.Slider(
        id = 'overall_slider',
        min = df['Overall'].min(),
        max = df['Overall'].max(),
        value = df['Overall'].max(),
        marks = {str(overall): str(overall) for overall in df['Overall'].unique()}
    ),
    html.H1("Players Overall vs. Age"),
    dcc.Graph(id = 'test-graph')
])

@app.callback(
    dash.dependencies.Output('test-graph', 'figure'),
    [dash.dependencies.Input('nationality-picker','value'),
     dash.dependencies.Input('overall_slider','value')])

def update_players(nat_picker, over_slide):
    if nat_picker is None or nat_picker == "":
        filtered_df = df[(df['Nationality'].isin([nationality for nationality in df[df['Overall'] > 80].Nationality.unique()])) & (df['Overall'] == over_slide)]
    else:
        filtered_df = df[(df['Nationality'].isin(nat_picker)) & (df['Overall'] == over_slide)]
    
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