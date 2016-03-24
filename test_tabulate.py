from tabulate import tabulate

table = [["Sun", 696000, 1989100000],
         ["Earth", 6371, 5973.6],
         ["Moon", 1737, 73.5],
         ["Mars", 3390, 641.85]]
print(tabulate(table))
print(tabulate(table, headers=["Planet","R (km)", "mass (x 10^29 kg)"]))