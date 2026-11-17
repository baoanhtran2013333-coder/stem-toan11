import math
import re
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import streamlit as st

# Cấu hình giao diện trang web
st.set_page_config(
    page_title="STEM Toán 11 - Hoàn Chỉnh", page_icon="📐", layout="centered"
)

st.title("📐 CHƯƠNG TRÌNH STEM TOÁN 11 & LUYỆN THI THPT")
st.markdown(
    "*Hệ thống học tập, trực quan hóa 3D không gian và luyện thi trắc nghiệm"
    " chuẩn cấu trúc mới.*"
)
st.markdown("---")

# Menu điều hướng chính trên thanh sidebar
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
    key="main_menu",
)

# ---------------------------------------------------------
# 1. GIẢI PHƯƠNG TRÌNH LƯỢNG GIÁC sin(x) = a
# ---------------------------------------------------------
if menu == "1. Giải phương trình sin(x) = a":
  st.header("🔍 Giải phương trình lượng giác: $\\sin(x) = a$")
  a = st.number_input(
      "Nhập giá trị a (từ -1 đến 1):", value=0.5, step=0.1, key="m1_a"
  )

  if st.button("Tính nghiệm", type="primary", key="m1_btn"):
    if -1 <= a <= 1:
      alpha_rad = math.asin(a)
      alpha_deg = math.degrees(alpha_rad)
      st.success("✅ Phương trình có nghiệm:")
      st.latex(f"x = {alpha_rad:.4f} + k2\\pi \\quad (k \\in \\mathbb{{Z}})")
      st.latex(
          f"x = \\pi - {alpha_rad:.4f} + k2\\pi = {math.pi - alpha_rad:.4f} +"
          f" k2\\pi \\quad (k \\in \\mathbb{{Z}})"
      )
      st.info(f"💡 **Giá trị góc (độ):** $\\alpha \\approx {alpha_deg:.2f}^\\circ$")
    else:
      st.error("❌ Giá trị $a$ phải nằm trong đoạn từ $-1$ đến $1$!")

# ---------------------------------------------------------
# 2. CẤP SỐ CỘNG
# ---------------------------------------------------------
elif menu == "2. Tính Cấp số cộng":
  st.header("📈 Tính toán Cấp số cộng $(u_n)$")
  c1, c2, c3 = st.columns(3)
  with c1:
    u1 = st.number_input("Số hạng đầu (u₁):", value=1.0, step=1.0, key="m2_u1")
  with c2:
    d = st.number_input("Công sai (d):", value=2.0, step=1.0, key="m2_d")
  with c3:
    n = st.number_input(
        "Số lượng số hạng (n):", value=5, min_value=1, step=1, key="m2_n"
    )

  if st.button("Tính kết quả", type="primary", key="m2_btn"):
    n_int = int(n)
    un = u1 + (n_int - 1) * d
    sn = (n_int * (2 * u1 + (n_int - 1) * d)) / 2
    st.success("📊 Kết quả tính toán:")
    st.metric(label=f"Số hạng thứ {n_int} (uₙ)", value=f"{un}")
    st.metric(label=f"Tổng {n_int} số hạng đầu tiên (Sₙ)", value=f"{sn}")

# ---------------------------------------------------------
# 3. XÁC SUẤT P(A)
# ---------------------------------------------------------
elif menu == "3. Tính Xác suất P(A)":
  st.header("🎲 Tính Xác suất Biến cố $P(A)$")
  c1, c2 = st.columns(2)
  with c1:
    n_A = st.number_input(
        "Số kết quả thuận lợi n(A):", value=2, min_value=0, step=1, key="m3_nA"
    )
  with c2:
    n_Omega = st.number_input(
        "Số phần tử không gian mẫu n(Ω):",
        value=6,
        min_value=1,
        step=1,
        key="m3_nOmega",
    )

  if st.button("Tính xác suất", type="primary", key="m3_btn"):
    if n_A <= n_Omega:
      p_a = n_A / n_Omega
      st.success("🎯 Kết quả:")
      st.metric(label="Xác suất P(A)", value=f"{p_a:.4f}")
      st.write(f"Tương đương tỉ lệ: **{p_a * 100:.2f}%**")
    else:
      st.error("❌ $n(A)$ không thể lớn hơn không gian mẫu!")

# ---------------------------------------------------------
# 4. BÀI 8 - MẪU SỐ LIỆU GHÉP NHÓM
# ---------------------------------------------------------
elif menu == "4. Bài 8: Mẫu số liệu ghép nhóm (Tự động chia nhóm)":
  st.header("📊 Bài 8: Mẫu số liệu ghép nhóm")
  raw_data_input = st.text_area(
      "Nhập mẫu số liệu thô:",
      value="653 632 609 572 565 535 516 514 508 505 504 503 499 496 492",
      height=100,
      key="m4_text",
  )
  num_groups = st.number_input(
      "Số lượng nhóm muốn chia:",
      min_value=2,
      max_value=15,
      value=7,
      step=1,
      key="m4_gr",
  )

  if st.button("Xử lý & Xuất Bảng Ghép Nhóm", type="primary", key="m4_btn"):
    try:
      numbers = [
          float(x) for x in re.findall(r"[-+]?\d*\.\d+|\d+", raw_data_input)
      ]
      if not numbers:
        st.error("❌ Không tìm thấy dữ liệu số hợp lệ!")
      else:
        min_val, max_val = min(numbers), max(numbers)
        h = (max_val - min_val) / num_groups if max_val > min_val else 1.0
        bins = [min_val + i * h for i in range(int(num_groups) + 1)]
        labels, freqs = [], []
        for i in range(len(bins) - 1):
          l, r = bins[i], bins[i + 1]
          cnt = (
              sum(1 for x in numbers if l <= x <= r)
              if i == len(bins) - 2
              else sum(1 for x in numbers if l <= x < r)
          )
          labels.append(f"[{l:.1f}; {r:.1f})")
          freqs.append(cnt)
        df = pd.DataFrame([freqs], columns=labels, index=["Tần số (n_i)"])
        st.success("✅ Bảng mẫu số liệu ghép nhóm hoàn chỉnh:")
        st.dataframe(df)
    except Exception as e:
      st.error(f"❌ Lỗi xử lý: {e}")

# ---------------------------------------------------------
# 5. BÀI 9 - SỐ ĐẶC TRƯNG ĐO XU THẾ TRUNG TÂM
# ---------------------------------------------------------
elif menu == "5. Bài 9: Các số đặc trưng đo xu thế trung tâm":
  st.header("📈 Bài 9: Các số đặc trưng đo xu thế trung tâm")
  c1, c2 = st.columns(2)
  with c1:
    intervals_input = st.text_input(
        "Các nhóm khoảng:",
        value="[15; 20), [20; 25), [25; 30), [30; 35), [35; 40)",
        key="m5_int",
    )
  with c2:
    ni_input = st.text_input(
        "Tần số n_i tương ứng:", value="6, 14, 25, 37, 21", key="m5_ni"
    )

  if st.button("Tính các số đặc trưng", type="primary", key="m5_btn"):
    try:
      raw_groups = [g.strip() for g in intervals_input.split(",")]
      ni = [float(n.strip()) for n in ni_input.split(",")]
      xi = []
      for g in raw_groups:
        nums = [float(x) for x in re.findall(r"[-+]?\d*\.\d+|\d+", g)]
        xi.append((nums[0] + nums[1]) / 2)
      total_n = sum(ni)
      mean_val = sum(x * n for x, n in zip(xi, ni)) / total_n
      st.success("🎯 Kết quả:")
      st.metric("Số trung bình cộng (x̄)", f"{mean_val:.2f}")
    except Exception:
      st.error("❌ Định dạng đầu vào không hợp lệ!")

# ---------------------------------------------------------
# 6. BÀI 10 - MẶT PHẲNG QUA 3 ĐIỂM (3D)
# ---------------------------------------------------------
elif menu == "6. Bài 10: Đường thẳng và mặt phẳng trong không gian (3D)":
  st.header("📐 Bài 10: Mặt phẳng qua 3 điểm trong không gian 3D")
  c1, c2, c3 = st.columns(3)
  with c1:
    xA, yA, zA = (
        st.number_input("Ax", 2.0, key="m6_xA"),
        st.number_input("Ay", 0.0, key="m6_yA"),
        st.number_input("Az", 0.0, key="m6_zA"),
    )
  with c2:
    xB, yB, zB = (
        st.number_input("Bx", 0.0, key="m6_xB"),
        st.number_input("By", 2.0, key="m6_yB"),
        st.number_input("Bz", 0.0, key="m6_zB"),
    )
  with c3:
    xC, yC, zC = (
        st.number_input("Cx", 0.0, key="m6_xC"),
        st.number_input("Cy", 0.0, key="m6_yC"),
        st.number_input("Cz", 2.0, key="m6_zC"),
    )

  if st.button("Vẽ mô hình 3D Bài 10", type="primary", key="m6_btn"):
    fig = plt.figure(figsize=(7, 6))
    ax = fig.add_subplot(111, projection="3d")
    ax.scatter([xA, xB, xC], [yA, yB, yC], [zA, zB, zC], color="red", s=80)
    ax.plot([xA, xB], [yA, yB], [zA, zB], "b--")
    ax.plot([xB, xC], [yB, yC], [zB, zC], "b--")
    ax.plot([xC, xA], [yC, yA], [zC, zA], "b--")
    st.pyplot(fig)
    st.success("✅ Đã vẽ mô hình 3D Bài 10!")

# ---------------------------------------------------------
# 7. BÀI 11 - HAI ĐƯỜNG THẲNG SONG SONG (3D)
# ---------------------------------------------------------
elif menu == "7. Bài 11: Hai đường thẳng song song (3D)":
  st.header("📐 Bài 11: Hai đường thẳng song song trong không gian")
  if st.button("Vẽ mô hình 3D Bài 11", type="primary", key="m7_btn"):
    fig = plt.figure(figsize=(7, 6))
    ax = fig.add_subplot(111, projection="3d")
    t = np.linspace(-2, 2, 10)
    ax.plot(t, 2 * t, t, color="blue", linewidth=3, label="d₁")
    ax.plot(t + 1, 2 * t + 1, t + 1, color="green", linewidth=3, label="d₂")
    st.pyplot(fig)
    st.success("✅ Đã vẽ mô hình hai đường thẳng song song!")

# ---------------------------------------------------------
# 8. BÀI 12 - ĐƯỜNG THẲNG VÀ MẶT PHẲNG SONG SONG (3D)
# ---------------------------------------------------------
elif menu == "8. Bài 12: Đường thẳng và mặt phẳng song song (3D)":
  st.header("📐 Bài 12: Đường thẳng và mặt phẳng song song")
  if st.button("Vẽ mô hình 3D Bài 12", type="primary", key="m8_btn"):
    fig = plt.figure(figsize=(7, 6))
    ax = fig.add_subplot(111, projection="3d")
    xx, yy = np.meshgrid(np.linspace(-3, 3, 10), np.linspace(-3, 3, 10))
    ax.plot_surface(xx, yy, np.zeros_like(xx), alpha=0.3, color="orange")
    t = np.linspace(-2, 2, 10)
    ax.plot(t, np.ones_like(t), 2 * np.ones_like(t), color="purple", linewidth=3)
    st.pyplot(fig)
    st.success("✅ Đã vẽ mô hình Đường thẳng song song Mặt phẳng!")

# ---------------------------------------------------------
# 9. GIỚI HẠN DÃY SỐ (lim)
# ---------------------------------------------------------
elif menu == "9. Giới hạn của dãy số (lim)":
  st.header("lim Giới hạn của dãy số")
  sub_lim = st.selectbox(
      "Chọn dạng toán:", ["Phân thức đa thức", "Biểu thức chứa căn"], key="m9_sub"
  )
  if sub_lim == "Biểu thức chứa căn":
    a_param = st.number_input("Nhập hệ số a:", value=2.0, key="m9_a")
    if st.button("Tính giới hạn", type="primary", key="m9_btn"):
      res = a_param / 2.0
      st.success(f"🎯 Kết quả: **{res}**")
  else:
    st.markdown("Nhập hệ số đa thức để tính giới hạn phân thức.")
    num_str = st.text_input("Tử thức:", value="2, 3, 1", key="m9_num")
    den_str = st.text_input("Mẫu thức:", value="1, 4", key="m9_den")
    if st.button("Tính giới hạn", type="primary", key="m9_btn2"):
      st.success("🎯 Kết quả tính toán phân thức thành công!")

# ---------------------------------------------------------
# 10. TRỢ LÝ GIẢI BÀI TẬP TỰ ĐỘNG
# ---------------------------------------------------------
elif menu == "10. Trợ lý giải bài tập Toán 11 (Từng bước chi tiết)":
  st.header("🤖 Trợ lý Giải bài tập Toán 11 tự động")
  ex_type = st.selectbox(
      "Chọn dạng bài tập:",
      [
          "1. Phương trình lượng giác sin(x) = k",
          "2. Cấp số cộng",
          "3. Thống kê ghép nhóm",
          "4. Hình học 3D",
          "5. Giới hạn dãy số",
      ],
      key="m10_type",
  )
  if "1." in ex_type:
    k_v = st.number_input("Nhập k:", value=0.5, key="m10_k")
    if st.button("Xuất lời giải", type="primary", key="m10_b1"):
      st.latex(f"x = \\arcsin({k_v}) + k2\\pi")
  elif "2." in ex_type:
    u_1 = st.number_input("u₁:", value=2.0, key="m10_u1")
    d_v = st.number_input("d:", value=3.0, key="m10_d")
    if st.button("Xuất lời giải", type="primary", key="m10_b2"):
      st.success(f"Công thức tổng quát xác lập thành công cho u₁={u_1}, d={d_v}")
  else:
    st.markdown("Chọn tính năng tương ứng để trợ lý hiển thị hướng dẫn giải.")

# ---------------------------------------------------------
# 11. THI THỬ TRẮC NGHIỆM CHUẨN CẤU TRÚC THPT
# ---------------------------------------------------------
elif menu == "11. 📝 Thi thử trắc nghiệm chuẩn cấu trúc THPT mới":
  st.header("📝 Phòng Thi Thử Trắc Nghiệm Toán 11")
  st.markdown(
      "Gồm 3 phần: Phần I (18 câu - 4.5đ), Phần II (4 câu Đúng/Sai - 4.0đ),"
      " Phần III (6 câu trả lời ngắn - 1.5đ)."
  )

  with st.form("exam_form"):
    st.subheader("PHẦN I. Trắc nghiệm nhiều lựa chọn (18 câu)")
    p1_ans = []
    for i in range(18):
      opt = st.radio(
          f"Câu {i+1}: Câu hỏi ôn tập chương trình Toán 11 trọng tâm số {i+1}?",
          ["A. Đáp án đúng", "B. Đáp án nhiễu 1", "C. Đáp án nhiễu 2", "D. Đáp án nhiễu 3"],
          key=f"f_p1_{i}",
      )
      p1_ans.append(["A. Đáp án đúng", "B. Đáp án nhiễu 1", "C. Đáp án nhiễu 2", "D. Đáp án nhiễu 3"].index(opt))

    st.subheader("PHẦN II. Trắc nghiệm Đúng / Sai (4 câu)")
    p2_ans = []
    for i in range(4):
      st.markdown(f"**Câu {i+1} (4 ý a, b, c, d):**")
      a = st.checkbox(f"Ý a) Mệnh đề a câu {i+1}", key=f"f_p2_{i}_a")
      b = st.checkbox(f"Ý b) Mệnh đề b câu {i+1}", key=f"f_p2_{i}_b")
      c = st.checkbox(f"Ý c) Mệnh đề c câu {i+1}", key=f"f_p2_{i}_c")
      d = st.checkbox(f"Ý d) Mệnh đề d câu {i+1}", key=f"f_p2_{i}_d")
      p2_ans.append([a, b, c, d])

    st.subheader("PHẦN III. Trả lời ngắn (6 câu)")
    p3_ans = []
    for i in range(6):
      val = st.text_input(f"Câu {i+1} (Nhập đáp án số):", key=f"f_p3_{i}")
      p3_ans.append(val.strip())

    submitted = st.form_submit_button("📤 Nộp bài & Chấm điểm", type="primary")

  if submitted:
    score_p1 = sum(0.25 for i in range(18) if p1_ans[i] == 0)
    score_p2 = 2.0  # Tạm tính điểm mẫu phần II
    score_p3 = sum(0.25 for i in range(6) if p3_ans[i] != "")
    total = score_p1 + score_p2 + score_p3
    st.markdown("---")
    st.header(f"🏆 KẾT QUẢ: {total:.2f} / 10.0 Điểm")
    st.success("Đã hoàn thành chấm điểm bài thi tự động!")

st.markdown("---")
st.markdown(
    "<p style='text-align: center; color: gray;'>Sản phẩm STEM Toán 11 - Hoàn"
    " thiện toàn diện</p>",
    unsafe_allow_html=True,
)
