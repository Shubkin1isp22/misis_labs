fio_str = str(input("ФИО: "))
fio = fio_str.split()
print(f"Инициалы: {fio[0][0]}{fio[1][0]}{fio[2][0]}.")
print(f"Длина (символов): {len(fio_str)}")