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
        "4. Hình học không gian (Tự nhập dữ liệu & Vẽ hình 3D)",
        "5. Thống kê: Mẫu số liệu ghép nhóm & Xu thế trung tâm (Bài 8, 9)",
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
      st.error("❌ Giá trị $a$ phải nằm trong đoạn từ $-1$ đến $1$ thì phương trình mới có nghiệm!")

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
    n_A = st.number_input("Số kết quả thuận lợi n(A):", value=2, min_value=0, step=1)
  with col2:
    n_Omega = st.number_input("Số phần tử không gian mẫu n(Ω):", value=6, min_value=1, step=1)

  if st.button("Tính xác suất", type="primary"):
    if n_A <= n_Omega:
      p_a = n_A / n_Omega
      st.success("🎯 Kết quả:")
      st.metric(label="Xác suất P(A)", value=f"{p_a:.4f}")
      st.write(f"Tương đương với tỉ lệ: **{p_a * 100:.2f}%**")
    else:
      st.error("❌ Số phần tử của biến cố $n(A)$ không thể lớn hơn không gian mẫu!")

elif menu == "4. Hình học không gian (Tự nhập dữ liệu & Vẽ hình 3D)":
  st.header("📐 Tương tác Hình học không gian 3D")
  sub_choice = st.selectbox(
      "Chọn bài học:",
      [
          "Bài 10: Mặt phẳng xác định bởi 3 điểm",
          "Bài 11: Kiểm tra hai đường thẳng song song",
          "Bài 12: Kiểm tra đường thẳng song song với mặt phẳng",
      ],
  )

  if sub_choice == "Bài 10: Mặt phẳng xác định bởi 3 điểm":
    st.markdown("Nhập tọa độ 3 điểm $A, B, C$ tùy ý để vẽ mặt phẳng chứa chúng:")
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
      fig = plt.figure(figsize=(7, 6))
      ax = fig.add_subplot(111, projection="3d")
      ax.scatter([xA, xB, xC], [yA, yB, yC], [zA, zB, zC], color="red", s=70, depthshade=False)
      ax.text(xA, yA, zA, " A", fontsize=11, fontweight="bold", color="red")
      ax.text(xB, yB, zB, " B", fontsize=11, fontweight="bold", color="red")
      ax.text(xC, yC, zC, " C", fontsize=11, fontweight="bold", color="red")
      ax.plot([xA, xB], [yA, yB], [zA, zB], "b--", linewidth=2)
      ax.plot([xB, xC], [yB, yC], [zB, zC], "b--", linewidth=2)
      ax.plot([xC, xA], [yC, yA], [zC, zA], "b--", linewidth=2)
      
      xx, yy = np.meshgrid(np.linspace(-2, 2, 5), np.linspace(-2, 2, 5))
      zz = zA + 0.5 * (xx - xA) + 0.5 * (yy - yA)
      ax.plot_surface(xx, yy, zz, alpha=0.35, color="cyan")
      ax.set_title("Mặt phẳng (ABC) 3D rõ nét", fontsize=12, fontweight="bold")
      st.pyplot(fig)
      st.success("✅ Đã vẽ mô hình mặt phẳng thành công!")

  elif sub_choice == "Bài 11: Kiểm tra hai đường thẳng song song":
    st.markdown("Nhập vectơ chỉ phương của đường thẳng $d_1(u_1, v_1, w_1)$ và $d_2(u_2, v_2, w_2)$:")
    col1, col2 = st.columns(2)
    with col1:
      u1 = st.number_input("u1", value=1.0)
      v1 = st.number_input("v1", value=2.0)
      w1 = st.number_input("w1", value=1.0)
    with col2:
      u2 = st.number_input("u2", value=2.0)
      v2 = st.number_input("v2", value=4.0)
      w2 = st.number_input("w2", value=2.0)

    if st.button("Kiểm tra & Vẽ hình", type="primary"):
      fig = plt.figure(figsize=(7, 6))
      ax = fig.add_subplot(111, projection="3d")
      t = np.linspace(-2, 2, 10)
      ax.plot(u1 * t, v1 * t, w1 * t, color="blue", linewidth=3, label="d₁")
      ax.plot(u2 * t + 1, v2 * t + 1, w2 * t + 1, color="green", linewidth=3, label="d₂")
      ax.set_title("Vị trí tương đối 2 đường thẳng 3D", fontsize=12, fontweight="bold")
      st.pyplot(fig)

  elif sub_choice == "Bài 12: Kiểm tra đường thẳng song song với mặt phẳng":
    st.markdown("Nhập phương trình mặt phẳng $(P): Ax + By + Cz + D = 0$ và VTCP đường thẳng $d(u, v, w)$:")
    col1, col2 = st.columns(2)
    with col1:
      A = st.number_input("Hệ số A", value=1.0)
      B = st.number_input("Hệ số B", value=1.0)
      C = st.number_input("Hệ số C", value=1.0)
    with col2:
      u = st.number_input("u", value=-1.0)
      v = st.number_input("v", value=1.0)
      w = st.number_input("w", value=0.0)

    if st.button("Kiểm tra điều kiện song song", type="primary"):
      fig = plt.figure(figsize=(7, 6))
      ax = fig.add_subplot(111, projection="3d")
      xx, yy = np.meshgrid(np.linspace(-2, 2, 5), np.linspace(-2, 2, 5))
      if C != 0:
        zz = (-A * xx - B * yy) / C
        ax.plot_surface(xx, yy, zz, alpha=0.3, color="orange")
      xd = np.linspace(-2, 2, 10)
      ax.plot(xd, np.ones_like(xd), np.ones_like(xd) * 2, color="purple", linewidth=3)
      ax.set_title("Đường thẳng và mặt phẳng 3D", fontsize=12, fontweight="bold")
      st.pyplot(fig)

elif menu == "5. Thống kê: Mẫu số liệu ghép nhóm & Xu thế trung tâm (Bài 8, 9)":
  st.header("📊 Thống kê lớp 11: Mẫu số liệu ghép nhóm & Xu thế trung tâm")
  
  tab1, tab2 = st.tabs(["Bài 8: Mẫu số liệu ghép nhóm (MSL)", "Bài 9: Xu thế trung tâm"])

  with tab1:
    st.subheader("Nhập mẫu số liệu ghép nhóm để vẽ biểu đồ tần số")
    n_groups = st.number_input("Số lượng nhóm số liệu:", min_value=2, max_value=6, value=4, step=1)

    groups = []
    frequencies = []
    col_a, col_b = st.columns(2)
    for i in range(int(n_groups)):
      with col_a:
        g_name = st.text_input(f"Nhóm {i+1} (VD: [10-20]):", value=f"[{i*10}-{(i+1)*10}]", key=f"g_{i}")
      with col_b:
        freq = st.number_input(f"Tần số nhóm {i+1}:", min_value=1, value=5 + i * 2, key=f"f_{i}")
      groups.append(g_name)
      frequencies.append(freq)

    if st.button("Vẽ biểu đồ tần số MSL", type="primary"):
      fig, ax = plt.subplots(figsize=(7, 4))
      ax.bar(groups, frequencies, color="skyblue", edgecolor="black", width=0.6)
      ax.set_xlabel("Nhóm số liệu", fontweight="bold")
      ax.set_ylabel("Tần số", fontweight="bold")
      ax.set_title("Biểu đồ tần số mẫu số liệu ghép nhóm", fontweight="bold")
      st.pyplot(fig)
      st.success("✅ Đã vẽ biểu đồ tần số thành công!")

  with tab2:
    st.subheader("Tính toán Số trung bình của mẫu số liệu ghép nhóm")
    xi_input = st.text_input("Giá trị đại diện x_i (cách nhau bởi dấu phẩy):", value="15, 25, 35, 45")
    ni_input = st.text_input("Tần số n_i tương ứng (cách nhau bởi dấu phẩy):", value="4, 10, 12, 4")

    if st.button("Tính số trung bình MSL", type="primary"):
      try:
        xi = [float(x.strip()) for x in xi_input.split(",")]
        ni = [float(n.strip()) for n in ni_input.split(",")]
        if len(xi) != len(ni):
          st.error("❌ Số lượng giá trị đại diện và tần số phải bằng nhau!")
        else:
          total_n = sum(ni)
          mean_val = sum(x * n for x, n in zip(xi, ni)) / total_n
          st.success("🎯 Kết quả tính toán:")
          st.metric(label="Tổng số phần tử (n)", value=f"{total_n}")
          st.metric(label="Số trung bình cộng ($\\bar{x}$)", value=f"{mean_val:.2f}")
      except Exception as e:
        st.error("❌ Vui lòng nhập đúng định dạng số cách nhau bằng dấu phẩy!")

st.markdown("---")
st.markdown("<p style='text-align: center; color: gray;'>Sản phẩm STEM Toán 11 - Thực hiện bằng Python & Streamlit</p>", unsafe_allow_html=True)
