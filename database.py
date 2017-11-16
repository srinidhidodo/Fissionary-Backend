from flask import Flask, url_for, render_template, request, session
import sqlite3
import time

app = Flask(__name__)

@app.route("/")
def index():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    #c.execute('''ALTER TABLE PLACE ADD FOREIGN KEY pid(pid) REFERENCES parent_table(columns)''')
    c.execute('''CREATE TABLE LOCATION(lid text primary key, lname text, lat decimal(8,6), lon decimal(9,6))''')
    c.execute('''CREATE TABLE LOC_PLACE(lid text, pid text primary key, pname text, lat decimal(8,6), lon decimal(9,6), threshold integer, foreign key (lid) references LOCATION(lid))''')
    c.execute('''CREATE TABLE PLACE(pid text primary key, time text, heatmap text, foreign key (pid) references LOC_PLACE(pid))''')
    #INSERT VALUES INTO TABLE LOCATION AND LOC_PLACE
    f1 = open('static/config_loc.txt','r')
    for line in f1.readlines():
        print(line)
        w = line.split(';')
        w = (w[0],w[1],w[2],w[3],)
        c.execute('''INSERT INTO LOCATION VALUES(?,?,?,?)''',w)
    f2 = open('static/config_place.txt','r')
    for line in f2.readlines():
        w = line.split(';')
        w = (w[0],w[1],w[2],w[3],w[4],w[5],)
        c.execute('''INSERT INTO LOC_PLACE VALUES(?,?,?,?,?,?)''',w)
    conn.commit()
    conn.close()
    return render_template('index.html')

#retrieve only place and location
@app.route("/retrieve_loc")
def retreive_loc():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    loc = ("wonderla",)
    #loc = request.form['loc']
    #time = request.form['time']
    #params = (loc,time,)
    #c.execute('''SELECT * FROM PLACE WHERE location = ? AND time = ?''',)
    c.execute('''SELECT * FROM LOCATION WHERE lname = ?''',loc)
    r = c.fetchone()
    #tm = r[0]
    #hm = r[2]
    conn.close()
    #return r 
    return render_template('heatmap.html',row=r)

@app.route("/retrieve_plc")
def retrieve_plc():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    #plc = request.form['plc']
    plc = ("01",)
    c.execute('''SELECT * FROM LOC_PLACE WHERE pid = ?''',plc)
    r = c.fetchone()
    #tm = r[0]
    #hm = r[2]
    conn.close()
    #return r
    return render_template('place.html',row=r)

@app.route("/update")
def update():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    #loc = request.form['loc']
    #heatmap = request.form['hm']
    #params = (loc,time.ctime(),heatmap,)
    params = ('wonderla','Sun 12 Jun 2017 19:56:01','heatmap001.png',)
    c.execute('''INSERT INTO PLACE VALUES(?,?,?)''',params) #inserting to the database
    conn.commit()
    conn.close()
    return render_template('update.html',row=params)

if __name__ == '__main__':
    app.run(
        host="127.0.0.1",
        port=int("5000")
  )
