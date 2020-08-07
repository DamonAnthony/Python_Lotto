from tkinter import *


window = Tk()
window.geometry("600x600")
window.title("Lotto")

ageFrame = Frame(window)
ageFrame.pack(fill=X)
ageLabel = Label(ageFrame, text="Please enter your age")
ageLabel.grid(column=0, row=0, ipadx=5, ipady=5)
ageEntry = Entry(ageFrame, width=20)
ageEntry.grid(column=1, row=0, ipadx=10, ipady=5)


def check_age():
    def alert(msg):
        alert_window = Toplevel(window)
        alert_window.title("Error")
        alert_frame = Frame(alert_window)
        alert_frame.pack(fill=BOTH)
        alert_label = Label(alert_window, text=msg)
        alert_label.grid(column=0, row=0, padx=5, pady=5)

        def close_alert():
            alert_window.destroy()

        alert_btn = Button(alert_label, text="Close", command=close_alert)
        alert_btn.grid(column=1, row=1, pady=10, padx=20, ipady=20)

    def open_lotto():
        lottoFrame["state"] = NORMAL

    try:
        age = int(ageEntry.get())
    except TypeError:
        alert("Enter your age as a number")
    except ValueError:
        alert("Enter your age as a number")
    if age > 18:
        open_lotto()
    elif age < 18:
        alert("You are underage and cannot play")


ageBtn = Button(ageFrame, text="Confirm", command=check_age)
ageBtn.grid(column=1, row=1, pady=10, ipadx=20, ipady=20)
lottoHeading = Label(window, text="LOTTO", font=24)
lottoHeading.pack(anchor=W)
lottoFrame = Frame(window)
lottoFrame.pack(fill=X)
num1label = Label(lottoFrame, text="Enter 1st number")
num1label.grid(column=0, row=0, padx=5, pady=5)
num1Entry = Entry(lottoFrame)
num1Entry.grid(column=1, row=0, padx=5, pady=5)
num2label = Label(lottoFrame, text="Enter 2nd number")
num2label.grid(column=2, row=0, padx=5, pady=5)
num2Entry = Entry(lottoFrame)
num2Entry.grid(column=3, row=0, padx=5, pady=5)
num3label = Label(lottoFrame, text="Enter 3rd number")
num3label.grid(column=4, row=0, padx=5, pady=5)
num3Entry = Entry(lottoFrame)
num3Entry.grid(column=5, row=0, padx=5, pady=5)
num4label = Label(lottoFrame, text="Enter 4th number")
num4label.grid(column=0, row=1, padx=5, pady=5)
num4Entry = Entry(lottoFrame)
num4Entry.grid(column=1, row=1, padx=5, pady=5)
num5label = Label(lottoFrame, text="Enter 5th number")
num5label.grid(column=2, row=1, padx=5, pady=5)
num5Entry = Entry(lottoFrame)
num5Entry.grid(column=3, row=1, padx=5, pady=5)
num6label = Label(lottoFrame, text="Enter 6th number")
num6label.grid(column=4, row=1, padx=5, pady=5)
num6Entry = Entry(lottoFrame)
num6Entry.grid(column=5, row=1, padx=5, pady=5)

btnFrame = Frame(window)
btnFrame.pack(fill=X)
window.mainloop()