'''Початковий внесок в банку дорівнює 1000 грн. Через кожен місяць розмір вкладу збільшується на P відсотків 
від наявної суми (P - дійсне число, 0 <P <25). За даним P визначити, через скільки місяців розмір вкладу
перевищить 1100 грн., і вивести знайдену кількість місяців K (ціле число) і підсумковий розмір вкладу S (дійсне число).'''

try:
    p = int(input("p:"))
    if p < 0 or p > 25:
        print("Введіть чісла в діапозоні 0 <P <25")
        p = int(input("p:"))
except ValueError:
    print("Введіть тільки числа  0 <P <25")
    p = int(input("p:"))
    if p < 0 or p > 25:
        print("Введіть чісла в діапозоні 0 <P <25")
        p = int(input("p:"))

bank = 1000
month = 0

while bank <= 1100:
    bank = bank + bank * (p / 100)
    month += 1

print(f" {bank} | {month} ")