#!/usr/bin/env python 
# -*- coding:utf-8 -*-


import mysql.connector
"""连接mysql"""
#执行INSERT等操作后要调用commit()提交事务
conn = mysql.connector.connect(user='root',password='root',database='world')
cursor=conn.cursor()

#创建User表
# cursor.execute('create table user (id varchar(20) primary key ,name varchar(20) )')
#插入记录 支持占位符 %s
cursor.execute('insert into user (id,name) values (%s,%s)',['3','tom'])
#读取表内容
print(cursor.rowcount)

#提交事务
conn.commit()
cursor.close()

#运行查询
cursor=conn.cursor()
cursor.execute('select * from user where id = %s',('1',))
values=cursor.fetchall()
print(values)
cursor.close()


cursor=conn.cursor()
for i in range(4,9):
    cursor.execute('insert into user (id,name) values (%s,%s)',[str(i),str(i)+'asd'])


cursor.close()
conn.commit()
conn.close()