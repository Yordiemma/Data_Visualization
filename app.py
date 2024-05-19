import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

# Mock data simulating abuse rates in different cities of Ethiopia
data = {
    "city": ["Addis Ababa", "Afar", "Amhara", "Benishangul-Gumuz", "Dire Dawa", "Gambela", "Harari", "Oromia", "Sidama", "Somali", "SNNPR", "Tigray"],
    "lat": [9.03, 11.5, 11.55, 10.05, 9.6, 8.25, 9.31, 8.98, 6.79, 9.41, 6.58, 13.5],
    "lon": [38.74, 41.0, 37.75, 35.75, 41.87, 34.52, 42.12, 39.7, 38.3, 44.05, 37.7, 39.05],
    "abuse_rate": [30, 45, 55, 50, 35, 60, 40, 70, 65, 75, 50, 80]
}

df = pd.DataFrame(data)

# Mapbox token for map rendering (replace with your own token if needed)
mapbox_token = 'YOUR_MAPBOX_ACCESS_TOKEN'
px.set_mapbox_access_token(mapbox_token)

# Create the scatter map
fig = px.scatter_mapbox(df, 
                        lat="lat", 
                        lon="lon", 
                        size="abuse_rate", 
                        color="abuse_rate",
                        hover_name="city", 
                        hover_data={"lat": False, "lon": False, "abuse_rate": True},
                        color_continuous_scale="Viridis", 
                        size_max=15, 
                        zoom=5,
                        mapbox_style="carto-darkmatter",  # Use dark matter style for black background
                        center={"lat": 9.145, "lon": 40.4897},
                        title="Abuse Rates in Different Cities of Ethiopia")

# Add annotations for each city with abuse rates
annotations = []
for i, row in df.iterrows():
    annotations.append(
        go.layout.Annotation(
            text=f"{row['city']}: {row['abuse_rate']}%",
            align='right',
            showarrow=False,
            xref='paper',
            yref='paper',
            x=1.1,
            y=1 - (i * 0.05),
            bordercolor="white",
            borderwidth=1,
            bgcolor="black",
            font=dict(color="white", size=12)
        )
    )

fig.update_layout(
    paper_bgcolor="black",  # Background color
    font=dict(color="white"),  # Font color for text
    margin={"r":150,"t":30,"l":0,"b":0},  # Increase right margin to accommodate annotations
    annotations=annotations
)

fig.show()
