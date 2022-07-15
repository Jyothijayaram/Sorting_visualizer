from tkinter import * 
from tkinter import ttk
import random
from Algorithms import bubble_sort, quick_sort,merge_sort


window = Tk()
window.title("Algorithms Visualiser")
window.geometry('900x600+200+80')
window.config(bg='#FFFFFF')



selected_algo = StringVar()
sppd = StringVar()


boxlable = Label(window,text = " Algorithm " ,font=16, bg='#C4C5BF' ,width = 15 , bd=5)
boxlable.place(x=280,y=4)

menu=ttk.Combobox(window,width=10,font=("new roman", 15, 'italic bold'),textvariable= selected_algo , values = ['Bubble Sort','Merge sort' ,'Quick sort'])
menu.place(x=450,y=5)
menu.current(0)





rec=Canvas(window,width=850,height=420,bg='#0CA8F6')
rec.place(x=25,y=160)


array = [ ]

def  Rectangle(array):
    rec.delete('all')
    canvas_height =420
    canvas_width=850
    x_width = canvas_width / (len(array) + 1)
    offset = 12
    spacing = 5
    normalizedData = [i / max(array) for i in array]

    for i, height in enumerate(normalizedData):
        x0 = i * x_width + offset + spacing 
        y0 = canvas_height - height * 390
        x1 = (i + 1) * x_width 
        y1 = canvas_height
        rec.create_rectangle(x0, y0, x1, y1, fill='#F7E806')
        
    window.update_idletasks()



def generate():

    global array
    
    for i in range(0, 100):
        random_value = random.randint(1, 150)
        array.append(random_value)

    Rectangle(array)



def speed():
   if  menu.get() == 'High' :
       return 0.001
   elif menu.get() =='Medium':
       return 0.1
   else:
       return 0.3
   

def sort():

    if selected_algo.get() == 'Bubble Sort':
        bubble_sort(array,Rectangle)
    elif selected_algo.get() ==  'Merge sort':
        merge_sort(array,Rectangle)
    elif selected_algo.get() == 'Quick sort':
        quick_sort(array,0,len(array)-1,Rectangle)






boxlable = Label(window,text = " Speed " ,font=16, bg='#C4C5BF' ,width = 15 , bd=5)
boxlable.place(x=280,y=49)

menu=ttk.Combobox(window,width=10,font=("new roman", 15, 'italic bold'),textvariable= sppd , values = ['Slow','Medium' ,'High'])
menu.place(x=450,y=50)
menu.current(0)





Genbutton=Button(window,text='Generate ',command=generate,bg='#65696B',font=("new roman", 14, 'italic bold'))
Genbutton.place(x=310,y=100) 

sortbutton=Button(window,text='sort',bg='#65696B',command=sort,font=("new roman", 14, 'italic bold'))
sortbutton.place(x=480,y=100) 





window.mainloop()