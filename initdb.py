import sqlite3
conn = sqlite3.connect('database.db')
c = conn.cursor()
c.execute('''CREATE TABLE LOCATION(lid text primary key, lname text, lat decimal(8,6), lon decimal(9,6))''')
c.execute('''CREATE TABLE PLACE(pid text primary key, pname text, lat decimal(8,6), lon decimal(9,6))''')
c.execute('''CREATE TABLE LOC_PLACE(lid text, pid text, threshold integer, primary key(lid, pid), foreign key (lid) references LOCATION(lid), foreign key (pid) references PLACE(pid))''')
c.execute('''CREATE TABLE CROWDTRENDS(lid text, pid text, time text, density decimal(5,2), primary key(lid, pid, time), foreign key (lid) references LOCATION(lid), foreign key (pid) references PLACE(pid))''')
f1 = open('db_config_data/config_loc.txt','r')
for line in f1.readlines():
    print(line)
    w = line.strip().split(';')
    w = (w[0],w[1],w[2],w[3],)
    c.execute('''INSERT INTO LOCATION VALUES(?,?,?,?)''',w)
f2 = open('db_config_data/config_place.txt','r')
for line in f2.readlines():
    w = line.strip().split(';');
    w1 = (w[1],w[2],w[3],w[4],)
    c.execute('''INSERT INTO PLACE VALUES(?,?,?,?)''',w1)
    w2 = (w[0],w[1],w[5],)
    c.execute('''INSERT INTO LOC_PLACE VALUES(?,?,?)''',w2)
conn.commit()
conn.close()