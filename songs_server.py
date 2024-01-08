from flask import Flask, render_template
from flask import request, session, redirect, url_for
import songs_database as db

app = Flask(__name__)
app.secret_key = "SECRETKEY" # should be random for security

def _format_length(seconds):
    mins = seconds // 60
    secs = seconds % 60
    return "{}:{:02d}".format(mins, secs)

@app.route("/logout")
def logout_page():
    session["userID"] = None
    return redirect("/login")

@app.route("/login", methods=["GET"])
def login_page():
    return render_template("songslogin.html", failed=False)

@app.route("/login", methods=["POST"])
def login_post():
    userID = db.login(request.values.get("userrname"),
                      request.values.get("password"))
    if userID == -1:
        return render_template("songslogin.html", failed=True)
    else:
        session["userID"] = userID
        return redirect("/")

@app.route("/signup", methods=["GET"])
def signup_page():
    return render_template("songssignup.html", failed=False)

@app.route("/signup", methods=["POST"])
def signup_post():
    userID = db.createAccount(request.values.get("fullname"),
            request.values.get("username"), request.values.get("password"))
    
    if userID == -1:
        return render_template("songssignup.html", failed=True)
    else:
        session["userID"] = userID
        return redirect("/")

@app.route("/", methods=["GET"])
def main_page():
    if len(session) == 0 or session["userID"] is None:
        return redirect("/login")
    else:
        search_artist = request.values.get("artist", "")
        search_name = request.values.get("name", "")
        search_genre = request.values.get("genre", "")

        songs = db.getSongs(search_artist, search_name, search_genre)
        songs = [{
            "id": _id,
            "name": name,
            "artist": artist,
            "length": _format_length(length),
            "genre": genre,
            "coverart": coverart,
            "audiofile": audiofile
        } for (_id, name, artist, length, genre, coverart, audiofile) in songs]

        return render_template("songs.html", artist=search_artist,
                               name=search_name, genre=search_genre, songs=songs)

@app.route("/song/<songID>", methods=["GET"])
def song_details(songID):
    if session["userID"] is None:
        return redirect("/login")
    else:
        details, comments = db.getSongDetails(songID)
        (_id, name, artist, length, genre, coverart, audiofile) = details
        details = {
            "id": _id,
            "name": name,
            "artist": artist,
            "length": _format_length(length),
            "genre": genre,
            "coverart": coverart,
            "audiofile": audiofile
        }

        comments = [{
            "user": user,
            "message": message
        } for (_id, user, songID, message) in comments]

        return render_template("songdetails.html", comments=comments, **details)

@app.route("/addcomment", methods=["POST"])
def addcomment():
    if session["userID"] is None:
        return redirect("/login")
    else:
        comment = request.values.get("comment", "").strip()
        songID = int(request.values.get("songID"))

        if len(comment):
            success = db.addComment(songID, comment, str(session["userID"]))
            if not success:
                print("Failed to add comment")

        return redirect("/song/{}".format(songID))


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080)

