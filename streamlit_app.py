
import streamlit
streamlit.title("My parents New healthy dinner")
streamlit.title("Breakfast menu")
streamlit.text("🥣 Omega 3 & Blueberry Oatmeal ")
streamlit.text("🥗 Kale, Spinach & Rocket smoothie ")
streamlit.text("🐔 Hard-boiled Free-Range egg ")
streamlit.text("🥑🍞 Avocado Toast ")
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

streamlit.dataframe(my_fruit_list)
