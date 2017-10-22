from flask import Flask, url_for, render_template, request, session
import sqlite3
import time

@app.route("/")
def index():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE PLACE(time text, location text, heatmap text)''')
    '''
        TIME -> A string for timestamp [Ex : 'Sun Oct 22 12:17:45 2017']
        LOCATION -> A string for location [Ex : 'B-Block','Student Lounge']
        HEATMAP -> A string which is the name of the heatmap file generated [Ex : 'heatmap1.png']
    '''
    conn.commit()
    conn.close()
    return render_template('index.html') # Go to Frontend home web page

@app.route("/retrieve",methods = ['POST'])
def retreive():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    loc = request.form['loc']
    #time = request.form['time']
    #params = (loc,time,)
    #c.execute('''SELECT * FROM PLACE WHERE location = ? AND time = ?''',)
    c.execute('''SELECT * FROM PLACE WHERE location = ''',loc)
    r = c.fetchone()
    tm = r[0]
    hm = r[2]
    conn.close()
    return render_template('heatmap.html',heatmap=hm,time=tm) #returning back to the required html page

@app.route("/store",methods = ['POST'])
def store():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    loc = request.form['loc']
    heatmap = request.form['hm']
    params = (time.ctime(),loc,heatmap)
    c.execute('''INSERT INTO PLACE VALUES(?,?,?)''',params) #inserting to the database
    conn.commit()
    conn.close()
    return render_template('index.html')

if __name__ == '__main__':
    app.run(
        host="127.0.0.1",
        port=int("5000")
  )