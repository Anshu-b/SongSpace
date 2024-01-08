CREATE TABLE users 
( 
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    name TEXT, 
    username TEXT, 
    password TEXT
); 
CREATE UNIQUE INDEX users_id_uindex ON users (id); 
CREATE UNIQUE INDEX users_username_uindex ON users (username); 

CREATE TABLE songs 
( 
    id INTEGER PRIMARY KEY, 
    name TEXT, 
    artist TEXT, 
    length INT, 
    genre TEXT, 
    coverart TEXT, 
    audiofile TEXT 
);

CREATE UNIQUE INDEX songs_id_uindex ON songs (id); 

CREATE TABLE comments 
( 
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    user TEXT, 
    songID TEXT, 
    message TEXT 
); 
CREATE UNIQUE INDEX comments_id_uindex ON comments (id); 

INSERT INTO songs (id, name, artist, length, genre, coverart, audiofile) 
VALUES (1, "Apollos Reel", "Washington State University Jazz Big Band", 379, "Jazz", "images/apollosreel.png", "songs/apollosreel.mp3"); 

INSERT INTO songs (id, name, artist, length, genre, coverart, audiofile) 
VALUES (2, "Take the A Train", "Duke Ellington", 198, "Jazz", "images/atrain.png", "songs/atrain.mp3");

INSERT INTO songs (id, name, artist, length, genre, coverart, audiofile) 
VALUES (3, "The Longest Time", "Billy Joel", 244 , "Pop", "images/thelongesttime.png", "songs/thelongesttime.mp3");

INSERT INTO songs (id, name, artist, length, genre, coverart, audiofile) 
VALUES (4, "I Want It That Way", "Backstreet Boys", 219, "Pop", "images/iwantit.png", "songs/iwantit.mp3");

INSERT INTO songs (id, name, artist, length, genre, coverart, audiofile) 
VALUES (5, "Take on Me", "a-ha", 227 , "Pop", "images/takeonme.png", "songs/takeonme.mp3");

INSERT INTO songs (id, name, artist, length, genre, coverart, audiofile) 
VALUES (6, "Better Now", "Post Malone", 201 , "Hip-Hop", "images/betternow.png", "songs/betternow.mp3");

INSERT INTO songs (id, name, artist, length, genre, coverart, audiofile) 
VALUES (7, "Panda", "Designer", 216 , "Hip-Hop", "images/panda.png", "songs/panda.mp3");