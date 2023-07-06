import tkinter as tk
import webbrowser as wb

root = tk.Tk()
#voot
def display_vo():
    user_enq = enq.get()
    print(user_enq)
    if user_enq:
        l2.config(text="Where did you hear about us?")
        wb.open("https://help.voot.com/categories/frequently-asked-questions/644441c5653d8255a05ee109")
    else:
        l2.config(text="Please enter required information")
        
#amazon
def display_ama():
    user_enq = enq.get()
    print(user_enq)
    if user_enq: 
        l2.config(text="Where did you hear about us?")
        wb.open("https://www.amazon.in/gp/help/customer/display.html?nodeId=GDF5PQP4Z6SUH4CQ")
    else:
        l2.config(text="Please enter required information")

#instagram
def display_ig():
        user_enq = enq.get()
        print(user_enq)
        if user_enq: 
            l2.config(text="Where did you hear about us?")
            wb.open("https://help.instagram.com/561062241952036")
        else:
            l2.config(text="Please enter required information")

#Google
def display_google():
    user_enq = enq.get()
    print(user_enq)
    if user_enq: 
        l2.config(text="Where did you hear about us?")
        wb.open("https://policies.google.com/faq?hl=en-US")
    else:
        print("Please enter required information")

enq = tk.Entry(root, 
               font=("Times New Roman", 20),
               width=30)
enq.grid(row=0,column=1)

l1 = tk.Label(root, 
              text="Enter enquiry:", 
              font=("Times New Roman", 25))
l1.grid(row=0,column=0)

l2 = tk.Label(root, 
              font=("Times New Roman", 25))
l2.grid()

#voot button
vo = tk.Button(root, 
               text="Voot", 
               font=("Times New Roman", 20),
               width=10,
               bg="purple", 
               activebackground="yellow", 
               command=display_vo)
vo.grid()

#amazon button
ama = tk.Button(root, 
               text="Amazon", 
               font=("Times New Roman", 20),
               width=10,
               bg="light blue", 
               activebackground="yellow", 
               command=display_ama)
ama.grid()

#insta button
ig = tk.Button(root, 
               text="Instagram", 
               font=("Times New Roman", 20),
               width=10,
               bg="pink", 
               activebackground="yellow", 
               command=display_ig)
ig.grid()

#google button
google = tk.Button(root, 
               text="Google", 
               font=("Times New Roman", 20),
               width=10, 
               bg="yellow", 
               activebackground="green", 
               command=display_google)
google.grid()



root.mainloop()