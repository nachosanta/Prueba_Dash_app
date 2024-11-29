import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px

# Datos de ejemplo
data = {
    'Year': [2010, 2011, 2012, 2013, 2014, 2015],
    'Sales': [100, 200, 300, 400, 500, 600],
    'Profit': [20, 50, 80, 90, 100, 120]
}
df = pd.DataFrame(data)

# Crear la aplicación Dash
app = dash.Dash(__name__)
server = app.server

app.layout = html.Div([
    html.H1("Dash App de Ejemplo", style={'text-align': 'center'}),
    dcc.RangeSlider(
        id='year-slider',
        min=df['Year'].min(),
        max=df['Year'].max(),
        step=1,
        marks={year: str(year) for year in df['Year']},
        value=[df['Year'].min(), df['Year'].max()]
    ),
    dcc.Graph(id='line-plot'),
])

@app.callback(
    Output('line-plot', 'figure'),
    Input('year-slider', 'value')
)
def update_graph(selected_years):
    filtered_df = df[(df['Year'] >= selected_years[0]) & (df['Year'] <= selected_years[1])]
    fig = px.line(filtered_df, x='Year', y='Sales', title='Ventas por Año')
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)
