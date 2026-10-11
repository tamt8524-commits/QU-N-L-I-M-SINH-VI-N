# -*- coding: utf-8 -*-
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Quản lý điểm sinh viên", layout="wide")
st.title("QUẢN LÝ ĐIỂM SINH VIÊN")

# 1. Dữ liệu 10 sinh viên
data = {
    "Họ và Tên": [
        "Trịnh Vinh Tâm", "Phan Lê Vy Thanh",
        "Lê Dương Bảo Lâm", "Kiều Minh Tuấn",
        "Lâm Vĩ Dạ", "Alexander",
        "Trịnh Trần Phương Tuấn", "Ngô Kiến Huy",
        "Bray", "Trần Minh Hiếu"
    ],
    "Điểm chuyên cần": [10, 9, 8, 10, 10, 4, 7, 6, 8, 9],
    "Điểm giữa kỳ": [9, 9, 8, 3, 10, 9, 7, 9, 10, 10],
    "Điểm cuối kỳ": [9, 10, 8, 8, 9, 1, 9, 10, 7, 9]
}

df = pd.DataFrame(data)

# 2. Tính điểm tổng kết: 20% chuyên cần, 30% giữa kỳ, 50% cuối kỳ
df["Điểm tổng kết"] = (
    df["Điểm chuyên cần"] * 0.2
    + df["Điểm giữa kỳ"] * 0.3
    + df["Điểm cuối kỳ"] * 0.5
).round(2)

# 3. Xếp loại
def xep_loai(diem):
    if diem >= 8.5:
        return "Giỏi"
    elif diem >= 7:
        return "Khá"
    elif diem >= 5:
        return "Trung bình"
    return "Yếu"

df["Xếp loại"] = df["Điểm tổng kết"].apply(xep_loai)

# 4. Bảng điểm
st.subheader("1. Bảng điểm")
st.dataframe(df, hide_index=True, use_container_width=True)

# 5. Thống kê lớp học
st.subheader("2. Thống kê lớp học")
diem_tb = df["Điểm tổng kết"].mean()
diem_cao_nhat = df["Điểm tổng kết"].max()
diem_thap_nhat = df["Điểm tổng kết"].min()
sv_cao_nhat = df.loc[df["Điểm tổng kết"] == diem_cao_nhat, "Họ và Tên"].tolist()
sv_thap_nhat = df.loc[df["Điểm tổng kết"] == diem_thap_nhat, "Họ và Tên"].tolist()
so_sv_dat = int((df["Điểm tổng kết"] >= 5).sum())

c1, c2, c3, c4 = st.columns(4)
c1.metric("Điểm trung bình", f"{diem_tb:.2f}")
c2.metric("Điểm cao nhất", f"{diem_cao_nhat:.2f}")
c3.metric("Điểm thấp nhất", f"{diem_thap_nhat:.2f}")
c4.metric("Số sinh viên đạt", f"{so_sv_dat}/10")

st.write("**Sinh viên có điểm cao nhất:** " + ", ".join(sv_cao_nhat))
st.write("**Sinh viên có điểm thấp nhất:** " + ", ".join(sv_thap_nhat))

# 6. Selectbox chọn một sinh viên và xem điểm chi tiết
st.subheader("3. Tra cứu điểm sinh viên")
ten_sv = st.selectbox("Chọn sinh viên", df["Họ và Tên"])
sv = df[df["Họ và Tên"] == ten_sv].iloc[0]

c1, c2, c3 = st.columns(3)
c1.metric("Điểm chuyên cần", f'{sv["Điểm chuyên cần"]:.1f}')
c2.metric("Điểm giữa kỳ", f'{sv["Điểm giữa kỳ"]:.1f}')
c3.metric("Điểm cuối kỳ", f'{sv["Điểm cuối kỳ"]:.1f}')
c4, c5 = st.columns(2)
c4.metric("Điểm tổng kết", f'{sv["Điểm tổng kết"]:.2f}')
c5.metric("Xếp loại", sv["Xếp loại"])

# 7. Biểu đồ cột điểm tổng kết của 10 sinh viên
st.subheader("4. Biểu đồ điểm tổng kết")
fig, ax = plt.subplots(figsize=(10, 5))
ax.barh(df["Họ và Tên"], df["Điểm tổng kết"])
ax.set_title("Điểm tổng kết của 10 sinh viên")
ax.set_xlabel("Điểm tổng kết")
ax.set_ylabel("Họ tên sinh viên")
ax.set_xlim(0, 10)
ax.invert_yaxis()
fig.tight_layout()
st.pyplot(fig)
plt.close(fig)

# 8. Thông tin người tạo ở cuối trang
st.divider()
st.caption("Người tạo: Trịnh Vinh Tâm | MSSV: 038208012383")
