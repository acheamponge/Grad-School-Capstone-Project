import streamlit as st

import utils.display as udisp

import src.pages.home
import src.pages.Technology
import src.pages.Validation
import src.pages.Analysis
import src.pages.Financial
import src.pages.Competition
import src.pages.Framework
import src.pages.Market
import src.pages.Demos
import src.pages.Resources


MENU = {
    "Home" : src.pages.home,
    "Technology Review" : src.pages.Technology,
    "Validation" : src.pages.Validation,
  
    "Decision Making Framework" : src.pages.Framework,
    "Go-To-Market Strategy" : src.pages.Market,
    "Market Analysis" : src.pages.Demos,
    "Launch Strategy" : src.pages.Resources
    }

def main():
    st.sidebar.title("Navigation")
    menu_selection = st.sidebar.radio("Pick an option...", list(MENU.keys()))

    menu = MENU[menu_selection]

    with st.spinner(f"Loading {menu_selection} ..."):
        udisp.render_page(menu)
    st.sidebar.title("")
if __name__ == "__main__":
    main()