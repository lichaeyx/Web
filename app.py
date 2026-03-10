from flask import Flask, render_template, request, redirect

app = Flask(__name__)

my_apps = [] 

@app.route('/')
def index():
    courses = [
        {"id": "MAT202", "name": "수학2", "status": "마감"},
        {"id": "OOP101", "name": "객체지향프로그래밍", "status": "여유"}
    ]
    return render_template('index.html', courses=courses, my_apps=my_apps)

@app.route('/apply', methods=['GET', 'POST'])
def apply():
    code = request.args.get('courseCode') or request.form.get('courseCode')
    
    if code:
        my_apps.append(code) 
        print(f"공격 성공: {code}")
    
    return redirect('/')
        
if __name__ == '__main__':
    app.run(debug=True)
