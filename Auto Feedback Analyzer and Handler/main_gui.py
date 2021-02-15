import tkinter as tk
from tkinter import ttk
from PIL import Image,ImageTk
import twitter
import email_extract
import feedback_check
import summary
from tkcalendar import Calendar, DateEntry
import reply

tup =  ()

date = None
handle = None
def handle():
    reply.start()

def grab_emails():
    email_extract.extract()

def grab_tweets(handle):
    twitter.see_tweets(handle.get() , date)

def date_entry(frame):
    def something(top):
        global date
        print(type(cal.get_date()))
        date = cal.get_date()
        #cal.quit()
    top = tk.Toplevel(frame)

    ttk.Label(top, text='Choose date').pack(padx=10, pady=10)

    cal = DateEntry(top, width=12, background='darkblue',
                    foreground='white', borderwidth=2)
    cal.pack(padx=10, pady=10)
    btn = tk.Button(top, text='ok', command =lambda: something(top))
    btn.pack()

def analyze_sentiments():
    global tup
    tup = feedback_check.predict()
def results():
    print(tup)
    feedback_check.result_viewer(tup)


def generate_summary():
    print(summary.summerize())



def Home():
    root = tk.Tk()
    root.geometry('600x500')
    root.title('tkinter')
    root.config(bg = '#f4f5db')
    handle = tk.StringVar(root)


    u_frame = tk.Frame(root)
    u_frame.grid(row= 0, column=0)
    

    headingLabel =  tk.Label(u_frame, text = ' Heading ', font='candara 30 bold',compound='left',bg='#f4f5db'  )
    headingLabel.grid(row = 0,column= 0)
    root.grid_columnconfigure(0, weight=1)

    u1_frame = tk.Frame(root,bg = '#f4f5db')
    u1_frame.grid(row=1, column = 0 )
    dateLabel = tk.Label(u1_frame, text = 'Starting Date ', font = 'candara 14', bg = '#f7f7e8' ).grid(row =0, sticky = 'w')
    tk.Button(u1_frame, text='DateEntry', command= lambda: date_entry(u1_frame) , relief = 'sunken').grid(row=0,column=0,columnspan = 2, padx=10, pady=10)
    
    Label1 = tk.Label(u1_frame, text = 'Twitter Handle', font = 'candara 14', bg = '#f7f7e8' ).grid(row =1,column = 0)
    Entry1 = tk.Entry(u1_frame, font = 'candara 12',textvariable = handle ).grid(row = 1,column = 1, padx = 10, pady = 10)

    Button1 = tk.Button(u1_frame, text = 'Get Tweets', font = 'candara 12', bg = 'white', command = lambda: grab_tweets(handle))
    Button1.grid(row = 2, column = 0,columnspan = 2,padx=10, pady=10)    

    label2 = tk.Label(u1_frame, text = 'Email  ' , font = 'candara 14' , bg = '#f7f7e8')
    label2.grid(row = 3, column =0,)
    button2 = tk.Button(u1_frame, text = 'Get Emails', font = 'candara 12', bg = '#f7f7e8', command = grab_emails)
    button2.grid(row = 3, column = 0, columnspan = 2,padx=10, pady=10)

    lowerFrame = tk.Frame(root , bg = '#f7f7e8' )
    lowerFrame.grid(row = 2, column = 0)
    button3 = tk.Button(lowerFrame , text = 'Analyze' , font = 'candara 12' , bg = '#f7f7e8', command = analyze_sentiments )
    button3.grid(row = 0, column = 0, padx = 20, pady = 10)
    button4 = tk.Button(lowerFrame, text = 'Handle', font = 'candara 12' , bg = '#f7f7e8', command = handle)
    button4.grid(row = 0, column = 1 , padx = 20, pady = 10)

    lowestFrame = tk.Frame(root, bg = '#f4f5db')
    lowestFrame.grid(row = 3, column = 0)
    Button5 = tk.Button(lowestFrame, text = 'Results',font = 'candara 12' , bg = '#f7f7e8', command = results )
    Button5.grid(row = 0, column = 1, padx = 20, pady = 10)
    button6 = tk.Button(lowestFrame,text = 'Generate Summary', font = 'candara 12' ,bg = '#f7f7e8', command = generate_summary )
    button6.grid(row=1, column = 1,  padx = 20, pady = 10)


    root.mainloop()

Home()