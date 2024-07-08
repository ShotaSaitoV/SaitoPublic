from initDB import makeManagementDatabase, makeOnlyDayUseDatabase, showOnlyDayUseDB, showSalary
from checkDB import out_time
from addDB import operationOnlyDayUseDB, operation_pay, operationSalary
from removeDB import delOnlyDayUse
import os
import datetime as dt
print('appLogic----------------------------------------------')
set_path='store_db/' #データベースファイルのパスを指定する（作業環境・作業ディレクトリによって書き換える、KenshuWebAppが作業ディレクトリの場合は書き換え不要）

def show_timenow():
    now = dt.datetime.now()
    date_now = now.strftime('%Y%m%d')
    min_now = now.strftime('%Y%m%d%H%M')
    d = now.strftime('%Y%m')
    return date_now, min_now, d

#以下はf_opration.pyで呼び出される関数

#アプリの初回起動時に各データベースの存在を確認、作成する関数を呼び出す。
def startApp():
    print('appLogic-startApp-------------------------------------')
    date_now, min_now, d = show_timenow()
    makeManagementDatabase(set_path) #メインデータベースの存在確認
    result_init = showSalary(set_path) #時給データの呼び出し
    judg=makeOnlyDayUseDatabase(set_path,date_now) #日次データベースの存在確認
    if judg==1:
        show_worktime=judg
        return (result_init, show_worktime)
    show_worktime = showOnlyDayUseDB(set_path,date_now) #日次データベースのデータの呼び出し
    #print(os.getcwd())
    return (result_init, show_worktime)

#新しい時給の登録データを受け取り、渡す
def startSalary(new_sal):
    print('appLogic-startSalary----------------------------------')
    date_now, min_now, d = show_timenow()
    return operationSalary(set_path,date_now,new_sal)

#従食（まかない）で使った金額を受け取り、渡す
def startOperationPay(input_pay):
    print('appLogic-startOperationPay----------------------------')
    date_now, min_now, d = show_timenow()
    operation_pay(set_path,date_now,input_pay)

#日次データベースへの時刻を受け取り、渡す
def startOnlyDayUseDB(input_time):
    print('appLogic-startOnlyDayUseDB----------------------------')
    date_now, min_now, d = show_timenow()
    print(input_time)
    merge_inputtime=str(date_now)+' '+input_time
    return operationOnlyDayUseDB(set_path,date_now,merge_inputtime)

#現在の時給を呼び出す
def startShowSalary():
    print('appLogic-startShowSalary------------------------------')
    return showSalary(set_path)

#日次データベースの値を呼び出す
def startShowOnlyDayUse():
    print('appLogic-startShowOnlyDayUse--------------------------')
    date_now, min_now, d = show_timenow()
    
    return showOnlyDayUseDB(set_path,date_now)

#日次データベースの値を削除する
def startDelOnlyDayUse(del_num):
    print('appLogic----------------------------------------------')
    date_now, min_now, d = show_timenow()
    delOnlyDayUse(set_path,date_now,del_num)

#日次データベースの値を確定する
def startCheck():
    print('appLogic-startCheck-----------------------------------')
    date_now, min_now, d = show_timenow()
    return out_time(set_path,date_now)
