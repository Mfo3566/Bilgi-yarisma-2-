print("bilgi yarismasina hosgeldin!")

isim = input("adin ne? ")

puan=0

print("Turkiyenin baskenti neresidir? ")

cevap = input("cevabin: ").strip().lower()

if cevap == "ankara":
    print("Dogru cevap!")
    puan += 10

else:
    print("yanlis! Dogru cevap ankara")

print(f"{isim},toplam puanin: {puan}")