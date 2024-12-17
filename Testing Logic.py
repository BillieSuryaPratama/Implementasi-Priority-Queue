import pandas as pd

MenuMakanan = "MenuMakanan.csv"

df = pd.read_csv(MenuMakanan)
print(df)
#Output
# 0    1       Nasi Goreng  15000
# 1    2        Mie Goreng  15000
# 2    3          Mie Ayam  15000
# 3    4        Nasi Putih   5000
# 4    5         Ikan Lele  25000
# 5    6        Semur Ayam  25000
# 6    7      Telur Balado  10000
# 7    8    Tumis Kangkung   5000
# 8    9  Perkedel Kentang   5000
# 9   10     Kepiting Asap  50000
# 10  11            Es Teh   5000
# 11  12          Es Jeruk   7000
# 12  13        Teh Hangat   4000
# 13  14      Jeruk Hangat   6000
print("")




print(len(df))
# Output
# 14
print("")




Data = df.iloc[0]
print(Data)
# Output
# id                 1
# nama     Nasi Goreng
# harga          15000
print("")




RincianNama = Data.iloc[1]
RincianHarga = Data.iloc[2]
print(RincianNama)
print(RincianHarga)
# Output
# Nasi Goreng
# 15000
print("")