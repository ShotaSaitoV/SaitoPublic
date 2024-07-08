from checkDB import out_time
from appLogic import startApp,startSalary,startOnlyDayUseDB,startShowSalary,startShowOnlyDayUse,startDelOnlyDayUse,startCheck,startOperationPay
from flask import Flask,render_template, url_for, request
import time
import os
import datetime as dt


app = Flask(__name__)

print('f_operationApp----------------------------------------')
@app.context_processor
def override_url_for():
    return dict(url_for=dated_url_for)


def dated_url_for(endpoint, **values):
    if endpoint == 'static':
        filename = values.get('filename', None)
        if filename:
            file_path = os.path.join(app.root_path,
                                     endpoint, filename)
            values['q'] = int(os.stat(file_path).st_mtime)
    return url_for(endpoint, **values)

@app.route("/")
def index():
    print('f_operationApp-index----------------------------------')
    result_init, show_worktime = startApp()
    show_worktime=startShowOnlyDayUse()
    if show_worktime==1:
        return render_template("error.html")
    length_showworktime=len(show_worktime)
    
    return render_template("index.html", result_init=result_init, show_worktime=show_worktime,length_showworktime=length_showworktime)

@app.route("/post_time", methods=['POST'])
def post_time():
    print('f_operationApp-post_time------------------------------')
    if request.method=='POST':
        try:
            input_time = request.form.get("input_time")
            input_min = request.form.get("input_min")
            print(type(input_time),type(input_min))
            if input_time.isnumeric() == False or input_min.isnumeric == False:
                print("入力された値が数字ではありません")
                return render_template("error.html")
            elif int(input_time) < 0 or int(input_time) > 24 or int(input_min) < 0 or int(input_min) > 59:
                print("入力された値が不正です")
                return render_template("error.html")
            else:
                
                merge_length = ('0'+input_time if int(input_time)<10 else input_time)+':'+input_min
                print(merge_length)
                startOnlyDayUseDB(merge_length)
                result_init=startShowSalary()
                show_worktime=startShowOnlyDayUse()
                length_showworktime=len(show_worktime)
                return render_template("index.html",result_init=result_init,input_time=input_time,input_min=input_min,show_worktime=show_worktime,length_showworktime=length_showworktime)
        except ValueError:
            return render_template("error.html")

@app.route("/post_pay", methods=['POST'])
def post_pay():
    print('f_operationApp-post_pay-------------------------------')
    if request.method=='POST':
        try:
            input_pay = request.form.get("input_pay")
           
            if input_pay.isnumeric() == False:
                print("入力された値が数字ではありません")
                return render_template("error.html")
            elif int(input_pay) < 0 or int(input_pay)>2000 :
                print("入力された値が不正です")
                return render_template("error.html")
            else:
                result_init=startShowSalary()
                startOperationPay(input_pay)
                print(input_pay)
                show_worktime=startShowOnlyDayUse()
                length_showworktime=len(show_worktime)
                return render_template("index.html",input_time=input_pay,result_init=result_init,show_worktime=show_worktime,length_showworktime=length_showworktime)
        except ValueError:
            return render_template("error.html")

@app.route("/post_sal", methods=['POST'])
def post_sal():
    print('f_operationApp-post_sal-------------------------------')
    if request.method=='POST':
        try:
            input_pay = request.form.get("input_sal")
            
            if input_pay.isnumeric() == False:
                print("入力された値が数字ではありません")
                return render_template("error.html")
            elif int(input_pay) < 0 or int(input_pay)>2000 :
                print("入力された値が不正です")
                return render_template("error.html")
            else:
                print(input_pay)
                startSalary(input_pay)
                show_worktime=startShowOnlyDayUse()
                length_showworktime=len(show_worktime)
                result_init=startShowSalary()
                return render_template("index.html",input_time=input_pay,result_init=result_init,show_worktime=show_worktime,length_showworktime=length_showworktime)
        except ValueError:
            return render_template("error.html")
        
@app.route("/del_time", methods=['POST'])   
def del_time():
    print('f_operationApp-del_time-------------------------------')
    if request.method=='POST':
        try:
            del_num=request.form.get("del_num")
            startDelOnlyDayUse(int(del_num))
            result_init=startShowSalary()
            show_worktime=startShowOnlyDayUse()
            length_showworktime=len(show_worktime)
            return render_template("index.html",result_init=result_init,show_worktime=show_worktime,length_showworktime=length_showworktime)
        except ValueError:
            return render_template("error.html")
        
@app.route("/send_time", methods=['POST'])   
def send_time():
    print('f_operationApp-send_time-----------------------------')
    if request.method=='POST':
        try:
            request.form.get("send_time")
            result_init=startShowSalary()
            check=startCheck()
            print("正常に完了しました") if check==0 else print("何らかの異常が起こりました")
            show_worktime={}
            length_showworktime=0
            return render_template("index.html",result_init=result_init,show_worktime=show_worktime,length_showworktime=length_showworktime)
        except ValueError:
            return render_template("error.html")
        
if __name__ == "__main__":
    app.run(debug=True)
