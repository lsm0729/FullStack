from flask import Flask

app = Flask(__name__)


@app.route("/hello")
def hello():
    return "<h1>Hello World!</h1>"

if __name__ == f'__main__':
    host_addr = "0.0.0.0"
    port_num = "8080"
    app.run(host=host_addr,port=port_num,debug=True)
    ##!! Enter http://172.30.1.25:8080/hello