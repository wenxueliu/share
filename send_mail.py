#!/usr/bin/env python
# encoding: utf-8


import smtplib

class SMTPClient(object):

    # SMTP协议默认端口是25
    # google cloud only 994 can work, see https://cloud.google.com/compute/docs/tutorials/sending-mail/
    def __init__(self, smtp_server, login, receivers, smtp_port=25):
        self._login = login
        self._smtp_server = smtp_server
        self._smtp_port = smtp_port
        self._receivers = receivers
        self._server = None

    #def on_debug():
    #    self._server.set_debuglevel(1)

    def send_email(self, body):
        return self._send_email(self._receivers, "bihu article update", body)

    def get_plain(self, subject, body):
        msg = MIMEText(body, 'plain', 'utf-8')
        msg['From'] = self._login["user"]
        msg['To'] = ",".join(self._receivers[1:])
        msg['Subject'] = subject
        msg['Cc'] = ",".join(subscriber)
        return msg

    def get_html(self, subject, body):
        msg = MIMEText('<html><body><h1>' + subject + '</h1>' +
        '<p>' + body + '</p>' +
        '</body></html>', 'html', 'utf-8')
        msg['From'] = self._login["user"]
        msg['To'] = ",".join(self._receivers)
        msg['Subject'] = subject
        return msg

    def _send_email(self, receivers, subject, body):
        log.debug("%s:%s", self._smtp_server, self._smtp_port)
        success = False
        try:
            # if timeout less than 5, timeout will be a problem
            self._server = smtplib.SMTP_SSL(self._smtp_server, self._smtp_port, timeout = 20)
            msg = self.get_plain(subject, body)
            self._server.login(self._login["user"], self._login["passwd"])
            self._server.sendmail(self._login["user"], self._receivers, msg.as_string())
            self._server.quit()
            success = True
        except Exception, e:
            log.error(e, exc_info=True)
        finally:
            if self._server is not None:
                self._server.close()
        return success


login = {
    "user" : "",
    "passwd" : ""
}

dest_list = [
    "xxxx@126.com"
]
smtp_client = SMTPClient("smtp.126.com", login, dest_list, smtp_port = 994)
