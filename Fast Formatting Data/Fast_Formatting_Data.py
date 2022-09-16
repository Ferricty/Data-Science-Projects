import multiprocessing
import pandas as pd
import os
#import time
#s=time.time()
dir=os.listdir()
def format_data():
    listas=[]
    for filename in dir:
        if filename!="Fast_Formatting_Data.py" and filename!="__pycache__" and filename!="Fast_Formatting_Data.exe":
            df=pd.read_excel(filename, index_col=None) 
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
    
    #df_all["Período"] = pd.to_datetime(df_all["Período"]).dt.strftime('%d/%m/%Y')
    #df_all["Fecha pago"] = pd.to_datetime(df_all["Fecha pago"]).dt.strftime('%d/%m/%Y')
    df_all["Años"]=pd.to_datetime(df_all["Fecha pago"]).dt.year
    df_all.to_excel("DataReady.xlsx",index=False) 
if __name__=="__main__":
    
    processes=multiprocessing.Process(target=format_data)
    processes.start()
    processes.join()
#e=time.time()
#print(e-s)


#The full code uncomented works!!












