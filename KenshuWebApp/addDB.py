import sqlite3
import datetime as dt


print('addDB-------------------------------------------------')


def operationSalary(set_path,date_now,new_sal):
    print('addDB-operationSalary---------------------------------')
    dbname = set_path+'ManagementDatabase.db'
    conn = sqlite3.connect(dbname)
    cur = conn.cursor()
    judg=dict(cur.execute('SELECT * FROM Salary WHERE SAL_ID='+date_now).fetchall())
    if judg=={}:
        cur.execute('INSERT INTO Salary(SAL_ID,SAL) values(?,?)',(date_now,new_sal))
        conn.commit()
    else:
        cur.execute('UPDATE Salary SET SAL = '+new_sal+' WHERE SAL_ID='+date_now)
        conn.commit()
    cur.execute('SELECT * from Salary')
    dict_key = ['id', 'salary']
    output_data = cur.fetchall()
    result_sal = dict(zip(dict_key, output_data[-1]))
    print(output_data,result_sal)
    cur.close()
    conn.close()
    return result_sal


def operationOnlyDayUseDB(set_path,date_now,input_time):
    print('addDB-operationOnlyDayUseDB---------------------------')
    onlyDayUse_dbname =set_path+'OnlyDayUse_Database/'+date_now+'.db'
    print(input_time)
    conn = sqlite3.connect(onlyDayUse_dbname)
    cur = conn.cursor()
    cur.execute('INSERT INTO INPUT(INPUT_TIME) values(?)',(input_time,))
    conn.commit()
    output_data =dict(cur.execute('SELECT * from INPUT WHERE INPUT_TIME').fetchall())
    print(dict(output_data))
    cur.close()
    conn.close()
    return output_data


def operation_pay(set_path,date_now,pay_something):
    print('addDB-operation_pay-----------------------------------')
    onlyDayUse_dbname =set_path+'OnlyDayUse_Database/'+date_now+'.db'
    conn = sqlite3.connect(onlyDayUse_dbname)
    cur = conn.cursor()
    cur.execute('INSERT INTO PAY(PAY_SOME) values(?)',(pay_something,))
    conn.commit()
    print(cur.fetchall())
    cur.close()
    conn.close()
