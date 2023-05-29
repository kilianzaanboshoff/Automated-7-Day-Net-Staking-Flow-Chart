import requests
import json
import plotly.graph_objects as go


url = "https://api.stakingrewards.com/public/query"


headers = {
    "x-api-key": "YOUR API KEY HERE"
}


query_gainers = """
{
  assets(where:{isActive:true},order:{metricKey_desc:"net_staking_flow_7d"},limit:10){
    name
    metrics(where:{metricKeys:["net_staking_flow_7d"]},limit:1){
      defaultValue
    }
  }
}
"""


query_losers = """
{
  assets(where:{isActive:true},order:{metricKey_asc:"net_staking_flow_7d"},limit:10){
    name
    metrics(where:{metricKeys:["net_staking_flow_7d"]},limit:1){
      defaultValue
    }
  }
}
"""


response_gainers = requests.post(url, headers=headers, json={'query': query_gainers}).json()
response_losers = requests.post(url, headers=headers, json={'query': query_losers}).json()


assets_gainers = response_gainers['data']['assets']
assets_losers = response_losers['data']['assets']


gainers_names = [asset['name'] for asset in assets_gainers]
gainers_values = [asset['metrics'][0]['defaultValue'] for asset in assets_gainers]


losers_names = [asset['name'] for asset in assets_losers]
losers_values = [asset['metrics'][0]['defaultValue'] for asset in assets_losers]


fig = go.Figure()


fig.add_trace(go.Bar(
    y=gainers_names,
    x=gainers_values,
    name='Net Inflows',
    orientation='h',
    marker=dict(
        color='rgb(0, 191, 255)',
        line=dict(color='rgb(255, 255, 255)', width=1)
    )
))

fig.add_trace(go.Bar(
    y=losers_names,
    x=losers_values,
    name='Net Outflows',
    orientation='h',
    marker=dict(
        color='rgb(255, 105, 180)',
        line=dict(color='rgb(255, 255, 255)', width=1)
    )
))

fig.update_layout(
    title_text='Net Staking Flow (Last 7 Days)',
    title_font=dict(size=30, family='Arial', color='rgb(248, 248, 249)'), 
    title_x=0.5, 
    height=800,
    template='plotly_dark',
    yaxis=dict(autorange="reversed"),
    xaxis=dict(title='Net Staking Flow ($)'),
)

fig.show()
