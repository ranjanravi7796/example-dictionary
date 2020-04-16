import re

# for i in range(int(input())):
#     N = input().strip()
   
#     if re.match(r"^[456]([\d]{15}|[\d]{3}(-[\d]{4}){3})$", N) and not re.search(r"([\d])\1\1\1", N.replace("-", "")):
#         print("Valid")
#     else:
#         print("Invalid")


# 100000
# 999999

N = input()

#patt = r"(^[1-9][\d]{5}$)"


patt1 = r"(\d)(?=\d\1)"

print(re.findall(patt1,N))

print()
        