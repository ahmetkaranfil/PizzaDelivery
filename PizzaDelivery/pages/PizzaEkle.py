import streamlit as st
import sqlite3

from streamlit import file_uploader

conn = sqlite3.connect("pizzaDB.sqlite3")
c = conn.cursor()

c.execute("CREATE TABLE IF NOT EXISTS pizzalar(name TEXT, smallPrice REAL, mediumPrice REAL, largePrice REAL,"
          "includes TEXT, picture TEXT)")
conn.commit()


st.header("Pizza Ekle")

with st.form("pizzaekle", clear_on_submit=True):
    name = st.text_input("Pizza İsmi")
    smallPrice = st.number_input("Small Fiyat")
    mediumPrice = st.number_input("Medium Fiyat")
    largePrice = st.number_input("Large Fiyat")
    includes = st.multiselect("İçindekiler", ["Mantar", "Pepperoni", "Mozerella", "Mısır", "Zeytin", "Tavuk",
                                              "Ton Balığı", "Dometes Sosu", "Fesleğen", "Salam", "Sosis"])
    picture = file_uploader("Pizza Resmi Ekleyiniz")
    add = st.form_submit_button("Pizza Ekle")

    if add:
        includes = str(includes)

        includes = includes.replace("[","")
        includes = includes.replace("]","")
        includes = includes.replace("'","")

        pictureURL = "images/"+picture.name
        open(pictureURL, "wb").write(picture.read())

        c.execute("INSERT INTO pizzalar VALUES(?,?,?,?,?,?)",
                  (name, smallPrice, mediumPrice, largePrice, includes, pictureURL))
        conn.commit()

        st.success("Pizza başarıyla eklendi")