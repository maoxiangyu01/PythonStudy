import pymysql
import datetime
import time
import random

conn = pymysql.connect(host='localhost',user='root',passwd='root',db='test')
cur = conn.cursor()

odate = datetime.datetime.strptime('2000-1-1','%Y-%m-%d')

for i in range(1,100):
    empCode='X'+str(i).zfill(4)
    empName='NAME'+str(i).zfill(4)

    ms = datetime.datetime.now().microsecond
    random.seed(ms)
    salary = random.randint(10000,20000)
    time.sleep(0.000001)
    indate =odate + datetime.timedelta(days=i)
    sql = "insert into d_employee (emp_no,emp_name,emp_salary,in_date) values ('%s','%s','%f','%s')" \
          % (empCode, empName, salary, indate.strftime("%Y-%m-%d"))
    cur.execute(sql)

conn.commit()
cur.close()
conn.close()



