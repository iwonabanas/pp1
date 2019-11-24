# 16. Napisz program, który dla następujących ułamków zwykłych 1/2, 1/3, ..., 1/10 wyznaczy ich wartość dziesiętną.
# Zastosuj instrukcję for.

for x in range(1,11):
    print("1/{0} = {1:6g}".format(x,1/x))