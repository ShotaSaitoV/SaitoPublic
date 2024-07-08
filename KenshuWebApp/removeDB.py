import sqlite3

def delOnlyDayUse(set_path,date_now,del_num):
    onlyDayUse_dbname =set_path+'OnlyDayUse_Database/'+date_now+'.db'
    conn = sqlite3.connect(onlyDayUse_dbname)
    cur = conn.cursor()
    print('DELETE FROM INPUT WHERE ID=(SELECT ID FROM INPUT LIMIT 1 OFFSET '+str(del_num)+')')
    cur.execute('DELETE FROM INPUT WHERE ID=(SELECT ID FROM INPUT LIMIT 1 OFFSET '+str(del_num)+')')
    conn.commit()
    cur.close()
    conn.close()
    return 0