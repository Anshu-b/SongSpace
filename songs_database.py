import sqlite3
import hashlib

con = sqlite3.connect("songs.db", check_same_thread=False)
db = con.cursor()

def _sha256(password):
    return hashlib.sha256(password.encode()).hexdigest()

def createAccount (name, username, password):
    #Check if account exists already
    if len(db.execute("SELECT * FROM users WHERE username = ?",
                      (username,)).fetchall()):
        return -1
    
    db.execute("INSERT INTO users (name, username, password) VALUES (?, ?, ?)",
               (name, username, _sha256(password)))
    con.commit()

    user = db.execute("SELECT id FROM users WHERE username = ? AND password = ?",
                      (username, _sha256(password))).fetchall()
    if len(user) == 0:
        return -1
    else:
        return user[0][0]

def login(username, password):
    user = db.execute("SELECT id FROM users WHERE username = ? AND password = ?",
                      (username, _sha256(password))).fetchall()
    if len(user) == 0:
        return -1
    else:
        return user[0][0]

def getSongDetails(songID):
    song = db.execute("SELECT * FROM songs WHERE id = ?",
                      (songID,)).fetchall()
    if len(song) == 0:
        return None, None
    else:
        comments = db.execute("SELECT * FROM comments WHERE songID = ?",
                              (songID,)).fetchall()
        return song[0], comments

def getSongs(artist, name, genre):
    if genre is None or len(genre.strip()) == 0 or genre.lower() == "any":
        genre = "%"

    if artist is None:
        artist = ""

    if name is None:
        name = ""

    songs = db.execute("SELECT * FROM songs WHERE name LIKE ? AND artist LIKE ? AND genre LIKE ?",
                       ("%"+name+"%", "%"+artist+"%", genre)).fetchall()
    return songs

def addComment(songID, comment, userID):
    user = db.execute("SELECT * FROM users WHERE id = ?",
                      (userID,)).fetchall()

    if len(user) == 0:
        return False

    db.execute("INSERT INTO comments (songID, message, user) VALUES (?, ?, ?)",
               (songID, comment, user[0][1]))
    con.commit()
    return True










    
