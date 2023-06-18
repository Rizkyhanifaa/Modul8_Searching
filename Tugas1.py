# Linear Search
def linear_search (plat, keyword):
    for i in range(len(plat)):
        if (plat[i]).lower() == keyword.lower():
            print("Hasil : ")
            print(f"Plat {keyword} terdapat di database kepolisisan no.{i+1}")
            return i
    print("Hasil : ")
    print(f"Plat {keyword} tidak terdapat dalam database kepolisian")
    return -1

plat = ['R 2477 SR', 'R 1234 DJ', 'R 7015 LP', 'R 0201 RR',  'R 3304 DA', 'R 2401 SK', 'R 2103 RT', 'R 1708 RI', 'R 1111 SR', '[R 4987 LH']
print("----Pengecekan No Plat Kendaraan----")
keyword = input("Masukkan Plat Kendaraan : ")
linear_search(plat, keyword)
