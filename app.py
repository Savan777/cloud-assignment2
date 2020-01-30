#importing requried libraries
import boto3
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)


#rendering the index.html file when on homepage
@app.route("/")
def hello():
	return '''<form method=POST enctype=multipart/form-data action="upload">
	<input type=file name=myfile>
	<input type=submit>
	</form>'''
    #return render_template("index.html")

@app.route('/upload',methods=['POST'])
def upload():
	s3 = boto3.resource('s3')
	s3.Bucket('cloud-assignment2-savan').put_object(Key=request.files['myfile'].filename, Body=request.files['myfile'])
	return '<h1>File saved to S3</h1>'
	
#when user navigates to addmusic/form url it will display the getdata.html file which
#contains the form that user filled out to add a song to the database
@app.route("/addmusic/form/",methods=['GET','POST'])
def add_music_form():
    message = ''
	#if the request was type post then read the values being sent from front-end and store in variable
    if request.method == 'POST':
        song=request.form.get('song')
        artist=request.form.get('artist')
        published=request.form.get('published')
		#try and add the data retrieved to the table and pass success message to rendered template
        try:
            message = "Song Added"
            return render_template("getdata.html", value=message)
        except Exception as e:
            return(str(e)) #show error message if failed to do try block
    return render_template("getdata.html")


#this method will do the searching for a specific song and return the details of the song if it exists
@app.route("/getsong", methods=['GET','POST'])
def get_song():
	
    if request.method == 'POST':
		#get value of variable from front-end
        song=request.form.get('song')
        try:
			#assign details of the song to respective variables
            songID = 1
            songName = "test"
            artist = "test"
            date = "01/01/01"
			#return the results to front-end
            return render_template("searchSong.html", value1=songID, value2=songName, value3=artist, value4=date)
        except Exception as e:
            return(str(e))
    return render_template("searchSong.html")

#get feedback from from and store in feedback table
@app.route("/feedback", methods=['GET','POST'])
def feedback():
    if request.method == 'POST':
        customer = request.form.get('cname')
        rating = request.form.get('rating')
        comments = request.form.get('comments')
        try:
			return render_template("index.html")
			#if user had already submitted feedback the provide message stating already submitted
        except Exception as e:
            return(str(e))
    return render_template("review.html")

if __name__ == '__main__':
    app.run()
