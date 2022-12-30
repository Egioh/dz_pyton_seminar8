import json
def Uid():
    with open('empl.json', 'r') as f:
        json_data = json.load(f)
        uid = max(json_data.keys())
        return int(uid)
def Show_empl():
    with open('empl.json', 'r', encoding='utf-8') as f:
        
        data = json.load(f)
       
        for key, value in data.items():
            print(f"{key}: {value}")
    input("Enter для возврата в меню")
    menu()
def Show_phones():
    with open('empl_phone.json', 'r') as f:
        data = json.load(f)
        for key, value in data.items():
            print(f"{key}: {value}")
    input("Enter для возврата в меню")
    menu()

def Show_departments():
    with open('departments.json', 'r') as f:
        data = json.load(f)
        for key, value in data.items():
            print(f"{key}: {value}")
    input("Enter для возврата в меню")
    menu()

def Show_positions():
    with open('positions.json', 'r') as f:
        data = json.load(f)
        for key, value in data.items():
            print(f"{key}: {value}")
    input("Enter для возврата в меню")
    menu()

def add_empl():
    
    with open('empl.json', 'r') as f:
        json_data = json.load(f)
    uid=Uid()+1
   
    json_data[str(uid)] = {}
    json_data[str(uid)]['name'] = input("Имя:")
    json_data[str(uid)]['sername'] = input("Фамилия:")
    json_data[str(uid)]['f_name'] = input("Отчество:")
    json_data[str(uid)]['bday'] = input("Дата рождения:")
    json_data[str(uid)]['id_position'] = input("Должность:")
    json_data[str(uid)]['id_department'] = input("Отдел:")

    
    with open('empl.json', 'w') as f:
        json.dump(json_data, f)
    input("Enter для возврата в меню")
    menu()
def add_empl_adres(uid):
    
    with open('empl_addresses.json', 'r') as f:
        address_data = json.load(f)
    if uid not in address_data:
        address_data[uid] = {}
    address_data[uid]["City"]=input("Город:")
    address_data[uid]["street"]=input("Улица:")
    address_data[uid]["homeNum"]=input("Дом:")
    address_data[uid]["Literal"]=input("Литера:")
    address_data[uid]["korpus"]=input("Корпус:")
    address_data[uid]["flat"]=input("Квартира:")
    
    with open('empl_addresses.json', 'w') as f:
        json.dump(address_data, f)
    input("Enter для возврата в меню")
    menu()
def add_email(uid):
    with open('empl_email.json', 'r') as f:
        mail_data = json.load(f)
    if uid not in mail_data:
        mail_data[uid] = {}
    mail_data[uid]["mail"]= input("введите электронную почту сотрудника: ")
    with open('empl_email.json', 'w') as f:
        json.dump(mail_data, f)
    input("Enter для возврата в меню")
    menu()
def add_phone(uid):
    with open('empl_phone.json', 'r') as f:
        phone_data = json.load(f)
    if uid not in phone_data:
        phone_data[uid] = {}
    phone_data[uid]["phone"]= input("введите телефон сотрудника: ")
    with open('empl_phone.json', 'w') as f:
        json.dump(phone_data, f)
    input("Enter для возврата в меню")
    menu()
def add_position():
    with open('positions.json', 'r') as f:
        pos_data = json.load(f)
    uid=input("придумайте уникальный идентификатор для новой должности: ")
    if str(uid) not in pos_data:
        pos_data[str(uid)]={}
        pos_data[str(uid)]["pos_name"]=input("название должности: ")
        pos_data[str(uid)]["pos_cost"]=int(input("зарплата сотрудника на должности: "))
    else:
        print("этот uid занят")
        add_position()
    with open('positions.json', 'w') as f:
        json.dump(pos_data, f)
    input("Enter для возврата в меню")
    menu()
def add_department():
    with open('departments.json', 'r') as f:
        dep_data = json.load(f)
    uid=input("придумайте уникальный идентификатор нового отдела: ")
    if str(uid) not in dep_data:
        dep_data[str(uid)]={}
        dep_data[str(uid)]["head"]=input("uid главы отдела: ")
        dep_data[str(uid)]["pos_cost"]=input("название отдела: ")
    else:
        print("этот uid занят")
        add_department()
    with open('departments.json', 'w') as f:
        json.dump(dep_data, f)
    input("Enter для возврата в меню")
    menu()

def show_employees_without_address():
    with open('empl.json', 'r') as f:
        employees_data = json.load(f)
    with open('empl_addresses.json', 'r') as f:
        addresses_data = json.load(f)
    employees_without_address = []
    for uid, employee in employees_data.items():
        # Проверяем, есть ли у сотрудника заполненный адрес
        if uid not in addresses_data:
            # Если нет, то добавляем uid сотрудника в список
            employees_without_address.append(uid)
    print (*employees_without_address)
    input("Enter для возврата в меню")
    menu()

def show_employees_without_phones():
    
    with open('empl.json', 'r') as f:
        employees_data = json.load(f)

    with open('empl_phone.json', 'r') as f:
        phones_data = json.load(f)

    employees_without_phones = []

    for uid, employee in employees_data.items():
        if uid not in phones_data:
            employees_without_phones.append(uid)
    print (*employees_without_phones)
    input("Enter для возврата в меню")
    menu()

def delete_empl(uid):
    with open('empl.json', 'r') as f:
        empl_data = json.load(f)
    del empl_data[uid]
    with open('empl.json', 'w') as f:
        json.dump(empl_data, f)
    input("Enter для возврата в меню")
    menu()





def menu():
    print ("""    1.Вывести список сотрудников
    2.внести нового сотрудника в базу
    3.Внести или изменить адрес сотрудника(по uid)
    4.Внести или изменить mail сотрудника
    5.Внести или изменить телефон сотрудника
    6.Добавить должность
    7.Добавить новый отдел
    8.Показать uid сотрудников для которых не заполнены адреса
    9.Показать uid сотрудников для которых не заполнены телефоны
    10.Показать телефоны
    11.Показать список отделов
    12.Показать список должностей
    13.Удалить запись о сотруднике по его uid""")
    act=int(input("Введите номер действия из списка:"))
    if act==1:
        Show_empl()
    elif act ==2:
        add_empl()
    elif act ==3:
        temp=input("введите uid сотрудника:")
        with open('empl.json', 'r') as f:
            json_data = json.load(f)
        if temp in  json_data:
            add_empl_adres(temp)
        else:
            print("такого сотрудника нет")
    elif act==4:
        temp=input("введите uid сотрудника:")
        with open('empl.json', 'r') as f:
            json_data = json.load(f)
        if temp in  json_data:
            add_email(temp)
        else:
            print("такого сотрудника нет")
            menu()
    elif act ==5:
        temp=input("введите uid сотрудника:")
        with open('empl.json', 'r') as f:
            json_data = json.load(f)
        if temp in  json_data:
            add_phone(temp)
        else:
            print("такого сотрудника нет")
            menu()
    elif act==6:
        add_position()
    elif act==7:
        add_department()
    elif act==8:
        show_employees_without_address()
    elif act==9:
        show_employees_without_phones()
    elif act ==10:
        Show_phones()
    elif act ==11:
        Show_departments()
    elif act ==12:
        Show_positions()
    elif act ==13:
        temp=input("введите uid сотрудника:")
        with open('empl.json', 'r') as f:
            json_data = json.load(f)
        if temp in  json_data:
            delete_empl(temp)
        else:
            print("такого сотрудника нет")
            menu()


