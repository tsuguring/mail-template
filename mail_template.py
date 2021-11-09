import smtplib
import ssl
from email.mime.text import MIMEText

#メールを作成する関数
def create_message(to, sub, body, sender):
    msg = MIMEText(body)
    msg["To"] = to
    msg["Subject"] = sub
    msg["From"] = "吉次 亮 <" + sender + ">"

    return msg

#本文に定型文を加える関数
def add_message(body, add_msg):

    body += add_msg + "\n"

    return body

#メールを送る関数
def send_message(msg, id, pw):
    server = smtplib.SMTP_SSL("smtp.gmail.com", 465, context=ssl.create_default_context())
    server.login(id, pw)
    server.send_message(msg)
    server.close()
    print("送信完了")

def main():
    #gmailログイン用のデータ
    gmail_account = "*******"
    gmail_password = "*******"

    #宛先,件名,宛名,挨拶,本文(exitで終了),締めの挨拶,署名を入力
    to = input("相手のメールアドレス: ")
    subject = input("件名: ")
    adress = input ("宛名: ")
    body1 = ""
    body1 = add_message(body1, adress)
    greetings = "\n" + "いつも大変お世話になっております。" + "\n" + "関西学院大学 理工学部 情報科学科 吉次亮です。" + "\n"
    body1 = add_message(body1, greetings)
    print("本文: ")
    body = body1 +"\n".join(iter(input, "exit"))
    closing_remarks = "\n\n" + "どうぞよろしくお願いいたします。"
    body = add_message(body, closing_remarks)
    signature = "\n\n" + "吉次 亮（Yoshitsugu Ryo）" + "\n" + "Tel: *******" + "\n" + "Mail: *******"
    body = add_message(body, signature)

    #関数を使用
    msg = create_message(to, subject, body, gmail_account)
    send_message(msg, gmail_account, gmail_password)

if __name__ == "__main__":
    main()