from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'


#Escreva '''set FLASK_APP=hello.py'''
#Após o codigo estar pronto, escreva no terminal '''flask run'''

#caso queira rodar no botão "run", utilize o código onde o __name__ tem o valor de __main__
if __name__ == "__main__":
    app.run()

