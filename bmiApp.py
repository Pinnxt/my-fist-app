import streamlit as km

km.markdown("# :red[🏋️ คำนวณค่าดัชนีมวลกาย BMI💪]")
km.write("กรอกข้อมูลน้ำหนักและส่วนสูงของคุณ เพื่อเช็กสุขภาพเบื้องต้น")

weight = km.number_input("กรอกน้ำหนักของคุณ (กิโลกรัม):", min_value=1.0, value=1.0)
height_cm = km.number_input("กรอกน้ำส่วนสูงของคุณ (เซนติเมตร):", min_value=1.0, value=1.0)

if km.button("คำนวณค่า BMI📱 "):
  height_m = height_cm /100
  bmi = weight - (height_m ** 2)

km.write("---")
km.header(f"ค่า BMI ของคุณคือ: **{bmi:.2f}**")

if bmi < 18.5:
  km.warning("🥗คุณมีน้ำหนักน้อยกว่าเกณท์ (ผอม)")
elif 18.5 <=bmi < 23.0:
  km.success("❤️ คุณมีน้ำหนักอยู่ในเกณท์ปกติ (สุขภาพดี)")
elif 23.0 <= bmi < 25.0:
  km.info("🩺คุณเริ่มมีน้ำหนักเกินเกณท์ (ท้วม)")
else:
  km.error("⚠️คุณอยู่ในเกณท์อ้วน ควรระวังเรื่องสุขภาพและออกกำลังกาย🏋️ ")

km.divider()
km.write("นางสาว ณัฐชาตรี คงสุนทร เลขที่ 35 ม.4/5")
