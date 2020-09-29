from  flask import Flask,Response,request,jsonify
import requests
app=Flask(__name__)
def giveMp4(query):
	url="https://y2mate.guru/api/convert/"
	full_link=f'https://www.youtube.com/watch?v={query}'
	data={"url":full_link}
	return requests.post(url,data=data).json()
def giveMp3(query):
	url="https://www.320youtube.com/v8/watch?v="+query
	html=requests.get(url).text
	link=(html.split('btn-success btn-lg" href=')[1]).split('" rel')[0]
	return {"link":link}

@app.route('/<path:path>')
def catch_all(path):
	if request.args.get('mp3') is None and request.args.get('mp4') is None:
		return "<h1> Please provide necessary mp3 or mp4 queries"
	elif request.args.get('mp3') is None:
		return jsonify(giveMp4(request.args.get('mp4')))
	elif request.args.get('mp4') is None:
		return jsonify(giveMp3(request.args.get('mp3')))
app.run(debug=True)