def sieve_of_eratosthenes(limit):
    # ایجاد لیستی از اعداد
    primes = [True] * (limit + 1)
    primes[0] = primes[1] = False  # 0 و 1 اول نیستند

    # الگوریتم غربال
    for num in range(2, int(limit**0.5) + 1):
        if primes[num]:
            for multiple in range(num * num, limit + 1, num):
                primes[multiple] = False

    # استخراج اعداد اول
    return [i for i in range(limit + 1) if primes[i]]

# پیدا کردن اعداد اول بین 1 تا 10 میلیون
limit = 10_000_000
prime_numbers = sieve_of_eratosthenes(limit)

# نمایش تعداد و چند عدد اول
print(f"تعداد اعداد اول: {len(prime_numbers)}")
print(f"چند عدد اول: {prime_numbers[:10]}")  # نمایش ۱۰ عدد اول
