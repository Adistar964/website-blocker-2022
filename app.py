from tkinter import *
from tkinter import messagebox

# this function consists of our app (go thru it if u want to know about this app)
def MainScreen():
	r = Tk()

	r.title('Website Blocker')
	r.resizable(False, False)
	r.config(bg='black')
	# r.iconbitmap(r'icon.ico') # the path should be a r-string like shown

	r.state('zoomed')

	

	host_path ='C:\\Windows\\System32\\drivers\\etc\\hosts'

	Label(r, bg='black',fg='white',
		font=('Helvetica', 24),
		padx=45,
		pady=45,
		text='Enter the url of the websites you want to block\n(Make sure they are seperated by comma(,)):').pack()



	def blockWeb():
		ip_address = '127.0.0.1 '
		iwebs = inp.get(1.0, END)
		webs = list(iwebs.split(','))
		with open(host_path, 'r+') as f:
			data = f.read()
			for i in webs:
				if len(webs) == 0:
					prog.config(text='Write some web address to continue!')
				elif i.strip() not in data:
					f.write(ip_address + i.strip() + '\n')
					prog.config(text='Blocked successfully!')
				else:
					prog.config(text='Already blocked')

	def unblock():
		res = messagebox.askyesno('Unblock sites!', 'Are you sure you want to unblock all the sites ?')
		if res:
			with open(host_path, 'w') as f: 
				pass # empties the file
			prog.config(text='Unblocked all sites successfully!')

	inp = Text(r,font=('Helvetica', 25) 
				,padx=10, pady=10, width=35, height=10)
	inp.config(highlightbackground='orange red', highlightthickness=2)
	inp.pack(pady=40)

	prog = Label(r,font=('Arial', 18), text='', bg='black',fg='white',)
	prog.pack()

	submit = Button(r,bg='white',fg='black', text='Submit', width=40, height=2, font=('Arial', 12))
	submit.config(command=blockWeb)
	submit.pack(pady=15)

	unblockbtn = Button(r,bg='white',fg='black', text='Unblock all sites', width=40, height=2, font=('Arial', 12))
	unblockbtn.config(command=unblock)
	unblockbtn.pack(pady=5)

	r.mainloop()


# This is the starting part of our app (security-check - to make sure only authorised people get in!)
def loginScreen():
	window = Tk()
	window.title("Web-Blocker Login")
	window.config(bg="black")
	window.geometry("500x300")
	# window.iconbitmap(r'icon.ico') # the path should be a r-string like shown
	window.resizable(False,False) # window is not resizable!	

	Label(window,text="",bg="black",fg="white").pack(pady=20) # some spacing at the top

	Label(window, text="Enter Password", bg="black",fg="white",font=("Arial",18)).pack(pady=10)

	passwordField = Entry(window,font=("Arial",18),show="*")
	passwordField.pack(pady=10)

	def login():
		password = passwordField.get()
		if password == "grantAccess":
			# Now we will move to the main screen
			window.destroy()
			MainScreen()
		else:
			messagebox.showerror(title="Login Error!", message="Wrong Password! please try again")

	Button(window, text="Login",
		bg="gold", fg="black",
		font=("Helvetica",13),
		padx=20, pady=6, # if padding option is given inside brackets, then it is internal padding (like width height)
		command=login
		).pack(pady=20)

	window.mainloop()



loginScreen()