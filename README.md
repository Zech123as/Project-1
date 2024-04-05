
# Options Trading Analysis Tool

## Overview
This repository hosts the Options Trading Analysis Tool, an application designed to assist traders in analyzing options trading strategies with a focus on expiry dates. Utilizing Python, Plotly, and Streamlit, it offers an interactive interface for users to visualize potential profits based on historical data.

## Features
- **TrueData Integration**: Connects to TrueData WebSockets API to fetch real-time historical data.
- **Dynamic Expiry Date Calculation**: Automatically calculates the nearest Thursday for options expiry.
- **GitHub Data Retrieval**: Fetches serialized objects directly from a specified GitHub repository for analysis.
- **Interactive Visualizations**: Leverages Plotly for dynamic, responsive charts.
- **Streamlit Application**: Provides an easy-to-use web interface for setting parameters and viewing results.

## Requirements
- Python 3.6 or later
- Plotly
- Streamlit
- pandas
- requests

Please ensure you have the above libraries installed before running the application. They can be installed using pip:

```bash
pip install plotly streamlit pandas requests
```

## Usage
To run the application, execute the following command in your terminal:

```bash
streamlit run Chart_Code.py
```

Navigate to the provided local URL in your browser to interact with the tool.

## Configuration
You may need to set up your TrueData and GitHub credentials within the script or as environment variables for data retrieval. Please refer to the respective services for obtaining these credentials.
