import requests
from tkinter import *
import datetime as dt
from tkinter import messagebox
import json
#print("Conneced")
#api_address=""
m = Tk()
m.title("Today's Weather App")
m.iconbitmap('weather.ico')
m.resizable(0,0)
m.geometry("600x250+300+300")
m.config(bg="#87ceeb")
bg_image = PhotoImage(file ="Weather.gif")
x = Label (image = bg_image)
w = Label(m, text=f"{dt.datetime.now():%a, %b %d %Y}", fg="white", bg="black", font=("helvetica", 12))
l=Label(m,text="Weather Checker App",bg="blue",fg="yellow",relief="raised",width=80,font="Bahnschrift 14")
city=Label(m,text="City",fg="Red",bg="white",font="Bahnschrift 9")
txtcity = Entry(m,relief="raised",width=20,font="Bahnschrift 10")
#txtcity.insert(0, 'Enter Your City')
def ask_quit():
    if messagebox.askokcancel("Quit", "You want to quit now?"):
        m.destroy()
m.protocol("WM_DELETE_WINDOW", ask_quit)
city.place(x=160,y=120)
txtcity.place(x=220,y=120)
def search():
    if txtcity.index("end")==0:
        msg=messagebox.showerror("Failed","Enter your city first")
    else:
        try:
            api_address="http://api.openweathermap.org/data/2.5/weather?APPID=c460d6a0dfcf81cd771487c46609401b&q="
            city=txtcity.get()
            #print(city)
            url=api_address+city
            #print(url)
            json_data=requests.get(url).json()
            '''parsed_json = (json.loads(json_data))
            print(json.dumps(parsed_json, indent=4, sort_keys=True))'''
            formatted_data=json_data['main']['temp']
            formatted_data2=json_data['weather'][0]['description']
            formatted_data=formatted_data-273.15
            #print(formatted_data)
            finaldata=str(round(formatted_data,2))+" °C tempature and Weather:"+str(formatted_data2)
            msg=messagebox.showinfo("Weather of {}".format(city),finaldata)
            txtcity.delete(0,END)
        except Exception as e:
            msg=messagebox.showerror("Failed","Enter the valid city")
            txtcity.delete(0,END)
seacrhbtn = Button(m, text = "Search", command =search,activebackground="#000fff000",activeforeground="Yellow",relief=RAISED)
seacrhbtn.place(x=180,y=180)
seacrhbtn.config(width=25,height=1)
l.pack()
w.pack()
x.pack()
m.mainloop()
