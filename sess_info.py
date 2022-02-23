with open("sess.txt","r") as file :
   first_line = file.readline()
   for last_line in file :
      pass
print("Первый раз используется : "+first_line)
print("Недавно использованный: "+last_line)
