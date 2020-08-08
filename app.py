from flask import Flask,request,redirect,render_template,Response
from flask_sqlalchemy import SQLAlchemy
from functions.fibs import task2
from functions.results import metrics
from werkzeug.exceptions import HTTPException
import logging,os
from logging.handlers import RotatingFileHandler
import csv,traceback,time
from core import Core


from datetime import datetime
startTime = datetime.now()
core = Core()


basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__,template_folder='templates')


# Set format that both loggers will use:
formatter = logging.Formatter("[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s")
# Set logger A for errors
log_handler = RotatingFileHandler('logs/errors.log', maxBytes=10000, backupCount=1)
log_handler.setFormatter(formatter)
log_handler.setLevel(logging.ERROR)
a = logging.getLogger('errors')
a.addHandler(log_handler)


@app.route('/',methods=["GET"])
def hello():
	return render_template('welcome.html')

@app.route('/fib/<number>', methods=["GET"])
def reqs(number):
	##check if number is negative , or something instead of numerical
	'''
	Functionality of fib(). <Number> will be used as input in the function.
	'''
	try:

		results,time,total=task2(int(number)) ## run function to generate the result
		core.add_request(time,int(number))
		#print(core.requests)
	
		with open('text.csv', 'a') as f:
			writer = csv.writer(f, delimiter=';')
			line=[int(number),float(time)]
			writer.writerow(line)
		return render_template("result.html", number=number, results= results,time=float(time),total=total)
	except ValueError as e:
		logging.getLogger('errors').error(traceback.format_exc())
		return 'Enter a valid number try an integer for example'
		 


@app.route('/health')
def health():

	'''
	Returns health of system:

	'''
	data_dict={}
	data_dict["fibonacci (int)"]=[]
	data_dict["time (sec)"]=[]

	##create to dic to pass in the metrics array to create the corresponding diagramm
	for i in list(core.requests):
			data_dict["fibonacci (int)"].append(int(core.requests[i].request))
			data_dict["time (sec)"].append(float(core.requests[i].time))
	index=metrics(data_dict) ##startTime time to response in each request and total request made
	times=datetime.now() - startTime ## define uptime
	return render_template("health.html",time=times,index=index,started=startTime)


@app.route('/logs')
def stream():
	def generate():
		with open('logs/errors.log') as f:
			while True:
				yield f.read()
				time.sleep(1)

	return app.response_class(generate(), mimetype='text/plain')

@app.errorhandler(404) ##redirect to home screen not founded webpages
def page_not_found(e):
    return render_template('welcome.html',error=404)

if __name__ == '__main__':
	
	
	
	app.run()