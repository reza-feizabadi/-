import random                       # random فراخوانی کتابخانه
import matplotlib.pyplot as plt     # matplotlib فراخوانی کتابخانه

# تعداد نقاط
num_points = 100000

# نقاط اولیه
x, y = 0, 0
x_vals, y_vals = [], []

# ماتریس‌های تبدیل (تغییر ضرایب برای تغییر شکل برگ)
transformations = [
    (0.0, 0.0, 0.0, 0.16, 0.0, 0.0, 0.01),  # ساقه
    (0.85, 0.02, -0.02, 0.83, 0.0, 1.6, 0.85),  # برگ‌های اصلی (کمی تغییر یافته)
    (0.2, -0.31, 0.29, 0.24, 0.0, 1.6, 0.07),  # برگ چپ (باریک‌تر)
    (-0.25, 0.26, 0.28, 0.31, 0.0, 0.44, 0.07),  # برگ راست (پهن‌تر)
]

# محاسبه نقاط
for _ in range(num_points):
    r = random.random()
    cumulative_probability = 0
    for a, b, c, d, e, f, p in transformations:
        cumulative_probability += p
        if r <= cumulative_probability:
            x, y = a * x + b * y + e, c * x + d * y + f
            x_vals.append(x)
            y_vals.append(y)
            break

# رسم نمودار
plt.figure(figsize=(8, 10))
plt.scatter(x_vals, y_vals, s=0.2, color="darkgreen")
plt.axis("off")
plt.title("Modified Barnsley Fern")
plt.show()
