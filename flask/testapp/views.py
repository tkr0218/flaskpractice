from testapp import app
from flask import render_template,Flask
n=1000000
s=[0 for i in range(n)]
t=[]
for i in range(2,n):
    if s[i]==0:
        t.append(i)
        if i<1001:
            for j in range(2*i,n,i):
                s[j]=1
@app.route('/')
def index():
    my_dict = {
        'insert_something1': 'views.pyのinsert_something2部分です。',
        'insert_something2': 'views.pyのinsert_something4部分です。',
        'test_titles': t
    }
    return render_template('testapp/index.html',my_dict=my_dict)
@app.route('/test')
def other1():
    return render_template('testapp/index2.html')
@app.route('/sampleform')
def sample_form():
    return render_template('testapp/sampleform.html')
@app.route('/sampleform-post', methods=['POST'])
def sample_form_temp():
    print('POSTデータ受け取ったので処理します')
    return 'POST受け取ったよ'
#if __name__ == '__main__':
    #app.run(debug=True, host='0.0.0.0', port=5000)