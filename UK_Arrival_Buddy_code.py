import tkinter as tk
import webbrowser
window=tk.Tk()
window.title("UK Arrival Buddy")
window.geometry("400x700")
window.configure(bg="#0b2a4a")
#function to clear window and open new window
def clear():
    for widget in window.winfo_children():
        widget.destroy()
#2nd page login
def show_login():
    clear()
    tk.Label(window,text="Login Here!",fg="white",bg="#0b2a4a",font=("Times",26,"italic")).pack(pady=80)
    tk.Label(window,text="Enter Email Address",fg="white",bg="#0b2a4a",font=("Times",26,"italic")).pack()
    tk.Entry(window,width=30).pack(pady=10)
    tk.Label(window,text="Password",fg="white",bg="#0b2a4a",font=("Times",26,"italic")).pack()
    tk.Entry(window,width=30,show="*").pack(pady=5)
    tk.Button(window,text="Login",font=("Times",16,"italic"),bg="#d9d9d9",fg="white",width=10,command=show_home).pack(pady=60)
#3rd page home
def show_home():
    clear()
    tk.Label(window,text="HOME",fg="white",bg="#0b2a4a",font=("Times",26,"italic")).pack(pady=40)
    tk.Button(window,text="Visa Verification",font=("Times",16,"italic"),bg="#d9d9d9",width=25,command=visa_page).pack(pady=10)
    tk.Button(window,text="Accommodation",font=("Times",16,"italic"),bg="#d9d9d9",width=25).pack(pady=10)
    tk.Button(window,text="SIM Card",font=("Times",16,"italic"),bg="#d9d9d9",width=25).pack(pady=10)
    tk.Button(window,text="Bank Account",font=("Times",16,"italic"),bg="#d9d9d9",width=25).pack(pady=10)
    tk.Button(window,text="GP Registration",font=("Times",16,"italic"),bg="#d9d9d9",width=25).pack(pady=5)
    tk.Button(window,text="Part-time Jobs",font=("Times",16,"italic"),bg="#d9d9d9",width=25).pack(pady=5)
    tk.Button(window,text="Transport", font=("Times",16,"italic"),bg="#d9d9d9",width=25).pack(pady=5)
    tk.Button(window,text="Emergency Contacts",font=("Times",16,"italic"),bg="#d9d9d9",width=25).pack(pady=5)
#4th page visa verification
def visa_page():
    clear()
    tk.Label(window,text="Visa Verification",fg="white",bg="#0b2a4a",font=("Times",22,"italic")).pack(pady=30)
    tk.Label(window,text="Full Name",fg="white",bg="#0b2a4a",font=("Times",12,"italic")).pack()
    name = tk.Entry(window,width=30)
    name.pack(pady=5)
    tk.Label(window,text="Passport Number",fg="white",bg="#0b2a4a",font=("Times",12,"italic")).pack()
    passport = tk.Entry(window,width=30)
    passport.pack(pady=5)
    tk.Label(window,text="Date of Birth",fg="white",bg="#0b2a4a",font=("Times",12,"italic")).pack()
    visa = tk.Entry(window,width=30)
    visa.pack(pady=5)
    tk.Button(window,text="Submit",font=("Times",12,"italic"),command=verification_submitted).pack(pady=20)
    tk.Button(window,text="Back",font=("Times",12,"italic"),command=show_home).pack()
#5th page submitted
def verification_submitted():
    clear()
    tk.Label(window,text="Verification Submitted",fg="white",bg="#0b2a4a",font=("Times",22,"italic")).pack(pady=200)
    tk.Button(window,text="Back to Home",font=("Times",12,"italic"),command=show_home).pack()    
#1st page get started
tk.Label(window,text="UK Arrival Buddy",fg="white",bg="#0b2a4a",font=("Times",26,"italic")).pack(pady=250)
tk.Button(window,text="Get Started",bg="#d9d9d9",width=15,command=show_login,font=("Times",26,"italic")).pack()
#run program
window.mainloop()
