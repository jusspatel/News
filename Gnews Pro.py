from tkinter import *
from gnewsclient import gnewsclient
import requests 
import json
import datetime #line:2
import tkinter .font as tkFont #line:6
import tkinter .messagebox #line:8
from urllib .request import urlopen #line:9
import base64 #line:10
import tkinter.ttk as ttk
from datetime import date




master = Tk()
def OnNewsClick():
    client = gnewsclient.NewsClient(language=lang.get() , location=loc.get() , topic = var.get() , use_opengraph = True ,max_results=10)
    news_list = client.get_news()
    txtarea.configure(state="normal")
    txtarea.delete("1.0",END)
    for i in range(len(news_list)):
        #txtarea.configure(font=("Bahnschrift", 22) )
        txtarea.insert(END, news_list[i]["title"] + "\n\n" )
        #txtarea.configure(font=("Bahnschrift", 20) )
        txtarea.insert(END, "Description:" +  str(news_list[i]["description"]) + "\n\n" )
        txtarea.insert(END, "Read More at:" +  str(news_list[i]["url"]) + "\n\n" )
        txtarea.insert(END , "--------------------------------- " + "\n")
        #txtarea.configure(state="disabled")

            
    
    

def WordMeaningShow():
    '''dictionary=PyDictionary()
    tkinter .messagebox .showinfo ("Sys Message",dictionary.meaning("%s" % lol.get()))#line:120'''
    txtarea.configure(state="normal")
    txtarea.delete("1.0",END)
    api_key ="27ff62c8dad44cc69d94e226f5346363"
    today = date.today()
    today=str(today)
    base_url= "http://newsapi.org/v2/everything"
    fontStyle2 = tkFont.Font(family="Roboto", size=15)

    main_url = base_url + "?q=" + lol.get() + "&from=" +  today + "&sortBy=popularity" + "&apiKey=" + api_key

    open_bbc_page = requests.get(main_url).json() 

    article = open_bbc_page["articles"] 

    for i in range(len(article)):
    
            
        txtarea.configure(font=("Bahnschrift", 15) )
        txtarea.insert(END, str(article[i]["title"]) + "\n" )
        txtarea.insert(END, "Description : " + str(article[i]["description"]) + "\n" )
        txtarea.insert(END, "Read More at:" +  str(article[i]["url"]) + "\n\n" )
        txtarea.insert(END , "--------------------------------- " + "\n")
    

master.geometry("1440x845")
master.resizable(False,False)
master.title("NEWS") 
  
master.configure(bg='black') 
title = Label(master, text="E- NewsPaper", font=("Raleway", 30, "bold"), 
                      pady=13, bd=5, relief=GROOVE , fg ="white" , bg ="black").pack(fill=X)   
result_title = StringVar()
result_link = StringVar() 

var = StringVar(master)
F1 = LabelFrame(master, text="News Categories", font=("Bahnschrift Light", 20, "bold"), bd=1, relief=RAISED,bg="black",fg = "white")
F1.place(x=0, y=80, width=540, relheight=0.34) 
Label(F1, text="Choose language :", justify=LEFT , font =("Roboto 16"),bg="black",fg = "white").grid(row=0, column=0)  
Label(F1, text="Choose Location :", justify=LEFT, font =("Roboto 16"),bg="black",fg = "white").grid(row=2, column=0)   
Label(F1, text="Choose news Topic :", justify=LEFT, font =("Roboto 16"),bg="black",fg = "white").grid(row=4, column=0)   
  
lang = ttk.Entry(F1, font =("Roboto 16"))
lang.grid(row=0 , column =1 , ipadx = 5) 
Label(F1, text="", justify=LEFT, font =("Roboto 16"),bg="black",fg = "white").grid(row=1, column=0)
Label(F1, text="", justify=LEFT, font =("Roboto 16"),bg="black",fg = "white").grid(row=3, column=0)

loc = ttk.Entry(F1, font =("Roboto 16")) 
loc.grid(row=2, column=1,ipadx = 5) 
F2 = ttk.Frame(master, borderwidth=1, relief=RAISED) 
F2.place(x=531, y=80, relwidth=0.3,width=480, relheight=0.9)
news_title = Label(F2, text="---------------------------------------News Area-------------------------------------", font=( "arial", 20, "bold"),borderwidth=2, relief=RAISED , bg = "black" , fg ="white").pack(fill=X) 
scroll_y = Scrollbar(F2, orient=VERTICAL)

txtarea = Text(F2, yscrollcommand=scroll_y.set, font=("Bahnschrift", 15 ), bg='black', fg = "White")
scroll_y.pack(side=RIGHT, fill=Y)

scroll_y.config(command=txtarea.yview)

txtarea.insert( END, "PLEASE SELECT ANY CATEGORY TO SHOW HEADLINES AND PLEASE BE PATIENT SINCE THIS PROCESS CAN TAKE FROM SOMEWHERE BETWEEN 2 - 15 SECONDS , DEPENDING ON PROCESSOR AND INTERNET SPEED") 
txtarea.pack(fill=BOTH, expand=1)
txtarea.configure(state="disabled")
choices = [
 'World',
 'Nation',
 'Business',
 'Technology',
 'Entertainment',
 'Sports',
 'Science',
 'Health']

top = OptionMenu(F1,var,*choices)
var.set(choices[4])

top.grid(row = 4 ,column =1 )
top.config(font = ("Roboto 16"))
F3=LabelFrame(master, text="Temperature Of the Hour", font=("Bahnschrift Light", 20, "bold" ), bd=3, relief=RAISED,bg = "black" ,fg="white")
F3.place(x=0, y=360, width=530, relheight=0.40)  
    
ttk.Button(F1, text="SHOW", command=OnNewsClick).grid(row = 6 ,column = 0 , columnspan = 2,ipadx = 25,pady = 20 , ipady=13) 

F4 = LabelFrame(master, text="Search news by term", font=("Bahnschrift Light", 20, "bold"), bd=1, relief=RAISED,bg="black",fg = "white")
F4.place(x=0, y=690, width=530, relheight=0.17)
ttk.Button(F4 , text="Show" , command=WordMeaningShow).grid(row=0,column=1)
lol = ttk.Entry(F4)
lol.grid(row=0,column=0,ipadx = 25 , ipady= 3)


def startup ():#line:16
    try :#line:17
        OO000O000O0O000O0 ="006d6dbf520677a12b92a3815f743041"#line:18
        O000O00000O00OOOO ="http://api.openweathermap.org/data/2.5/weather?"#line:19
        OOO0OO0OOO000000O =O000O00000O00OOOO +"appid="+OO000O000O0O000O0 +"&q="+city_name .get ()#line:20
        O0O0O00O0O0O00000 =requests .get (OOO0OO0OOO000000O )#line:21
        OO0000000O000O0O0 =O0O0O00O0O0O00000 .json ()#line:22
        O0O00000000O00O0O =OO0000000O000O0O0 ["main"]#line:23
        O00000OO000OO0OO0 =round (O0O00000000O00O0O ["temp"])#line:24
        ct .set (O00000OO000OO0OO0 -273 )#line:25
        OO0O0000OOOOO0000 =O0O00000000O00O0O ["pressure"]#line:26
        cp .set (OO0O0000OOOOO0000 )#line:27
        O000OOOO0O00000O0 =O0O00000000O00O0O ["humidity"]#line:28
        ch .set (O000OOOO0O00000O0 )#line:29
        O0OOO0OO00O00O00O =round (O0O00000000O00O0O ["temp_max"])#line:30
        cm .set (O0OOO0OO00O00O00O -273 )#line:31
        O00O0O0O000O0O00O =round (O0O00000000O00O0O ["temp_min"])#line:32
        cmi .set (O00O0O0O000O0O00O -273 )#line:33
        OOOOO0O0OOOOO00OO =round (O0O00000000O00O0O ["feels_like"])#line:34
        cc .set (OOOOO0O0OOOOO00OO -273 )#line:35
        O00000000OOO0O0OO =OO0000000O000O0O0 ["visibility"]#line:36
        aa .set (O00000000OOO0O0OO )#line:37
        O0000OOOO00OOO0O0 =OO0000000O000O0O0 ["wind"]#line:38
        OO0O000O0O0OOOOO0 =O0000OOOO00OOO0O0 ["speed"]#line:39
        cs .set (OO0O000O0O0OOOOO0 )#line:40
        OOOOO0000OO000OOO =O0000OOOO00OOO0O0 ["deg"]#line:41
        cd .set (OOOOO0000OO000OOO )#line:42
        O0O000O0OO0000OOO =OO0000000O000O0O0 ["coord"]#line:43
        OOO0000OO0O00O0O0 =O0O000O0OO0000OOO ["lon"]#line:44
        OOOO0OO0OOO0O00O0 =O0O000O0OO0000OOO ["lat"]#line:45
        OO0O0O00000O0O00O =OO0000000O000O0O0 ["dt"]#line:46
        OO0OOO000O0OOO000 =datetime .datetime .fromtimestamp (OO0O0O00000O0O00O )#line:47
        jj .set (OO0OOO000O0OOO000 )#line:48
        OOO0OO0000OOOO00O =OO0000000O000O0O0 ["weather"]#line:49
        O0OO0O0O00O00OO0O =OOO0OO0000OOOO00O [0 ]["description"]#line:50
        zz .set (O0OO0O0O00O00OO0O )#line:51
        OOOO0OO00O0O0OOO0 =OO0000000O000O0O0 ["weather"][0 ]["icon"]#line:52
        OO0OO0O00OOO0OOOO ="http://openweathermap.org/img/w/"+OOOO0OO00O0O0OOO0 +".png"#line:53
        OOO0O0OOOO0OOO00O =OO0000000O000O0O0 ["clouds"]#line:54
        OOO00000O00O0OOO0 =OOO0O0OOOO0OOO00O ["all"]#line:55
        dd .set (OOO00000O00O0OOO0 )#line:56
        O00OO00O0OO0OO00O =OO0000000O000O0O0 ["sys"]#line:57
        OOOOO0O0OOO0OOOOO =O00OO00O0OO0OO00O ["country"]#line:58
        ee .set (OOOOO0O0OOO0OOOOO )#line:59
        OO0O00OOO00OO0000 =O00OO00O0OO0OO00O ["sunrise"]#line:60
        OO0OO00O00OOO0O00 =O00OO00O0OO0OO00O ["sunset"]#line:61
        OOOO00O00O0O000OO =datetime .datetime .fromtimestamp (OO0O00OOO00OO0000 )#line:62
        dti .set (OOOO00O00O0O000OO )#line:63
        O0O00O000OOOOO000 =datetime .datetime .fromtimestamp (OO0OO00O00OOO0O00 )#line:64
        dth .set (O0O00O000OOOOO000 )#line:65
        O00OO00OOO0O0OOO0 =OO0000000O000O0O0 ["name"]#line:66
        ll .set (O00OO00OOO0O0OOO0 )#line:67
        O00O0000O0O0OOO0O =tkFont .Font (family ="Lucida Grande",size =27 )#line:70
        O0OOO00OO0000O000 =tkFont .Font (family ="Helvetica",size =13 )#line:71
        OO00O000O00O00000 =tkFont .Font (family ="Roboto",size =15 )#line:72
        Label (F3 ,text ="",textvariable =ct ,font =O00O0000O0O0OOO0O ,fg ="white",bg = "black").grid (row =1 ,column =0 ,columnspan =1 ,rowspan =1 )#line:73
        Label (F3 ,text ="Max Temperature (C): ",font=("Bahnschrift Light", 11 ),fg ="white",bg = "black" ).grid (row =3 ,column =0 )#line:74
        Label (F3 ,text ="",textvariable =cm ,font=("Bahnschrift Light", 11 ),fg ="white",bg = "black" ).grid (row =3 ,column =1 )#line:75
        Label (F3 ,text ="Min Temperature (C): ",font=("Bahnschrift Light", 11 ),fg ="white",bg = "black" ).grid (row =4 ,column =0 )#line:76
        Label (F3 ,text ="",textvariable =cmi ,font=("Bahnschrift Light", 11 ),fg ="white",bg = "black" ).grid (row =4 ,column =1 )#line:77
        Label (F3 ,text ="Temperature Feels like (C): ",font=("Bahnschrift Light", 11 ),fg ="white",bg = "black" ).grid (row =5 ,column =0 )#line:78
        Label (F3 ,text ="",textvariable =cc ,font=("Bahnschrift Light", 11 ),fg ="white",bg = "black" ).grid (row =5 ,column =1 )#line:79
        Label (F3 ,text ="Visibility (in m): ",font=("Bahnschrift Light", 11 ),fg ="white",bg = "black" ).grid (row =6 ,column =0 )#line:80
        Label (F3 ,text ="",textvariable =aa ,font=("Bahnschrift Light", 11 ),fg ="white",bg = "black" ).grid (row =6 ,column =1 )#line:81
        Label (F3 ,text ="Wind Speed (in km): ",font=("Bahnschrift Light", 11 ),fg ="white",bg = "black" ).grid (row =7 ,column =0 )#line:82
        Label (F3 ,text ="",textvariable =cs ,font=("Bahnschrift Light", 11 ),fg ="white",bg = "black" ).grid (row =7 ,column =1 )#line:83
        Label (F3 ,text ="Wind Degree: ",font=("Bahnschrift Light", 11 ),fg ="white" ,bg = "black").grid (row =3 ,column =2 )#line:84
        Label (F3 ,text ="",textvariable =cd ,font=("Bahnschrift Light", 11 ),fg ="white",bg = "black" ).grid (row =3 ,column =3 )#line:85
        Label (F3 ,text ="Pressure (in hPa): ",font=("Bahnschrift Light", 11 ),fg ="white",bg = "black" ).grid (row =4 ,column =2 )#line:86
        Label (F3 ,text ="",textvariable =cp ,font=("Bahnschrift Light", 11 ),fg ="white",bg = "black" ).grid (row =4 ,column =3 )#line:87
        Label (F3 ,text ="Humidity (%): ",font=("Bahnschrift Light", 11 ) ,fg ="white",bg = "black").grid (row =5 ,column =2 )#line:88
        Label (F3 ,text ="",textvariable =ch ,font=("Bahnschrift Light", 11 ),fg ="white",bg = "black" ).grid (row =5 ,column =3 )#line:89
        Label (F3 ,text ="Weather Description: ",font=("Bahnschrift Light", 11 ) ,fg ="white",bg = "black").grid (row =6 ,column =2 )#line:90
        Label (F3 ,textvariable =zz ,font=("Bahnschrift Light", 11 ) ,fg ="white",bg = "black").grid (row =6 ,column =3 )#line:91
        '''Label (F3 ,text ="Sunrise Time:",font=("Bahnschrift Light", 11 ) ).grid (row =7 ,column =2 )#line:92
        Label (F3 ,textvariable =dti ,font=("Bahnschrift Light", 11 ) ).grid (row =7 ,column =3 )#line:93
        Label (F3 ,text ="Sunset Time:",font=("Bahnschrift Light", 11 ) ).grid (row =8 ,column =2 )#line:94
        Label (F3 ,textvariable =dth ,font=("Bahnschrift Light", 11 ) ).grid (row =8 ,column =3 )#line:95'''
        O0O00OOOO0OOOOOO0 =Label (F3 ,textvariable =jj ,font =OO00O000O00O00000,fg ="white",bg = "black" ).grid (row =0 ,column =2 ,columnspan =2 )#line:96
        Label (F3 ,textvariable =ll ,font =OO00O000O00O00000 ,fg ="white",bg = "black").grid (row =1 ,column =2 )#line:97
        Label (F3 ,textvariable =ee ,font =OO00O000O00O00000 ,fg ="white",bg = "black").grid (row =1 ,column =3 )#line:99
        O0O0O000OO000OOOO =Label (F3 ,text ="AQI:",font=("Bahnschrift Light", 11 ),fg ="white" ,bg = "black");O0O0O000OO000OOOO .grid (row =7 ,column =2 )#line:100
        O00O0O00O00OO000O =urlopen (OO0OO0O00OOO0OOOO ).read ()#line:104
        OOOO0OOO000OO0OOO =base64 .encodestring (O00O0O00O00OO000O )#line:105
        OOOO00O00OOO00OO0 =PhotoImage (data =OOOO0OOO000OO0OOO )#line:106
        OOOO00O00OOO00OO0 =OOOO00O00OOO00OO0 .zoom (2 ,2 )#line:107
        O00O0OO000O0O0OOO =Label (F3 ,image =OOOO00O00OOO00OO0,bg = "black" )#line:108
        O00O0OO000O0O0OOO .image =OOOO00O00OOO00OO0 #line:109
        O00O0OO000O0O0OOO .grid (row =9 ,column =0 ,columnspan =4 )#line:110
        OOO00O00OO000OOO0 ="https://api.waqi.info/feed/"+city_name .get ()+"/?token=0574c99883d41944c6ddd40f22de31ffbf39e7b2"#line:111
        OO00O00OO0000O000 =requests .get (OOO00O00OO000OOO0 )#line:112
        OOO0OO0O0O0OO0O00 =OO00O00OO0000O000 .json ()#line:113
        O0OO000O0O0O00000 =OOO0OO0O0O0OO0O00 ["data"]#line:114
        OOOOO0O0OOOO0000O =O0OO000O0O0O00000 [str ("aqi")]#line:115
        aq .set (OOOOO0O0OOOO0000O )#line:116
        Label (F3 ,textvariable =aq ,font=("Bahnschrift Light", 11 ) ,fg ="white",bg = "black").grid (row =7 ,column =3 )#line:117
    except KeyError :#line:119
        tkinter .messagebox .showerror ("Sys Message","City Not Found")#line:120
    except TypeError :#line:121
        tkinter .messagebox .showerror ("Sys Message","The AQI given for the following country is incorrect, beccause there aren't any nearby air quality stations in this location")#line:122
ct =StringVar ()#line:123
cp =StringVar ()#line:124
ch =StringVar ()#line:125
cm =StringVar ()#line:126
cmi =StringVar ()#line:127
cc =StringVar ()#line:128
aa =StringVar ()#line:129
cs =StringVar ()#line:130
cd =StringVar ()#line:131
zz =StringVar ()#line:132
dd =StringVar ()#line:133
dti =StringVar ()#line:134
dth =StringVar ()#line:135
jj =StringVar ()#line:136
ll =StringVar ()#line:137
ee =StringVar ()#line:138
aq =StringVar ()#line:139
b =ttk.Button (F3 ,text ="Check",command =startup )#line:140
b .grid (row =0 ,column =1 )#line:141
city_name =ttk.Entry (F3 ,width =25 )#line:143
city_name .grid (row =0 ,column =0 , ipady = 3)#line:144

mainloop() 
