import math
import re
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import streamlit as st

st.set_page_config(page_title="STEM Toán 11", page_icon="📐", layout="centered")

st.title("📐 CHƯƠNG TRÌNH STEM TOÁN 11")
st.markdown("*Công cụ hỗ trợ học tập môn Toán lớp 11 trực quan, sinh động.*")
st.markdown("---")

st.sidebar.header("📋 Danh mục bài học")
menu = st.sidebar.selectbox(
    "Chọn bài học:",
    [
        "1. Giải phương trình sin(x) = a",
        "2. Tính Cấp số cộng",
        "3. Tính Xác suất P(A)",
        "4. Bài 8: Mẫu số liệu ghép nhóm (Tự động chia nhóm)",
        "5. Bài 9: Các số đặc trưng đo xu thế trung tâm",
        "6. Bài 10: Đường thẳng và mặt phẳng trong không gian",
        "7. Bài 11: Hai đường thẳng song song",
        "8. Bài 12: Đường thẳng và mặt phẳng song song",
        "9. Giới hạn của dãy số",
        "10. Trợ lý giải bài tập Toán 11 (Tự động giải)",
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
        str_arcsin, str_pi_minus = "0", "\\pi"
      elif abs(a - 0.5) < eps:
        str_arcsin, str_pi_minus = "\\frac{\\pi}{6}", "\\frac{5\\pi}{6}"
      elif abs(a - math.sqrt(2) / 2) < eps:
        str_arcsin, str_pi_minus = "\\frac{\\pi}{4}", "\\frac{3\\pi}{4}"
      elif abs(a - math.sqrt(3) / 2) < eps:
        str_arcsin, str_pi_minus = "\\frac{\\pi}{3}", "\\frac{2\\pi}{3}"
      elif abs(a - 1) < eps:
        str_arcsin, str_pi_minus = "\\frac{\\pi}{2}", "\\frac{\\pi}{2}"
      elif abs(a - (-0.5)) < eps:
        str_arcsin, str_pi_minus = "-\\frac{\\pi}{6}", "\\frac{7\\pi}{6}"
      elif abs(a - (-math.sqrt(2) / 2)) < eps:
        str_arcsin, str_pi_minus = "-\\frac{\\pi}{4}", "\\frac{5\\pi}{4}"
      elif abs(a - (-math.sqrt(3) / 2)) < eps:
        str_arcsin, str_pi_minus = "-\\frac{\\pi}{3}", "\\frac{4\\pi}{3}"
      elif abs(a - (-1)) < eps:
        str_arcsin, str_pi_minus = "-\\frac{\\pi}{2}", "\\frac{3\\pi}{2}"
      else:
        str_arcsin = f"{alpha_rad:.4f}"
        str_pi_minus = f"\\pi - {alpha_rad:.4f}"

      st.success("✅ Phương trình có nghiệm:")
      st.latex(f"x = {str_arcsin} + k2\\pi \\quad (k \\in \\mathbb{{Z}})")
      st.latex(f"x = {str_pi_minus} + k2\\pi \\quad (k \\in \\mathbb{{Z}})")
      st.info(f"💡 **Giá trị góc (deg):** $\\alpha \\approx {alpha_deg:.2f}^\\circ$")
    else:
      st.error("❌ Giá trị $a$ phải nằm trong đoạn từ $-1$ đến $1$!")

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
      st.error("❌ $n(A)$ không thể lớn hơn không gian mẫu!")

elif menu == "4. Bài 8: Mẫu số liệu ghép nhóm (Tự động chia nhóm)":
  st.header("📊 Bài 8: Mẫu số liệu ghép nhóm")
  st.markdown("Dán dãy số liệu thô bất kỳ vào ô bên dưới, hệ thống sẽ tự động chia nhóm có độ dài bằng nhau và xuất ra bảng tần số chuẩn SGK:")

  raw_data_input = st.text_area(
      "Nhập mẫu số liệu thô (cách nhau bằng dấu cách, dấu phẩy hoặc xuống dòng):",
      value="653 632 609 572 565 535 516 514 508 505 504 504 503 499 496 492",
      height=100,
  )

  num_groups = st.number_input(
      "Số lượng nhóm muốn chia:", min_value=2, max_value=15, value=7, step=1
  )

  if st.button("Xử lý & Xuất Bảng Ghép Nhóm", type="primary"):
    try:
      numbers = [float(x) for x in re.findall(r"[-+]?\d*\.\d+|\d+", raw_data_input)]
      if len(numbers) == 0:
        st.error("❌ Không tìm thấy dữ liệu số hợp lệ! Vui lòng kiểm tra lại.")
      else:
        min_val = min(numbers)
        max_val = max(numbers)
        range_val = max_val - min_val
        h = range_val / num_groups if range_val > 0 else 1.0

        st.info(
            f"💡 **Phân tích sơ bộ:** Tổng số phần tử $N = {len(numbers)}$ | "
            f"$\\min = {min_val}$ | $\\max = {max_val}$ | Độ dài mỗi nhóm $h \\approx {h:.2f}$"
        )

        bins = [min_val + i * h for i in range(int(num_groups) + 1)]
        group_labels = []
        frequencies = []

        for i in range(len(bins) - 1):
          left, right = bins[i], bins[i + 1]
          if i == len(bins) - 2:
            count = sum(1 for x in numbers if left <= x <= right)
            label = f"[{left:.1f}; {right:.1f}]"
          else:
            count = sum(1 for x in numbers if left <= x < right)
            label = f"[{left:.1f}; {right:.1f})"
          group_labels.append(label)
          frequencies.append(count)

        table_df = pd.DataFrame(
            [frequencies], columns=group_labels, index=["Tần số (Số lượng)"]
        )
        st.success("✅ Bảng mẫu số liệu ghép nhóm hoàn chỉnh:")
        st.dataframe(table_df)
    except Exception as e:
      st.error(f"❌ Lỗi xử lý dữ liệu: {e}")

elif menu == "5. Bài 9: Các số đặc trưng đo xu thế trung tâm":
  st.header("📈 Bài 9: Các số đặc trưng đo xu thế trung tâm")
  st.markdown("Nhập các nhóm khoảng $[a_i; b_i)$ và tần số $n_i$ để tính **Số trung bình cộng, Trung vị và Mốt**:")

  col1, col2 = st.columns(2)
  with col1:
    intervals_input = st.text_input(
        "Các nhóm khoảng (cách nhau bởi dấu phẩy):",
        value="[15; 20), [20; 25), [25; 30), [30; 35), [35; 40)",
    )
  with col2:
    ni_input = st.text_input(
        "Tần số n_i tương ứng (cách nhau bởi dấu phẩy):",
        value="6, 14, 25, 37, 21",
    )

  if st.button("Tính các số đặc trưng", type="primary"):
    try:
      raw_groups = [g.strip() for g in intervals_input.split(",")]
      ni = [float(n.strip()) for n in ni_input.split(",")]

      if len(raw_groups) != len(ni):
        st.error("❌ Số lượng nhóm và số lượng tần số phải bằng nhau!")
      else:
        xi = []
        bounds = []
        for g in raw_groups:
          nums = [float(x) for x in re.findall(r"[-+]?\d*\.\d+|\d+", g)]
          if len(nums) >= 2:
            bounds.append((nums[0], nums[1]))
            xi.append((nums[0] + nums[1]) / 2)
          else:
            raise ValueError("Định dạng nhóm không hợp lệ")

        total_n = sum(ni)
        mean_val = sum(x * n for x, n in zip(xi, ni)) / total_n

        half_n = total_n / 2
        cum_freq = 0
        me_val = 0
        for i, n_val in enumerate(ni):
          if cum_freq + n_val >= half_n:
            a_p, b_p = bounds[i]
            me_val = a_p + ((half_n - cum_freq) / n_val) * (b_p - a_p)
            break
          cum_freq += n_val

        max_idx = int(np.argmax(ni))
        a_m, b_m = bounds[max_idx]
        n_m = ni[max_idx]
        n_prev = ni[max_idx - 1] if max_idx > 0 else 0
        n_next = ni[max_idx + 1] if max_idx < len(ni) - 1 else 0
        denom = (n_m - n_prev) + (n_m - n_next)
        mo_val = a_m + ((n_m - n_prev) / denom) * (b_m - a_m) if denom != 0 else a_m

        st.success("🎯 Kết quả các số đặc trưng của mẫu số liệu ghép nhóm:")
        c1, c2, c3, c4 = st.columns(4)
        c1.metric("Cỡ mẫu (n)", f"{int(total_n)}")
        c2.metric("Số trung bình (x̄)", f"{mean_val:.2f}")
        c3.metric("Trung vị (Me)", f"{me_val:.2f}")
        c4.metric("Mốt (Mo)", f"{mo_val:.2f}")
    except Exception:
      st.error("❌ Vui lòng nhập đúng định dạng nhóm (VD: [15; 20)) và tần số tương ứng!")

elif menu == "6. Bài 10: Đường thẳng và mặt phẳng trong không gian":
  st.header("📐 Bài 10: Đường thẳng và mặt phẳng trong không gian")
  st.markdown("Nhập tọa độ 3 điểm $A, B, C$ không thẳng hàng để xác định và vẽ mặt phẳng $(\\alpha)$:")

  col1, col2, col3 = st.columns(3)
  with col1:
    xA = st.number_input("Ax", value=2.0)
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

  if st.button("Vẽ mô hình 3D Bài 10", type="primary"):
    pA, pB, pC = np.array([xA, yA, zA]), np.array([xB, yB, zB]), np.array([xC, yC, zC])
    normal = np.cross(pB - pA, pC - pA)

    if np.linalg.norm(normal) < 1e-6:
      st.error("❌ 3 điểm A, B, C thẳng hàng nên không xác định được một mặt phẳng duy nhất!")
    else:
      fig = plt.figure(figsize=(7, 6))
      ax = fig.add_subplot(111, projection="3d")
      ax.scatter([xA, xB, xC], [yA, yB, yC], [zA, zB, zC], color="red", s=80, depthshade=False)
      ax.text(xA, yA, zA, "  A", fontsize=12, fontweight="bold", color="red")
      ax.text(xB, yB, zB, "  B", fontsize=12, fontweight="bold", color="red")
      ax.text(xC, yC, zC, "  C", fontsize=12, fontweight="bold", color="red")

      ax.plot([xA, xB], [yA, yB], [zA, zB], "b--", linewidth=2)
      ax.plot([xB, xC], [yB, yC], [zB, zC], "b--", linewidth=2)
      ax.plot([xC, xA], [yC, yA], [zC, zA], "b--", linewidth=2)

      a_n, b_n, c_n = normal
      d_n = -np.dot(normal, pA)
      lim_min = min(xA, xB, xC, yA, yB, yC) - 1
      lim_max = max(xA, xB, xC, yA, yB, yC) + 1
      xx, yy = np.meshgrid(np.linspace(lim_min, lim_max, 10), np.linspace(lim_min, lim_max, 10))
      if abs(c_n) > 1e-5:
        zz = (-a_n * xx - b_n * yy - d_n) / c_n
        ax.plot_surface(xx, yy, zz, alpha=0.35, color="cyan")

      ax.set_title("Bài 10: Mặt phẳng (ABC) trong không gian 3D", fontsize=12, fontweight="bold")
      ax.set_xlabel("Trục X")
      ax.set_ylabel("Trục Y")
      ax.set_zlabel("Trục Z")
      st.pyplot(fig)
      st.success(f"✅ Phương trình mặt phẳng (ABC): ${a_n:.1f}x + ({b_n:.1f})y + ({c_n:.1f})z + ({d_n:.1f}) = 0$")

elif menu == "7. Bài 11: Hai đường thẳng song song":
  st.header("📐 Bài 11: Hai đường thẳng song song")
  st.markdown("Nhập tọa độ điểm đi qua và vectơ chỉ phương của hai đường thẳng $d_1$ và $d_2$:")

  col1, col2 = st.columns(2)
  with col1:
    st.markdown("**Đường thẳng $d_1$ (qua $M_1$, VTCP $\\vec{u}_1$)**")
    x1, y1, z1 = st.number_input("x₁", value=0.0), st.number_input("y₁", value=0.0), st.number_input("z₁", value=0.0)
    u1, v1, w1 = st.number_input("u₁", value=1.0), st.number_input("v₁", value=2.0), st.number_input("w₁", value=1.0)
  with col2:
    st.markdown("**Đường thẳng $d_2$ (qua $M_2$, VTCP $\\vec{u}_2$)**")
    x2, y2, z2 = st.number_input("x₂", value=1.0), st.number_input("y₂", value=0.0), st.number_input("z₂", value=1.0)
    u2, v2, w2 = st.number_input("u₂", value=2.0), st.number_input("v₂", value=4.0), st.number_input("w₂", value=2.0)

  if st.button("Kiểm tra & Vẽ mô hình 3D Bài 11", type="primary"):
    vec1, vec2 = np.array([u1, v1, w1]), np.array([u2, v2, w2])
    m1_m2 = np.array([x2 - x1, y2 - y1, z2 - z1])

    is_collinear = np.linalg.norm(np.cross(vec1, vec2)) < 1e-5
    is_same_line = is_collinear and (np.linalg.norm(np.cross(m1_m2, vec1)) < 1e-5)

    if is_same_line:
      st.info("ℹ️ Kết luận: Hai đường thẳng **trùng nhau** ($d_1 \\equiv d_2$).")
    elif is_collinear:
      st.success("✅ Kết luận: Hai đường thẳng **song song** ($d_1 \\parallel d_2$).")
    else:
      st.warning("⚠️ Kết luận: Hai đường thẳng **cắt nhau hoặc chéo nhau** (không song song).")

    fig = plt.figure(figsize=(7, 6))
    ax = fig.add_subplot(111, projection="3d")
    t = np.linspace(-2, 2, 10)
    ax.plot(x1 + u1 * t, y1 + v1 * t, z1 + w1 * t, color="blue", linewidth=3, label="Đường thẳng d₁")
    ax.plot(x2 + u2 * t, y2 + v2 * t, z2 + w2 * t, color="green", linewidth=3, label="Đường thẳng d₂")
    ax.legend()
    ax.set_title("Bài 11: Vị trí tương đối hai đường thẳng", fontsize=12, fontweight="bold")
    ax.set_xlabel("Trục X")
    ax.set_ylabel("Trục Y")
    ax.set_zlabel("Trục Z")
    st.pyplot(fig)

elif menu == "8. Bài 12: Đường thẳng và mặt phẳng song song":
  st.header("📐 Bài 12: Đường thẳng và mặt phẳng song song")
  st.markdown("Nhập phương trình mặt phẳng $(P): Ax + By + Cz + D = 0$ và đường thẳng $d$ đi qua $M_0(x_0, y_0, z_0)$, VTCP $\\vec{u}(u, v, w)$:")

  col1, col2 = st.columns(2)
  with col1:
    st.markdown("**Mặt phẳng $(P)$**")
    A = st.number_input("Hệ số A", value=1.0)
    B = st.number_input("Hệ số B", value=1.0)
    C = st.number_input("Hệ số C", value=1.0)
    D = st.number_input("Hệ số D", value=0.0)
  with col2:
    st.markdown("**Đường thẳng $d$**")
    x0, y0, z0 = st.number_input("x₀", value=0.0), st.number_input("y₀", value=0.0), st.number_input("z₀", value=2.0)
    u, v, w = st.number_input("u", value=-1.0), st.number_input("v", value=1.0), st.number_input("w", value=0.0)

  if st.button("Kiểm tra & Vẽ mô hình 3D Bài 12", type="primary"):
    dot_prod = A * u + B * v + C * w
    point_in_plane = abs(A * x0 + B * y0 + C * z0 + D) < 1e-5

    if abs(dot_prod) < 1e-5:
      if point_in_plane:
        st.info("ℹ️ Kết luận: Đường thẳng $d$ **nằm trong** mặt phẳng $(P)$ ($d \\subset (P)$).")
      else:
        st.success("✅ Kết luận: Đường thẳng $d$ **song song** với mặt phẳng $(P)$ ($d \\parallel (P)$).")
    else:
      st.error("❌ Kết luận: Đường thẳng $d$ **cắt** mặt phẳng $(P)$.")

    fig = plt.figure(figsize=(7, 6))
    ax = fig.add_subplot(111, projection="3d")
    xx, yy = np.meshgrid(np.linspace(-3, 3, 10), np.linspace(-3, 3, 10))
    if abs(C) > 1e-5:
      zz = (-A * xx - B * yy - D) / C
      ax.plot_surface(xx, yy, zz, alpha=0.35, color="orange")

    t = np.linspace(-2, 2, 10)
    ax.plot(x0 + u * t, y0 + v * t, z0 + w * t, color="purple", linewidth=3, label="Đường thẳng d")
    ax.scatter([x0], [y0], [z0], color="red", s=60, label="Điểm M₀")
    ax.legend()
    ax.set_title("Bài 12: Đường thẳng và Mặt phẳng trong 3D", fontsize=12, fontweight="bold")
    ax.set_xlabel("Trục X")
    ax.set_ylabel("Trục Y")
    ax.set_zlabel("Trục Z")
    st.pyplot(fig)

elif menu == "9. Giới hạn của dãy số":
  st.header("lim Giới hạn của dãy số")
  st.markdown(
      "Công cụ hỗ trợ tính toán và hướng dẫn giải các dạng giới hạn dãy số"
      " thường gặp ($lim$). Chọn dạng toán bạn muốn khảo sát:"
  )

  sub_limit = st.selectbox(
      "Chọn dạng toán giới hạn:",
      [
          "Dạng 1: Phân thức hữu tỉ (Đa thức trên đa thức)",
          "Dạng 2: Biểu thức chứa căn thức",
      ],
  )

  if sub_limit == "Dạng 1: Phân thức hữu tỉ (Đa thức trên đa thức)":
    st.markdown(
        "Xét giới hạn dạng: $L = \\lim \\frac{a_k n^k + ... + a_0}{b_m n^m +"
        " ... + b_0}$"
    )

    col1, col2 = st.columns(2)
    with col1:
      numer_input = st.text_input(
          "Hệ số tử (từ bậc cao đến thấp, cách nhau bởi phẩy):", value="2, 3, 1"
      )
    with col2:
      denom_input = st.text_input(
          "Hệ số mẫu (từ bậc cao đến thấp, cách nhau bởi phẩy):", value="1, 4"
      )

    if st.button("Tính giới hạn phân thức", type="primary"):
      try:
        numer_coefs = [float(x.strip()) for x in numer_input.split(",")]
        denom_coefs = [float(x.strip()) for x in denom_input.split(",")]

        deg_numer = len(numer_coefs) - 1
        deg_denom = len(denom_coefs) - 1

        st.info(
            f"💡 **Bậc cao nhất của tử:** $k = {deg_numer}$ | **Bậc cao nhất của mẫu:**"
            f" $m = {deg_denom}$"
        )

        lead_numer = numer_coefs[0]
        lead_denom = denom_coefs[0]

        if deg_numer < deg_denom:
          st.success("🎯 Kết quả: **L = 0** (Do bậc tử nhỏ hơn bậc mẫu)")
        elif deg_numer == deg_denom:
          ans = lead_numer / lead_denom
          st.success(
              f"🎯 Kết quả: **L = {lead_numer} / {lead_denom} = {ans:.4f}** (Do"
              " bậc tử bằng bậc mẫu)"
          )
        else:
          sign = "+\\infty" if (lead_numer * lead_denom > 0) else "-\\infty"
          st.success(f"🎯 Kết quả: **L = {sign}** (Do bậc tử lớn hơn bậc mẫu)")
      except Exception as e:
        st.error(f"❌ Lỗi định dạng đầu vào: {e}")

  elif sub_limit == "Dạng 2: Biểu thức chứa căn thức":
    st.markdown(
        "Khảo sát giới hạn dạng cơ bản chứa căn: $\\lim (\\sqrt{n^2 + an} - n)$"
    )
    a_param = st.number_input("Nhập hệ số a:", value=2.0, step=1.0)

    if st.button("Tính giới hạn căn thức", type="primary"):
      result = a_param / 2.0
      st.success("🎯 Kết quả phân tích và tính toán:")
      st.latex(
          f"\\lim (\\sqrt{{n^2 + {a_param}n}} - n) = \\frac{{{a_param}}}{{2}}"
          f" = {result}"
      )
      st.info(
          "💡 **Phương pháp giải:** Sử dụng lượng liên hợp nhân chia với"
          " $(\\sqrt{n^2 + an} + n)$ để khử dạng vô định."
      )

elif menu == "10. Trợ lý giải bài tập Toán 11 (Tự động giải)":
  st.header("🤖 Trợ lý Giải bài tập Toán 11 tự động")
  st.markdown(
      "Chọn dạng bài tập bạn cần giải quyết, nhập đề bài hoặc số liệu, hệ thống"
      " sẽ tự động phân tích và đưa ra lời giải chi tiết từng bước:"
  )

  exercise_type = st.selectbox(
      "Chọn dạng bài toán cần giải:",
      [
          "1. Giải phương trình lượng giác cơ bản",
          "2. Tìm số hạng tổng quát của Cấp số cộng",
          "3. Thống kê: Chuyển dữ liệu thô thành bảng ghép nhóm & Tính số trung bình",
      ],
  )

  if exercise_type == "1. Giải phương trình lượng giác cơ bản":
    st.markdown("---")
    st.markdown("#### Giải phương trình dạng: $a \\sin(x) + b = 0$ hoặc $\\sin(x) = k$")
    eq_val = st.number_input("Nhập giá trị k (trong sin(x) = k):", value=0.5, min_value=-1.0, max_value=1.0, step=0.05)
    
    if st.button("📝 Xuất lời giải chi tiết", type="primary"):
      st.markdown("### 📚 HƯỚNG DẪN LỜI GIẢI CHI TIẾT:")
      st.markdown(f"**Đề bài:** Giải phương trình lượng giác $\\sin(x) = {eq_val}$")
      st.markdown("**Bước 1: Kiểm tra điều kiện có nghiệm**")
      st.markdown(f"Vì $-1 \\le {eq_val} \\le 1$ nên phương trình có nghiệm.")
      
      val_rad = math.asin(eq_val)
      val_deg = math.degrees(val_rad)
      st.markdown("**Bước 2: Sử dụng công thức nghiệm**")
      st.latex(f"\\sin(x) = {eq_val} \\iff \\sin(x) = \\sin({val_rad:.4f})")
      st.markdown("**Bước 3: Viết nghiệm tổng quát**")
      st.latex(f"\\begin{aligned} x &= {val_rad:.4f} + k2\\pi \\quad (k \\in \\mathbb{{Z}}) \\\\ x &= \\pi - {val_rad:.4f} + k2\\pi = {math.pi - val_rad:.4f} + k2\\pi \\quad (k \\in \\mathbb{{Z}}) \\end{aligned}")
      st.success("✅ Đã hoàn thành lời giải bài toán lượng giác!")

  elif exercise_type == "2. Tìm số hạng tổng quát của Cấp số cộng":
    st.markdown("---")
    st.markdown("#### Tìm số hạng $u_n$ và tổng $S_n$ của Cấp số cộng $(u_n)$")
    col_a, col_b, col_c = st.columns(3)
    with col_a:
      ex_u1 = st.number_input("Số hạng đầu u₁:", value=3.0)
    with col_b:
      ex_d = st.number_input("Công sai d:", value=4.0)
    with col_c:
      ex_n = st.number_input("Cần tìm số hạng thứ (n):", value=10, min_value=1, step=1)

    if st.button("📝 Xuất lời giải chi tiết", type="primary"):
      st.markdown("### 📚 HƯỚNG DẪN LỜI GIẢI CHI TIẾT:")
      st.markdown(f"**Đề bài:** Cho cấp số cộng $(u_n)$ có số hạng đầu $u_1 = {ex_u1}$ và công sai $d = {ex_d}$. Tìm số hạng thứ {int(ex_n)} và tổng {int(ex_n)} số hạng đầu tiên.")
      st.markdown("**Bước 1: Áp dụng công thức số hạng tổng quát**")
      st.latex(f"u_n = u_1 + (n-1)d")
      ans_un = ex_u1 + (ex_n - 1) * ex_d
      st.markdown(f"Thay số ta được: $u_{{{int(ex_n)}}} = {ex_u1} + ({int(ex_n)}-1) \\cdot {ex_d} = **{ans_un}**$")
      
      st.markdown("**Bước 2: Áp dụng công thức tính tổng $S_n$**")
      st.latex(f"S_n = \\frac{{n \\cdot (2u_1 + (n-1)d)}}{{2}}")
      ans_sn = (ex_n * (2 * ex_u1 + (ex_n - 1) * ex_d)) / 2
      st.markdown(f"Thay số ta được: $S_{{{int(ex_n)}}} = **{ans_sn}**$")
      st.success("✅ Đã hoàn thành lời giải cấp số cộng!")

  elif exercise_type == "3. Thống kê: Chuyển dữ liệu thô thành bảng ghép nhóm & Tính số trung bình":
    st.markdown("---")
    st.markdown("#### Giải bài tập Thống kê mẫu số liệu ghép nhóm")
    ex_data = st.text_area("Nhập dãy số liệu thô của đề bài:", value="15 18 22 25 28 30 32 35 38 42 45 48 50")
    ex_groups = st.number_input("Số nhóm yêu cầu:", value=4, min_value=2, max_value=10, step=1)

    if st.button("📝 Xuất lời giải chi tiết", type="primary"):
      try:
        nums = [float(x) for x in re.findall(r"[-+]?\d*\.\d+|\d+", ex_data)]
        mn, mx = min(nums), max(nums)
        h_val = (mx - mn) / ex_groups
        st.markdown("### 📚 HƯỚNG DẪN LỜI GIẢI CHI TIẾT:")
        st.markdown(f"- **Cỡ mẫu:** $N = {len(nums)}$")
        st.markdown(f"- **Giá trị nhỏ nhất:** $\\min = {mn}$, **Giá trị lớn nhất:** $\\max = {mx}$")
        st.markdown(f"- **Độ dài mỗi nhóm:** $h = \\frac{{\\max - \\min}}{{\\text{{số nhóm}}}} = \frac{{{mx} - {mn}}}{{{ex_groups}}} = {h_val:.2f}$")
        
        bins = [mn + i * h_val for i in range(int(ex_groups) + 1)]
        labels, freqs = [], []
        for i in range(len(bins) - 1):
          l, r = bins[i], bins[i + 1]
          # Đã sửa lỗi syntax bằng cách viết chuẩn điều kiện logic thông thường
          if i == len(bins) - 2:
            cnt = sum(1 for x in nums if l <= x <= r)
          else:
            cnt = sum(1 for x in nums if l <= x < r)
          labels.append(f"[{l:.1f}; {r:.1f})")
          freqs.append(cnt)

        df_sol = pd.DataFrame([freqs], columns=labels, index=["Tần số (n_i)"])
        st.markdown("**Bảng tần số mẫu số liệu ghép nhóm:**")
        st.dataframe(df_sol)
        st.success("✅ Đã tự động lập bảng và giải chi tiết bài toán thống kê!")
      except Exception as e:
        st.error(f"❌ Lỗi xử lý dữ liệu: {e}")

st.markdown("---")
st.markdown(
    "<p style='text-align: center; color: gray;'>Sản phẩm STEM Toán 11 - Thực"
    " hiện bằng Python & Streamlit</p>",
    unsafe_allow_html=True,
)
