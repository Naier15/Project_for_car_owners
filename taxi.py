import tkinter as tk
from tkinter.ttk import *
from tkinter import *
import sqlite3


values = ["Выберите гос. номер"]
data = []
kms = []
date = []

# Подключение и создание базы данных
db = sqlite3.connect('sqlite.db')
sql = db.cursor()

sql.execute("""CREATE TABLE IF NOT EXISTS cars(num TEXT, date VARCHAR, debt INT, km INT)""")
db.commit()


# Создание приложения
app = tk.Tk()
app.title("TaxiV")
app.configure(background="#ececec")
app.geometry('550x400')

# fra1 = Frame(app, width=500, height=100, bg="darkred")
# fra1.pack()

# Приложение добавления машины
def Add_new_car():

  # Функция регистрации машины
  def reg (car_n, car_d, car_k, car_da):
    sql.execute (f"INSERT INTO cars VALUES (?, ?, ?, ?)", (car_n, car_da, car_d, car_k))
    db.commit ()
    anc.destroy ()

  # Добавление новой машины
  def addCar ():
    if textCar.get ().strip () != "":
      if textCarD.get () != None:
        if textCarK.get () != None:

          car_new = textCar.get ()
          car_debt = textCarD.get ()
          car_km = textCarK.get()
          car_date = textCarS.get()

          if car_new in values:
            print ("Already exists")
          else:
            reg (car_new, car_debt, car_km, car_date)
            print ("Okay")

  anc = tk.Tk ()
  anc.title ("Добавляем новую машинку")
  anc.configure (background="#ececec")
  anc.geometry ('600x100')

  # Кнопка регистрации машины
  text_l = ttk.Label (anc, text="   Гос. номер машины", font="roboto 10")
  text_l.grid (row=1, column=0)

  text_ll = ttk.Label (anc, text="Долг водителя, руб.", font="roboto 10")
  text_ll.grid (row=1, column=1)

  text_lll = ttk.Label (anc, text="Километраж машины, км.", font="roboto 10")
  text_lll.grid (row=1, column=2)

  text_llll = ttk.Label (anc, text="Дата замены страхования", font="roboto 10")
  text_llll.grid (row=1, column=3)

  add_car = ttk.Button (anc, text="Добавить", width=10, command=addCar)
  add_car.grid (row=3, column=0)

  textCar = ttk.Entry (anc, width=15)
  textCar.grid (row=2, column=0)

  textCarD = ttk.Entry (anc, width=20)
  textCarD.grid (row=2, column=1)

  textCarK = ttk.Entry (anc, width=20)
  textCarK.grid (row=2, column=2)

  textCarS = ttk.Entry (anc, width=20)
  textCarS.grid (row=2, column=3)

  textCar.focus_force()
  anc.resizable (False, False)
  anc.mainloop ()

# Приложенние редактирования имени
def CreateName():

  def createN ():
    if text_field.get () != None:
      res = text_field.get()
      s = values[combo.current ()]
      sql.execute (f"""UPDATE cars SET num='{res}' WHERE num='{s}'""")
      db.commit ()
      cn.destroy ()


  cn = tk.Tk ()
  cn.title ("Редактируем имя водителя")
  cn.configure (background="#ececec")
  cn.geometry ('400x100')

  # Заполнение Combobox данными из ДБ
  sql.execute (f"SELECT num FROM cars")
  b = sql.fetchall ()
  values.clear()
  for i in b:
    if i[0] not in values:
      values.append ('{num}'.format (num=i[0]))


  # Выбор машины
  car_label = ttk.Label (cn, text="Гос.номер машины", font="roboto 10")
  car_label.grid (row=1, column=0)

  # Combobox
  combo = ttk.Combobox (cn, values=values)
  combo.current (0)  # установим вариант по умолчанию
  combo.grid (row=2, column=0)

  # Текстовое поле
  text_label = ttk.Label (cn, text="Введите новое имя", font="roboto 10")
  text_label.grid (row=1, column=1)

  text_field = ttk.Entry (cn, width=40)
  text_field.grid (row=2, column=1)

  # Кнопка
  btn_search = ttk.Button (cn, text="Ввести", width=10, command=createN)
  btn_search.grid (row=3, column=1)

  cn.resizable (False, False)
  cn.mainloop ()

# Приложение изменения долга
def ChangeCar():

  # Смена долга
  def change ():
    if text_field.get () != None:
      res = int(data[combo.current()-1]) - int(text_field.get())
      s = values[combo.current ()]
      sql.execute(f"""UPDATE cars SET debt='{res}' WHERE num='{s}'""")
      db.commit()
      cc.destroy()

  def changeDebt ():
    change ()

  def changeBtn (event):
    change ()

  cc = tk.Tk ()
  cc.title ("Изменяем долг водителя")
  cc.configure (background="#ececec")
  cc.geometry ('400x200')

  # Заполнение Combobox данными из ДБ
  sql.execute (f"SELECT num, debt FROM cars")
  b = sql.fetchall ()
  data.clear()
  for i in b:
    if i[0] not in values:
      values.append ('{num}'.format (num=i[0]))
    data.append ('{debt}'.format (debt=i[1]))

  # Надпись
  search_label = ttk.Label (cc, text="Выбирете машину и \n введите сумму платежа", font="verdana 12 ", justify=CENTER,
                            foreground="#333")
  search_label.grid (row=0, column=0, columnspan=2)

  # Выбор машины
  car_label = ttk.Label (cc, text="Гос.номер машины", font="roboto 10")
  car_label.grid (row=1, column=0)

  # Combobox
  combo = ttk.Combobox (cc, values=values)
  combo.current (0)  # установим вариант по умолчанию
  combo.grid (row=2, column=0)

  # Текстовое поле
  text_label = ttk.Label (cc, text="Сумма платежа, руб.", font="roboto 10")
  text_label.grid (row=1, column=1)

  text_field = ttk.Entry (cc, width=40)
  text_field.grid (row=2, column=1)

  # Кнопка
  btn_search = ttk.Button (cc, text="Ввести", width=10, command=changeDebt)
  btn_search.grid (row=3, column=1)

  text_field.bind ('<Return>', changeBtn)

  text_field.focus_force ()
  cc.resizable (False, False)
  cc.mainloop ()

# Приложение смены масла:
def ChangeOil():
  # Смена масла
  def change1 ():
    if text_field1.get () != '':
      res1 = int(text_field1.get())
      s1 = values[combo.current ()]
      sql.execute(f"""UPDATE cars SET km='{res1}' WHERE num='{s1}'""")
      db.commit()
    else:
      print('Значение не установлено')

  def changeOilS ():
    change1 ()

  def changeOilBtn (event):
    change1 ()

  co = tk.Tk ()
  co.title ("Сменили масло?")
  co.configure (background="#ececec")
  co.geometry ('330x200')

  # Заполнение Combobox данными из ДБ
  sql.execute (f"SELECT num, km FROM cars")
  b = sql.fetchall ()
  kms.clear ()
  for i in b:
    if i[0] not in values:
      values.append ('{num}'.format (num=i[0]))
    kms.append ('{km}'.format (km=i[1]))

  # Выбор машины
  car_label = ttk.Label (co, text="Гос.номер машины:", font="roboto 10")
  car_label.grid (row=1, column=0)

  # Combobox
  combo = ttk.Combobox (co, values=values)
  combo.current (0)  # установим вариант по умолчанию
  combo.grid (row=2, column=0)

  # Метка пробега следующей замены
  text_ch = ttk.Label (co, text="Рекомендуемый пробег следующей замены масла:", font="roboto 10")
  text_ch.grid (row=3, column=0)

  # Обновление текущего пробега
  def km():

    global kmInfo
    if combo.current () != 0:
      if kms[combo.current () - 1] != '':
        kms1 = int(kms[combo.current() - 1]) + 7000
      else:
        kms1 = 0
    else:
      kms1 = 0
    kmInfo = ttk.Label (co, text="{kms}".format (kms=kms1), font="roboto 10", foreground='white', background='#43ba55')
    kmInfo.grid (row=4, column=0)
    co.after(1000, km2)
  def km2():
    kmInfo.destroy()
    co.after (0, km)
  km ()

  # Текстовое поле
  text_oil = ttk.Label (co, text="На каком пробеге производили замену масла?", font="roboto 10")
  text_oil.grid (row=5, column=0)

  text_field1 = ttk.Entry (co, width=25)
  text_field1.grid (row=6, column=0)

  # Кнопка
  btn_search1 = ttk.Button (co, text="Ввести", width=10, command=changeOilS)
  btn_search1.grid (row=7, column=0)

  text_field1.bind ('<Return>', changeOilBtn)

  text_field1.focus_force()
  co.resizable (False, False)
  co.mainloop ()

# Приложение замены страхования
def Security():
  def change3 ():
    if text_field1.get () != None:
      res = text_field1.get()
      s = values[combo.current ()]
      sql.execute(f"""UPDATE cars SET date='{res}' WHERE num='{s}'""")
      db.commit()
      sec.destroy()

  sec = tk.Tk ()
  sec.title ("Сменим дату следующего страхования?")
  sec.configure (background="#ececec")
  sec.geometry ('160x150')

  # Заполнение Combobox данными из ДБ
  sql.execute (f"SELECT num, date FROM cars")
  b = sql.fetchall ()
  for i in b:
    if i[0] not in values:
      values.append ('{num}'.format (num=i[0]))
      date.append ('{date}'.format (date=i[1]))

  # Выбор машины
  car_label = ttk.Label (sec, text="Гос.номер машины:", font="roboto 10")
  car_label.grid (row=1, column=0)

  # Combobox
  combo = ttk.Combobox (sec, values=values)
  combo.current (0)  # установим вариант по умолчанию
  combo.grid (row=2, column=0)

  # Текстовое поле
  text_sec = ttk.Label (sec, text="Какая следующая дата\n замены страхования?", font="roboto 10")
  text_sec.grid (row=3, column=0)

  text_field1 = ttk.Entry (sec, width=25)
  text_field1.grid (row=4, column=0)
  text_field1.focus_force()

  # Кнопка
  btn_search1 = ttk.Button (sec, text="Ввести", width=10, command=change3)
  btn_search1.grid (row=5, column=0)

  sec.resizable (False, False)
  sec.mainloop ()

# Приложение удаления машины
def DelCar():

  def Delete():
    s = values[combo.current ()]
    sql.execute(f"""DELETE FROM cars WHERE num='{s}'""")
    db.commit()
    f = values.pop(combo.current ())
    dc.destroy()

  dc = tk.Tk ()
  dc.title ("Какую машину удалить?")
  dc.configure (background="#ececec")
  dc.geometry ('150x150')

  # Заполнение Combobox данными из ДБ
  sql.execute (f"SELECT num FROM cars")
  b = sql.fetchall ()
  for i in b:
    if i[0] not in values:
      values.append ('{num}'.format (num=i[0]))

  # Выбор машины
  car_label = ttk.Label (dc, text="Гос.номер машины:", font="roboto 10")
  car_label.grid (row=1, column=0)

  # Combobox
  combo = ttk.Combobox (dc, values=values)
  combo.current (0)  # установим вариант по умолчанию
  combo.grid (row=2, column=0)

  # Кнопка
  btn_search1 = ttk.Button (dc, text="Удалить", width=10, command=Delete)
  btn_search1.grid (row=7, column=0)


  dc.resizable (False, False)
  dc.mainloop ()

# Меню: Добавление машины
mainmenu=Menu(app)
app.config(menu=mainmenu)
mainmenu.add_command(label="Добавить машинку", command=Add_new_car)

# Меню: Редаактирование имени
mainmenu.add_command(label="Редактировать имя", command=CreateName)

# Меню: Изменение Долга
mainmenu.add_command(label="Внести платеж", command=ChangeCar)

# Меню: Изменение километража
mainmenu.add_command(label="Сменить километраж", command=ChangeOil)

# Меню: Изменение страхования
mainmenu.add_command(label="Замена страхования", command=Security)

# Меню: Удалить машину
mainmenu.add_command(label="Удалить машину", command=DelCar)


def tab():
  # Создаем таблицу
  global tree
  columns = ('Гос. номер', 'Дата замены страхования', 'Размер долга, руб.', 'Километраж, км.')
  tree = Treeview(app, columns=columns, show='headings')

  tree.column('Гос. номер', width=40, anchor='center')
  tree.column ('Дата замены страхования', width=80, anchor='center')
  tree.column ('Размер долга, руб.', width=40, anchor='center')
  tree.column ('Километраж, км.', width=60, anchor='center')

  for col in columns:
    tree.heading(col, text=col)

  sql.execute ('''SELECT * FROM cars''')
  for x in sql.fetchall():
    tree.insert('', 'end', values=x)

  tree.pack (expand=1, fill=BOTH)

  global scrollbar
  scrollbar = Scrollbar(tree, command=tree.yview)
  tree.configure (yscrollcommand=scrollbar.set)
  scrollbar.pack (side=RIGHT, fill=Y)

  app.after(3000, tab2)
def tab2():
  tree.destroy()
  scrollbar.pack_forget()
  app.after(0, tab)
tab()

# Приложение всегда поверх остальных
# app.wm_attributes('-topmost', True)
# Фокусировка на текстовом поле
# text_field.focus()

# Не управлять границами
app.resizable(False, True)

# Вечный цикл
app.mainloop()
db.close()