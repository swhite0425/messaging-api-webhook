from flask import Flask, request

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()  # 解析收到的 JSON 資料
    print('Received webhook data:', data)  # 顯示收到的資料
    return 'Webhook received', 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
