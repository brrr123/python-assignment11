import plotly.express as px
import plotly.data as pldata
df = pldata.wind(return_type='pandas')

print(df.head(10))
print(df.tail(10))

df['strength'] = df['strength'].str.replace(r'[^\d.]', '', regex=True).astype(float)


fig = px.scatter(
    df, 
    x='strength', 
    y='frequency', 
    color='direction',
    title='Wind Strength vs Frequency by Direction',
    labels={'strength': 'Wind Strength', 'frequency': 'Frequency', 'direction': 'Direction'},
    hover_data=['strength', 'frequency', 'direction']
)


fig.write_html('wind.html')


