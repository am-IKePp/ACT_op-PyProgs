#камень-ножницы-бумага
import random
figures: list[str] = ["камень", "ножницы", "бумага"]
pc_option: str = random.choice(figures)
join: str = input("Что у Вас? ")
print(pc_option)

if (join == "камень" and pc_option == "камень") \
    or (join == "ножницы" and pc_option == "ножницы") \
        or (join == "бумага" and pc_option == "бумага"):
    print("Ничья")
elif (join == "камень" and pc_option == "ножницы") \
    or (join == "ножницы" and pc_option == "бумага") \
        or (join == "бумага" and pc_option == "камень"):
    print("Вы выиграли")
elif join not in figures:
    print("Вы не можете так писать")
else:
    print("Проиграли")