import os
from delphivcl import *

class Form1(Form):

    def __init__(self, owner):
        self.Panel1 = None
        self.ImageSS = None
        self.Label1 = None
        self.editFilePath = None
        self.ButtonTakeSS = None
        self.Bevel1 = None
        self.Label2 = None
        self.EditHttpRequest = None
        self.ButtonHttpRequest = None
        self.MemoHttpResponse = None
        self.Bevel2 = None
        self.Label3 = None
        self.EditSMTPServer = None
        self.Label4 = None
        self.EditPort = None
        self.Label5 = None
        self.EditUsername = None
        self.EditPassword = None
        self.Label6 = None
        self.Label7 = None
        self.EditEmailTo = None
        self.EditSubject = None
        self.Label8 = None
        self.MemoBodyMsg = None
        self.Label9 = None
        self.ButtonSendMail = None
        self.LabelEmailStatus = None
        self.LoadProps(os.path.join(os.path.dirname(os.path.abspath(__file__)), "Unit1.pydfm"))

def main():
    Application.Initialize()
    Application.Title = 'Form1'
    MainForm = Form1(Application)
    MainForm.Show()
    FreeConsole()
    Application.Run()

if __name__ == '__main__':
    main()
