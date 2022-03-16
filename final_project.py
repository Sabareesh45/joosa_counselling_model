import pandas as pd

df=pd.read_csv("/Users/SABAREESH/Downloads/College_data.csv")
dfstd=pd.read_csv("/Users/SABAREESH/Downloads/d2.csv")
a=len(df)-1
k=(len(df.columns))
college_dict={}
for i in range(a):
    input_name=str(df.iloc[i,0])
    seat_dic={}
    j = 1
    while(j<k):
        if str(df.iloc[i,j])=="Nan":
            seat_dic[str(df.columns[j])]=0
        else:
            seat_dic[str(df.columns[j])]=int(df.iloc[i,j])
        j+=1
    college_dict[input_name]=seat_dic


b=len(dfstd)-1
k=(len(dfstd.columns))
student_dict={}
for i in range(b):
    input_name=str(dfstd.iloc[i,1])
    pref_list=[]
    j=5
    while(j<k):
        if str(dfstd.iloc[i,j])=="Nan":
            pref_list.append(None)
        else:
            pref_list.append(str(dfstd.iloc[i,j]))
        j+=1
    student_dict[input_name]=[str(dfstd.iloc[i,2]),int(dfstd.iloc[i,3]),str(dfstd.iloc[i,4]),pref_list]


sort_df=dfstd.sort_values(dfstd.columns[3],axis=0)
print(sort_df)



