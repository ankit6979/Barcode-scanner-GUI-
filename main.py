from pymongo import MongoClient
import scan_modified as sm
import password_gui as pw
import serial
import time
client= MongoClient('localhost:27017')
db= client.data
from tkinter import *

def insert():
     global root1
     global barcode
     global weight
     global height
     global length
     global breadth
     global pin
     global payment
     global price
     root1 = Tk()
     root1.attributes('-fullscreen',True)
     root1.title("") 
     root1.configure(background = 'navy blue')
     label = Label(root1, text="Welcome to Parcel Sorting Main Menu", font=("Arial Bold", 32), fg = 'Red', bg= 'navy blue')
     label.pack()
     Button1 = Button(root1, text = 'Insert   ', font = ("Arial Bold", 26), bg = 'orange', fg = 'Blue', command = insert)
     Button1.place(x=50, y = 90)
     Button2 = Button(root1, text = 'Update ',font = ("Arial Bold", 26), bg = 'orange', fg = 'Blue', command = update)
     Button2.place(x=50, y = 190)
     Button3 = Button(root1, text = '  Read  ', font = ("Arial Bold", 26), bg = 'orange', fg = 'Blue', command = read)
     Button3.place(x=50, y = 290)
     Button4 = Button(root1, text = ' Delete ', font = ("Arial Bold", 26), bg = 'orange', fg = 'Blue', command = delete)
     Button4.place(x=50, y = 390)
     Button6 = Button(root1, text = '    Quit  ', font = ("Arial Bold", 26), bg = 'orange', fg = 'Blue', command = quite)
     Button6.place(x=50, y = 490) 
 
     barcode = Label(root1, text='Barcode: ', font=("Arial Bold", 22), fg = 'black', bg ='sky blue') 
     weight = Label(root1, text='Weight: ', font=("Arial Bold", 22), fg = 'black', bg ='sky blue') 
     height = Label(root1, text='Height: ', font=("Arial Bold", 22), fg = 'black', bg ='sky blue') 
     length = Label(root1, text='Length: ', font=("Arial Bold", 22), fg = 'black', bg ='sky blue')
     breadth = Label(root1, text='Breadth: ', font=("Arial Bold", 22), fg = 'black', bg ='sky blue') 
     pin = Label(root1, text='Pin: ', font=("Arial Bold", 22), fg = 'black', bg ='sky blue')
     payment = Label(root1, text='Payment: ', font=("Arial Bold", 22), fg = 'black', bg ='sky blue')
     price = Label(root1, text='Price: ', font=("Arial Bold", 22), fg = 'black', bg ='sky blue')
##     barcode.grid(row=7, column=50, sticky=W)   
##     weight.grid(row=10, column=10, sticky=W)
##     height.grid(row=13, column=10, sticky=W)   
##     length.grid(row=16, column=10, sticky=W)
##     breadth.grid(row=19, column=10, sticky=W)   
##     pin.grid(row=22, column=10, sticky=W)
##     payment.grid(row=25, column=10, sticky=W)
##     price.grid(row=28, column=10, sticky=W)
     barcode.place(x=400 , y=90)   
     weight.place(x=900 , y=90)
     height.place(x=400 , y=250)   
     length.place(x=900 , y=250)
     breadth.place(x= 400, y=410)   
     pin.place(x= 900, y=410)
     payment.place(x=400 , y=570)
     price.place(x=900 , y=570) 
     barcode = Entry(root1, bg='white')
     weight = Entry(root1,bg='white')
     height = Entry(root1, bg='white') 
     length = Entry(root1, bg='white')
     breadth = Entry(root1, bg='white') 
     pin = Entry(root1, bg='white')
     payment = Entry(root1, bg='white')
     price = Entry(root1, bg='white')
##     barcode.grid(row=1, column=4) 
##     weight.grid(row=3, column=4)
##     height.grid(row=5, column=4) 
##     length.grid(row=7, column=4)
##     breadth.grid(row=9, column=4) 
##     pin.grid(row=11, column=4)
##     payment.grid(row=13, column=4)
##     price.grid(row=15, column=4)
     barcode.place(x=600, y=90) 
     weight.place(x=1100, y=90)
     height.place(x=600, y=270) 
     length.place(x=1100, y=270)
     breadth.place(x=600, y=420) 
     pin.place(x=1100, y=420)
     payment.place(x=600, y=580)
     price.place(x=1100, y=580)
     button = Button(root1, text = 'Submit', font = ("Arial Bold", 24), bg = 'bisque', fg = 'Blue',command = insert_call)
     button.place(x = 700, y = 650)

def insert_call():
     db.data.insert_one(
     {
     "barcode":barcode.get(),
     "weight":weight.get(),
      "height":height.get(),
     "length":length.get(),
     "breadth":breadth.get(),
     "pincode":pin.get(),
     "payment": payment.get(),
     "price" : price.get()
     })
     root1.destroy()

def read():
     bar = sm. _return_barcode(directory)
     itemdata = db.data.find({"barcode":bar})
     for i in range(0,len(itemdata)):
          val = answers[i]
          data = itemdata[i]
          val["text"] = data
     
def delete():
     global b11
     global root2
     root2=Tk()
     root2.configure(background='blue')
     root2.geometry('400x400')
     c1 = Label(root2, text="Enter item to delete", font=("Arial Bold", 18), fg = 'Dark green', bg= 'slate gray')
     c1.place(x=80,y=60)
     a11=Entry(root2, bd=5)
     a11.place(x=130,y=150)
     btn= Button(root2, text = 'Delete  ', font = ("Arial Bold", 18), bg = 'peach puff', fg = 'IndianRed', command = delete_call)
     btn.place(x=140,y=200)
     root2.mainloop()
     b11=a11.get() 
   
def delete_call():
     root2.destroy()

def exit_call():
     root.destroy()

def update():
     global root3
     global barcode
     global weight
     global height
     global length
     global breadth
     global pin
     global payment
     global price
     root3 = Tk()
     root3.attributes('-fullscreen',True)
     root3.title("") 
     root3.configure(background = 'navy blue')
     label = Label(root3, text="Update Menu", font=("Arial Bold", 32), fg = 'Red', bg= 'navy blue')
     label.pack()
     barcode = Label(root3, text='Barcode: ', font=("Arial Bold", 24), fg = 'black', bg ='sky blue') 
     weight = Label(root3, text='Weight: ', font=("Arial Bold", 24), fg = 'black', bg ='sky blue') 
     height = Label(root3, text='Height: ', font=("Arial Bold", 24), fg = 'black', bg ='sky blue') 
     length = Label(root3, text='Length: ', font=("Arial Bold", 24), fg = 'black', bg ='sky blue')
     breadth = Label(root3, text='Breadth: ', font=("Arial Bold", 24), fg = 'black', bg ='sky blue') 
     pin = Label(root3, text='   Pin:   ', font=("Arial Bold", 24), fg = 'black', bg ='sky blue')
     payment = Label(root3, text='Payment: ', font=("Arial Bold", 24), fg = 'black', bg ='sky blue')
     price = Label(root3, text='Price: ', font=("Arial Bold", 24), fg = 'black', bg ='sky blue')
     barcode.place(x=100 , y=90)   
     weight.place(x=800 , y=90)
     height.place(x=100 , y=250)   
     length.place(x=800 , y=250)
     breadth.place(x= 100, y=410)   
     pin.place(x= 800, y=410)
     payment.place(x=100 , y=570)
     price.place(x=800 , y=570) 
     barcode = Entry(root3, bg='white')
     weight = Entry(root3,bg='white')
     height = Entry(root3, bg='white') 
     length = Entry(root3, bg='white')
     breadth = Entry(root3, bg='white') 
     pin = Entry(root3, bg='white')
     payment = Entry(root3, bg='white')
     price = Entry(root3, bg='white')
     barcode.place(x=400, y=100) 
     weight.place(x=1100, y=100)
     height.place(x=400, y=270) 
     length.place(x=1100, y=270)
     breadth.place(x=400, y=420) 
     pin.place(x=1100, y=420)
     payment.place(x=400, y=580)
     price.place(x=1100, y=580)
     button = Button(root3, text = 'Update', font = ("Arial Bold", 24), bg = 'dark green', fg = 'Blue',command = update_call)
     button.place(x = 650, y = 650)

def update_call():
     root3.destroy()
     
##def send_data(pincode):	
##     if pincode>"600000" and pincode<"620000" :
##          ser.write('a'.encode())
##          print('A')
##     if pincode>"382000" and pincode<"390000" :
##          ser.write('s'.encode())
##          print('S')
##     if pincode>"100000" and pincode<"120000" :
##          ser.write('d'.encode())
##          print('D')
##     if pincode>"250000" and pincode<"270000" :
##          ser.write('f'.encode())
##          print('F')

def main():
     global root
     global barcode_ans
     global weight_ans
     global height_ans
     global length_ans
     global breadth_ans
     global pin_ans
     global payment_ans
     global price_ans
     root = Tk()
     root.attributes('-fullscreen',True)
     root.title("") 
     root.configure(background = 'navy blue')
     label = Label(root, text="Welcome to Parcel Sorting Main Menu", font=("Arial Bold", 32), fg = 'Red', bg= 'navy blue')
     label.pack()
     Button1 = Button(root, text = 'Insert   ', font = ("Arial Bold", 26), bg = 'orange', fg = 'Blue', command = insert)
     Button1.place(x=50, y = 90)
     Button2 = Button(root, text = 'Update ',font = ("Arial Bold", 26), bg = 'orange', fg = 'Blue', command = update)
     Button2.place(x=50, y = 210)
     Button3 = Button(root, text = '  Read  ', font = ("Arial Bold", 26), bg = 'orange', fg = 'Blue', command = read)
     Button3.place(x=50, y = 330)
     Button4 = Button(root, text = ' Delete ', font = ("Arial Bold", 26), bg = 'orange', fg = 'Blue', command = delete)
     Button4.place(x=50, y = 450)
     Button6 = Button(root, text = '    Quit  ', font = ("Arial Bold", 26), bg = 'orange', fg = 'Blue', command = exit_call)
     Button6.place(x=50, y = 570)

     barcode = Label(root, text='Barcode: ', font=("Arial Bold", 26), fg = 'black', bg ='sky blue')
     weight = Label(root, text='Weight: ', font=("Arial Bold", 26), fg = 'black', bg ='sky blue')
     height = Label(root, text='Height: ', font=("Arial Bold", 26), fg = 'black', bg ='sky blue')
     length = Label(root, text='Length: ', font=("Arial Bold", 26), fg = 'black', bg ='sky blue')
     breadth = Label(root, text='Breadth: ', font=("Arial Bold", 26), fg = 'black', bg ='sky blue')
     pin = Label(root, text='   Pin:    ', font=("Arial Bold", 26), fg = 'black', bg ='sky blue')
     payment = Label(root, text='Payment: ', font=("Arial Bold", 26), fg = 'black', bg ='sky blue')
     price = Label(root, text='  Price:   ', font=("Arial Bold", 26), fg = 'black', bg ='sky blue')
     barcode.place(x = 400, y= 90)
     weight.place(x = 900, y= 90)
     height.place(x = 400, y= 290)
     length.place(x = 900, y= 290)
     breadth.place(x = 400, y= 490)
     pin.place(x = 900, y= 490)
     payment.place(x = 400, y= 690)
     price.place(x = 900, y= 690)
     barcode_ans = Label(root, text= '               ', font=("Arial Bold", 26), fg = 'dark slate gray', bg ='white')
     weight_ans = Label(root, text= '               ', font=("Arial Bold", 26), fg = 'dark slate gray', bg ='white')
     height_ans = Label(root, text='               ', font=("Arial Bold", 26), fg = 'dark slate gray', bg ='white')
     length_ans = Label(root, text='               ', font=("Arial Bold", 26), fg = 'dark slate gray', bg ='white')
     breadth_ans = Label(root, text='               ', font=("Arial Bold", 26), fg = 'dark slate gray', bg ='white')
     pin_ans = Label(root, text='               ', font=("Arial Bold", 26), fg = 'dark slate gray', bg ='white')
     payment_ans = Label(root, text='               ', font=("Arial Bold", 26), fg = 'dark slate gray', bg ='white')
     price_ans = Label(root, text='               ', font=("Arial Bold", 26), fg = 'dark slate gray', bg ='white')
     barcode_ans.place(x = 600, y= 90)
     weight_ans.place(x = 1100, y= 90)
     height_ans.place(x = 600, y= 290)
     length_ans.place(x = 1100, y= 290)
     breadth_ans.place(x = 600, y= 490)
     pin_ans.place(x = 1100, y= 490)
     payment_ans.place(x = 600, y= 690)
     price_ans.place(x = 1100, y= 690)

#ser = serial.Serial('COM14',9600)
directory = "C://Program Files (x86)//ZBar//bin//zbarcam.exe"

main()

