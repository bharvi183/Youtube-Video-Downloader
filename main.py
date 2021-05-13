
# https://youtu.be/wabuuM7YgQQ

from flask import Flask, request, render_template
from pytube import YouTube
import os
import subprocess
  
app = Flask(__name__)
id = ""
@app.route("/")
def home():
    return render_template("mp4.html")

@app.route("/link",methods=['POST'])
def link():
    try:
        #yt_link = request.args.get("link")
        yt_link = request.form.get("pass_link")
        yt_obj = YouTube(yt_link)
        filters = yt_obj.streams.filter(progressive=True, file_extension='mp4')
        filters.get_lowest_resolution().download()
        return render_template("success.html")
    except Exception as e:
        return str(e)   

    


@app.route("/linktowatch",methods = ['POST'])
def linktowatch():
    
    if request.method == 'POST':
        try:
            #yt_link = request.args.get("link")
            yt_link = request.form.get("towatch")
            yt_obj = YouTube(yt_link)
            id = yt_obj.video_id
            return render_template("watch.html",id=id)
        except Exception as e:
            return str(e) 
    



@app.route("/mpthree",methods=['POST'])
def mpthree():
    try:
        cwd = os.getcwd()
        y = request.form.get("mpthree_link")
        yt = YouTube(y)
        # extract only audio
        video = yt.streams.filter(only_audio=True).first()
        # download the file
        out_file = video.download(output_path=cwd)
        # save the file
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file)
        return render_template("success.html")
    except Exception as e:
        return str(e)   

@app.route('/watch')
def watch():

    return render_template('watch.html')

@app.route('/mp4')
def mp4():

    return render_template('mp4.html')

@app.route('/mp3')
def mp3():

    return render_template('mp3.html')

@app.route('/desc')
def desc():

    return render_template('description.html')

if __name__ == '__main__':
    app.run(debug=True)