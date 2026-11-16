import streamlit as km

km.title("🛒โปรแกรมคำนวณส่วนลดสินค้าและ VAT")

price = km.number_input("กรอกราคาสินค้า (บาท)")
sale = km.number_input("กรอกส่วนลด (%)")

discount = price * sale / 100
vat = (price - discount) * 0.07
netprice = (price - discount) + vat

km.subheader("ราคาสุทธิที่ต้องจ่าย")
km.write(netprice, "บาท")
km.write("ราคาหลังหักส่วนลด:", price - discount, "บาท")
km.write("ภาษีมูลค่าเพิ่ม (VAT 7%):", vat, "บาท")

km.write("นางณัฐชาตรี คงสุนทร เลขที่ 35  ม.4/5")
