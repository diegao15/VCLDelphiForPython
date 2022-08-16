from delphivcl import *
import os
import pyautogui
import requests
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class MainForm(Form):
    def __init__(self, owner):
        self.LoadProps(os.path.join(os.path.dirname(os.path.abspath(__file__)),"Unit1.pydfm"))
        self.__config_comps()        
    def __config_comps(self):
        self.ButtonTakeSS.SetProps(Caption = "Screen Shot from python", OnClick = self.__on_screen_shot_click)
        self.ButtonHttpRequest.SetProps(Caption = "Http request", OnClick = self.__on_http_request_click)
        self.ButtonSendMail.SetProps(Caption = "Send email", OnClick = self.__on_send_email_click)
    def __on_screen_shot_click(self,sender):
        ss = pyautogui.screenshot()
        ss.save(self.editFilePath.Text)
        self.ImageSS.Picture.LoadFromFile(self.editFilePath.Text)
    def __on_http_request_click(self, sender):
        self.MemoHttpResponse.Lines.Text = requests.get(self.EditHttpRequest.Text).text
    def __on_send_email_click(self, sender):
        self.LabelEmailStatus.Font.Color = "$000C16E7"
        server = smtplib.SMTP(self.EditSMTPServer.Text,self.editPort.Text)
        server.connect(self.EditSMTPServer.Text,self.editPort.Text)
        server.starttls()
        try:
            server.login(self.EditUsername.Text,self.EditPassword.Text)
            msg = MIMEMultipart('alternative')
            msg['Subject'] = self.EditSubject.Text
            msg['From'] = self.EditUsername.Text
            msg['To'] = self.EditEmailTo.Text
            mailBody = MIMEText(self.MemoBodyMsg.Lines.Text, 'html')
            msg.attach(mailBody)
            server.sendmail(self.EditUsername.Text,self.EditEmailTo.Text,msg.as_string())
            server.quit()
            self.LabelEmailStatus.Caption = "Email sent successfuly.."
            self.LabelEmailStatus.Font.Color = "$00A20F0F"
        except:
            self.LabelEmailStatus.Caption = "Failed to send email..."
            self.LabelEmailStatus.Font.Color = "$000C16E7"
        
        #ButtonSendMail
def main():
    Application.Initialize()
    Application.Title = "Python tool";
    Main = MainForm(Application)
    Main.Show()
    FreeConsole()
    Application.Run()
    Main.Destroy()
    
if __name__ == '__main__':
    main()
