#!/usr/bin/env python 
# -*- coding:utf-8 -*-

"""对象关系模型映射框架SQLAlchemy"""

from sqlalchemy import Column,String,create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

#创建对象基类
Base = declarative_base()

#定义User对象
class User(Base):
    #表名
    __tablename__='user'

    #表结构
    id=Column(String(20),primary_key=True)
    name=Column(String(20))

#初始化数据库连接  create_engine()用来初始化数据库连接 '数据库类型+数据库驱动名称://用户名:口令@机器地址:端口号/数据库名'
"""mysql+mysqlconnector://root:password@localhost:3306/test"""
engine = create_engine('mysql+mysqlconnector://root:root@localhost:3306/world')
#创建DBSession类型
DBSession=sessionmaker(bind=engine)

#创建session对象
session = DBSession()

#创建User对象
new_User=User(id='9',name='bob')

#添加到session中
session.add(new_User)
#提交保存数据库
session.commit()

#关闭session
session.close()

#创建session
session=DBSession()
#创建query查询 filter是条件,最后调用one()返回一行，all()返回所有行
user=session.query(User).filter(User.id=='5').one()
#打印类型和对象属性
print('type:',type(user))
print('name:',user.name)
#关闭session
session.close()

