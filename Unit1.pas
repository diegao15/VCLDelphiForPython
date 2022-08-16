unit Unit1;

interface

uses
  Winapi.Windows, Winapi.Messages, System.SysUtils, System.Variants, System.Classes, Vcl.Graphics,
  Vcl.Controls, Vcl.Forms, Vcl.Dialogs, Vcl.StdCtrls, Vcl.ExtCtrls;

type
  TForm1 = class(TForm)
    Panel1: TPanel;
    ImageSS: TImage;
    Label1: TLabel;
    editFilePath: TEdit;
    ButtonTakeSS: TButton;
    Bevel1: TBevel;
    Label2: TLabel;
    EditHttpRequest: TEdit;
    ButtonHttpRequest: TButton;
    MemoHttpResponse: TMemo;
    Bevel2: TBevel;
    Label3: TLabel;
    EditSMTPServer: TEdit;
    Label4: TLabel;
    EditPort: TEdit;
    Label5: TLabel;
    EditUsername: TEdit;
    EditPassword: TEdit;
    Label6: TLabel;
    Label7: TLabel;
    EditEmailTo: TEdit;
    EditSubject: TEdit;
    Label8: TLabel;
    MemoBodyMsg: TMemo;
    Label9: TLabel;
    ButtonSendMail: TButton;
    LabelEmailStatus: TLabel;
  private
    { Private declarations }
  public
    { Public declarations }
  end;

var
  Form1: TForm1;

implementation

{$R *.dfm}

end.
