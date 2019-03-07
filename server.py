from flask import Flask,render_template,request,jsonify
import multiprocessing as mp
import feedparser
import tweepy
import time
from dateutil import parser

#config
app = Flask(__name__)

#setup variables
setup=[]
feed=[]
running=False
process=None
user = "Bot Inactive"

#authenticating twitter account
def authenticate():
	global user
	auth = tweepy.OAuthHandler(setup[0], setup[1])
	auth.set_access_token(setup[2], setup[3])
	api = tweepy.API(auth)
	user=api.me().screen_name


#start bot process
def start():
	global process
	try:
		authenticate()
	except Exception as e:
		print("\n!! ERROR : "+e+"\n")
		return False
	if not running:
		process=mp.Process(target=feedUpdate, args=(setup,feed))
		process.start()
		return True
	return False

#terminate bot process
def stop():
	global process
	try:
		if running:
			process.terminate()
			process=None
			print("\nBot Stopped\n")
			return True
		return False
	except Exception as e:
		print("\n!! ERROR : "+e+"\n")
		return False

#bot
def feedUpdate(setup,urls):
	print("\nBot Started\n")
	auth = tweepy.OAuthHandler(setup[0], setup[1])
	auth.set_access_token(setup[2], setup[3])
	ap = tweepy.API(auth)
	lastUpdate = time.time()
	tweetInterval=int(setup[4])
	startTime = lastUpdate
	while True:
		if (time.time()-lastUpdate) < tweetInterval :
			continue
		print("\n!! Fetching Updates !!\n")
		for url in urls:
			feed = feedparser.parse(url)
			for feeds in feed['entries']:
				dt = parser.parse(feeds["published"]).timestamp()
				if lastUpdate < dt:
					print("\n**New Feed Posted From "+str(feed['feed']['title'])+'\n-->'+feeds['title']+'\n')
					msg = feeds['title']+" "+feeds['link']
					try:
						ap.update_status(msg)
					except Exception as e: 
						print("\n!! ERROR : "+str(e)+" !!\n")
		lastUpdate = time.time()


#routes

#homepage
@app.route('/index/')
@app.route('/')
def index():
	if setup==[]:
		return render_template('index.html',erorr="Bot not Configured. Visit Settings tab to configure.",run=running,user=user)
	return render_template('index.html',run=running,user=user)

#settings route
@app.route('/settings/',methods = ['POST', 'GET'])
def settings():
	global setup
	if request.method == 'POST':
		try:
			setup=[]
			setup.append(request.form['consumer_key']+"\n")
			setup.append(request.form['consumer_secret_key']+"\n")
			setup.append(request.form['access_token']+"\n")
			setup.append(request.form['access_token_secret']+"\n")
			setup.append(request.form['interval']+"\n")
			file = open("secret.txt","w")
			file.writelines(setup)
			file.close()
			setup = [x.rstrip() for x in setup]
			if running:
				stop()
				start()
		except:
			return render_template('settings.html',setup=setup,message="ERROR Please Check Again")
		return render_template('settings.html',setup=setup,message="UPDATED SUCCESFULLY")
	else:
		return render_template('settings.html',setup=setup)

#feed edit route
@app.route('/feed_list/',methods = ['POST', 'GET'])
def feed_list():
	global feed
	update=""
	if request.method == 'POST':
		feed=[x.rstrip().replace('\t','') for x in request.form['feed_list'].split('\n') if x.rstrip().replace('\t','')!=""]
		print("\nFeed List updated:-\n",feed)
		try:
			file = open("feed_list.txt","w")
			file.writelines([x+"\n" for x in feed])
			file.close()
			if running:
				stop()
				start()
			update="UPDATED SUCCESFULLY"
		except Exception as e:
			print("\n!! ERROR : "+e+"\n")
			update="ERROR : COULDN'T UPDATE"
	return render_template('feed_list.html',feed=feed,message=update)

#bot access route
@app.route('/changestate')
def changestate():
	global running
	global user
	if request.method != 'GET':
		return "ERORR"
	state = request.args.get('state') 
	if state!=str(running) or setup==[]:
		return jsonify(
			resp="False",
			erorr="Configuration Erorr"
			)
	elif feed==[]:
		return jsonify(
			resp="False",
			erorr="Feed List is Empty. Add RSS Feeds"
			)
	else:
		if not running:
			if start():
				resp=jsonify(pstate=str(not running),resp='True',stat='Running',color='#25abff',user=user)
				running= not running
				return resp
			else:
				return jsonify(resp="False",erorr="PROCESS/AUTH ERORR")
		else:
			if stop():
				user="Bot Inactive"
				resp=jsonify(pstate=str(not running),resp='True',stat='Start',color='red',user=user)
				running= not running
				return resp
			else:
				return jsonify(resp="False",erorr="PROCESS ERORR")

#main running development server
if __name__ == '__main__':
	running=False
	#initializing if setup exists
	try:
		file = open("secret.txt","r")
		setup = [x.rstrip() for x in file.readlines()]
		file.close()
	except:
		pass
	try:
		file = open("feed_list.txt","r")
		feed = [x.rstrip() for x in file.readlines()]
		file.close()
	except:
		pass
	app.run('0.0.0.0')
