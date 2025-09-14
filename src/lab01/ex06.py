N = int(input("in_1: "))
ochn = 0
zaochn = 0
switch_case = {
    "False": ochn,
    "True" : zaochn
}
for i in range(N):
    s = input(f"in_{i+2}: ").split()
    if s[3] == "True":
        ochn += 1
    elif s[3] == "False":
        zaochn += 1
print("out: ", ochn, zaochn)