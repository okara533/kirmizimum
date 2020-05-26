pair_df=pd.read_csv("pairlist.csv",header=None)[1]
pairs=[]
for pair in range(len(pair_df)):
    pairs.append(pair_df[pair])
#STOPSUZ GETİRİ
result_list=[]
count=0
for a in pairs:  
    result={}
    df_raw=pd.read_csv(a+".csv")
    if len(df_raw)>100:
        df=df_raw["close"].pct_change()
        df.index=df_raw["timestamp"]
        df.dropna(inplace=True)
        money=100
        for i in range(len(df)):
            money=money*(1+df.iloc[i])
        money_str=100
        for i in range(1,len(df)):
            if df.iloc[i-1]<0:
                money_str=money_str*(0.999+df.iloc[i])
            elif df.iloc[i-1]>0:
                money_str=money_str*(0.999-df.iloc[i])
        money_str2=100
        for i in range(1,len(df)):
            if df.iloc[i-1]>0:
                money_str2=money_str2*(0.999+df.iloc[i])
            elif df.iloc[i-1]<0:
                money_str2=money_str2*(0.999-df.iloc[i])
        result["coin"]=a
        result["HODL"]=money
        result["strategy1"]=money_str
        result["strategy2"]=money_str2
        result["count"]=count
        result_list.append(result)
df_result=pd.DataFrame(result_list) 
df_result["success"]=df_result["strategy1"]-df_result["strategy2"]
print("strateji1 başarı :{}".format((df_result["strategy1"]>100).sum()))
print("strateji1 başarısızlık  :{}".format((df_result["strategy1"]<100).sum()))
print("strateji2 başarı :{}".format((df_result["strategy2"]>100).sum()))
print("strateji2 başarısızlık  :{}".format((df_result["strategy2"]<100).sum()))
print("HODL başarı :{}".format((df_result["HODL"]>100).sum()))
print("HODL başarısızlık :{}".format((df_result["HODL"]<100).sum()))
print("****ortalamalar****\n"+str(df_result.mean()))
