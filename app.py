import math
import re
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import streamlit as st

# Cấu hình giao diện trang web
st.set_page_config(
    page_title="STEM Toán 11 - Ôn Thi THPT", page_icon="📐", layout="centered"
)

st.title("📐 CHƯƠNG TRÌNH STEM TOÁN 11 & LUYỆN THI THPT")
st.markdown(
    "*Hệ thống học tập, trực quan hóa và luyện thi trắc nghiệm chuẩn cấu trúc"
    " mới.*"
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
        "7. Giới hạn của dãy số (lim)",
        "8. 📝 Thi thử trắc nghiệm chuẩn cấu trúc THPT mới",
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
      value="653 632 609 572 565 535 516 514 508 505 504 504 503 499 496 492",
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
# 7. GIỚI HẠN DÃY SỐ (lim)
# ---------------------------------------------------------
elif menu == "7. Giới hạn của dãy số (lim)":
  st.header("lim Giới hạn của dãy số")
  sub_lim = st.selectbox(
      "Chọn dạng toán:", ["Phân thức đa thức", "Biểu thức chứa căn"], key="m7_sub"
  )

  if sub_lim == "Biểu thức chứa căn":
    a_param = st.number_input(
        "Nhập hệ số a trong lim(sqrt(n² + an) - n):", value=2.0, key="m7_a"
    )
    if st.button("Tính giới hạn", type="primary", key="m7_btn"):
      res = a_param / 2.0
      st.success("🎯 Kết quả tính toán:")
      st.latex(
          f"\\lim \\left(\\sqrt{{n^2 + {a_param}n}} - n\\right) ="
          f" \\frac{{{a_param}}}{{2}} = {res}"
      )
  else:
    st.markdown(
        "Nhập hệ số đa thức của tử và mẫu (từ bậc cao đến thấp, cách nhau bởi"
        " dấu phẩy):"
    )
    num_str = st.text_input("Tử thức:", value="2, 3, 1", key="m7_num")
    den_str = st.text_input("Mẫu thức:", value="1, 4", key="m7_den")

    if st.button("Tính giới hạn", type="primary", key="m7_btn2"):
      try:
        nums = [float(x.strip()) for x in num_str.split(",")]
        dens = [float(x.strip()) for x in den_str.split(",")]
        deg_num = len(nums) - 1
        deg_den = len(dens) - 1

        st.markdown("---")
        st.write(
            f"**Phân tích bậc:** Bậc tử k = {deg_num} | Bậc mẫu m = {deg_den}"
        )

        if deg_num < deg_den:
          st.success("🎯 Kết quả: L = 0")
          st.latex("L = \\lim \\frac{\\text{Tử}}{\\text{Mẫu}} = 0")
        elif deg_num == deg_den:
          ans = nums[0] / dens[0]
          st.success(f"🎯 Kết quả: L = {ans:.4f}")
          st.latex(f"L = \\frac{{{nums[0]}}}{{{dens[0]}}} = {ans:.4f}")
        else:
          sign = "+\\infty" if (nums[0] * dens[0] > 0) else "-\\infty"
          st.success(f"🎯 Kết quả: L = {sign}")
          st.latex(f"L = {sign}")
      except Exception as e:
        st.error(f"❌ Lỗi định dạng đầu vào: {e}")

# ---------------------------------------------------------
# 8. THI THỬ TRẮC NGHIỆM CHUẨN CẤU TRÚC THPT
# ---------------------------------------------------------
elif menu == "8. 📝 Thi thử trắc nghiệm chuẩn cấu trúc THPT mới":
  st.header("📝 Phòng Thi Thử Trắc Nghiệm Toán 11")
  st.markdown(
      "Đề thi chuẩn cấu trúc Bộ GD&ĐT gồm 3 phần: **Phần I** (18 câu trắc nghiệm"
      " nhiều lựa chọn - 4.5đ), **Phần II** (4 câu Đúng/Sai - 4.0đ), **Phần"
      " III** (6 câu trả lời ngắn - 1.5đ)."
  )

  with st.form("exam_form"):
    st.subheader(
        "PHẦN I. Câu trắc nghiệm nhiều phương án lựa chọn (18 câu - 4.5 điểm)"
    )

    p1_questions = [
        {
            "q": (
                "Câu 1: Nghiệm của phương trình $\\sin x = \\frac{1}{2}$ là:"
            ),
            "options": [
                (
                    "A. $x = \\frac{\\pi}{6} + k2\\pi, x ="
                    " \\frac{5\\pi}{6} + k2\\pi$"
                ),
                "B. $x = \\frac{\\pi}{3} + k2\\pi$",
                "C. $x = \\frac{\\pi}{6} + k\\pi$",
                "D. $x = -\\frac{\\pi}{6} + k2\\pi$",
            ],
            "ans": 0,
        },
        {
            "q": "Câu 2: Tập giá trị của hàm số $y = \\cos x$ là:",
            "options": [
                "A. $\\mathbb{R}$",
                "B. $[-1; 1]$",
                "C. $(0; 1)$",
                "D. $[-1; 0]$",
            ],
            "ans": 1,
        },
        {
            "q": (
                "Câu 3: Cho cấp số cộng $(u_n)$ có $u_1 = 3$ và công sai $d ="
                " 2$. Số hạng thứ 5 ($u_5$) bằng:"
            ),
            "options": ["A. 9", "B. 11", "C. 13", "D. 15"],
            "ans": 1,
        },
        {
            "q": (
                "Câu 4: Cho cấp số nhân $(u_n)$ có $u_1 = 2$ và công bội $q ="
                " 3$. Số hạng thứ 3 ($u_3$) bằng:"
            ),
            "options": ["A. 6", "B. 9", "C. 18", "D. 54"],
            "ans": 2,
        },
        {
            "q": "Câu 5: Giới hạn $\\lim \\frac{2n + 1}{n + 3}$ bằng:",
            "options": ["A. 1", "B. 2", "C. $\\frac{1}{3}$", "D. 0"],
            "ans": 1,
        },
        {
            "q": (
                "Câu 6: Giới hạn $\\lim \\frac{n^2 - n + 1}{2n^2 + 3}$ bằng:"
            ),
            "options": ["A. $\\frac{1}{2}$", "B. 1", "C. 0", "D. $+\\infty$"],
            "ans": 0,
        },
        {
            "q": "Câu 7: Đạo hàm của hàm số $y = x^3$ là:",
            "options": ["A. $3x^2$", "B. $x^2$", "C. $3x$", "D. $2x^2$"],
            "ans": 0,
        },
        {
            "q": "Câu 8: Cho hàm số $y = \\sin x$. Đạo hàm $y'$ là:",
            "options": [
                "A. $\\cos x$",
                "B. $-\\cos x$",
                "C. $\\sin x$",
                "D. $-\\sin x$",
            ],
            "ans": 0,
        },
        {
            "q": (
                "Câu 9: Cho hình chóp $S.ABCD$ có đáy $ABCD$ là hình bình hành."
                " Giao tuyến của hai mặt phẳng $(SAB)$ và $(SCD)$ là:"
            ),
            "options": [
                "A. Đường thẳng qua $S$ và song song với $AB$",
                "B. Đường thẳng $SA$",
                "C. Đường thẳng $SB$",
                "D. Đường thẳng qua $S$ và cắt $CD$",
            ],
            "ans": 0,
        },
        {
            "q": (
                "Câu 10: Cho hai đường thẳng phân biệt $a$ và $b$ trong không"
                " gian. Điều kiện nào sau đây khẳng định $a$ và $b$ song song?"
            ),
            "options": [
                "A. $a$ và $b$ không có điểm chung",
                (
                    "B. $a$ và $b$ nằm trong cùng một mặt phẳng và không có"
                    " điểm chung"
                ),
                (
                    "C. $a$ và $b$ cùng song song với mặt phẳng $(P)$"
                ),
                "D. $a$ và $b$ cắt nhau",
            ],
            "ans": 1,
        },
        {
            "q": (
                "Câu 11: Phép chiếu song song biến ba điểm thẳng hàng thành:"
            ),
            "options": [
                "A. Ba điểm thẳng hàng",
                "B. Ba điểm tạo thành một tam giác",
                "C. Hai điểm trùng nhau",
                "D. Ba điểm bất kỳ",
            ],
            "ans": 0,
        },
        {
            "q": (
                "Câu 12: Gieo một con xúc xắc cân đối đồng chất 1 lần. Xác"
                " suất ra mặt số nguyên tố là:"
            ),
            "options": [
                "A. $\\frac{1}{2}$",
                "B. $\\frac{1}{3}$",
                "C. $\\frac{1}{6}$",
                "D. $\\frac{2}{3}$",
            ],
            "ans": 0,
        },
        {
            "q": (
                "Câu 13: Chọn ngẫu nhiên 2 học sinh từ một nhóm gồm 5 nam và"
                " 4 nữ. Số phần tử của không gian mẫu $n(\\Omega)$ là:"
            ),
            "options": [
                "A. $C_9^2 = 36$",
                "B. $A_9^2 = 72$",
                "C. $9$",
                "D. $20$",
            ],
            "ans": 0,
        },
        {
            "q": "Câu 14: Số các chỉnh chập chập 2 của 7 phần tử ($A_7^2$) là:",
            "options": ["A. 42", "B. 21", "C. 49", "D. 14"],
            "ans": 0,
        },
        {
            "q": "Câu 15: Số các tổ hợp chập 3 của 5 phần tử ($C_5^3$) là:",
            "options": ["A. 10", "B. 20", "C. 60", "D. 5"],
            "ans": 0,
        },
        {
            "q": (
                "Câu 16: Khoảng biến thiên của mẫu số liệu: 2, 5, 8, 12, 20"
                " là:"
            ),
            "options": ["A. 18", "B. 20", "C. 2", "D. 10"],
            "ans": 0,
        },
        {
            "q": "Câu 17: Số trung bình của mẫu số liệu 4, 6, 8, 10 là:",
            "options": ["A. 7", "B. 8", "C. 6", "D. 9"],
            "ans": 0,
        },
        {
            "q": "Câu 18: Cho hàm số $f(x) = 2x + 1$. Giá trị của $f'(1)$ bằng:",
            "options": ["A. 2", "B. 1", "C. 3", "D. 0"],
            "ans": 0,
        },
    ]

    p1_answers = []
    for idx, q_item in enumerate(p1_questions):
      ans_choice = st.radio(
          q_item["q"], q_item["options"], key=f"form_p1_q_{idx}"
      )
      p1_answers.append(q_item["options"].index(ans_choice))

    st.subheader(
        "PHẦN II. Câu trắc nghiệm đúng sai (4 câu - 4.0 điểm)"
    )
    st.markdown(
        "*Quy chế tính điểm:* Đúng hết 4 ý = 1.0đ | Sai 1 ý = 0.5đ | Sai 2 ý ="
        " 0.25đ | Sai 3 ý = 0.1đ | Sai 4 ý = 0.0đ"
    )

    p2_data = [
        (
            "Câu 1: Cho hàm số lượng giác $y = \\sin x$.",
            [
                "Hàm số có tập xác định là R",
                "Hàm số là hàm số chẵn",
                "Hàm số có chu kỳ $2\\pi$",
                "Giá trị lớn nhất của hàm số bằng 1",
            ],
        ),
        (
            "Câu 2: Cho cấp số cộng $(u_n)$ có $u_1 = 2, d = 3$.",
            [
                "Số hạng thứ 4 là $11$",
                "Công thức số hạng tổng quát $u_n = 3n - 1$",
                "Tổng 5 số hạng đầu tiên là $40$",
                "Hiệu $u_{10} - u_5 = 15$",
            ],
        ),
        (
            "Câu 3: Về đường thẳng và mặt phẳng trong không gian 3D.",
            [
                (
                    "Nếu đường thẳng $a$ song song với mặt phẳng $(P)$ thì $a$"
                    " không có điểm chung với $(P)$"
                ),
                (
                    "Hai đường thẳng phân biệt không cắt nhau thì song song"
                ),
                (
                    "Nếu ba mặt phẳng cắt nhau theo ba giao tuyến phân biệt"
                    " thì ba giao tuyến đó đồng quy hoặc song song"
                ),
                (
                    "Qua một điểm nằm ngoài mặt phẳng cho trước, vẽ được vô"
                    " số đường thẳng song song với mặt phẳng đó"
                ),
            ],
        ),
        (
            "Câu 4: Về giới hạn và đạo hàm.",
            [
                "$\\lim \\frac{1}{n} = 0$",
                "Đạo hàm của $y = x^2$ tại điểm $x = 1$ bằng $2$",
                "Hàm số $y = \\tan x$ xác định với mọi $x \\in \\mathbb{R}$",
                "$\\lim (2n^2 - n) = +\\infty$",
            ],
        ),
    ]

    p2_choices = []
    standard_p2 = [
        [True, False, True, True],
        [True, True, True, True],
        [True, False, True, False],
        [True, True, False, True],
    ]

    for i, (title, sub_list) in enumerate(p2_data):
      st.markdown(f"**{title}**")
      sub_ans = []
      for j, sub_text in enumerate(sub_list):
        val = st.checkbox(f"Ý {chr(97+j)}) {sub_text}", key=f"form_p2_{i}_{j}")
        sub_ans.append(val)
      p2_choices.append(sub_ans)

    st.subheader(
        "PHẦN III. Câu trắc nghiệm trả lời ngắn (6 câu - 1.5 điểm)"
    )
    p3_questions = [
        (
            "Câu 1: Tính tổng 10 số hạng đầu của cấp số cộng có $u_1 = 1, d ="
            " 2$. (Nhập số nguyên)"
        ),
        (
            "Câu 2: Tính giá trị của giới hạn $\\lim \\frac{3n + 5}{n + 1}$."
            " (Nhập kết quả số)"
        ),
        (
            "Câu 3: Gieo 2 con xúc xắc cân đối. Tính xác suất để tổng số"
            " chấm bằng 7. Nhập số thập phân làm tròn 2 chữ số: 0.17"
        ),
        (
            "Câu 4: Đạo hàm của hàm số $y = 4x^3 - 2x + 1$ tại điểm $x = 1$"
            " bằng bao nhiêu?"
        ),
        (
            "Câu 5: Cho hình chóp có diện tích đáy bằng $6$, chiều cao bằng"
            " $4$. Thể tích khối chóp đó bằng bao nhiêu?"
        ),
        (
            "Câu 6: Giá trị lớn nhất của hàm số $y = 3 \\sin x + 4$ bằng bao"
            " nhiêu?"
        ),
    ]
    standard_p3 = ["100", "3", "0.17", "10", "8", "7"]

    p3_answers = []
    for i, q_text in enumerate(p3_questions):
      val = st.text_input(q_text, key=f"form_p3_{i}")
      p3_answers.append(val.strip())

    submitted = st.form_submit_button(
        "📤 Nộp bài và Chấm điểm ngay", type="primary"
    )

  if submitted:
    # Chấm điểm Phần I
    score_p1 = sum(
        0.25
        for i in range(18)
        if p1_answers[i] == p1_questions[i]["ans"]
    )

    # Chấm điểm Phần II
    score_p2 = 0.0
    for i in range(4):
      correct_count = sum(
          1 for j in range(4) if p2_choices[i][j] == standard_p2[i][j]
      )
      if correct_count == 4:
        score_p2 += 1.0
      elif correct_count == 3:
        score_p2 += 0.50
      elif correct_count == 2:
        score_p2 += 0.25
      elif correct_count == 1:
        score_p2 += 0.10

    # Chấm điểm Phần III
    score_p3 = sum(0.25 for i in range(6) if p3_answers[i] == standard_p3[i])

    total_score = score_p1 + score_p2 + score_p3
    st.markdown("---")
    st.header(f"🏆 KẾT QUẢ BÀI THI THỬ: {total_score:.2f} / 10.0 ĐIỂM")
    st.metric(
        "Điểm Phần I (Trắc nghiệm nhiều lựa chọn)", f"{score_p1:.2f} / 4.5đ"
    )
    st.metric("Điểm Phần II (Đúng / Sai)", f"{score_p2:.2f} / 4.0đ")
    st.metric("Điểm Phần III (Trả lời ngắn)", f"{score_p3:.2f} / 1.5đ")

    if total_score >= 8.0:
      st.balloons()
      st.success("🎉 Xuất sắc! Bạn đạt kết quả loại Giỏi/Xuất sắc.")
    else:
      st.info(
          "💡 Ôn tập thêm kiến thức các phần chưa chính xác để nâng cao điểm"
          " số nhé!"
      )

st.markdown("---")
st.markdown(
    "<p style='text-align: center; color: gray;'>Sản phẩm STEM Toán 11 - Ôn thi"
    " THPT Quốc Gia</p>",
    unsafe_allow_html=True,
)
