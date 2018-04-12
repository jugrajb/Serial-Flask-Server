from flask import Flask, render_template,request, redirect, url_for
import serial
import serial.tools.list_ports
import string


app = Flask(__name__)

PORT = 'COM16'
try:
 ser.close();
except:
 print();
try:
 ser = serial.Serial(PORT, 115200, timeout=100,
                     bytesize = serial.EIGHTBITS,
                     parity = serial.PARITY_NONE,
                     stopbits = serial.STOPBITS_ONE)
except:
 print ('Serial port %s is not available' % PORT);
 portlist=list(serial.tools.list_ports.comports())
 print('Trying with port %s' % portlist[0][0]);
 ser = serial.Serial(portlist[0][0], 115200, timeout=100)
ser.isOpen()



# we are able to make 2 different requests on our webpage
# GET = we just type in the url
# POST = some sort of form submission like a button
@app.route('/', methods = ['POST','GET'])
def hello_world():

    # variables for template page (templates/index.html)
    author = "Jugraj"
    readval = 10

    # if we make a post request on the webpage aka press button then do stuff
    if request.method == 'POST':

        # if we press the turn on button
        if request.form['submit'] == 'Forward': 
            print ('FORWARD')
            ser.flushInput()
            ser.flushOutput()
            ser.write("forward\r".encode('ascii'));
            strin = ser.readline();
            strin = ser.readline();
            print(strin.decode('ascii'));
        # if we press the turn off button
        elif request.form['submit'] == 'Stop': 
            print ('STOP')
            ser.flushInput()
            ser.flushOutput()
            ser.write("stop\r".encode('ascii'));
            strin = ser.readline();
            strin = ser.readline();
            print(strin.decode('ascii'));
        elif request.form['submit'] == 'Backwards': 
            print ('BACKWARDS')
            ser.flushInput()
            ser.flushOutput()
            ser.write("back\r".encode('ascii'));
            strin = ser.readline();
            strin = ser.readline();
            print(strin.decode('ascii'));
        elif request.form['submit'] == 'Left': 
            print ('LEFT')
            ser.flushInput()
            ser.flushOutput()
            ser.write("left\r".encode('ascii'));
            strin = ser.readline();
            strin = ser.readline();
            print(strin.decode('ascii'));
        elif request.form['submit'] == 'Right': 
            print ('RIGHT')
            ser.flushInput()
            ser.flushOutput()
            ser.write("right\r".encode('ascii'));
            strin = ser.readline();
            strin = ser.readline();
            print(strin.decode('ascii'));

        else:
            pass
    
    # the default page to display will be our template with our template variables
    return render_template('index.html', author=author, value=100*(readval/1023.))


if __name__ == "__main__":

    # lets launch our webpage!
    # do 0.0.0.0 so that we can log into this webpage
    # using another computer on the same network later
    app.run(host='0.0.0.0')