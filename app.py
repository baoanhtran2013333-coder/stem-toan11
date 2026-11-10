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
        "4. Hình học không gian (Bài 10, 11, 12)",
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

elif menu == "4. Hình học không gian (Bài 10, 11, 12)":
  st.header("📐 Hình học không gian trực quan sắc nét")

  sub_choice = st.selectbox(
      "Chọn bài học:",
      [
          "Bài 10: Mặt phẳng xác định bởi 3 điểm",
          "Bài 11: Hai đường thẳng song song",
          "Bài 12: Đường thẳng song song với mặt phẳng",
      ],
  )

  if sub_choice == "Bài 10: Mặt phẳng xác định bởi 3 điểm":
    st.markdown(
        "Mô phỏng mặt phẳng đi qua 3 điểm không thẳng hàng $A, B, C$ trong không"
        " gian 3D."
    )

    if st.button("Vẽ hình minh họa rõ nét", type="primary"):
      fig = plt.figure(figsize=(7, 6))
      ax = fig.add_subplot(111, projection="3d")

      # Tọa độ 3 điểm A, B, C
      xA, yA, zA = 1, 0, 0
      xB, yB, zB = 0, 2, 0
      xC, yC, zC = 0, 0, 2

      # Vẽ các điểm và tên điểm
      ax.scatter(
          [xA, xB, xC],
          [yA, yB, yC],
          [zA, zB, zC],
          color="red",
          s=70,
          depthshade=False,
      )
      ax.text(xA + 0.1, yA, zA, "A(1,0,0)", fontsize=11, fontweight="bold", color="red")
      ax.text(xB, yB + 0.1, zB, "B(0,2,0)", fontsize=11, fontweight="bold", color="red")
      ax.text(xC, yC, zC + 0.1, "C(0,0,2)", fontsize=11, fontweight="bold", color="red")

      # Vẽ tam giác ABC khung mặt phẳng
      ax.plot([xA, xB], [yA, yB], [zA, zB], "b--", linewidth=2)
      ax.plot([xB, xC], [yB, yC], [zB, zC], "b--", linewidth=2)
      ax.plot([xC, xA], [yC, yA], [zC, zA], "b--", linewidth=2)

      # Tô màu mặt phẳng minh họa
      xx, yy = np.meshgrid(np.linspace(0, 1.2, 5), np.linspace(0, 1.2, 5))
      zz = 2 - 2 * xx - yy
      ax.plot_surface(xx, yy, zz, alpha=0.35, color="cyan")

      ax.set_title("Mặt phẳng (ABC) trong không gian 3D", fontsize=12, fontweight="bold")
      ax.set_xlabel("Trục X")
      ax.set_ylabel("Trục Y")
      ax.set_zlabel("Trục Z")
      st.pyplot(fig)
      st.success("✅ Đã vẽ mô hình không gian Bài 10 sắc nét thành công!")

  elif sub_choice == "Bài 11: Hai đường thẳng song song":
    st.markdown("Mô phỏng hai đường thẳng song song $d_1 \\parallel d_2$.")

    if st.button("Vẽ hình minh họa rõ nét", type="primary"):
      fig = plt.figure(figsize=(7, 6))
      ax = fig.add_subplot(111, projection="3d")

      t = np.linspace(-1, 3, 10)
      # Đường thẳng d1
      xd1, yd1, zd1 = t, np.zeros_like(t), np.zeros_like(t)
      # Đường thẳng d2 (song song d1)
      xd2, yd2, zd2 = t, np.ones_like(t) * 2, np.ones_like(t) * 1

      ax.plot(xd1, yd1, zd1, color="blue", linewidth=3, label="Đường thẳng d₁")
      ax.plot(xd2, yd2, zd2, color="green", linewidth=3, label="Đường thẳng d₂")

      ax.text(1.5, 0, 0, "d₁", fontsize=12, fontweight="bold", color="blue")
      ax.text(1.5, 2, 1, "d₂ (d₁ || d₂)", fontsize=12, fontweight="bold", color="green")

      ax.set_title("Hai đường thẳng song song trong không gian", fontsize=12, fontweight="bold")
      ax.set_xlabel("Trục X")
      ax.set_ylabel("Trục Y")
      ax.set_zlabel("Trục Z")
      st.pyplot(fig)
      st.success("✅ Đã vẽ mô hình Bài 11 thành công!")

  elif sub_choice == "Bài 12: Đường thẳng song song với mặt phẳng":
    st.markdown("Mô phỏng đường thẳng $d$ song song với mặt phẳng $(\\alpha)$.")

    if st.button("Vẽ hình minh họa rõ nét", type="primary"):
      fig = plt.figure(figsize=(7, 6))
      ax = fig.add_subplot(111, projection="3d")

      # Mặt phẳng
      xx, yy = np.meshgrid(np.linspace(-1, 3, 5), np.linspace(-1, 3, 5))
      zz = np.zeros_like(xx)
      ax.plot_surface(xx, yy, zz, alpha=0.3, color="orange")
      ax.text(1, 1, 0, "Mặt phẳng (α)", fontsize=11, fontweight="bold", color="darkorange")

      # Đường thẳng song song phía trên
      xd = np.linspace(-1, 3, 10)
      yd = np.ones_like(xd) * 1
      zd = np.ones_like(xd) * 2
      ax.plot(xd, yd, zd, color="purple", linewidth=3)
      ax.text(1, 1, 2.1, "Đường thẳng d || (α)", fontsize=11, fontweight="bold", color="purple")

      ax.set_title("Đường thẳng song song với Mặt phẳng", fontsize=12, fontweight="bold")
      ax.set_xlabel("Trục X")
      ax.set_ylabel("Trục Y")
      ax.set_zlabel("Trục Z")
      st.pyplot(fig)
      st.success("✅ Đã vẽ mô hình Bài 12 sắc nét thành công!")

elif menu == "5. Thống kê: Mẫu số liệu ghép nhóm & Xu thế trung tâm (Bài 8, 9)":
  st.header("📊 Thống kê lớp 11: Mẫu số liệu ghép nhóm & Xu thế trung tâm")

  tab1, tab2 = st.tabs(["Bài 8: Mẫu số liệu ghép nhóm", "Bài 9: Các số đặc trưng đo xu thế trung tâm"])

  with tab1:
    st.subheader("Biểu đồ tần số ghép nhóm")
    st.markdown("Nhập các khoảng giá trị (nhóm) và tần số tương ứng để vẽ biểu đồ:")
    
    # Nhập mẫu dữ liệu mẫu
    n_groups = st.number_input("Số lượng nhóm:", min_value=2, max_value=6, value=4, step=1)
    
    groups = []
    frequencies = []
    
    col_a, col_b = st.columns(2)
    for i in range(int(n_groups)):
      with col_a:
        g_name = st.text_input(f"Tên nhóm {i+1} (VD: [10-20]):", value=f"[{i*10}-{(i+1)*10}]", key=f"g_{i}")
      with col_b:
        freq = st.number_input(f"Tần số nhóm {i+1}:", min_value=1, value=5+i*3, key=f"f_{i}")
      groups.append(g_name)
      frequencies.append(freq)

    if st.button("Vẽ biểu đồ tần số", type="primary"):
      fig, ax = plt.subplots(figsize=(7, 4))
      ax.bar(groups, frequencies, color='skyblue', edgecolor='black', width=0.6)
      ax.set_xlabel("Nhóm số liệu", fontweight='bold')
      ax.set_ylabel("Tần số", fontweight='bold')
      ax.set_title("Biểu đồ tần số mẫu số liệu ghép nhóm", fontweight='bold')
      st.pyplot(fig)
      st.success("✅ Đã vẽ biểu đồ tần số thành công!")

  with tab2:
    st.subheader("Tính số trung bình, trung vị và mốt của mẫu số liệu ghép nhóm")
    st.markdown("Nhập các giá trị đại diện $x_i$ và tần số $n_i$ của các nhóm:")

    # Cho phép nhập nhanh chuỗi số liệu
    xi_input = st.text_input("Giá trị đại diện (cách nhau bởi dấu phẩy):", value="15, 25, 35, 45")
    ni_input = st.text_input("Tần số tương ứng (cách nhau bởi dấu phẩy):", value="4, 10, 12, 4")

    if st.button("Tính toán các số đặc trưng", type="primary"):
      try:
        xi = [float(x.strip()) for x in xi_input.split(",")]
        ni = [float(n.strip()) for n in ni_input.split(",")]
        
        if len(xi) != len(ni):
          st.error("❌ Số lượng giá trị đại diện và tần số phải bằng nhau!")
        else:
          total_n = sum(ni)
          mean_val = sum(x * n for x, n in zip(xi, ni)) / total_n

          st.success("🎯 Kết quả các số đặc trưng:")
          st.metric(label="Tổng số phần tử (n)", value=f"{total_n}")
          st.metric(label="Số trung bình cộng ($\\bar{x}$)", value=f"{mean_val:.2f}")
          st.info("💡 **Lưu ý:** Trung vị và mốt đối với số liệu ghép nhóm được xác định dựa vào công thức nội suy trong sách giáo khoa Toán 11.")
      except Exception as e:
        st.error("❌ Vui lòng nhập đúng định dạng số cách nhau bằng dấu phẩy!")

st.markdown("---")
st.markdown(
    "<p style='text-align: center; color: gray;'>Sản phẩm STEM Toán 11 - Thực"
    " hiện bằng Python & Streamlit</p>",
    unsafe_allow_html=True,
)
