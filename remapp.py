from threading import Thread
from time import sleep, strftime
from tkinter import ACTIVE, MULTIPLE, N, SW, IntVar, Checkbutton, Label, SE, Spinbox, S, CENTER, DISABLED, E, INSERT, SINGLE, TOP, W, Button, Entry, StringVar, Tk, Listbox, END, Text, LabelFrame
from tkinter.font import NORMAL
from numpy import save, load
from os import system, path, listdir, remove
import pythoncom
from win32com.client import Dispatch
from win10toast import ToastNotifier
from pyttsx3 import init
root = Tk()
speaker = init()
voices = speaker.getProperty('voices')
speaker.setProperty('voice', voices[1].id)
speaker.setProperty("rate", 160)
system("cls")
root.resizable(False, False)
window_width = 600
window_height = 420
root.title("Remainder APP - Bidhan, Inc")
root.iconbitmap("others\\a.ico")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
position_top = int(screen_height / 2 - window_height / 2)
position_right = int(screen_width / 2 - window_width / 2)
root.geometry(
    f'{window_width}x{window_height}+{position_right}+{position_top}')
root.config(background="#008cff")
listFolderFirst = "list\\"
username = (path.split(path.expanduser('~'))[-1])

def check_options():
    try:
        _v_state = int(load("options\\enablevoice.npy"))
        voiceVar.set(_v_state)
    except:
        pass
    try:
        _n_state = int(load("options\\enablenotification.npy"))
        notiVar.set(_n_state)
    except:
        pass
    try:
        _t_state = int(load("options\\remindonce.npy"))
        notiTimeVar.set(_t_state)
    except:
        pass

#Voicevar
def save_voice_check_state():
    save("options\\enablevoice.npy", voiceVar.get())

#notitimevar
def check_noticheck_state():
    save("options\\enablenotification.npy", notiVar.get())

#notivar
def check_notitimecheck_state():
    save("options\\remindonce.npy", notiTimeVar.get())

startUp = f"C:\\Users\\{username}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\"
s_path = path.join(startUp, "REMAPP.lnk")
def create_shortcut_startup():
    pythoncom.CoInitialize()    
    target = f"C:\\bidhanInc\\remapp\\remapp.exe"
    wDir = f"C:\\bidhanInc\\remapp\\"
    shell = Dispatch("WScript.Shell")
    shortcut = shell.CreateShortCut(s_path)
    shortcut.Targetpath = target
    shortcut.WorkingDirectory = wDir
    shortcut.save()

hourVar = StringVar()
minVar = StringVar()
ampmVar = StringVar()
listVar = StringVar()
remVar = StringVar()
discVar = StringVar()
voiceVar = IntVar()
notiVar = IntVar()
notiTimeVar = IntVar()

todoList = Listbox(root, bg="#008cff", cursor="hand2",
                   font=("arial", 15), selectmode=SINGLE, bd=0)
todoList.place(x=0, y=0, height=420, width=300)

discFrame = LabelFrame(root, bd=0, bg="#5C5C5C")
discFrame.place(x=300, y=0, width=300, height=60)


def multiOrSingleSelect():
    if todoList["selectmode"] == SINGLE:
        todoList.config(selectmode=MULTIPLE)
    elif todoList["selectmode"] == MULTIPLE:
        todoList.config(selectmode=SINGLE)


def talk(text):
    h_r = strftime("%I")
    m_n = strftime("%M")
    a_p = strftime("%p")
    if h_r[0] == "0":
        h_r = h_r.replace("0","")
    if m_n[0] == "0":
        m_n = m_n.replace("0", "")
    sayCTime = f"{h_r} {m_n} {a_p}"
    fullText = f"hey its {sayCTime} and this is time to {text}"
    speaker.say(fullText)
    speaker.runAndWait()


def showDiscriptionThread():
    thread = Thread(target=showDiscription)
    thread.start()


global running
running = True


def showDiscription():
    while running:
        listFolder1 = listdir(listFolderFirst)
        showDisc.config(state=NORMAL)
        showDisc.delete(1.0, END)
        if len(listFolder1) != 0:
            global discription3
            discription1 = todoList.get(ACTIVE)
            discription1 = discription1.replace("Time:", "")
            discription1 = discription1.replace(":", "")
            discription2 = f"list\\{discription1}.npy"
            discription3 = load(discription2)
            showDisc.insert(INSERT, discription3)
            showDisc.config(state=DISABLED)
        sleep(1)


def showTodoList():
    listFolder = listdir(listFolderFirst)
    if len(listFolder) != 0:
        for nameList in listFolder:
            if nameList.endswith(".npy"):
                nameList = nameList.replace(".npy", "")
                nameList = nameList[:2] + ":" + nameList[2:]
                nameList = nameList[:5] + ":" + nameList[5:]
                nameList = f"Time:{nameList}"
                todoList.insert(END, nameList)


def takeList():
    if remVar.get() != "":
        if checkHour() != None and checkMinute() != None and checkAmpm() != None:
            listDiscription = discVar.get()
            listTitle = remVar.get()
            givenTime = f"Time:{str(checkHour())}:{str(checkMinute())}:{str(checkAmpm())}"
            filenameTime = f"{str(checkHour())}{str(checkMinute())}{str(checkAmpm())}"
            discription = f"Title:{listTitle}\nDiscription:{listDiscription}"
            filename = f"list\\{filenameTime}"
            if path.isfile(f"list\\{filenameTime}.npy") == False:
                save(filename, discription)
                todoList.insert(END, givenTime)
            else:
                print("Already exists with same time")
        else:
            print("Invalid Time")
    else:
        print("You need to add details")


def removeMultipleItems():
    deleteMultipleItems()
    selected_checkboxs = todoList.curselection()
    for selected_checkbox in selected_checkboxs[::-1]:
        todoList.delete(selected_checkbox)


def deleteMultipleItems():
    for i in todoList.curselection():
        apple = todoList.get(i)
        apple = apple.replace(":", "")
        apple = apple.replace("Time", "")
        remove(f"list\\{apple}.npy")


showDisc = Text(discFrame, bg="#008cff", font=("Arial", 15), cursor="arrow")
showDisc.pack(side=TOP)
showDisc.config(state=DISABLED)


def checkHour():
    checkHour = hourVar.get()
    if len(checkHour) != 0:
        if checkHour.isdigit():
            checkHour = int(checkHour)
            if checkHour <= 12 and checkHour > 0:
                if checkHour <= 9:
                    checkHour1 = str(checkHour)
                    checkHour2 = "0"+checkHour1
                    return checkHour2
                else:
                    return checkHour


def checkMinute():
    checkMinute = minVar.get()
    if len(checkMinute) != 0:
        if checkMinute.isdigit():
            checkMinute = int(checkMinute)
            if checkMinute <= 59:
                if checkMinute <= 9:
                    checkMinute1 = str(checkMinute)
                    checkMinute2 = "0"+checkMinute1
                    return checkMinute2
                else:
                    return checkMinute


def checkAmpm():
    checkAmpm = ampmVar.get()
    if len(checkAmpm) == 2:
        upperAmpm = checkAmpm.upper()
        if upperAmpm == "AM" or upperAmpm == "PM":
            return upperAmpm


def checkTimeThread():
    thread = Thread(target=checkTime)
    thread.start()


def checkTime():
    while running:
        listDirectory = listdir("list\\")
        listDirectory = [s.replace(".npy", "") for s in listDirectory]
        currentHour = strftime("%I")
        currentMinute = strftime("%M")
        currentNoon = strftime("%p")
        currentTime = f"{currentHour}{currentMinute}{currentNoon}"
        if currentTime in listDirectory:
            if notiTimeVar.get() == 1:
                notificationThread(currentTime)
                sleep(54)
            else:
                notificationThread(currentTime)
                sleep(3)
        sleep(1)


def exitApp():
    global running
    running = False
    root.destroy()


timeFrame = LabelFrame(root, text="Enter Time",
                       labelanchor="n", bd=0, bg="#008cff")
timeFrame.place(x=300, y=60, width=300, height=80)

hourSB = Spinbox(timeFrame, textvariable=hourVar, from_=1,
                 to=12, width=2, bd=0, font=("Arial", 20))
hourSB.place(relx=0.10, rely=0.30, anchor=W)
hourLabel = Label(timeFrame, text="   Hour", bd=0, bg="#008cff")
hourLabel.place(relx=0.10, rely=0.90, anchor=SW)

minuteSB = Spinbox(timeFrame, textvariable=minVar, from_=0,
                   to=59, width=2, bd=0, font=("Arial", 20))
minuteSB.place(relx=0.50, rely=0.30, anchor=CENTER)
minuteLabel = Label(timeFrame, text="Minute", bd=0, bg="#008cff")
minuteLabel.place(relx=0.50, rely=0.90, anchor=S)

ampmEntry = Entry(timeFrame, textvariable=ampmVar,
                  width=3, font=("Arial", 20), bd=0)
ampmEntry.insert(0, "AM")
ampmEntry.place(relx=0.90, rely=0.30, anchor=E)
ampmLabel = Label(timeFrame, text="AM/PM", bd=0, bg="#008cff")
ampmLabel.place(relx=0.90, rely=0.90, anchor=SE)

remFrame = LabelFrame(root, text="Enter Title",
                      labelanchor="n", bd=0, bg="#008cff")
remFrame.place(x=300, y=140, width=300, height=80)

remName = Entry(remFrame, width=25, textvariable=remVar,
                font=("arial", 15), bd=0)
remName.place(relx=0.50, rely=0.50, anchor=CENTER)

discFrame = LabelFrame(root, text="Enter Discription",
                       labelanchor="n", bd=0, bg="#008cff")
discFrame.place(x=300, y=220, width=300, height=80)

discEntry = Entry(discFrame, width=25, textvariable=discVar,
                  font=("arial", 15), bd=0)
discEntry.place(relx=0.50, rely=0.50, anchor=S)

buttonFrame = LabelFrame(root, bd=0, bg="#008cff",
                         text="Actions", labelanchor="n")
buttonFrame.place(x=450, y=300, width=150, height=120)

addButton = Button(buttonFrame, width=12, text="Add", cursor="hand2",
                   font=("Arial", 10), bd=0, command=takeList)
addButton.place(relx=0.50, rely=0.10, anchor=N)

removeButton = Button(buttonFrame, width=12, text="Remove", cursor="hand2",
                      command=removeMultipleItems, font=("Arial", 10), bd=0)
removeButton.place(relx=0.50, rely=0.60, anchor=S)

stopButton = Button(buttonFrame, width=12, text="Exit app", cursor="hand2",
                    command=exitApp, font=("Arial", 10), bd=0)
stopButton.place(relx=0.50, rely=0.88, anchor=S)

opFrame = LabelFrame(root, bd=0, bg="#008cff", text="Options", labelanchor="n")
opFrame.place(x=300, y=300, width=150, height=120)

voiceCheck = Checkbutton(opFrame, cursor="hand2", bg="#008cff", width=10, variable=voiceVar,
                         activebackground="#008cff", font=("Arial", 10), text="Enable Voice ", command = save_voice_check_state)
voiceCheck.pack()

multipleCheck = Checkbutton(opFrame, cursor="hand2", width=10, bg="#008cff", activebackground="#008cff", font=(
    "Arial", 10), text="Multi Select   ", command=multiOrSingleSelect)
multipleCheck.pack()

notiCheck = Checkbutton(opFrame, cursor="hand2", width=10, bg="#008cff", variable=notiVar,
                        activebackground="#008cff", font=("Arial", 10), text="Notification     ", command=check_noticheck_state)
notiCheck.pack()

notiTimeCheck = Checkbutton(opFrame, cursor="hand2", width=10, bg="#008cff", variable=notiTimeVar,
                            activebackground="#008cff", font=("Arial", 10), text="Remind once  ", command=check_notitimecheck_state)
notiTimeCheck.pack()


def notificationThread(thisIsCurrentTime):
    thread = Thread(target=showNotification(thisIsCurrentTime))
    thread.start()


def showNotification(thisIsCurrentTime):
    fullSentence = load(f"list\\{thisIsCurrentTime}.npy")
    fullSentence = str(fullSentence)
    sentence1 = fullSentence.replace(":", " ")
    sentence2 = sentence1.split()
    sentence3 = sentence2[1:sentence2.index("Discription")]
    sentence4 = sentence2[sentence2.index("Discription")+1:]
    notificationTitle = (" ".join(sentence4))
    notificationBody = (" ".join(sentence3))
    if voiceVar.get() == 1:
        talk(notificationBody)
    if notiVar.get() == 1:
        toast = ToastNotifier()
        toast.show_toast(notificationBody, notificationTitle,
                         duration=6, icon_path="others\\a.ico")


def hideWindow():
    root.iconify()

def check_options_thread():
    thread = Thread(target=check_options)
    thread.start()

showDiscriptionThread()
checkTimeThread()
showTodoList()
check_options_thread()
create_shortcut_startup()
root.protocol('WM_DELETE_WINDOW', hideWindow)
root.mainloop()
# This much
