from tkinter import *
from mydb import Database
from  tkinter import messagebox
from myapi import API

class NLPApp:
    def __init__(self):
        self.dbo = Database()
        self.apio = API()
        # login ka gui load karna
        self.root = Tk()
        self.root.title('NLPApp')
        self.root.iconbitmap('resources/favicon1.png')
        self.root.geometry('360x500')
        self.root.configure(bg='#34495E')
        self.login_gui()
        self.root.mainloop()
    def login_gui(self):
        # clear the existing ones
        self.clear_gui()

        heading = Label(self.root,text='NLPApp',fg='white')
        # when we made any labels we need to tell the gui geometry managers - pack and  grid
        heading.pack(pady =(30,30))
        heading.configure(font=('verdana',24,'bold'),bg='#34495E')

        label1 = Label(self.root,text='Enter Email',border=4,borderwidth=5,fg='black')
        label1.pack(pady=(10,10))
        # Entry box did not take height parameter
        self.email_input = Entry(self.root,width=50)
        self.email_input.pack(pady=(5,10),ipady=5)

        label2 = Label(self.root, text='Enter Password', border=4, borderwidth=5, fg='black')
        label2.pack(pady=(10, 10))
        self.password_input = Entry(self.root, width=50,show='*')
        self.password_input.pack(pady=(5, 10), ipady=5)
        # button  can take height parameter
        login_button = Button(self.root,text='Login',width=15,height=2,command=self.perform_login)
        login_button.pack(pady=(10,10))

        label3 = Label(self.root, text='Not a member?', border=4, borderwidth=5, fg='black')
        label3.pack(pady=(20, 10))

        redirect_button = Button(self.root, text='Register Now', width=30, height=2,command=self.register_gui)
        redirect_button.pack(pady=(10, 10))

    def register_gui(self):
        self.clear_gui()
        heading1 = Label(self.root,text='NLP Registration',fg='White')
        heading1.pack(pady=(10,10))
        heading1.configure(font=('verdana', 24, 'bold'), bg='#34495E')

        label0= Label(self.root, text='Enter Name', border=4, borderwidth=5, fg='black')
        label0.pack(pady=(10, 10))
        # Entry box did not take height parameter
        self.name_input = Entry(self.root, width=50)
        self.name_input.pack(pady=(5, 10), ipady=5)

        label1 = Label(self.root, text='Enter Email', border=4, borderwidth=5, fg='black')
        label1.pack(pady=(10, 10))
        # Entry box did not take height parameter
        self.email_input = Entry(self.root, width=50)
        self.email_input.pack(pady=(5, 10), ipady=5)

        label2 = Label(self.root, text='Enter Password', border=4, borderwidth=5, fg='black')
        label2.pack(pady=(10, 10))
        self.password_input = Entry(self.root, width=50, show='*')
        self.password_input.pack(pady=(5, 10), ipady=5)

        label3 = Label(self.root, text='Confirm your Password', border=4, borderwidth=5, fg='black')
        label3.pack(pady=(10, 10))
        self.confirm_password_input = Entry(self.root, width=50, show='*')
        self.confirm_password_input.pack(pady=(5, 10), ipady=5)

        # button  can take height parameter
        register_button = Button(self.root, text='Register', width=15, height=2,command=self.perform_registration)
        register_button.pack(pady=(10, 10))

        label4 = Label(self.root, text='Already a member?', border=4, borderwidth=5, fg='black')
        label4.pack(pady=(20, 10))

        redirect_button = Button(self.root, text='Login Now', width=30, height=2, command=self.login_gui)
        redirect_button.pack(pady=(10, 10))
    def clear_gui(self):
        for i in self.root.pack_slaves():
            i.destroy()
    def perform_registration(self):
        # fecthing the data from gui
        name = self.name_input.get()
        email = self.email_input.get()
        password =self.password_input.get()

        response = self.dbo.add_data(name,email, password)

        if response:
            messagebox.showinfo('Success','Registraion Successful ! you can login now')
        else:
            messagebox.showerror('Error','Email Already Exists')
    def perform_login(self):
        email = self.email_input.get()
        password = self.password_input.get()
        response = self.dbo.login_page(email,password)
        if response:
            messagebox.showinfo('Success','Login Successful')
            self.home_gui()
        else:
            messagebox.showerror('Error','Incorrect Email/password')
    def home_gui(self):
        self.clear_gui()
        # analysis part
        heading = Label(self.root, text='NLPApp', fg='white')
        # when we made any labels we need to tell the gui geometry managers - pack and  grid
        heading.pack(pady=(30, 30))
        heading.configure(font=('verdnan', 24, 'bold'), bg='#34495E')

        sentiment_btn = Button(self.root,text='Sentiment Analysis',width =30,height=4,command=self.sentiment_gui)
        sentiment_btn.pack(pady=(10,10))

        ner_btn = Button(self.root, text='Named Entity Recognition', width=30, height=4,command=self.named_entity_recognition_gui)
        ner_btn.pack(pady=(10, 10))

        emotion_btn = Button(self.root, text='Emotion prediction', width=30, height=4,command=self.emotion_gui)
        emotion_btn.pack(pady=(10, 10))

        logout_btn = Button(self.root, text='Logout', width=10, height=2,command=self.login_gui)
        logout_btn.pack(pady=(10, 10))
    def sentiment_gui(self):
        self.clear_gui()
        heading = Label(self.root, text='NLPApp', fg='white')
        # when we made any labels we need to tell the gui geometry managers - pack and  grid
        heading.pack(pady=(30, 30))
        heading.configure(font=('verdana', 24, 'bold'), bg='#34495E')

        heading1 = Label(self.root, text='Sentiment Analysis', fg='white')
        # when we made any labels we need to tell the gui geometry managers - pack and  grid
        heading1.pack(pady=(10, 20))
        heading1.configure(font=('verdana', 20), bg='#34495E')

        label1 = Label(self.root,text='Enter the text')
        label1.pack(pady=(10,10))
        self.sentiment_input = Entry(self.root, width=50)
        self.sentiment_input.pack(pady=(5, 10), ipady=5)

        sentiment_btn = Button(self.root, text='Analyze sentiment', width=30, height=3, command=self.do_sentiment_analysis)
        sentiment_btn.pack(pady=(10, 10))

        self.ner_result = Label(self.root,text='',bg='#34495E',fg='white')
        self.ner_result.pack(pady=(10,10))
        self.ner_result.configure(font=('verdana',16))

        goback_btn = Button(self.root, text='Go Back', width=10, height=3, command=self.home_gui)
        goback_btn.pack(pady=(10, 10))
    def do_sentiment_analysis(self):

        input_text = self.sentiment_input.get()
        result = self.apio.sentiment_analysis(input_text)

        txt = ''
        for i in result['sentiment']:
            txt = txt + i + ' -> ' + str(result['sentiment'][i]) + '\n'

        self.sentiment_result['text'] = txt

    def named_entity_recognition_gui(self):
        self.clear_gui()
        heading = Label(self.root, text='NLPApp', fg='white')
        # when we made any labels we need to tell the gui geometry managers - pack and  grid
        heading.pack(pady=(30, 30))
        heading.configure(font=('verdana', 24, 'bold'), bg='#34495E')

        heading1 = Label(self.root, text='Named Entity Recognition', fg='white')
        # when we made any labels we need to tell the gui geometry managers - pack and  grid
        heading1.pack(pady=(10, 20))
        heading1.configure(font=('verdana', 20), bg='#34495E')

        label1 = Label(self.root, text='Enter the text')
        label1.pack(pady=(10, 10))
        self.named_entity_recognition_input = Entry(self.root, width=50)
        self.named_entity_recognition_input.pack(pady=(5, 10), ipady=5)

        sentiment_btn = Button(self.root, text='Analyze Ner', width=30, height=3,
                               command=self.do_ner_analysis)
        sentiment_btn.pack(pady=(10, 10))

        self.ner_result = Label(self.root, text='', bg='#34495E', fg='white')
        self.ner_result.pack(pady=(10, 10))
        self.ner_result.configure(font=('verdana', 16))

        goback_btn = Button(self.root, text='Go Back', width=10, height=3, command=self.home_gui)
        goback_btn.pack(pady=(10, 10))
    def do_ner_analysis(self):
        named_input = self.named_entity_recognition_input.get()
        result = self.apio.ner_analysis(named_input)

        self.ner_result['text'] = result
    def emotion_gui(self):
        self.clear_gui()
        heading = Label(self.root, text='NLPApp', fg='white')
        # when we made any labels we need to tell the gui geometry managers - pack and  grid
        heading.pack(pady=(30, 30))
        heading.configure(font=('verdana', 24, 'bold'), bg='#34495E')

        heading1 = Label(self.root, text='Emotion Analysis', fg='white')
        # when we made any labels we need to tell the gui geometry managers - pack and  grid
        heading1.pack(pady=(10, 20))
        heading1.configure(font=('verdana', 20), bg='#34495E')

        label1 = Label(self.root, text='Enter the text')
        label1.pack(pady=(10, 10))
        self.emotion_input = Entry(self.root, width=50)
        self.emotion_input.pack(pady=(5, 10), ipady=5)

        sentiment_btn = Button(self.root, text='Analyze Emotion', width=30, height=3,
                               command=self.do_emotion_analysis)
        sentiment_btn.pack(pady=(10, 10))

        self.emotion_result = Label(self.root, text='', bg='#34495E', fg='white')
        self.emotion_result.pack(pady=(10, 10))
        self.emotion_result.configure(font=('verdana', 16))

        goback_btn = Button(self.root, text='Go Back', width=10, height=3, command=self.home_gui)
        goback_btn.pack(pady=(10, 10))
    def do_emotion_analysis(self):
        emotion_named_input = self.emotion_input.get()
        result = self.apio.emotion_analysis(emotion_named_input)

        self.emotion_result['text'] = result





nlp = NLPApp()