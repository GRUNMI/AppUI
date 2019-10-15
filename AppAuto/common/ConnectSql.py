# coding:utf-8
__author__ = 'GRUNMI'


from AppAuto.common.ReadConfig import ReadConfig
import pymssql
import pymysql


class SqlServer:
    def __init__(self, sectionName):
        data = ReadConfig().get_all_value(sectionName)
        self.host = data["host"]
        self.port = data["port"]
        self.user = data["user"]
        self.password = data["password"]
        self.database = data["database"]
        self.charset = "utf8"

    def connect_SqlServer(self):
        self.db = pymssql.connect(
            host=self.host, port=self.port, user=self.user,
            password=self.password, database=self.database, charset=self.charset)
        self.cursor = self.db.cursor()
        return self.cursor

    def execute_query(self, sql):
        self.cursor = self.connect_SqlServer()
        self.cursor.execute(sql)
        # row = self.cursor.fetchone()  # 一次获取一行数据
        # data = self.cursor.fetchmany(10)  # 获取10行数据
        # data = self.cursor.fetchall()  # 一次获取全部数据
        # self.cursor.close()
        # self.db.close()
        for value in self.cursor.fetchall()[0]:
            # print(value)
            self.cursor.close()
            self.db.close()
            return value

    def execute_no_query(self, sql):
        self.cursor = self.connect_SqlServer()
        self.cursor.execute(sql)
        self.cursor.commit()
        self.cursor.close()
        self.db.close()


class MySql:
    def __init__(self, sectionName):
        data = ReadConfig().get_all_value(sectionName)
        self.host = data["host"]
        self.port = int(data["port"])
        self.user = data["user"]
        self.password = data["password"]
        self.database = data["database"]
        self.charset = "utf8"

    def connect_MySql(self):
        self.db = pymysql.connect(
            host=self.host, port=self.port, user=self.user,
            password=self.password, database=self.database, charset=self.charset)
        self.cursor = self.db.cursor()
        return self.cursor

    def execute_query(self, sql):
        self.cursor = self.connect_MySql()
        self.cursor.execute(sql)
        # row = self.cursor.fetchone()  # 一次获取一行数据
        # data = self.cursor.fetchmany(10)  # 获取10行数据
        # data = self.cursor.fetchall()  # 一次获取全部数据
        for value in self.cursor.fetchall()[0]:
            self.cursor.close()
            self.db.close()
            return value

    def execute_no_query(self, sql):
        self.cursor.execute(sql)
        self.cursor.commit()
        self.cursor.close()
        self.db.close()


if __name__ == '__main__':
    value = SqlServer('sqlserver').execute_query("SELECT Col_002 from TB_DomainSJDCodeNEW WHERE Col_001=N'{}'".format("花都花东点部"))
    print(value)
    value = MySql('mysql').execute_query("SELECT * FROM atm.ta_logicno_psn WHERE LogicNo IN ('20761271172')")
    print(value)

