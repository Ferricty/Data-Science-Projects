from multiprocessing import Process, freeze_support
import pandas as pd
from os import listdir
import sys
from tkinter import *
from tkinter import filedialog
from time import time
from PIL import ImageTk,Image


################# The magic start here############    

def format_data(dir):
    r=listdir(dir)
    listas=[]
    for filename in r:
        if filename!="Fast_Formatting_Data.py" and filename!="__pycache__" and filename!="Fast_Formatting_Data.exe":
            df=pd.read_excel(dir+filename, index_col=None) 
            cant=[0]
            df.insert(0,"Municipios","")
            x=[0]
            inicio=0
                
            for i in df["Cliente"]:
                if str(i)[:3]=="DPA":
                        x=str(i).split("(Cant.=")
                        df.iloc[inicio:,0]=x[0]
                        inicio=inicio+int(x[1][0:-1])+1
                        cant.append(inicio)
            df.drop(labels=cant, inplace=True)
            listas.append(df)
    
    df_all=pd.concat(listas, sort=False)
    df_all.drop(columns=["Bonif. pago electrónico ($)","Bonif. pronto pago ($)","Canal pago"], inplace=True)
    
    df_all["Período"] = pd.to_datetime(df_all["Período"]).dt.strftime('%d/%m/%Y')
    df_all["Fecha pago"] = pd.to_datetime(df_all["Fecha pago"]).dt.strftime('%d/%m/%Y')
    df_all["Años"]=pd.to_datetime(df_all["Fecha pago"]).dt.year
    return df_all

def main():

    dir1=e1.get()
    dir2=e2.get()
    start=time() 

    if dir2=="":
        e2.destroy()
        format_data(dir1).to_excel("DataReady.xlsx",index=False) 

        end1=time()
        
        l2=Label(root,text="The operation conclude sucessfully in "+str(round(end1-start,2))+" seconds processing "+str(len(listdir(dir1)))+" files.")
        l2.config(bg=color_var,font=("Helvetica",12))
        l2.grid(row=4,column=0,pady=5)

        return 
    elif dir1=="":

        
        format_data(dir2).to_excel("DataReady.xlsx",index=False) 
        end3=time()
        l2=Label(root,text="The operation conclude sucessfully in "+str(round(end3-start,2))+" seconds processing "+str(len(listdir(dir2)))+" files.")
        l2.config(bg=color_var,font=("Helvetica",12))
        l2.grid(row=4,column=0,pady=5)

        return 
    else:

        df_all=pd.concat([format_data(dir1),format_data(dir2)], sort=False)
        
        df_all.to_excel("DataReady.xlsx",index=False) 

    end2=time() 
    l2=Label(root,text="The operation conclude sucessfully in "+str(round(end2-start,2))+" seconds processing "+str(len(listdir(dir1))+len(listdir(dir2)))+" files.")
    l2.config(bg=color_var,font=("Helvetica",12),pady=5)
    l2.grid(row=4,column=0,columnspan=2)   

################# The magic end here############    




################# This is the same application but using parallel programing in two different directories############


# def format_data(dir):
#     r=listdir(dir)
#     listas=[]
#     for filename in r:
#         if filename!="Fast_Formatting_Data.py" and filename!="__pycache__" and filename!="Fast_Formatting_Data.exe":
#             df=pd.read_excel(dir+filename, index_col=None) 
#             cant=[0]
#             df.insert(0,"Municipios","")
#             x=[0]
#             inicio=0
                
#             for i in df["Cliente"]:
#                 if str(i)[:3]=="DPA":
#                         x=str(i).split("(Cant.=")
#                         df.iloc[inicio:,0]=x[0]
#                         inicio=inicio+int(x[1][0:-1])+1
#                         cant.append(inicio)
#             df.drop(labels=cant, inplace=True)
#             listas.append(df)

#     df_all=pd.concat(listas, sort=False)
#     df_all.drop(columns=["Bonif. pago electrónico ($)","Bonif. pronto pago ($)","Canal pago"], inplace=True)
    
#     df_all["Período"] = pd.to_datetime(df_all["Período"]).dt.strftime('%d/%m/%Y')
#     df_all["Fecha pago"] = pd.to_datetime(df_all["Fecha pago"]).dt.strftime('%d/%m/%Y')
#     df_all["Años"]=pd.to_datetime(df_all["Fecha pago"]).dt.year
#     df_all.to_excel(dir+"DataReady.xlsx",index=False) 


# def main():

#     dir1=e1.get()
#     dir2=e2.get()
#     start=time() 
#     processes=[Process(target=format_data,args=[dir1]),Process(target=format_data,args=[dir2])]
#     if dir2=="":
#         e2.destroy()
#         processes[0].start()
#         processes[0].join()
#         end1=time()
#         l2=Label(root,text="The operation conclude sucessfully in "+str(round(end1-start,2))+" seconds processing "+str(len(listdir(dir1))-1)+" files.")
#         l2.config(bg=color_var,font=("Helvetica",12))
#         l2.grid(row=4,column=0,pady=5)
        
#         df=pd.read_excel(dir1+"DataReady.xlsx", index_col=None)
#         df.to_excel("DataReady.xlsx",index=False)  
#         return 
#     elif dir1=="":
        
#         processes[1].start()
#         processes[1].join()
#         end3=time()
#         l2=Label(root,text="The operation conclude sucessfully in "+str(round(end3-start,2))+" seconds processing "+str(len(listdir(dir2))-1)+" files.")
#         l2.config(bg=color_var,font=("Helvetica",12))
#         l2.grid(row=4,column=0,pady=5)
        
#         df=pd.read_excel(dir2+"DataReady.xlsx", index_col=None)
#         df.to_excel("DataReady.xlsx",index=False)  
#         return 
#     else:
#         for process in processes:
#             process.start()
            
#         for process in processes:
#             process.join()
#     # listas=[]
#     # dirs=[dir1,dir2]
#     # for i in dirs:
#     #     listas.append(pd.read_excel(i+"DataReady.xlsx", index_col=None))
#     # df_add=pd.concat(listas, sort=False)
#     # df_add.to_excel("DataReady.xlsx",index=False)  
#     end2=time() 
#     l2=Label(root,text="The operation conclude sucessfully in "+str(round(end2-start,2))+" seconds processing "+str(len(listdir(dir1))+len(listdir(dir2))-2)+" files.")
#     l2.config(bg=color_var,font=("Helvetica",12),pady=5)
#     l2.grid(row=4,column=0,columnspan=2)   
    
    
################# This is the end of the application using parallel programing in two different directories############    
    
 
 
 
 
 
    
######################################################################
########################Tkinter Application Start######################    
######################################################################


global b3
color_var="#7832dd"
def borrar():
    global b3
    e2.destroy()
    b2.config(image=photoim,command=lambda:opendirectory(2))
    b3.destroy()
    b3=Button(root, image=res_img_b3,borderwidth=0,command=borrar)

def opendirectory(var):

    
    if var==1:
        dir=filedialog.askdirectory()
    
        if dir=="":
            return
        e1.insert(0,dir+"/")

        
    elif var==2:
        global e2
        b2.config(image=new_pic_b1,command=lambda:opendirectory(3))
        e2=Entry(root,width=70,font=("Helvetica",10))
        e2.grid(row=2,column=0,padx=10)
        
        b3.config(bg=color_var)
        b3.grid(row=2,column=2)
       
    else: 
        
        dir=filedialog.askdirectory()   
        e2.insert(0,dir+"/")

  
if __name__=="__main__":
    freeze_support()
    root=Tk()
    root.title("Fast Formatting Data")  # Title of the aplication
    root.iconbitmap("Fast.ico")         # Adding an .ico
    root.geometry("660x300")            # Window size width x height
    root.resizable(0,0)
    root.config(bg=color_var)
    l=Label(root,text="Directory of Excels to Format")
    l.config(bg=color_var,font=("Helvetica",20))
    l.grid(row=0,columnspan=3,pady=(20))
    # Set the directory manually
    e1=Entry(root,width=70,font=("Helvetica",10))
    e1.grid(row=1,column=0,padx=10)

    
    
    #Load img
    imgb1=Image.open("open_folder_blue.png")
    #Resize image
    res_img_b1=imgb1.resize((40,40))
    new_pic_b1=ImageTk.PhotoImage(res_img_b1)
    #Explore to the directory and adding to entry e1
    b1=Button(root, image=new_pic_b1,borderwidth=0,command=lambda:opendirectory(1))
    b1.config(bg=color_var)
    b1.grid(row=1,column=1)
    
    
    photo=PhotoImage(file="plus1.png")
    photoim=photo.subsample(5)
    b2=Button(root,image=photoim,command=lambda:opendirectory(2),borderwidth=0)
    b2.config(bg=color_var)
    b2.grid(row=2,column=1)
    
    #Load img
    imgb3=PhotoImage(file="menos2.png")
    #Resize image
    res_img_b3=imgb3.subsample(7)
    #Explore to the directory and adding to entry e1
    
    b3=Button(root, image=res_img_b3,borderwidth=0,command=borrar)

    ##Load image
    imgsubmit=Image.open("submit2.png")
    #Resize image
    res_img_submit=imgsubmit.resize((100,40))
    new_pic=ImageTk.PhotoImage(res_img_submit)
    submitbtn=Button(root,image=new_pic,command=main,borderwidth=0) #This button start the Data Formatting
    submitbtn.config(bg=color_var)
    submitbtn.grid(row=3,column=0)
    
    root.mainloop()    

######################################################################
########################Tkinter Application End######################    
######################################################################












