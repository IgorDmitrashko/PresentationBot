import os
import random
import string
import time

from pydantic import BaseModel

import requests

API = 'https://www.1secmail.com/api/v1/'
domain_list = ["1secmail.com", "1secmail.org", "1secmail.net"]
domain = random.choice(domain_list)
leter = ''

class Disposable_mail:
    def generate_user_name(self):
        name = string.ascii_lowercase + string.digits
        user_name = ''.join(random.choice(name) for i in range(10))
        return user_name

    def check_mail(self, mail):
            req_link = f'{API}?action=getMessages&login={mail.split("@")[0]}&domain={mail.split("@")[1]}'
            req = requests.get(req_link).json()
            lenght = len(req)

            if lenght == 0:
                print("Все плохо")
            else:
                id_list = []
                for i in req:
                    for k, v in i.items():
                        if k == 'id':
                            id_list.append(v)

                print(f'входящих {lenght}')
                current_directory = os.getcwd()
                final_directory = os.path.join(current_directory, 'all_mails')

                if not os.path.exists(final_directory):
                    os.makedirs(final_directory)

                for i in id_list:
                    read_msg = f'{API}?action=readMessage&login={mail.split("@")[0]}&domain={mail.split("@")[1]}&id={i}'
                    req = requests.get(read_msg).json()

                    sender = req.get('from')
                    subject = req.get('subject')
                    date = req.get('date')
                    content = req.get('textBody')
                    mail_file_path = os.path.join(final_directory, f'{i}.txt')

                    with open(mail_file_path, 'w') as file:
                        leter = f'Отправитель: {sender}\nКому: {mail}\nТема: {subject}\nDate: {date}\nСодержимое:{content}'
                        print(leter)

                        file.write(
                            f'Отправитель: {sender}\nКому: {mail}\nТема: {subject}\nDate: {date}\nСодержимое:{content}')

    def delete_mail(mail=''):
        url = f'https://www.1secmail.com/mailbox'
        data = {
            'action': 'dleteMailbox',
            'login': mail.split('@')[0],
            'domain': mail.split('@')[1],
        }
        req = requests.post(url, data=data)
        print(f'[X] Почтовый адрес {mail} - удален!\n')

    def main(self):

        try:
            user_name = self.generate_user_name()
            mail = f'{user_name}@{domain}'
            print(f'Ваша почта: {mail}')

            mail_req = requests.get(f'{API}?login={mail.split("@")[0]}&domain={mail.split("@")[1]}')

            while True:
                self.check_mail(mail=mail)
                time.sleep(10)

        except Exception as ex:
            print(f"Не вышла почта {ex}")
        pass

    if __name__ == '__main__':
        main()
