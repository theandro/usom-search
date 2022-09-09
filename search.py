# -*- coding: utf-8 -*-
"""
@author: theandro
Discord: andro#1337
"""
try:
    import re, requests
except:
    print("Projeye dahil edilmiş kütüphanelerin yüklü olduğundan emin olun.")


def update_list():
    header = {"User-Agent":"Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0"}
    update = requests.get("https://www.usom.gov.tr/url-list.txt", headers=header)
    with open("data.txt", "w") as upd:
        upd.write(update.text)
        upd.close()

if __name__ == "__main__":
    update_list()
    with open("data.txt", "r") as file:
         data = file.read()
         print("[Q] Quit")
         while True:
             word = str(input("Gir >"))
             word = word.replace("https://", "")
             word = word.replace("http://", "")
             word = word.strip()
             
             find = re.findall(word, data)
             if word == "Q" or word == "q":
                 break
             if find:
                 print("Bu domain USOM'a yakalanmistir:",find[0])
             else:
                 print("Bulunamadi.")
