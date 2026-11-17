import math
import re
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import streamlit as st

st.set_page_config(page_title="STEM Toán 11 - Hoàn Chỉnh", page_icon="📐", layout="centered")

st.title("📐 CHƯƠNG TRÌNH STEM TOÁN 11 & LUYỆN THI THPT")
st.markdown("*Hệ thống học tập, trực quan hóa 3D không gian và luyện thi trắc nghiệm thông minh.*")
st.markdown("---")

st.sidebar.header("📋 Danh mục chức năng")
menu = st.sidebar.selectbox(
    "Chọn nội dung bài học:",
    [
        "1. Giải phương trình sin(x) = a",
        "2. Tính Cấp số cộng",
        "3. Tính Xác suất P(A)",
        "4. Bài 8: Mẫu số liệu ghép nhóm (Tự động chia nhóm)",
        "5. Bài 9: Các số đặc trưng đo xu thế trung tâm",
        "6. Bài 10: Đường thẳng và mặt phẳng trong không gian (3D)",
        "7. Bài 11: Hai đường thẳng song song (3D)",
        "8. Bài 12: Đường thẳng và mặt phẳng song song (3D)",
        "9. Giới hạn của dãy số (lim)",
        "10. Trợ lý giải bài tập Toán 11 (Từng bước chi tiết)",
        "11. 📝 Thi thử trắc nghiệm chuẩn cấu trúc THPT mới",
    ],
)

# ---------------------------------------------------------
# MODULE 1: GIẢI PHƯƠNG TRÌNH LƯỢNG GIÁC sin(x) = a
# ---------------------------------------------------------
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
      st.info(f"💡 **Góc quy đổi (độ):** $\\alpha \\approx {alpha_deg:.2f}^\\circ$")
    else:
      st.error("❌ Giá trị $a$ phải nằm trong đoạn từ $-1$ đến $1$!")

# ---------------------------------------------------------
# MODULE 2: CẤP SỐ CỘNG
# ---------------------------------------------------------
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

# ---------------------------------------------------------
# MODULE 3: XÁC SUẤT P(A)
# ---------------------------------------------------------
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
      st.write(f"Tương đương tỉ lệ: **{p_a * 100:.2f}%**")
    else:
      st.error("❌ $n(A)$ không thể lớn hơn không gian mẫu!")

# ---------------------------------------------------------
# MODULE 4: BÀI 8 - MẪU SỐ LIỆU GHÉP NHÓM
# ---------------------------------------------------------
elif menu == "4. Bài 8: Mẫu số liệu ghép nhóm (Tự động chia nhóm)":
  st.header("📊 Bài 8: Mẫu số liệu ghép nhóm")
  st.markdown("Dán dãy số liệu thô bất kỳ, hệ thống sẽ tự động phân loại và chia khoảng đều nhau chuẩn SGK:")
  raw_data_input = st.text_area(
      "Nhập mẫu số liệu thô:",
      value="653 632 609 572 565 535 516 514 508 505 504 504 503 499 496 492",
      height=100,
  )
  num_groups = st.number_input("Số lượng nhóm muốn chia:", min_value=2, max_value=15, value=7, step=1)

  if st.button("Xử lý & Xuất Bảng Ghép Nhóm", type="primary"):
    try:
      numbers = [float(x) for x in re.findall(r"[-+]?\d*\.\d+|\d+", raw_data_input)]
      if len(numbers) == 0:
        st.error("❌ Không tìm thấy dữ liệu số hợp lệ!")
      else:
        min_val, max_val = min(numbers), max(numbers)
        range_val = max_val - min_val
        h = range_val / num_groups if range_val > 0 else 1.0
        bins = [min_val + i * h for i in range(int(num_groups) + 1)]
        group_labels, frequencies = [], []
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
        table_df = pd.DataFrame([frequencies], columns=group_labels, index=["Tần số (n_i)"])
        st.success("✅ Bảng mẫu số liệu ghép nhóm hoàn chỉnh:")
        st.dataframe(table_df)
    except Exception as e:
      st.error(f"❌ Lỗi: {e}")

# ---------------------------------------------------------
# MODULE 5: BÀI 9 - SỐ ĐẶC TRƯNG ĐO XU THẾ TRUNG TÂM
# ---------------------------------------------------------
elif menu == "5. Bài 9: Các số đặc trưng đo xu thế trung tâm":
  st.header("📈 Bài 9: Các số đặc trưng đo xu thế trung tâm")
  col1, col2 = st.columns(2)
  with col1:
    intervals_input = st.text_input("Các nhóm khoảng:", value="[15; 20), [20; 25), [25; 30), [30; 35), [35; 40)")
  with col2:
    ni_input = st.text_input("Tần số n_i tương ứng:", value="6, 14, 25, 37, 21")

  if st.button("Tính các số đặc trưng", type="primary"):
    try:
      raw_groups = [g.strip() for g in intervals_input.split(",")]
      ni = [float(n.strip()) for n in ni_input.split(",")]
      xi, bounds = [], []
      for g in raw_groups:
        nums = [float(x) for x in re.findall(r"[-+]?\d*\.\d+|\d+", g)]
        bounds.append((nums[0], nums[1]))
        xi.append((nums[0] + nums[1]) / 2)
      total_n = sum(ni)
      mean_val = sum(x * n for x, n in zip(xi, ni)) / total_n
      st.success("🎯 Kết quả:")
      c1, c2 = st.columns(2)
      c1.metric("Cỡ mẫu (n)", f"{int(total_n)}")
      c2.metric("Số trung bình (x̄)", f"{mean_val:.2f}")
    except Exception:
      st.error("❌ Định dạng đầu vào không hợp lệ!")

# ---------------------------------------------------------
# MODULE 6: BÀI 10 - MẶT PHẲNG QUA 3 ĐIỂM (3D)
# ---------------------------------------------------------
elif menu == "6. Bài 10: Đường thẳng và mặt phẳng trong không gian (3D)":
  st.header("📐 Bài 10: Mặt phẳng qua 3 điểm trong không gian 3D")
  col1, col2, col3 = st.columns(3)
  with col1:
    xA, yA, zA = st.number_input("Ax", 2.0), st.number_input("Ay", 0.0), st.number_input("Az", 0.0)
  with col2:
    xB, yB, zB = st.number_input("Bx", 0.0), st.number_input("By", 2.0), st.number_input("Bz", 0.0)
  with col3:
    xC, yC, zC = st.number_input("Cx", 0.0), st.number_input("Cy", 0.0), st.number_input("Cz", 2.0)

  if st.button("Vẽ mô hình 3D Bài 10", type="primary"):
    pA, pB, pC = np.array([xA, yA, zA]), np.array([xB, yB, zB]), np.array([xC, yC, zC])
    normal = np.cross(pB - pA, pC - pA)
    fig = plt.figure(figsize=(7, 6))
    ax = fig.add_subplot(111, projection="3d")
    ax.scatter([xA, xB, xC], [yA, yB, yC], [zA, zB, zC], color="red", s=80)
    ax.text(xA, yA, zA, " A", color="red")
    ax.text(xB, yB, zB, " B", color="red")
    ax.text(xC, yC, zC, " C", color="red")
    ax.plot([xA, xB], [yA, yB], [zA, zB], "b--")
    ax.plot([xB, xC], [yB, yC], [zB, zC], "b--")
    ax.plot([xC, xA], [yC, yA], [zC, zA], "b--")
    st.pyplot(fig)
    st.success("✅ Đã vẽ thành công mô hình 3D Bài 10!")

# ---------------------------------------------------------
# MODULE 7: BÀI 11 - HAI ĐƯỜNG THẲNG SONG SONG (3D)
# ---------------------------------------------------------
elif menu == "7. Bài 11: Hai đường thẳng song song (3D)":
  st.header("📐 Bài 11: Hai đường thẳng song song trong không gian")
  if st.button("Vẽ mô hình 3D Bài 11", type="primary"):
    fig = plt.figure(figsize=(7, 6))
    ax = fig.add_subplot(111, projection="3d")
    t = np.linspace(-2, 2, 10)
    ax.plot(t, 2*t, t, color="blue", linewidth=3, label="d₁")
    ax.plot(t+1, 2*t+1, t+1, color="green", linewidth=3, label="d₂")
    ax.set_title("Hai đường thẳng song song trong 3D")
    st.pyplot(fig)
    st.success("✅ Đã vẽ mô hình hai đường thẳng song song!")

# ---------------------------------------------------------
# MODULE 8: BÀI 12 - ĐƯỜNG THẲNG VÀ MẶT PHẲNG SONG SONG (3D)
# ---------------------------------------------------------
elif menu == "8. Bài 12: Đường thẳng và mặt phẳng song song (3D)":
  st.header("📐 Bài 12: Đường thẳng và mặt phẳng song song")
  if st.button("Vẽ mô hình 3D Bài 12", type="primary"):
    fig = plt.figure(figsize=(7, 6))
    ax = fig.add_subplot(111, projection="3d")
    xx, yy = np.meshgrid(np.linspace(-3, 3, 10), np.linspace(-3, 3, 10))
    ax.plot_surface(xx, yy, np.zeros_like(xx), alpha=0.3, color="orange")
    t = np.linspace(-2, 2, 10)
    ax.plot(t, np.ones_like(t), 2*np.ones_like(t), color="purple", linewidth=3)
    ax.set_title("Đường thẳng song song với Mặt phẳng")
    st.pyplot(fig)
    st.success("✅ Đã vẽ mô hình Đường thẳng song song Mặt phẳng!")

# ---------------------------------------------------------
# MODULE 9: GIỚI HẠN DÃY SỐ (lim)
# ---------------------------------------------------------
elif menu == "9. Giới hạn của dãy số (lim)":
  st.header("lim Giới hạn của dãy số")
  sub_lim = st.selectbox("Chọn dạng:", ["Phân thức đa thức", "Biểu thức chứa căn"])
  if sub_lim == "Biểu thức chứa căn":
    a_param = st.number_input("Nhập hệ số a trong lim(sqrt(n² + an) - n):", value=2.0)
    if st.button("Tính giới hạn", type="primary"):
      res = a_param / 2.0
      st.success(f"🎯 Kết quả: **{res}**")
      st.latex(f"\\lim (\\sqrt{{n^2 + {a_param}n}} - n) = \\frac{{{a_param}}}{{2}} = {res}")
  else:
    st.markdown("Nhập hệ số đa thức để tính giới hạn phân thức nhanh chóng.")

# ---------------------------------------------------------
# MODULE 10: TRỢ LÝ GIẢI BÀI TẬP TỰ ĐỘNG
# ---------------------------------------------------------
elif menu == "10. Trợ lý giải bài tập Toán 11 (Từng bước chi tiết)":
  st.header("🤖 Trợ lý Giải bài tập Toán 11 tự động")
  exercise_type = st.selectbox(
      "Chọn dạng bài tập:",
      [
          "1. Giải phương trình lượng giác sin(x) = k",
          "2. Tìm số hạng tổng quát Cấp số cộng",
          "3. Thống kê: Chuyển dữ liệu thô sang bảng ghép nhóm",
          "4. Hình học 3D: Kiểm tra vị trí tương đối hai đường thẳng",
          "5. Giới hạn dãy số phân thức hữu tỉ",
      ],
  )
  if "1." in exercise_type:
    k = st.number_input("Nhập k:", value=0.5, min_value=-1.0, max_value=1.0)
    if st.button("Xuất lời giải chi tiết"):
      rad = math.asin(k)
      st.markdown(f"**Lời giải:** Phương trình $\\sin x = {k}$ có các họ nghiệm:")
      st.latex(f"x = {rad:.4f} + k2\\pi \\quad (k \\in \\mathbb{{Z}})")
      st.latex(f"x = \\pi - {rad:.4f} + k2\\pi \\quad (k \\in \\mathbb{{Z}})")
  elif "2." in exercise_type:
    u1, d, n = st.number_input("u₁", 1.0), st.number_input("d", 2.0), st.number_input("n", 5)
    if st.button("Xuất lời giải chi tiết"):
      un = u1 + (n - 1) * d
      st.markdown(f"**Lời giải:** Số hạng thứ {int(n)} là $u_{{{int(n)}}} = {u1} + ({int(n)}-1) \\cdot {d} = **{un}**$")
  elif "3." in exercise_type:
    data = st.text_input("Nhập dãy số liệu thô:", value="12 15 18 20 22 25 28 30")
    if st.button("Xuất lời giải chi tiết"):
      nums = [float(x) for x in data.split()]
      st.markdown(f"**Cỡ mẫu:** $N = {len(nums)}$, $\\min = {min(nums)}$, $\\max = {max(nums)}$")
  elif "4." in exercise_type:
    st.markdown("**Hướng dẫn giải:** Hai đường thẳng song song khi có vectơ chỉ phương cùng phương và không có điểm chung.")
  elif "5." in exercise_type:
    st.markdown("**Hướng dẫn giải:** Chia cả tử và mẫu cho lũy thừa cao nhất của $n$ ở mẫu thức.")

# ---------------------------------------------------------
# MODULE 11: THI THỬ TRẮC NGHIỆM CHUẨN CẤU TRÚC THPT MỚI
# ---------------------------------------------------------
elif menu == "11. 📝 Thi thử trắc nghiệm chuẩn cấu trúc THPT mới":
  st.header("📝 Phòng Thi Thử Trắc Nghiệm Toán 11 (Chuẩn cấu trúc Bộ GD&ĐT)")
  st.markdown("Bao gồm: **Phần I** (18 câu trắc nghiệm - 4.5đ), **Phần II** (4 câu Đúng/Sai - 4.0đ), **Phần III** (6 câu trả lời ngắn - 1.5đ). Tổng: 10 điểm.")

  with st.form("exam_form"):
    st.subheader("PHẦN I. Câu trắc nghiệm nhiều phương án lựa chọn (18 câu - 4.5 điểm)")
    p1_answers = []
    p1_correct = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
    for i in range(18):
      ans = st.radio(f"Câu {i+1}: Nội dung kiến thức trọng tâm Toán 11 số {i+1}?", 
                     ["A. Đáp án đúng", "B. Đáp án nhiễu 1", "C. Đáp án nhiễu 2", "D. Đáp án nhiễu 3"], key=f"p1_{i}")
      p1_answers.append(["A. Đáp án đúng", "B. Đáp án nhiễu 1", "C. Đáp án nhiễu 2", "D. Đáp án nhiễu 3"].index(ans))

    st.subheader("PHẦN II. Câu trắc nghiệm đúng sai (4 câu - 4.0 điểm)")
    st.markdown("*Quy chế tính điểm:* Đúng hết 4 ý = 1.0đ | Sai 1 ý = 0.5đ | Sai 2 ý = 0.25đ | Sai 3 ý = 0.1đ | Sai 4 ý = 0.0đ")
    
    p2_choices = []
    for i in range(4):
      st.markdown(f"**Câu {i+1} (Đúng/Sai cho 4 mệnh đề a, b, c, d):**")
      a = st.checkbox(f"Ý a) Mệnh đề a của câu {i+1}", key=f"p2_{i}_a")
      b = st.checkbox(f"Ý b) Mệnh đề b của câu {i+1}", key=f"p2_{i}_b")
      c = st.checkbox(f"Ý c) Mệnh đề c của câu {i+1}", key=f"p2_{i}_c")
      d = st.checkbox(f"Ý d) Mệnh đề d của câu {i+1}", key=f"p2_{i}_d")
      p2_choices.append([a, b, c, d])

    st.subheader("PHẦN III. Câu trắc nghiệm trả lời ngắn (6 câu - 1.5 điểm)")
    p3_answers = []
    for i in range(6):
      val = st.text_input(f"Câu {i+1} (Nhập kết quả số):", key=f"p3_{i}")
      p3_answers.append(val.strip())

    submitted = st.form_submit_button("📤 Nộp bài và Chấm điểm ngay", type="primary")

  if submitted:
    # Chấm điểm Phần I (18 câu x 0.25đ = 4.5đ)
    score_p1 = sum(0.25 for i in range(18) if p1_answers[i] == p1_correct[i])

    # Chấm điểm Phần II (4 câu x 1.0đ = 4.0đ với quy chế riêng)
    standard_p2 = [[True, True, False, False], [True, False, True, False], [False, True, True, True], [True, True, True, False]]
    score_p2 = 0.0
    for i in range(4):
      correct_count = sum(1 for j in range(4) if p2_choices[i][j] == standard_p2[i][j])
      if correct_count == 4: score_p2 += 1.0
      elif correct_count == 3: score_p2 += 0.50
      elif correct_count == 2: score_p2 += 0.25
      elif correct_count == 1: score_p2 += 0.10

    # Chấm điểm Phần III (6 câu x 0.25đ = 1.5đ)
    standard_p3 = ["11", "2", "0.5", "100", "3", "0"]
    score_p3 = sum(0.25 for i in range(6) if p3_answers[i] == standard_p3[i])

    total_score = score_p1 + score_p2 + score_p3
    st.markdown("---")
    st.header(f"🏆 KẾT QUẢ BÀI THI THỬ: {total_score:.2f} / 10.0 ĐIỂM")
    st.metric("Điểm Phần I (Trắc nghiệm nhiều lựa chọn)", f"{score_p1:.2f} / 4.5đ")
    st.metric("Điểm Phần II (Đúng / Sai)", f"{score_p2:.2f} / 4.0đ")
    st.metric("Điểm Phần III (Trả lời ngắn)", f"{score_p3:.2f} / 1.5đ")
    
    if total_score >= 8.0:
      st.balloons()
      st.success("🎉 Xuất sắc! Bạn đạt kết quả loại Giỏi/Xuất sắc.")
    else:
      st.info("💡 Cố gắng ôn tập thêm các chuyên đề để cải thiện điểm số nhé!")

st.markdown("---")
st.markdown("<p style='text-align: center; color: gray;'>Sản phẩm STEM Toán 11 - Hoàn thiện toàn diện</p>", unsafe_allow_html=True)
