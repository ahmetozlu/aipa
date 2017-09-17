# authentication_password.py is the first layer of Security Module. This system works with traditional user - password architecture.

from Tkinter import *

# destroys the authentication window
def quit(self):
    self.root.destroy()

def authentication_password_main():
	root = Tk()

	root.geometry("500x200")
	root.wm_title("Authentication")

	'''
	These lines for adding text area on top of the authentication UI
	T = Text(root, height=1, width=8)
	T.pack()
	T.insert(END, "your text")
	'''

	username = "admin"
	password = "admin_123456" #that's the given password

	#username entry
	username_entry = Entry(root)
	username_entry.pack()

	#password entry
	password_entry = Entry(root, show='*')
	password_entry.pack()

	def trylogin(): #this method is called when the button is pressed
	    #to get what's written inside the entries, I use get()
	    #check if both username and password in the entry is same of the given ones
	    if username == username_entry.get() and password == password_entry.get():
		print("Login is successful!")
		root.quit() # Authentication is successfull
		#add your codes after this line for specifying what program does when login is successful
	    else:
		print("Wrong")

	#when you press this button, trylogin is called
	button = Button(root, text="Login", command = trylogin) 
	button.pack()

	#App starter
	root.mainloop()

authentication_password_main()
