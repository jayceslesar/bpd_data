import plotly.express as px
import plotly.graph_objects as go
import pandas as pd



df = pd.read_csv(r"graph_this.csv")



fig = go.Figure()
fig.add_trace(go.Bar(x=df["year"],
                y=df["white_prop"],
                name='white',
                marker_color='rgb(255, 255, 255)'
                ))
fig.add_trace(go.Bar(x=df["year"],
                y=df["black_prop"],
                name='black',
                marker_color='rgb(0, 0, 0)'
                ))

fig.update_layout(
    title="Charge Rates by Race Over Proportion of Race in BTV",
    title_x=0.5,
    xaxis_title="Year",
    yaxis_title="Ratio (Proportion of Charges by Race Over Proportion of City Population by Race)",
    legend_title="Legend",
    font=dict(
        family="Times New Roman",
        size=18
    )
)
fig.show()