import tkinter
from tkinter import ttk

class main:

    def combo_generator(self,window,row,column,text,values,label,data):
        index = text#str(row)+str(column)
        label[index] = ttk.Labelframe(window,text=text)
        data[index] = ttk.Combobox(label[index],values=values,state='readonly')
        data[index].current(0)
        label[index].grid(row=row,column=column)
        data[index].grid(row=row,column=column)

    def entry_generator(self,window,row,column,text,label,data):
        index = str(row)+str(column)
        label[index]=ttk.Labelframe(window,text=text)
        label[index].grid(row=row,column=column)
        data[index]=ttk.Entry(label[index])
        data[index].grid(row=row,column=column)

    def code_generator(self,entry,size,data):#,inputs,outputs,size,data_type):

        for key in entry:
            print(entry.get(key).get())
        
        for key in size:
            print(size.get(key).get())

        for key in data:
            print(data.get(key).get())

        return
##        code = tkinter.Tk()
##        if size>1:
##            #vector code
##            #bit 0,1
##            #boolean True,False
##            #integer -2,147,483,647 to +2,147,483,647
##            #real -1.0E38 to +1.0E38
##            #std_logic 0,1,x,z
##        else:
##            #non vector code

    def entry_window(self,data):#inputs,outputs):
        entry_window = tkinter.Tk()

        size = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16)
        data_type = ('bit','BOOLEAN','integer','real','std_logic',
                     'std_ulogic','array') #use ieee.std_logic_1164.all;

        ports = data
        label_text = ("Input ","Size ","Data Type ")
        labels = {}
        entry = {}
        size_combo = {}
        data_combo = {}
        offset=0
        
        for port in ports:
            for row in range(0,int(ports.get(port).get())):
                #print("row",row,"offset",row+offset)
                for column in range(0,3):
                    if column == 0:
                        self.entry_generator(entry_window,row+offset,0,port+str(row)+":",labels,entry)
                    elif column == 1:                    
                        self.combo_generator(entry_window,row+offset,1,port+label_text[column]+str(row)+":",size,labels,size_combo)
                    else:                    
                        self.combo_generator(entry_window,row+offset,2,port+label_text[column]+str(row)+":",data_type,labels,data_combo)
                offset=row+offset+1
            
##        for key in size_combo:
##            print(size_combo.get(key).get())
##
##        for key in data_combo:
##            print(data_combo.get(key).get())

        CreateButton = ttk.Button(entry_window, text="Create", command=lambda entry = entry,
                                  size = size_combo, data = data_combo:self.code_generator(entry,size,data))

        CreateButton.grid(row=row+offset,column=1)
        
                
    def __init__(self):
        window = tkinter.Tk()
        
        numbers = (1,2,3,4,5,6,7,8,9,10)
        labels = {}
        data = {}

        self.combo_generator(window,1,1,"IN ",numbers,labels,data)
        self.combo_generator(window,2,1,"OUT ",numbers,labels,data)
        self.combo_generator(window,3,1,"INOUT ",numbers,labels,data)
        self.combo_generator(window,4,1,"BUFFERS ",numbers,labels,data)

        CreateButton = ttk.Button(window, text="Create",command=lambda
                                  d=data:self.entry_window(d))

        CreateButton.grid(row=5,column=1)

main_window = main()
