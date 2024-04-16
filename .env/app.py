from flask import Flask,request,render_template

Mahmoud=Flask(__name__,template_folder='templates')

@Mahmoud.route('/',methods=['GET','POST'])
def login():

  return  '<h1> THIS IS THE FIRST FLASK APP  </h1>'
# def printHello() :
#     print('123456')
#     if(request.method=='GET'):
#      return '<h1>HELLO WORLD</h1>'
#     elif(request.method=='POST'):
#         return "THE METHOD USED IS POST"
@Mahmoud.route('/Signup',methods=['GET','POST'])
def Signup():
  return  render_template('Signup.html')
@Mahmoud.route('/xyz')
def Hello() :
   Ages=[18,15,17,18,20]
   return render_template('Ages.html',AL=Ages)

@Mahmoud.route('/greet/<name>')
def greet(name):
    return f"hello {name}"
@Mahmoud.route('/add/<int:num1>/<int:num2>')
def add(num1,num2):
    return f'{num1+num2}'
@Mahmoud.route('/HandleParams')
def handle():
    if('name' in request.args.keys() and 'age' in request.args.keys()):
       name=request.args['name']
       Age=request.args.get('age')
       return f"the name is {name} and he/she is {Age} old"
    else:
        return "SOME PARAMS ARE MISSING"

if __name__ =='__main__':
    Mahmoud.run(debug=True,host='0.0.0.0')