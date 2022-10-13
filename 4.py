years=int(input("Введите количество лет: "))
exhibit=2800000

exhibit_in_day=8*60//5
visackos_years=(years//4)
y_without_v=(years-visackos_years)
days=visackos_years*366+y_without_v*365
exh_human=exhibit_in_day*days
exh_human=str(exh_human)

print("будет просмотрено"+" "+exh_human+" "+"экспонатов")
print("-"*50)

exhibits=int(input("Введите количество экспонатов в Эрмитаже (более 2,8 млн): "))
if exhibits>2800000 or exhibits==2800000:
    years=exhibits/exhibit_in_day
    visackos_years=(years//4)
    y_without_v=(years-visackos_years)
    days=visackos_years*366+y_without_v*365
    minutes=days*24*60
    years=str(years)
    days=str(days)
    minutes=str(minutes)
    print("На просмотр заданного колличества экспонатов будет потрачено"+" "+years+" "+"лет/год"+" "+"или"+" "+days+" "+"дней"+" "+"или"+" "+minutes+" "+"минут")
else:
    print("Неверное заданное количество экспонатов. Коллекция Эрмитажа насчитывает более 2,8 млн экспонатов.")

