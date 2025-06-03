from dash import Dash, dcc, html, Input, Output
import plotly.express as px
app = Dash(__name__)
server = app.server

# Load the gapminder dataset
df = px.data.gapminder()

# Get unique countries for dropdown (as a Series)
countries = df['country'].drop_duplicates()

# Initialize Dash app
app = Dash(__name__)

# Layout
app.layout = html.Div([
    dcc.Dropdown(
        id="country-dropdown",
        options=[{"label": country, "value": country} for country in countries],
        value="Canada"
    ),
    dcc.Graph(id="gdp-growth")
])

# Callback for dynamic updates
@app.callback(
    Output("gdp-growth", "figure"),
    [Input("country-dropdown", "value")]
)
def update_graph(country):
    # Filter data for the selected country
    filtered_df = df[df['country'] == country]

    # Create line plot
    fig = px.line(filtered_df, x="year", y="gdpPercap", 
                 title=f"GDP Per Capita Growth for {country}")
    return fig

# Run the app
if __name__ == "__main__": 
    app.run(debug=True)
