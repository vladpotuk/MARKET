try:
 password = "Admin"
 user_enter_login = input("Введіть пароль : ")
 user_enter_parol = input("Введіть пароль : ")
 while user_enter_login and user_enter_parol :
    if user_enter_login == password and user_enter_parol == password:
            print('Доступ надано')
            good_collection = []
            info_for_user = ["Введіть найменування товару : ", "Введіть ціну : ", "Введіть Кількість: "]
            goods_print = ["Товар: ", "Ціна: ", "Кількість: ", "Тотал:  "]
            quantity = int(input("Введіть кількість товару:"))
            for i in range(0, quantity):
                for j in range(0, 4):
                    if j == 0:
                        good_collection.append(input(info_for_user[j]))
                    elif j == 3:
                        good_collection.append(good_collection[j-1] * good_collection[j-2])

                    else:
                        good_collection.append(float(input(info_for_user[j])))

            for i in range(0, quantity):
                for j in range(0, 4):
                    print(goods_print[j], good_collection[i * 4 + j])
                    print("")
            break
    elif user_enter_login != password and user_enter_parol != password:
            print('Невірний пароль')
            break


except Exception as e:
    print(e)









