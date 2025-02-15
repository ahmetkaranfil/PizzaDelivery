import streamlit as st
import sqlite3


conn = sqlite3.connect("pizzaDB.sqlite3")
c = conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS siparisler(infos1 TEXT, infos2 TEXT, choosePizza TEXT, size TEXT, drink TEXT, price REAL)")
conn.commit()

c.execute("SELECT name FROM pizzalar")
names = c.fetchall()


namesList = []
for i in names:
    namesList.append(i[0])


st.header("Sipariş")

with (st.form("siparis", clear_on_submit=True)):
    infos1 = st.text_input("İsim Soyisim")
    infos2 = st.text_area("Adres")
    choosePizza = st.selectbox("Pizza Seç", namesList)
    size = st.selectbox("Boy", ["Select an option...", "Small", "Medium", "Large"])
    drink = st.selectbox("İçecek", ["Select an option", "İstemiyorum", "Ayran", "CocaCola", "IceTea", "Çay", "Su"])
    order = st.form_submit_button("Sipariş Ver")

    if order:
        if size=="Small":
            c.execute("SELECT smallPrice FROM pizzalar WHERE name=?", (choosePizza,))
            price = c.fetchone()

        elif size=="Medium":
            c.execute("SELECT mediumPrice FROM pizzalar WHERE name=?", (choosePizza,))
            price = c.fetchone()

        elif size=="Large":
            c.execute("SELECT largePrice FROM pizzalar WHERE name=?", (choosePizza,))
            price = c.fetchone()

        drinks = {
            "İstemiyorum":0,
            "Ayran":35,
            "CocaCola":55,
            "IceTea":55,
            "Çay":20,
            "Su":10
        }
        drinksPrice = drinks[drink]

        totalPrice = price[0] + drinksPrice

        c.execute("INSERT INTO siparisler VALUES(?,?,?,?,?,?)", (infos1, infos2, choosePizza, size, drink, totalPrice))
        conn.commit()
        st.success(f"Sipariş başarılı bir şekilde gerçekleştirildi. Toplam Ücret: {totalPrice}₺")

        st.write(totalPrice)