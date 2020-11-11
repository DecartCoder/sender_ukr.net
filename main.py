import smtplib
import email.message
import tempmail
import tolist
import database


def start_send():
    tolist.get_all_email()
    get_len_list = tolist.get_len_list()
    for i in range(get_len_list):
        try:
            msg = email.message.Message()
            msg['Subject'] = tempmail.subject
            msg['From'] = 'sale@decart.space'
            msg['To'] = tolist.all_mail[i]
            password = "irifeg84"
            msg.add_header('Content-Type', 'text/html')
            msg.add_header('MIME-Version', '1.0')
            msg.set_payload(tempmail.email_content)
            #Server
            s = smtplib.SMTP(host='vm1543634.1ssd.had.wf', port=587)
            s.starttls()
            # Login Credentials for sending the mail
            s.login(msg['From'], password)
            print(str(msg['From']))
            
            print(str(msg['To']))
            s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
            #database and i
            print(msg['To'])
            database.addlog(msg['To'])
            i += 1
        except:
            i += 2

if __name__ == "__main__":
    while True:
        start_send()
