from flask import Flask, render_template, request, jsonify
from bot_modules import translator, debugger, summarizer, gpt

app = Flask(__name__)

@app.route('/')
def home():
    #讓用户選機器人
    return render_template('index.html')

@app.route('/chat')
def chat():
    # 从查询参数获取机器人类型，默认为 'gpt'
    bot_type = request.args.get('bot', 'gpt')
    # 渲染聊天页面，传递机器人类型到模板
    return render_template('chat.html', bot_type=bot_type)

@app.route('/respond', methods=['POST'])
def respond():
    # 获取AJAX请求的数据
    data = request.json
    message = data['message']
    bot_type = data.get('bot_type', 'gpt')

    if bot_type == 'translator':
        response = translator(message)
    elif bot_type == 'debugger':
        response = debugger(message)
    elif bot_type == 'summarizer':
        response = summarizer(message)
    else:  # 默认为 GPT 机器人
        response = gpt(message)

    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
