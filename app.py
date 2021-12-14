from flask import Flask
from datetime import datetime
app = Flask(__name__)

now = datetime.now()
print(datetime.now().strftime("%d/%m/%Y %H:%M:%S %p"))
@app.route("/", methods=['GET'])
def home():
    return {"data":"Hello Flask!"}

@app.route("/current_datetime", methods=['GET'])
def current_datetime():
    message = ''
    if now.hour < 12:
        message = 'Bom dia!'
    if now.hour >= 12 and now.hour <= 18:
        message = 'Boa tarde!'
    if now.hour > 18:
        message = 'Boa noite!'
    return {"current_datetime": datetime.now().strftime("%d/%m/%Y %H:%M:%S %p"), "message": message}
