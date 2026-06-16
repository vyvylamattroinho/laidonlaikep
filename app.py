import streamlit as st

# Tiêu đề
st.title("💰 App tính tiền gửi tiết kiệm")

# Nhập dữ liệu
C = st.number_input("Nhập số tiền gốc (VNĐ)", value=700000000)
i = st.number_input("Nhập lãi suất năm (ví dụ 0.05 = 5%)", value=0.05, format="%.4f")
n = st.number_input("Nhập số tháng", value=5)

# Nút tính toán
if st.button("Tính toán"):
    # Lãi đơn
    lai_don = C * (1 + (i / 12) * n)

    # Lãi kép
    lai_kep = C * ((1 + i / 12) ** n)

    # Hiển thị kết quả
    st.subheader("📊 Kết quả")
    st.write(f"**Số tiền nhận được theo lãi đơn:** {round(lai_don):,} VNĐ")
    st.write(f"**Số tiền nhận được theo lãi kép:** {round(lai_kep):,} VNĐ")
