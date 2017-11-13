from flask import Flask, url_for, render_template, request, session
import sqlite3
import time

@app.route("/")
def index():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    #c.execute('''ALTER TABLE PLACE ADD FOREIGN KEY pid(pid) REFERENCES parent_table(columns)''')
    c.execute('''CREATE TABLE LOCATION(lid text primary key, lname text, lat decimal(8,6), lon decimal(9,6))''')
    c.execute('''CREATE TABLE LOC_PLACE(pid text primary key, lid text, pname text, lat decimal(8,6), lon decimal(9,6), threshold integer, foreign key (lid) references LOCATION(lid))''')
    c.execute('''CREATE TABLE PLACE(pid text primary key, time text, heatmap text, foreign key (pid) references LOC_PLACE(pid))''')
    #INSERT VALUES INTO TABLE LOCATION AND LOC_PLACE
    f1 = open('config_loc.txt','r')
    for line in f1.read():
        w = line.split(';')
        c.execute('''INSERT INTO LOCATION VALUES(?,?,?,?)''',w)
    f2 = open('config_place.txt','r')
    for line in f2.read():
        w = line.split(';')
        c.execute('''INSERT INTO LOC_PLACE VALUES(?,?,?,?,?,?)''',w)
    conn.commit()
    conn.close()
    #return render_template('index.html') # Go to Frontend home web page

#retrieve only place and location
@app.route("/retrieve_loc",methods = ['POST'])
def retreive_loc():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    loc = request.form['loc']
    #time = request.form['time']
    #params = (loc,time,)
    #c.execute('''SELECT * FROM PLACE WHERE location = ? AND time = ?''',)
    c.execute('''SELECT * FROM LOCATION WHERE location = ''',loc)
    r = c.fetchone()
    #tm = r[0]
    #hm = r[2]
    conn.close()
    return r 
    #return render_template('heatmap.html',heatmap=hm,time=tm) #returning back to the required html page

@app.route("/retrieve_plc",methods=['POST'])
def retrieve_plc():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    plc = request.form['plc']
    c.execute('''SELECT * FROM LOC_PLACE WHERE plc = ''',plc)
    r = c.fetchone()
    #tm = r[0]
    #hm = r[2]
    conn.close()
    return r

@app.route("/update",methods = ['POST'])
def update():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    loc = request.form['loc']
    heatmap = request.form['hm']
    params = (loc,time.ctime(),heatmap)
    c.execute('''INSERT INTO PLACE VALUES(?,?,?)''',params) #inserting to the database
    conn.commit()
    conn.close()
    #return render_template('index.html')

if __name__ == '__main__':
    app.run(
        host="127.0.0.1",
        port=int("5000")
  )