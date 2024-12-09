import math

# تابع بسط تیلور برای تابع خطای erf
def erf_taylor(x, terms=5):
    result = 0
    for n in range(terms):
        result += ((-1)*n) * (x*(2*n + 1)) / (math.factorial(n) * (2*n + 1))
    return result * (2 / math.sqrt(math.pi))

# تابع بسط تیلور برای CDF توزیع نرمال
def cdf_taylor(mean, std_dev, x, terms=5):
    z = (x - mean) / (std_dev * math.sqrt(2))
    erf_value = erf_taylor(z, terms)
    return 0.5 * (1 + erf_value)

# مقادیر میانگین‌ها و انحراف معیارها
means = [10, 11, 12, 33, 14]
std_devs = [1, 2, 5]

# مقدار x برای محاسبه CDF
x_value = 26 # مقدار جدید

# محاسبه و چاپ CDF برای هر ترکیب از میانگین و انحراف معیار
for mean in means:
    for std_dev in std_devs:
        cdf_value = cdf_taylor(mean, std_dev, x_value)
        print(f"Mean: {mean}, Std Dev: {std_dev}, CDF({x_value}): {cdf_value:.6f}")
