import smtplib
import email.utils
from email.mime.text import MIMEText
from config import Config
class ActionList():

    smtpObj = smtplib.SMTP(Config.MAIL_SERVER)
 
    def ice_email(self):

        FROM = Config.EMAIL_FROM

        FROM_NAME = Config.EMAIL_FROM_NAME

        TO = Config.EMAIL_TO
        TO_NAME = Config.EMAIL_TO_NAME
        
        SUBJECT = Config.ICY_EMAIL_SUBJECT
        
        BODY = MIMEText("The parking lost is icy this morning. Please be careful")
        BODY['To'] = email.utils.formataddr((TO_NAME, TO))
        BODY['From'] = email.utils.formataddr((FROM_NAME, FROM))
        BODY['Subject'] = SUBJECT

        self.smtpObj.sendmail(FROM, TO, BODY.as_string())
        self.smtpObj.quit()

        

    def error_email(self, error_code):

        FROM = Config.EMAIL_FROM
        FROM_NAME = Config.EMAIL_FROM_NAME
        TO = Config.ERROR_EMAIL
        SUBJECT = Config.ERROR_EMAIL_SUBJECT
        BODY = MIMEText(str(error_code))
        BODY['To'] = email.utils.formataddr((Config.ERROR_EMAIL_TO_NAME, TO))
        BODY['From'] = email.utils.formataddr((FROM_NAME, FROM))
        BODY['Subject'] = SUBJECT
        self.smtpObj.sendmail(FROM, TO, BODY.as_string())
        self.smtpObj.quit()

if __name__ == '__main__':
    ActionList()