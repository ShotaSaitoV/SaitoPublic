import sqlite3
import os
import time
from copy import deepcopy
print('initDB------------------------------------------------')



def showOnlyDayUseDB(set_path,date_now):
    print('initDB-showOnlyDayUseDB-------------------------------')
    onlydayuse_dbname =  set_path+'OnlyDayUse_Database/'+date_now+'.db'
    while (os.path.isfile(onlydayuse_dbname) == False): #日次データがない場合は処理を1秒止めることを繰り返す
        time.sleep(1)
    conn = sqlite3.connect(onlydayuse_dbname)
    cur = conn.cursor()
    output_data = dict(cur.execute('SELECT * FROM INPUT').fetchall())
    #日次データベースに格納されているデータはAUTOINCREMENTによってIDが振られているため、削除を挟むと間の数が空いてしまいHTMLでの処理に不都合が出る
    #不都合を解消するために、新たな辞書型変数に新たにIDを振り直している
    if output_data!={}:
        change_data=dict()
        for i in range(0,len(output_data),):
            print(list(output_data)[i])
            change_data [i]=output_data[list(output_data)[i]]
    #output_dataが空（時間が格納されていない場合）はchange_dataにそのままoutput_dataをディープコピーしている（シャロ―コピーでもいい気がする）
    else:
        change_data=deepcopy(output_data)
    conn.commit()
    cur.close()
    conn.close()
    return change_data

def showSalary(set_path):
    print('initDB-showSalary-------------------------------------')
    dbname = set_path+'ManagementDatabase.db'
    conn = sqlite3.connect(dbname)
    cur = conn.cursor()
    result_init = cur.execute('SELECT max(rowid),* from Salary').fetchall()
    cur.close()
    conn.close()
    return (result_init[0][-1])

def makeManagementDatabase(set_path):
    print('initDB-makeManagementDatabase-------------------------')
    dbname =  set_path+'ManagementDatabase.db'
    print(dbname)
    if os.path.isfile(dbname) == True: #メインデータベースが存在すれば何もしない
        return 0
    else: #メインデータベースが存在しなければ作成し、Salaryテーブルの時給部分にデフォルト値としてSAL_ID:20240407,SAL:1200を格納する。
        conn = sqlite3.connect(dbname)
        cur = conn.cursor()
        cur.execute('CREATE TABLE Salary(SAL_ID INTEGER PRIMARY KEY AUTOINCREMENT,SAL INT)')
        cur.execute('CREATE TABLE Proletariat(Job_ID INTEGER PRIMARY KEY,Jobsum INT,Pay INT)')
        cur.execute('INSERT INTO Salary(SAL_ID,SAL) values(20240407,1200)')
        conn.commit()
        cur.close()
        conn.close()
        return 0


def makeOnlyDayUseDatabase(set_path,date_now):
    print('initDB-makeOnlyDayUseDatabase-------------------------')
    if os.path.isfile(set_path+'OnlyDayUse_Database/'+'legacy_'+date_now+'.db') == True: #legacy_+日付のファイルが存在した場合すでに日次データはメインデータベースに格納された後なのでその場合はそこで処理を終える
        return 1
    onlydayuse_dbname = set_path+'OnlyDayUse_Database/'+date_now+'.db'
    if os.path.isfile(onlydayuse_dbname) == True: #日次データベースが存在すれば何もしない
        return 0
    else: #日次データベースが存在しなければ作成し、デフォルト値としてID:0,PAY_SOME:0を格納する
        conn = sqlite3.connect(onlydayuse_dbname)
        cur = conn.cursor()
        cur.execute('CREATE TABLE INPUT(ID INTEGER PRIMARY KEY AUTOINCREMENT,INPUT_TIME TEXT)')
        cur.execute('CREATE TABLE PAY(ID INTEGER PRIMARY KEY AUTOINCREMENT,PAY_SOME INT)')
        cur.execute('INSERT INTO PAY(ID,PAY_SOME) values(0,0)')
        conn.commit()
        cur.close()
        conn.close()
        return 0
