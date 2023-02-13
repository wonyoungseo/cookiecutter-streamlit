import streamlit as st


def app_base_config():
    st.set_page_config(
        page_title="{{ cookiecutter.app_name }}",
        initial_sidebar_state="expanded",
    )