import datetime as dt
import sqlite3,os

print('checkDB-----------------------------------------------')

#日次データベースの時刻データを実働時間に変換する関数
#result_onlyday[i+1]-result_onlyday[1]をresult_onlydayの長さ実行、iは2ずつ進めることで走査する。
def calc_timedelta(result_onlyday):
    print('checkDB-calc_timedelta--------------------------------')
    calc_data= dt.timedelta ( days=0 , seconds=0 , microseconds=0 , milliseconds=0 , minutes=0 , hours=0 , weeks=0 )
    for i in range(1,len(result_onlyday),2):
        delta_data1= dt.datetime.strptime(result_onlyday[i+1], '%Y%m%d %H:%M')
        print(delta_data1)
        delta_data2= dt.datetime.strptime(result_onlyday[i], '%Y%m%d %H:%M')
        print(delta_data2)
        calc_data=calc_data+(delta_data1-delta_data2)
        print(calc_data)
    return calc_data.seconds

#
def out_time(set_path,date_now):
    print('checkDB-out_time--------------------------------------')
    
    onlyDayUse_dbname = set_path+'OnlyDayUse_Database/'+date_now+'.db'
    conn = sqlite3.connect(onlyDayUse_dbname)
    cur = conn.cursor()
    output_data_time =cur.execute('SELECT * FROM INPUT').fetchall()
    output_data_pay=cur.execute('SELECT COALESCE(SUM(PAY_SOME),0)FROM PAY WHERE PAY_SOME').fetchall()
    cur.close()
    conn.close()
    result_pay=list(output_data_pay)
    print(result_pay[0][0],type(result_pay))
    result_onlyday = dict(output_data_time)
    show_timedelta=calc_timedelta(result_onlyday)
    print(result_onlyday,type(result_onlyday))
    
    dbname =  set_path+'ManagementDatabase.db'
    conn = sqlite3.connect(dbname)
    cur = conn.cursor()
    cur.execute('INSERT INTO Proletariat(Job_ID,Jobsum,Pay) VALUES(?,?,?)',(date_now,show_timedelta,result_pay[0][0]))
    conn.commit()
    cur.close()
    conn.close()
    old_filename=set_path+'OnlyDayUse_Database/'+date_now+'.db'
    new_filrname=set_path+'OnlyDayUse_Database/legacy_'+date_now+'.db'
    os.rename(old_filename,new_filrname)
    return 0