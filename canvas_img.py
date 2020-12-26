from tkinter import *

root = Tk()
root.title('museum map') 
root.iconbitmap('c:/gui/codemy.ico')#put here the map which is drawn by hand
root.geometry("800x600")//?

w = 5.4#x coordibnates we can multiply with suitable values with the same ratio
h = 3#y coordinates
x = 0#x points the origin
y = 0#y points the origin

my_canvas = Canvas(root, width=w, heigh=h, bg="white")
my_canvas.pack(pady=20)



# Add Image To Canvas
img = PhotoImage(file="c:/gui/images/me.png")#upload moving photo here 
my_image = my_canvas.create_image(0,0, anchor=NW, image=img)#image which is moving is initially at the origin

#create two variable then compare them with the previous position update the cuurent location
#
def left(event):
	x = -10 #
	y = 0
	my_canvas.move(my_image, x, y)

def right(event):
	x = 10
	y = 0
	my_canvas.move(my_image, x, y)


def up(event):
	x = 0
	y = -10
	my_canvas.move(my_image, x, y)


def down(event):
	x = 0
	y = 10
	my_canvas.move(my_image, x, y)



root.bind("<Left>", left)
root.bind("<Right>", right)
root.bind("<Up>", up)
root.bind("<Down>", down)




root.mainloop()

