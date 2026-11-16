import streamlit as km

km.title("🛒โปรแกรมคำนวณส่วนลดสินค้าและ VAT")

price = km.number_input("ราคาสินค้า")
sale = km.number_input("เปอร์เซ็นต์ส่วนลด")

discount = price * sale / 100
vat = (price - discount) * 0.07
netprice = (price - discount) + vat

km.header("ผลการคำนวณ")
km.write("ราคาสินค้า:", price)
km.write("เปอร์เซ็นต์ส่วนลด:", sale, "%")
km.write("ส่วนลด:", discount, "บาท")
km.write("VAT 7%:", vat, "บาท")
km.write("ราคาสุทธิ:", netprice, "บาท")
km.write("นางณัฐชาตรี คงสุนทร เลขที่ 35  ม.4/5")
