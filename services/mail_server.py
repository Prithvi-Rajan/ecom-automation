import yagmail
from decouple import config


class MailServer:
    @staticmethod
    def send_mail(to: str, subject='', body=''):
        user = config('MAIL_ID')
        app_password = config('APP_PASSWORD')
        with yagmail.SMTP(user, app_password) as yag:
            yag.send(to, subject, body)
            print('Sent email successfully')
