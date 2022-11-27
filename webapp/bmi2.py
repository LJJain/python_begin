# BMI計算器 網頁應用程式(二)
# 利用自訂函式
from flask import Flask, request
app = Flask(__name__)

def getBMI(w, h):
    bmi = w / (h / 100) ** 2
    return bmi

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        if request.form.get('w') != '' and request.form.get('h') != '':
            w = int(request.form.get('w'))
            h = int(request.form.get('h'))            
            return f"你的BMI值為 {getBMI(w, h):.2f} "
        
    return """
    <form method='post'>
        <label for 'h'>身高(cm)</label>
        <input type='text' name='h' id='h'><br>
        <label for 'w'>體重(kg)</label>
        <input type='text' name='w' id='w'><br>
        <button type='submit'>計算</button>
    </form>
    """

if __name__ == "__main__":
    app.run()