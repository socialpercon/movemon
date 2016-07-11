import mechanize
import argparse
import sys
import datetime
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import random
import yaml
import os

def get_smtp_config():
    try:
        #config_file = "${AUTO_MONACO_HOME}/etc/smtp.yml"
        config_file = "/home/social/util/monaco/etc/smtp.yml"
        config_file = os.path.expandvars(config_file)
        with open(config_file, 'r') as stream:
            return yaml.load(stream)
    except IOError as e:
        sys.stderr.write('[ERROR] file: {0}, reason: {1}\n'.format(config_file, repr(e)))
        sys.stderr.flush()



def send_mail(cfg_smtp, output_data):
    try:
        title = "{0} CAPTURE COMPLIETE EVENT NOTIFICATION".format(
            time.strftime('%Y/%m/%d %H:%M:%S', datetime.datetime.now().timetuple()))
        cfg_smtp = cfg_smtp["SMTP"]
        msg = MIMEMultipart('alternative')
        msg['From'] = cfg_smtp['ACCOUNT']
        msg['TO'] = ','.join(cfg_smtp['TO_LIST'])
        msg['Subject'] = title
        msg.attach(MIMEText(output_data, 'html', 'utf-8'))

        mail_server = smtplib.SMTP(cfg_smtp['HOST'], cfg_smtp['PORT'])
        mail_server.ehlo()
        mail_server.starttls()
        mail_server.ehlo()
        mail_server.login(cfg_smtp['ACCOUNT'], cfg_smtp['PASSWORD'])
        mail_server.sendmail(cfg_smtp['ACCOUNT'], cfg_smtp['TO_LIST'], msg.as_string())
        mail_server.close()
        return "OK"
    except BaseException as e:
        print "send mail failed, reason: {0}".format(repr(e))
        return "FAIL"

def main(argv):
    try:
        now = datetime.datetime.now()
        now_str = time.strftime('%Y-%m-%d %H-%M-%S', now.timetuple())
        login_str = "capture, time: {0}".format(now_str)
        print login_str
        send_mail(get_smtp_config(), login_str +'\n')
    except BaseException, e:
        print "capture failed, reason: {0}".format(repr(e))

if __name__ == "__main__":
    main(sys.argv[1:])
