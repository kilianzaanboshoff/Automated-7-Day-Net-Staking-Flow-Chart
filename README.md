# Automated-7-Day-Net-Staking-Flow-Chart
This repository contains a Python script that fetches, analyzes, and visualizes the staking flow data of various crypto assets from the Staking Rewards API.

# Description
The script uses the Staking Rewards API to fetch the net staking flow data for the top 10 gainers and top 10 losers in the last 7 days. It then uses the data to generate a bar chart with Plotly, presenting net staking flows of these assets.

The net staking flow represents the total amount of a crypto asset being staked minus the total amount being unstaked in a particular time period. This data is valuable for understanding the changes in the staking ecosystem of these assets.

# Features
Fetches data from the Staking Rewards API.
Analyzes and parses JSON data to fetch the top 10 gainers and top 10 losers in terms of net staking flow.
Generates a bar chart using Plotly, a Python graphing library, to visualize this data.
The chart generated provides clear, insightful, and visually appealing representation of the staking flows of various assets.
How to Use
To use this script, you will need Python and the following Python libraries installed:

# Plotly for data visualization.
Requests for making HTTP requests to fetch data from the API.
You'll also need to have a Staking Rewards API key to fetch the data. Please replace "Your_API_Key_Here" in the script with your actual API key.
