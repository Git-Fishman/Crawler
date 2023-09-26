# -*- coding: UTF-8 -*-
import pymysql


class DataBase(object):
    def __init__(self, host='127.0.0.1', port=3306, user='root', passwd='123456', db='FOC'):
        # 建立数据库连接
        self.connect = pymysql.connect(host=host, port=port, user=user, passwd=passwd, db=db)
        # 创建游标对象
        self.cursor = self.connect.cursor()

    def data_select(self, sql):
        """数据查询"""
        # 执行sql语句
        self.cursor.execute(sql)
        # 获取查询结果
        data = self.cursor.fetchall()
        return data

    def data_execute(self, sql):
        """更新/插入/删除"""
        try:
            # 执行sql语句
            self.cursor.execute(sql)
            # 提交事务
            self.connect.commit()
        except Exception as e:
            # 回滚事务
            self.connect.rollback()

    def __del__(self):
        # 关闭游标对象
        self.cursor.close()
        # 关闭数据库连接
        self.connect.close()
