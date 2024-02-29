payroll = [("Messi", 10_000), ("Ronaldo", 7_000), ("Zidane", 5_000)]

adjusted_patroll = [(item[0], item[1]*0.93) for item in payroll]

print(adjusted_patroll)


adjusted_patroll = [(name.upper(), 0.93*pay) for name, pay in payroll]

print(adjusted_patroll)





mp = ["John", "Jane", "Tim"]
pays = [100, 150, 75]

zipped = zip(mp, pays)

for elem in zipped:
    print(elem)

payroll = [tup for tup in zip(mp, pays)]
print(payroll)

print(list(zip(mp,pays)))

def check_triplets(a,b,c):
    return c**2 == a**2 + b**2

triples = [(a,b,c) for a in range(1,51) for b in range(1,51) for c in range(1,51) if check_triplets(a,b,c)]

print(triples)
