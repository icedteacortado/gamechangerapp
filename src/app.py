
#%% import pkgs
#import packages
from dash import Dash, html, dash_table, dcc, callback, Output, Input
import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc

#%% assign data variables
adf = pd.read_csv('src/gamechangerdata.csv', encoding='utf-8')

#%%init
# Initialize the app
app = Dash(__name__, 
        update_title="Game Changer Data",
         external_stylesheets=[dbc.themes.BOOTSTRAP],
    meta_tags=[
        {"name": "viewport", "content": "width=device-width, initial-scale=1"}
    ],)
server = app.server
#%% app layout
app.layout = html.Div([
    dash_table.DataTable(id='datatable',
                        data=adf.to_dict('records'), 
                        editable=True,
                        sort_action="native",
                        page_size=8),
    dcc.RadioItems(id = 'radio-items',
                    options=[
                {'label': 'Appearances', 'value': 'Appearances'},
                {'label': 'Competitive Episodes', 'value': 'Competitive Episodes'},
                {'label': 'Win Count', 'value': 'Win Count'},
                {'label': 'Total Points', 'value': 'Total Points'}
            ], 
                        value='Appearances', 
                        inline=True),
    dcc.Graph(id='bar-chart'),
])

#%% callback
@app.callback(
    Output('bar-chart', 'figure'),
    [Input('radio-items', 'value')]
)
def update_bar_chart(selected_y_axis):
    fig = px.bar(adf, 
                 x='Player', 
                 y=selected_y_axis,
                 text_auto=True)
    fig.update_layout(xaxis={'categoryorder':'total descending'})

    return fig
#%% run app

if __name__ == '__main__':
    app.run(debug=True)
# %%
