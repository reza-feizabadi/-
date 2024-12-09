import matplotlib.pyplot as plt

def draw_triangle(vertices):
    # افزودن اولین نقطه مجدداً برای بستن مثلث
    vertices.append(vertices[0])

    # جدا کردن مختصات X و Y
    x_coords, y_coords = zip(*vertices)

    # رسم مثلث
    plt.figure(figsize=(6, 6))
    plt.plot(x_coords, y_coords, marker="o", color="blue", linestyle="-")
    plt.fill(x_coords, y_coords, color="skyblue", alpha=0.5)  # رنگ‌آمیزی داخل مثلث
    plt.title("Triangle")
    plt.axis("equal")
    plt.grid(True)
    plt.show()

# دریافت مختصات از کاربر
print("لطفاً مختصات سه رأس مثلث را وارد کنید:")
x1, y1 = map(float, input("مختصات رأس اول (x1 y1): ").split())
x2, y2 = map(float, input("مختصات رأس دوم (x2 y2): ").split())
x3, y3 = map(float, input("مختصات رأس سوم (x3 y3): ").split())

# فراخوانی تابع رسم
triangle_vertices = [(x1, y1), (x2, y2), (x3, y3)]
draw_triangle(triangle_vertices)
