import tkinter as tk
from tkinter import messagebox


def calculate_pifagor_square(date):
    numbers = [int(digit) for digit in date if digit.isdigit()]
    total_sum = sum(numbers)
    while total_sum > 9:
        total_sum = sum(map(int, str(total_sum)))
    return total_sum


def determine_characteristics(date):
    pifagor_square = calculate_pifagor_square(date)
    characteristics = {
        1: "Характер: Утонченный эгоист, Эго, воля, осознание",
        2: "Характер: Обычные в биоэнергетическом отношении люди, Биоэнергетика, страстность, сексуальность",
        3: "Характер: Обычно очень чистоплотные или пунктуальные люди, Внутренний склад человека, хозяйственность, порядочность",
        4: "Характер: Здоровье среднее, необходимо закалять организм; болезни подступают к старости, Здоровье, сексуальность",
        5: "Характер: Открытый канал при рождении, Интуиция",
        6: "Характер: Такой человек пришел на землю приобрести ремесло, физический труд необходим, но он его не любит, Степень заземленности, логика, расчетливость",
        7: "Характер: Этот человек родился, чтобы зарабатывать семерки, Божья искра, Мера таланта, связь с высшими силами",
        8: "Характер: Соответствует почти полному отсутствию чувства долга, Чувство долга",
        9: "Характер: Человек от рождения не блестит умом, ему необходимо умственно развиваться, много и усердно учиться, но это ему дается не просто, Интеллект"
       
    }
    return characteristics.get(pifagor_square, "Неизвестная характеристика")


def on_submit():
    date = entry_date.get()
    if date:
        characteristics = determine_characteristics(date)
        messagebox.showinfo("Характеристики", characteristics)
    else:
        messagebox.showerror("Ошибка", "Введите дату рождения!")


root = tk.Tk()
root.title("Анализ характеристик по квадрату Пифагора")


label_date = tk.Label(root, text="Введите дату рождения (дд.мм.гггг):")
label_date.pack(pady=5)
entry_date = tk.Entry(root)
entry_date.pack(pady=5)
button_calculate = tk.Button(root, text="Рассчитать характеристики", command=on_submit)
button_calculate.pack(pady=5)

root.mainloop()


