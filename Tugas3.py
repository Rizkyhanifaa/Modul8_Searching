# Binary Search

def bubble_sort(keyword, bilangan):
    for i in range(len(bilangan)):
        for j in range(len(bilangan) - i - 1):
            if bilangan[j] > bilangan[j+1]:
                bilangan[j], bilangan[j + 1] = bilangan[j + 1], bilangan[j]
    return binary_search(keyword, bilangan)

def binary_search(keyword, bilangan):
    left = 0
    right = len(bilangan) - 1
    
    while left <= right:
        mid = (left + right)//2
        
        if str(bilangan[mid]).lower() > keyword.lower():
            right = mid - 1
        elif str(bilangan[mid]).lower() < keyword.lower():
            left = mid + 1
        else:
            print("\nDaftar Bilangan setelah diurutkan :",bilangan)
            print(f"Angka {keyword} berada di urutan ke-{mid + 1}")
            return mid
    print(f"\nAngka {keyword} tidak ditemukan daftar bilangan acak")
    return -1

bilangan = [ 17, 2, 15, 7, 72, 31, 12, 57, 63, 71, 23, 92, 1]
print("----Pencarian Bilangan Acak ----")
print()
print("Daftar Bilangan Acak :", bilangan)
keyword = input("Cari bilangan acak : ")
bubble_sort(keyword, bilangan)

