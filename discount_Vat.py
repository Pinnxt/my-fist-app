import streamlit as km

km.title("🛒โปรแกรมคำนวณส่วนลดสินค้าและ VAT")

price = km.number_input("กรอกราคาสินค้า (บาท)")
sale = km.number_input("กรอกส่วนลด (%)")

discount = price * sale / 100
vat = (price - discount) * 0.07
netprice = (price - discount) + vat

km.header("ราคาสุทธิที่ต้องจ่าย", netprice, "บาท")
km.write("ส่วนลด:", discount, "บาท")
km.write("ราคาหลังหักส่วนลด:", price - discount)
km.write("ภาษีมูลค่าเพิ่ม (VAT 7%):", vat, "บาท")

km.write("นางณัฐชาตรี คงสุนทร เลขที่ 35  ม.4/5")
