import random
def nimi(nimi:int,inimesed):
    """
    """
    inimesed=int(input("mite inimesed osaleda?"))
    if inimesed==1: 
        nimi=int(input("sissetage sinu nimi:"))




def kontroli():
    """
    """
    kokku=int(input("mitu küsimust?"))
    for i in range (kokku):
       järjend=choice=([...])


# Опрашиваем трех человек
results = []
for i in range(3):
    name = input("Введите ваше имя: ")
    results.append(interview(name))

# Сохраняем результаты
passed = sorted([r for r in results if r[1] >= 3], key=lambda r: r[1], reverse=True)
failed = sorted([r for r in results if r[1] < 3], key=lambda r: r[0])
with open("oiged.txt", "a", encoding="utf-8") as f:
    for r in passed:
        f.write(f"{r[0]}: {r[1]}\n")
with open("valed.txt", "a", encoding="utf-8") as f:
    for r in failed:
        f.write(f"{r[0]}: {r[1]}\n")

# Выводим результаты
print("Список успешно прошедших опросник:")
for r in passed:
    print(f"{r[0]}: {r[1]}")
print("Список не прошедших опросник:")
for r in failed:
    print(f"{r[0]}: {r[1]}")
