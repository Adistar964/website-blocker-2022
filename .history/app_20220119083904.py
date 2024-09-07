from tkinter import *
from tkinter import messagebox

r = Tk()

r.title('Website Blocker')
r.resizable(False, False)
r.config(bg='black')
r.iconbitmap('icon.ico')

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
			pass
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

# unblockbtn = Button(r,bg='white',fg='black', text='Unblock all sites', width=40, height=2, font=('Arial', 12))
# unblockbtn.config(command=unblock)
# unblockbtn.pack(pady=5)

r.mainloop()