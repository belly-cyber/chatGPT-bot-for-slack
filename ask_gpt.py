import os
import openai
from flask import Flask, render_template, url_for,request
    
hidden_url = '/some/hidden/folder/really/deep/to/find/'
response_template = {"response_type": "in_channel","text": "{}" }
openai.api_key = "df;adkfja;iaa;vrierie9o30epfpo"

def ask_chatgpt(user_question,tokens=100):
    respond = openai.Completion.create( model="text-davinci-003",prompt=user_question,max_tokens=tokens)
    return  respond['choices'][0]['text']
    

app = Flask(__name__)

@app.route(hidden_url,methods=['POST'])
def question():
    if request.method == 'POST':
        results=request.form.to_dict()
        question = results['text']
        if len(question) > 1 :
            answer = ask_chatgpt(question)
            response = response_template['text'].format(answer)
        return response
    
    else:
        return """<html><body>
        Something went horribly wrong
        </body></html>"""


if __name__ =='__main__':
    app.run(host='0.0.0.0',debug=True)
