# s = str(input("in: "))
# output = ''
# for i in s:
#     if i.isupper():
#         output += i
#         for j in s:
#             if j.isdigit():
#                 for x in s[s.index(j)+1::3]:
#                     output += x
#                 break
# print("out: ",output)
s = 'thisisabracadabraHt1eadljjl12ojh.'
output = ''
int_check = 0
for i in s:
    if i.isupper():
        output = i + output
    elif i.isdigit() and not int_check:
        int_check += 1
        for x in s[s.index(i)+1::3]:
            output += x
        
print('out: ', output)
