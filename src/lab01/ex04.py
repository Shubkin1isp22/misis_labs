m = int(input("Минуты: "))
if m > 1440:
    m -= 1440
    print(f"{m//60:02d}:{m%60:02d}")
else:
    print(f"{m//60:02d}:{m%60:02d}")