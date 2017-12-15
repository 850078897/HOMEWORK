n = 100
approx = n/2
while True:
    better = (approx + n/approx)/2
    if abs(approx - better) < .0000000001:
        break
    approx = better
print(better)
