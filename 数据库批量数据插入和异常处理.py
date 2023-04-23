#!/usr/bin/python
# -*- coding: UTF-8 -*-

import mysql.connector  # 引入mysql包
from faker import Faker  # 引入faker库

faker = Faker("en_US")  # 指定faker库造什么语言的假数据，中文：zh-CN，英文：en_US

#创建连接对象，设置连接信息
#如果不设置端口（port），则会按默认的3306端口连接
try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="111111",
        port=33206,
        database='world',
        auth_plugin='mysql_native_password'
    )
except mysql.connector.Error as e:
    print('connect fail!{}'.format(e))

cursor = conn.cursor()  # 使用cursor()方法获取操作游标

# 创建测试表
# 若表已存在，则不创建
try:
    sql = '''
         create table if not exists test_data(
           name varchar(20) not null comment '姓名',
           phone_number varchar(20) not null comment '电话号码',
           age varchar(3) not null comment '年龄',
           address varchar(64) not null comment '地址')
        '''
    cursor.execute(sql)  # 执行sql语句
except mysql.connector.Error as e:
    print('create error!{}'.format(e))


# 定义sql插入数据语句
insertNumber = 2 #设置要插入的数据量
try:
    for i in range(insertNumber):
        myName = faker.name()
        myPhoneNumber = faker.phone_number()
        myAge = faker.random_int(1, 99)
        myAddress = faker.address()
        sql = "insert into test_data(name,phone_number,age,address)values('%s','%s','%s','%s')" % (
            myName, myPhoneNumber, myAge, myAddress)
        print("插入的数据：", myName, myPhoneNumber, myAge, myAddress)
        cursor.execute(sql)  # 执行sql语句
    conn.commit()  # 数据表内容有更新，必须使用到该语句，否则会出现 虽然执行成功但表未新增记录的情况
    print("插入", insertNumber, "条数据成功！")
except mysql.connector.Error as e:
    print('insert error!{}'.format(e))

finally:
    cursor.close()  # 关闭指针对象
    conn.close()  # 关闭连接对象

