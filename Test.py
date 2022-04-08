from datetime import datetime, timedelta, time
from plotly.subplots import make_subplots
from truedata_ws.websocket.TD import TD
import plotly.graph_objects as go
import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

@st.cache(allow_output_mutation=True)
def Truedata_login(hash_funcs = {TD : id}):
	td_obj = TD('wssand041', 'sandeep041', live_port=None)
	return td_obj

td_obj = Truedata_login()
