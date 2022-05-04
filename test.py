# # a_string = "0100AM"
# # a_string = a_string[:2] + ":" + a_string[2:]
# # a_string = a_string[:5] + ":" + a_string[5:]
# # print(a_string)
# # a_string = a_string.replace(":","")
# # print(a_string)

# # from numpy import save, load
# # from os import path
# # time = "8:00 pm"
# # discription = "This is test Remainder"
# # listTitle = "Test Remainder"
# # showEmpty = " "*20+"Empty"
# # def takeList():
# #     myList = f"Label:{discription}\nTime:{time}"
# #     fileName = f"{listTitle}.npy"
# #     titleA = "D:\\Projects\\Remainder App\\list\\"+fileName
# #     if path.isfile(f"D:\\Projects\\Remainder App\\list\\{fileName}") == False:
# #         save(titleA, myList)
# #     else:
# #         print("File already exists.")

# # Import module
# # from tkinter import *

# # # Create object
# # root = Tk()

# # # Adjust size
# # root.geometry( "200x200" )

# # # Change the label text
# # def show():
# # 	label.config( text = clicked.get() )

# # # Dropdown menu options
# # options = [
# # 	"1",
# # 	"2",
# # 	"3",
# # 	"4",
# # 	"5",
# # 	"6",
# # 	"7"
# # ]

# # # datatype of menu text
# # clicked = StringVar()

# # # initial menu text
# # clicked.set( "Monday" )

# # # Create Dropdown menu
# # drop = OptionMenu( root , clicked , *options )
# # drop.pack()

# # # Create button, it will change label text
# # button = Button( root , text = "click Me" , command = show ).pack()

# # # Create Label
# # label = Label( root , text = " " )
# # label.pack()

# # # Execute tkinter
# # root.mainloop()
# # for i in range(60):
# #     print(f"'{i}',", end="")

# # import tkinter as tk
# # from tktimepicker import AnalogPicker, AnalogThemes
# # # note: you can also make use of mouse wheel or keyboard to scroll or enter the spin timepicker
# # root = tk.Tk()

# # time_picker = AnalogPicker(root)
# # time_picker.pack(expand=True, fill="both")

# # # theme = AnalogThemes(time_picker)
# # # theme.setDracula()

# # root.mainloop()
# # if __name__ == "__main__":
# #     from win10toast import ToastNotifier
# #     toast = ToastNotifier()
# #     toast.show_toast("Notification","Notification body",duration=20,icon_path="D:\\Projects\\Remainder App\\others\\a.ico")

# # time = []
# # print(time)
# # for i in range(5):
# #     a = input("Enter Time:")
# #     time.append(a)
# # time.pop(2)
# # print(time)

# # from numpy import save
# # from os import listdir
# # time = []
# # save("time1","this is time")
# # save("time2","This is another time")
# # save("time3","this is another another time")
# # save("time4","this is another another another time")
# # for i in listdir():
# #     if i.endswith(".npy"):
# #         time.append(i)
# # print(time)
# # if "time8.npy" in time:
# #     print("Yes it is.")
# # else:
# #     print("No.")



# # from datetime import datetime   #To set date and time
# # from playsound import playsound     #To play sound

# # def validate_time(alarm_time):
# #     if len(alarm_time) != 11:
# #         return "Invalid time format! Please try again..."
# #     else:
# #         if int(alarm_time[0:2]) > 12:
# #             return "Invalid HOUR format! Please try again..."
# #         elif int(alarm_time[3:5]) > 59:
# #             return "Invalid MINUTE format! Please try again..."
# #         elif int(alarm_time[6:8]) > 59:
# #             return "Invalid SECOND format! Please try again..."
# #         else:
# #             return "ok"

# # while True:
# #     alarm_time = input("Enter time in 'HH:MM:SS AM/PM' format: ")
    
# #     validate = validate_time(alarm_time.lower())
# #     if validate != "ok":
# #         print(validate)
# #     else:
# #         print(f"Setting alarm for {alarm_time}...")
# #         break

# # alarm_hour = alarm_time[0:2]
# # alarm_min = alarm_time[3:5]
# # alarm_sec = alarm_time[6:8]
# # alarm_period = alarm_time[9:].upper()

# # while True:
# #     now = datetime.now()

# #     current_hour = now.strftime("%I")
# #     current_min = now.strftime("%M")
# #     current_sec = now.strftime("%S")
# #     current_period = now.strftime("%p")

# #     if alarm_period == current_period:
# #         if alarm_hour == current_hour:
# #             if alarm_min == current_min:
# #                 if alarm_sec == current_sec:
# #                     print("Wake Up!")
# #                     playsound('D:/Library/Documents/Projects/Coding/Beginner Python Projects/Alarm Clock/alarm.wav')
# #                     break

# # import pickle
# # dataset = ["4525","9856","7584","5623","7532"]
# # dataset.append("4652")
# # outputFile = "time.data"
# # fw = open(outputFile, "wb")
# # pickle.dump(dataset, fw)
# # fw.close()

# # import pickle
# # inputFile = 'time.data'
# # fd = open(inputFile, 'rb')
# # dataset = pickle.load(fd)
# # print(dataset)


# # def removeList():
# #     if todoList.get(ACTIVE) != " "*20+"Empty":
# #         toRemoveFile = todoList.get(ACTIVE)
# #         toRemove = f"D:\\Projects\\Remainder App\\list\\{toRemoveFile}.npy"
# #         print(toRemove)
# #         index = todoList.curselection()
# #         todoList.delete(index)
# #         remove(toRemove)
# #     else:
# #         print("List is empty")

# # list = ["58245","12562","84756","52654","85654"]
# # if "12562" in list:
# #     print("Yes")

# # from os import system
# # system("cls")
# # sentence = "Title:apple ball cat dog\nDiscription:These are the words whick we learnt when we were kid"
# # sentence1 = sentence.replace(":"," ")
# # sentence2 = sentence1.split()
# # sentence3 = sentence2[1:sentence2.index("Discription")]
# # sentence4 = sentence2[sentence2.index("Discription")+1:]
# # notificationTitle =  (" ".join(sentence4))
# # notificationBody = (" ".join(sentence3))
# # print(notificationTitle)
# # print(notificationBody)

# # import pyttsx3
# # engine = pyttsx3.init()
# # voices = engine.getProperty('voices')
# # engine.setProperty('voice', voices[1].id)
# # engine.setProperty("rate", 150)
# # def talk(text):
# #     engine.say(text)
# #     engine.runAndWait()
# # talk("my name is bidhan acharya")

# # from infi.systray import SysTrayIcon
# # from tkinter import Tk, Button
# # root = Tk()
# # def say_hello(systray):
# #     print("Hello, World!")
# # def sysTray():
# #     menu_options = (("Say Hello", None, say_hello),)
# #     systray = SysTrayIcon("D:\\Projects\\Remainder App\\others\\a.ico", "Example tray icon", menu_options)
# #     systray.start()
# # Button(root, text="click", command= sysTray).pack()
# # root.mainloop()
# from tkinter import *
# from pystray import MenuItem as item
# import pystray
# from PIL import Image, ImageTk

# # Create an instance of tkinter frame or window
# win=Tk()
# win.title("System Tray Application")

# # Set the size of the window
# win.geometry("700x350")

# # Define a function for quit the window
# def quit_window(icon, item):
#    icon.stop()
#    win.destroy()

# # Define a function to show the window again
# def show_window(icon, item):
#    icon.stop()
#    win.after(0,win.deiconify())

# # Hide the window and show on the system taskbar
# def hide_window():
#    win.withdraw()
#    image=Image.open("D:\\Projects\\Remainder App\\others\\a.ico")
#    menu=(item('Quit', quit_window), item('Show', show_window))
#    icon=pystray.Icon("name", image, "My System Tray Icon", menu)
#    icon.run()

# win.protocol('WM_DELETE_WINDOW', hide_window)

# win.mainloop()
# import os
# try:
#     os.mkdir("listt")
# except Exception as e:
#     print(e)