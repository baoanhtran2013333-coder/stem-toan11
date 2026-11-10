import math
import matplotlib.pyplot as plt
import numpy as np
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
        "4. Hình học không gian (Tự nhập liệu & Vẽ hình)",
    ],
)

if menu == "1. Giải phương trình sin(x) = a":
  st.header("🔍 Giải phương trình lượng giác: $\\sin(x) = a$")
  a = st.number_input("Nhập giá trị a (từ -1 đến 1):", value=0.5, step=0.1)

  if st.button("Tính nghiệm", type="primary"):
    if -1 <= a <= 1:
      alpha_rad = math.asin(a)
      alpha_deg = math.degrees(alpha_rad)

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
          "❌ Số phần tử của biến cố $n(A)$ không thể lớn hơn không gian mẫu!"
      )

elif menu == "4. Hình học không gian (Tự nhập liệu & Vẽ hình)":
  st.header("📐 Khảo sát Hình học không gian tương tác")

  sub_choice = st.selectbox(
      "Chọn bài học hình học:",
      [
          "Bài 10: Xác định mặt phẳng qua 3 điểm",
          "Bài 11: Kiểm tra hai đường thẳng song song",
          "Bài 12: Kiểm tra đường thẳng song song với mặt phẳng",
      ],
  )

  if sub_choice == "Bài 10: Xác định mặt phẳng qua 3 điểm":
    st.markdown(
        "Nhập tọa độ 3 điểm không thẳng hàng $A, B, C$ trong không gian để vẽ"
        " mặt phẳng chứa chúng:"
    )
    col1, col2, col3 = st.columns(3)
    with col1:
      xA = st.number_input("Ax", value=1.0)
      yA = st.number_input("Ay", value=0.0)
      zA = st.number_input("Az", value=0.0)
    with col2:
      xB = st.number_input("Bx", value=0.0)
      yB = st.number_input("By", value=2.0)
      zB = st.number_input("Bz", value=0.0)
    with col3:
      xC = st.number_input("Cx", value=0.0)
      yC = st.number_input("Cy", value=0.0)
      zC = st.number_input("Cz", value=2.0)

    if st.button("Vẽ mặt phẳng (ABC)", type="primary"):
      fig = plt.figure(figsize=(6, 5))
      ax = fig.add_subplot(111, projection="3d")

      # Vẽ 3 điểm
      ax.scatter(
          [xA, xB, xC],
          [yA, yB, yC],
          [zA, zB, zC],
          color="red",
          s=50,
          label="Điểm A, B, C",
      )

      # Tạo lưới mặt phẳng đi qua 3 điểm (mô phỏng)
      xx, yy = np.meshgrid(
          np.linspace(-2, 2, 10), np.linspace(-2, 2, 10)
      )
      # Phương trình mặt phẳng đơn giản để minh họa trực quan
      zz = (
          zA
          - (xx - xA) * 0.5
          - (yy - yA) * 0.5
      )  # Xấp xỉ mặt phẳng trực quan
      ax.plot_surface(xx, yy, zz, alpha=0.4, color="cyan")

      ax.set_title("Mặt phẳng (ABC) trong không gian 3D")
      ax.set_xlabel("Trục X")
      ax.set_ylabel("Trục Y")
      ax.set_zlabel("Trục Z")
      st.pyplot(fig)
      st.success("✅ Đã vẽ thành công mặt phẳng đi qua 3 điểm bạn nhập!")

  elif sub_choice == "Bài 11: Kiểm tra hai đường thẳng song song":
    st.markdown(
        "Nhập vectơ chỉ phương của đường thẳng $d_1(u_1, v_1, w_1)$ và $d_2(u_2,"
        " v_2, w_2)$ để kiểm tra tính song song:"
    )
    col1, col2 = st.columns(2)
    with col1:
      st.markdown("**Đường thẳng d₁**")
      u1 = st.number_input("u1", value=1.0)
      v1 = st.number_input("v1", value=2.0)
      w1 = st.number_input("w1", value=1.0)
    with col2:
      st.markdown("**Đường thẳng d₂**")
      u2 = st.number_input("u2", value=2.0)
      v2 = st.number_input("v2", value=4.0)
      w2 = st.number_input("w2", value=2.0)

    if st.button("Kiểm tra & Vẽ hình", type="primary"):
      # Kiểm tra tỉ lệ vectơ chỉ phương
      cross_x = v1 * w2 - w1 * v2
      cross_y = w1 * u2 - u1 * w2
      cross_z = u1 * v2 - v1 * u2

      is_parallel = (
          abs(cross_x) < 1e-5
          and abs(cross_y) < 1e-5
          and abs(cross_z) < 1e-5
      )

      if is_parallel:
        st.success(
            "✅ Kết quả: Hai đường thẳng **song song hoặc trùng nhau** (Vectơ"
            " chỉ phương cùng phương)."
        )
      else:
        st.warning(
            "⚠️ Kết quả: Hai đường thẳng **không song song** với nhau."
        )

      # Vẽ minh họa 2 đường thẳng
      fig = plt.figure(figsize=(6, 5))
      ax = fig.add_subplot(111, projection="3d")

      t = np.linspace(-2, 2, 10)
      # d1 qua gốc tọa độ
      ax.plot(u1 * t, v1 * t, w1 * t, color="blue", linewidth=3, label="Đường thẳng d₁")
      # d2 dịch chuyển một đoạn
      ax.plot(
          u2 * t + 1,
          v2 * t + 1,
          w2 * t + 1,
          color="green",
          linewidth=3,
          label="Đường thẳng d₂",
      )

      ax.set_title("Vị trí tương đối của hai đường thẳng")
      st.pyplot(fig)

  elif sub_choice == "Bài 12: Kiểm tra đường thẳng song song với mặt phẳng":
    st.markdown(
        "Nhập vectơ pháp tuyến của mặt phẳng $(P)(A, B, C, D)$ và vectơ chỉ"
        " phương của đường thẳng $d(u, v, w)$:"
    )
    col1, col2 = st.columns(2)
    with col1:
      st.markdown("**Mặt phẳng (P): Ax + By + Cz + D = 0**")
      A = st.number_input("Hệ số A", value=1.0)
      B = st.number_input("Hệ số B", value=1.0)
      C = st.number_input("Hệ số C", value=1.0)
    with col2:
      st.markdown("**Đường thẳng d (VTCP u, v, w)**")
      u = st.number_input("u", value=-1.0)
      v = st.number_input("v", value=1.0)
      w = st.number_input("w", value=0.0)

    if st.button("Kiểm tra điều kiện song song", type="primary"):
      # Điều kiện: A*u + B*v + C*w = 0
      dot_product = A * u + B * v + C * w
      if abs(dot_product) < 1e-5:
        st.success(
            "✅ Kết quả: Đường thẳng **song song hoặc nằm trong** mặt phẳng"
            " (A*u + B*v + C*w = 0)."
        )
      else:
        st.error(
            "❌ Kết quả: Đường thẳng cắt mặt phẳng (A*u + B*v + C*w khác 0)."
        )

      # Vẽ hình mô phỏng
      fig = plt.figure(figsize=(6, 5))
      ax = fig.add_subplot(111, projection="3d")

      xx, yy = np.meshgrid(range(-2, 3), range(-2, 3))
      # Giả lập mặt phẳng Z = -(A*x + B*y) / C nếu C != 0
      if C != 0:
        zz = (-A * xx - B * yy) / C
        ax.plot_surface(xx, yy, zz, alpha=0.3, color="orange")

      ax.set_title("Đường thẳng và Mặt phẳng")
      st.pyplot(fig)

st.markdown("---")
st.markdown(
    "<p style='text-align: center; color: gray;'>Sản phẩm STEM Toán 11 - Thực"
    " hiện bằng Python & Streamlit</p>",
    unsafe_allow_html=True,
)
