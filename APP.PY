import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
st.title("QUẢN LÝ ĐIỂM SINH VIÊN")
data = {
  "Họ và Tên": [
    "Trịnh Vinh Tâm","Phan Lê Vy Thanh",
    "Lê Dương Bảo Lâm","Kiều Minh Tuấn",
    "Lâm Vĩ Dạ","Alexander",
    "Trịnh Trần Phương Tuấn","Ngô Kiến Huy",
    "Bray","Trần Minh Hiếu"
    ],
  "điểm chuyên cần" : [10,9,8,10,10,4,7,6,8,9],
  "điểm giữa kì" : [9,9,8,3,10,9,7,9,12,10],
  "điểm cuối kì" : [9,10,8,8,9,1,9,10,7,9]
}
df = pd.DataFrame(data)
