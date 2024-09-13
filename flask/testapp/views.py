from testapp import app
from flask import render_template,request,redirect, url_for
from testapp import db
from testapp.models.employee import Employee
from random import randint
s=["グー","チョキ","パー"]
t=[[0,1,2],[2,0,1],[1,2,0]]
ke=["あいこだよ","あなたの勝ち!","あなたの負け!"]
@app.route('/')
def index():
    my_dict = {
        'insert_something1': 'views.pyのinsert_something2部分です。',
        'insert_something2': 'views.pyのinsert_something4部分です。',
        'test_titles': [1,2,3,4,5]
    }
    return render_template('testapp/index.html',my_dict=my_dict)
@app.route('/test')
def other1():
    return render_template('testapp/index2.html')
@app.route('/sampleform')
def sample_form():
    return render_template('testapp/sampleform.html')
@app.route('/sampleform',methods=['GET', 'POST'])
def sample_form_temp():
    if request.method == 'GET':
        return render_template('testapp/sampleform.html')
    if request.method == 'POST':
        print('POSTデータ受け取ったので処理します')
        req1 = request.form['janken']
        pl,en=int(req1),randint(0,2)
        result = {
            'enemy_hand_ja': s[en],
            'player_hand_ja': s[pl],
            'judgement': ke[t[pl][en]],
        }
        return render_template('testapp/janken_result.html', result=result)
@app.route('/add_employee', methods=['GET', 'POST'])
def add_amployee():
    if request.method == 'GET':
        return render_template('testapp/add_employee.html')
    if request.method == 'POST':
        form_name = request.form.get('name')  # str
        form_mail = request.form.get('mail')  # str
        # チェックなしならFalse。str -> bool型に変換
        form_is_remote = request.form.get('is_remote', default=False, type=bool)
        form_department = request.form.get('department')  # str
        # int, データないとき０
        form_year = request.form.get('year', default=0, type=int)

        employee = Employee(
            name=form_name,
            mail=form_mail,
            is_remote=form_is_remote,
            department=form_department,
            year=form_year
        )
        db.session.add(employee)
        db.session.commit()
        return redirect(url_for('index'))
@app.route('/employees')
def employee_list():
    employees = Employee.query.all()
    return render_template('testapp/employee_list.html', employees=employees)
@app.route('/employees/<int:id>')
def employee_detail(id):
    employee = Employee.query.get_or_404(id)
    return render_template('testapp/employee_detail.html', employee=employee)

#if __name__ == '__main__':
    #app.run(debug=True, host='0.0.0.0', port=5000)