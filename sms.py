import requests, os, sys, time, datetime
from sys import platform
from requests import get
starttime = datetime.datetime.now().strftime("%X")
def clear():
    if platform == "linux" or platform == "linux2":
        os.system("clear")
    elif platform == "win32":
        os.system('cls')
print("Создал: github.com/Sanif007  ")
print("Перевел: t.me/lamer112311  Для канала t.me/smoke_software")
print("Версия 4.0 ")
print("Проверка зависимостей... ")
time.sleep(2)
os.system("bash rq.sh")
def menu() :
    print("[1] Отправить анонимное смс")
    print("[2] Проверить статус смс")
    print("[3] Помощь")
    print("[4] Проверьте предыдущую историю! ")
    print("[5] Выход")
def control() :
    ctrl = input("Что вы хотите сделать: ")
    if ctrl == "1" :
        sms()
    elif ctrl == "2" :
        status()
    elif ctrl == "3" :
        help()
    elif ctrl == "4" :
        history()
    elif ctrl == "5" :
        print("Спасибо за использование программы\nt.me/smoke_software")
        exit()
    else :
        print("Неверный номер")
def sms() :
   phone_no = input("Введите номер телефона: ")
   msg = input("Текст сообщения: ")

   resp = requests.post('https://textbelt.com/text',{
	'phone' : phone_no,
	'message' : msg ,
	'key' : 'textbelt'
   })
   print(resp.text)
   time = datetime.datetime.now()
   clock = time.strftime("%X")  
   date = time.strftime("%x")
   save = open("sess.txt", "a")
   save.write(f"\nip = {ip} : Время = {clock} : Дата = {date} : stats = {resp.text} : Телефон.  = {phone_no} ")
def history() :
    if os.path.exists("sess.txt") :
        with open("sess.txt","r") as file :
            sessions = file.read().splitlines()
            ses_numbers = len(sessions)
            if ses_numbers > 1 :
                os.system("python sess_info.py")
                more_details = input("Хотите увидить все сессии? (По умолчанию: no) : ").lower()
                if more_details == "yes" or more_details == "y" :
                    os.system("cat sess.txt")
                else :
                    print("Спасибо за использование sms-scammer.\nt.me/smoke_software")
            elif ses_number == 1: 
                print(file.readline)
            else :
                print("либо файл пуст, либо произошла ошибка!")
    else :
        print("Либо вы используете это впервые, либо, возможно, вы удалили историю.")
def status() :
  textID = input("Введите текстID смс : ") 
  os.system(f"curl https://textbelt.com/status/{textID}")
def help() :
    print("пожалуйста, выберите вашу проблему из нижеуказанных условий! ")
    print("A. Не могу отправить смс после одной попытки на один и тот же номер!")
    print("B. Не могу отправить смс из-за большой нагрузки на сайт. ")
    print("C. Невозможно отправить более одной смс даже на разные номера. ")
    print("D. Другое")
    qna = input(">>> ").lower()
    if qna == "a" :
        print("Потому что это просто демо-версия, поэтому она может отправлять только 1 смс в день на один и тот же номер, однако вы можете отправлять на другой номер с помощью VPN.")
    elif qna == "b" :
        print("иногда, когда сайт используется в большом количестве, они отключают бесплатные смс на некоторое время. Пожалуйста, подождите некоторое время...")
    elif qna == "c" :
        print("Пожалуйста, внимательно проверьте свой VPN и используйте только лучший VPN. Например, nordvpn, protonvpn и т. д.")
    elif qna == "d" :
        print("извините за любую проблему! Пожалуйста, напишите нам о своей проблеме на hackersacademyofindia@gmail.com или вы можете указать свою проблему на github.com/Sanif007")
    else :
        print("Неверный вариант!! \n выход.. Извините..")
        exit()
clear()
os.system("toilet -f mono12 -F gay Scammer")
print("########################## Vr. 4.0 m#########################  ")
print("[Coded by github.com/Sanif007 ")
print("Перевел: t.me/lamer112311  Для канала t.me/smoke_software")
print(f"Програма стартовала: {starttime}")
ip = get("https://api.ipify.org").text
ip_c = input("Вы хотите увидеть свой текущий ip? (y/n): ").lower()
if ip_c == "yes" or ip_c == "y" :
   print(f"Вы в настоящее время используете с ip:{ip} ")
elif ip_c == "no" or ip_c == "n" :
   print("Надеюсь, ты знаешь, что делаешь. :)")
else :
   print("неверный вариант!! напиши y или n")
menu()
control()

