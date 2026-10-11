import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Quản lý điểm sinh viên", layout="wide")
st.title("QUẢN LÝ ĐIỂM SINH VIÊN")

data = {
    "Họ và Tên": [
        "Trịnh Vĩnh Tâm", "Phan Lê Vy Thanh",
        "Lê Dương Bảo Lâm", "Kiều Minh Tuấn",
        "Lâm Vĩ Dạ", "Alexander",
        "Trịnh Trần Phương Tuấn", "Ngô Kiến Huy",
        "Bray", "Trần Minh Hiếu"
    ],
    "Điểm chuyên cần": [10,9,8,10,10,4,7,6,8,9],
    "Điểm giữa kì": [9,9,8,3,10,9,7,9,10,10],
    "Điểm cuối kì": [9,10,8,8,9,1,9,10,7,9]
}

df = pd.DataFrame(data)

df["Điểm tổng kết"] = (
    df["Điểm chuyên cần"] * 0.2
    + df["Điểm giữa kì"] * 0.3
    + df["Điểm cuối kì"] * 0.5
).round(2)

def xep_loai(diem):
    if diem >= 8.5:
        return "Giỏi"
    elif diem >= 7:
        return "Khá"
    elif diem >= 5:
        return "Trung bình"
    return "Yếu"

df["Xếp loại"] = df["Điểm tổng kết"].apply(xep_loai)

st.subheader("1. Bảng điểm")
st.dataframe(df, hide_index=True, use_container_width=True)

st.subheader("2. Thống kê lớp học")
c1, c2, c3, c4 = st.columns(4)
c1.metric("Điểm trung bình", f'{df["Điểm tổng kết"].mean():.2f}')
c2.metric("Điểm cao nhất", f'{df["Điểm tổng kết"].max():.2f}')
c3.metric("Điểm thấp nhất", f'{df["Điểm tổng kết"].min():.2f}')
c4.metric("Số sinh viên đạt", f'{(df["Điểm tổng kết"] >= 5).sum()}/10')

st.subheader("3. Biểu đồ điểm tổng kết")
fig, ax = plt.subplots(figsize=(10, 6))
ax.barh(df["Họ và Tên"], df["Điểm tổng kết"])
ax.set_title("Điểm tổng kết của 10 sinh viên")
ax.set_xlabel("Điểm tổng kết")
ax.set_ylabel("Tên sinh viên")
ax.set_xlim(0, 10)
ax.invert_yaxis()
fig.tight_layout()
st.pyplot(fig)
plt.close(fig)

st.subheader("4. Lọc sinh viên theo xếp loại")
loai = st.selectbox("Chọn xếp loại", ["Tất cả", "Giỏi", "Khá", "Trung bình", "Yếu"])
if loai == "Tất cả":
    st.dataframe(df, hide_index=True, use_container_width=True)
else:
    st.dataframe(df[df["Xếp loại"] == loai], hide_index=True, use_container_width=True)
