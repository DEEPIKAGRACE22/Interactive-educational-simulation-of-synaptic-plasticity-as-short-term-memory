"""SynaptiLab Streamlit entry point.

The full interactive simulation will be implemented in a later milestone.
"""

import streamlit as st


st.set_page_config(page_title="SynaptiLab", page_icon="🧠", layout="wide")

st.title("SynaptiLab")
st.subheader("How Synapses Become Short-Term Memory")
st.write(
    "An educational project exploring how temporary changes in synaptic state "
    "can support recall, decay, and interference."
)
st.markdown("### Central question")
st.write("Can a changing synaptic connection act as short-term memory?")
st.info("The interactive simulation is under development.")

with st.sidebar:
    st.header("Explore")
    st.write("Use the pages in the sidebar as the project develops.")
    st.caption("The simplified educational model is not a complete implementation of BDH.")
