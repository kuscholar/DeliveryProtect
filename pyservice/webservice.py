#!/usr/bin/env python
import sqlite3
import smtplib
import cgi
import json
import cv2
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from email.mime.text import MIMEText
from email.MIMEMultipart import MIMEMultipart
from email.MIMEImage import MIMEImage

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()
        self.wfile.write("Parcel sensor service running!")
        return
    def cam(self):
        
        cam0 = cv2.VideoCapture(2)
        ret, image = cam0.read()
        cv2.imwrite('/home/pi/Desktop/Kusch/images/parcel.jpg' ,image)
        cam0.release()
        cv2.destroyAllWindows()
    def camTaken(self):
        
        cam1 = cv2.VideoCapture(0)
        ret, image = cam1.read()
        cv2.imwrite('/home/pi/Desktop/Kusch/images/taken.jpg' ,image)
        cam1.release()
        cv2.destroyAllWindows()
    def do_POST(self):
        content_len = int(self.headers.getheader('content-length', 0))
        post_body = self.rfile.read(content_len)
        # print(post_body)
        sender = 'example@gmail.com'
        receivers = ['receiver@hotmail.com']
        password = 'password'
        fromad = 'Raspberry Pi Parcel Sensor <example@gmail.com>'
        toad = 'Name <receiver@hotmail.com>'       
        body = ''
        msg = MIMEMultipart('related')
        msg['From'] = fromad
        msg['To'] = toad
        
        
        if(post_body == "0"):
            subject = 'A new parcel has been delivered'
            # self.cam()
            # fp = open('/home/pi/Desktop/Kusch/images/parcel.jpg', 'rb')
            # msgImage = MIMEImage(fp.read(), _subtype="jpeg")
            # fp.close()
            # msg.attach(msgImage)
        elif(post_body == "1"):
            subject = 'The parcel has been taken'
            self.camTaken()
            fp = open('/home/pi/Desktop/Kusch/images/taken.jpg', 'rb')
            msgImage = MIMEImage(fp.read(), _subtype="jpeg")
            fp.close()
            msg.attach(msgImage)
        print(subject)
        msg['Subject'] = subject
        msgTEXT = MIMEText(body)
        
        try:
            
            smtp = smtplib.SMTP('smtp.gmail.com',587)
            
            smtp.ehlo()
            
            smtp.starttls()
            
            smtp.ehlo()
            
            smtp.login(sender,password)
            
            smtp.sendmail(sender, receivers, msg.as_string())
            print("Email sent!")
            smtp.close()
        except smtplib.SMTPException:
            print("Error: unable to send email")
            
class WebService():
    port = 8081
    def start_server(self):
        server = HTTPServer(('', self.port), RequestHandler)
        server.serve_forever()
        
if __name__ == "__main__":
    webservice = WebService()
    webservice.start_server()

