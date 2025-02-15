import streamlit as st
import sqlite3
import pandas

st.header("Ana Sayfa")

conn = sqlite3.connect("pizzaDB.sqlite3")
c = conn.cursor()

c.execute("SELECT * FROM siparisler")
orders = c.fetchall()

df = pandas.DataFrame(orders)
df.columns=["infos1", "infos2", "choosePizza", "size", "drink", "totalPrice"]

st.table(df)