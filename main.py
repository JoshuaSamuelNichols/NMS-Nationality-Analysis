import pandas as pd
import plotly.express as px
import dash
from dash import dcc
from dash import html

# Read file
url = ('https://raw.githubusercontent.com/Nichols-Tech/NMS-Data-Nationality/main/NMSDataCountryV1.csv')
df = pd.read_csv(url)

# Create Plotly chart
fig = px.pie(df, names='Country', values='Count')

# Create the Dash app
app = dash.Dash(__name__)

# Define the layout
app.layout = html.Div(children=[
    html.H1('Nashville Music School Nationalities'),
    dcc.Graph(figure=fig)
])

# Run app
if __name__ == '__main__':
    app.run_server(debug=True)
