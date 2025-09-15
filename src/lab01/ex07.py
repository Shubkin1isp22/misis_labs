s = str(input("in: "))
output = ''
for i in s:
    if i.isupper():
        output += i
        for j in s:
            if j.isdigit():
                for x in s[s.index(j)+1::3]:
                    output += x
                break
print("out: ",output)