import math
import streamlit as st

st.set_page_config(page_title="STEM Toán 11", page_icon="📐", layout="centered")

st.title("📐 CHƯƠNG TRÌNH STEM TOÁN 11")
st.markdown("*Công cụ hỗ trợ học tập môn Toán lớp 11 trực quan, sinh động.*")
st.markdown("---")

st.sidebar.header("📋 Danh mục chức năng")
menu = st.sidebar.selectbox(
    "Chọn tính năng bạn muốn sử dụng:",
    [
        "1. Giải phương trình sin(x) = a",
        "2. Tính Cấp số cộng",
        "3. Tính Xác suất P(A)",
    ],
)

if menu == "1. Giải phương trình sin(x) = a":
  st.header("🔍 Giải phương trình lượng giác: $\\sin(x) = a$")
  a = st.number_input("Nhập giá trị a (từ -1 đến 1):", value=0.5, step=0.1)

  if st.button("Tính nghiệm", type="primary"):
    if -1 <= a <= 1:
      alpha_rad = math.asin(a)
      alpha_deg = math.degrees(alpha_rad)

      # Nhận diện các giá trị góc đặc biệt chuẩn không cần làm tròn
      eps = 1e-3
      if abs(a - 0) < eps:
        str_arcsin = "0"
        str_pi_minus = "\\pi"
      elif abs(a - 0.5) < eps:
        str_arcsin = "\\frac{\\pi}{6}"
        str_pi_minus = "\\frac{5\\pi}{6}"
      elif abs(a - math.sqrt(2) / 2) < eps:
        str_arcsin = "\\frac{\\pi}{4}"
        str_pi_minus = "\\frac{3\\pi}{4}"
      elif abs(a - math.sqrt(3) / 2) < eps:
        str_arcsin = "\\frac{\\pi}{3}"
        str_pi_minus = "\\frac{2\\pi}{3}"
      elif abs(a - 1) < eps:
        str_arcsin = "\\frac{\\pi}{2}"
        str_pi_minus = "\\frac{\\pi}{2}"
      elif abs(a - (-0.5)) < eps:
        str_arcsin = "-\\frac{\\pi}{6}"
        str_pi_minus = "\\frac{7\\pi}{6}"
      elif abs(a - (-math.sqrt(2) / 2)) < eps:
        str_arcsin = "-\\frac{\\pi}{4}"
        str_pi_minus = "\\frac{5\\pi}{4}"
      elif abs(a - (-math.sqrt(3) / 2)) < eps:
        str_arcsin = "-\\frac{\\pi}{3}"
        str_pi_minus = "\\frac{4\\pi}{3}"
      elif abs(a - (-1)) < eps:
        str_arcsin = "-\\frac{\\pi}{2}"
        str_pi_minus = "\\frac{3\\pi}{2}"
      else:
        str_arcsin = f"{alpha_rad:.4f}"
        str_pi_minus = f"\\pi - {alpha_rad:.4f}"

      st.success("✅ Phương trình có nghiệm:")
      st.latex(f"x = {str_arcsin} + k2\\pi \\quad (k \\in \\mathbb{{Z}})")
      st.latex(f"x = {str_pi_minus} + k2\\pi \\quad (k \\in \\mathbb{{Z}})")
      st.info(f"💡 **Giá trị góc (độ):** $\\alpha \\approx {alpha_deg:.2f}^\\circ$")
    else:
      st.error(
          "❌ Giá trị $a$ phải nằm trong đoạn từ $-1$ đến $1$ thì phương trình"
          " mới có nghiệm!"
      )

elif menu == "2. Tính Cấp số cộng":
  st.header("📈 Tính toán Cấp số cộng $(u_n)$")
  col1, col2, col3 = st.columns(3)
  with col1:
    u1 = st.number_input("Số hạng đầu (u₁):", value=1.0, step=1.0)
  with col2:
    d = st.number_input("Công sai (d):", value=2.0, step=1.0)
  with col3:
    n = st.number_input("Số lượng số hạng (n):", value=5, min_value=1, step=1)

  if st.button("Tính kết quả", type="primary"):
    n_int = int(n)
    un = u1 + (n_int - 1) * d
    sn = (n_int * (2 * u1 + (n_int - 1) * d)) / 2
    st.success("📊 Kết quả tính toán:")
    st.metric(label=f"Số hạng thứ {n_int} (uₙ)", value=f"{un}")
    st.metric(label=f"Tổng {n_int} số hạng đầu tiên (Sₙ)", value=f"{sn}")

elif menu == "3. Tính Xác suất P(A)":
  st.header("🎲 Tính Xác suất Biến cố $P(A)$")
  col1, col2 = st.columns(2)
  with col1:
    n_A = st.number_input(
        "Số kết quả thuận lợi n(A):", value=2, min_value=0, step=1
    )
  with col2:
    n_Omega = st.number_input(
        "Số phần tử không gian mẫu n(Ω):", value=6, min_value=1, step=1
    )

  if st.button("Tính xác suất", type="primary"):
    if n_A <= n_Omega:
      p_a = n_A / n_Omega
      st.success("🎯 Kết quả:")
      st.metric(label="Xác suất P(A)", value=f"{p_a:.4f}")
      st.write(f"Tương đương với tỉ lệ: **{p_a * 100:.2f}%**")
    else:
      st.error(
          "❌ Số phần tử của biến cố $n(A)$ không thể lớn hơn không gian mẫu"
          " $n(\\Omega)$!"
      )

st.markdown("---")
st.markdown(
    "<p style='text-align: center; color: gray;'>Sản phẩm STEM Toán 11 - Thực"
    " hiện bằng Python & Streamlit</p>",
    unsafe_allow_html=True,
)
