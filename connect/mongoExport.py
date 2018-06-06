import time
import xlsxwriter
from pymongo import MongoClient
from connect.timer import Timer


class MongoExport(object):

    def __init__(self,path,fileName):
        self.path = path+fileName
        self.client =  MongoClient()

    def buildBook(self,fileds):
        self.fields = fileds
        self.workbook = xlsxwriter.Workbook(self.path, {'nan_inf_to_errors': True})  # 处理无穷大
        self.worksheet = self.workbook.add_worksheet()
        # 设置行头
        for j in range(len(self.fields)):
            self.worksheet.write(0, j, self.fields[j])

    def export(self,dbName,colName):
        timer = Timer(time.time())
        db = self.client.get_database(dbName)
        job = db.get_collection(colName)
        rlist = job.find()
        i =0
        for r in rlist:
            j = 0
            for j in range(len(self.fields)):
                self.worksheet.write(i, j, r[self.fields[j]])
            i = i + 1
        self.workbook.close()
        timer.print()

if __name__ == '__main__':
    export = MongoExport("E:/Python练习/excel/","job2.xlsx")
    fields = ['jobId', 'jobName', 'arera', 'cAdress', 'cName', 'wage']
    export.buildBook(fields)
    export.export('spider','job')