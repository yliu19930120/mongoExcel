import time
import xlsxwriter
from pymongo import MongoClient
from connect.timer import Timer


class MongoExport(object):

    def __init__(self, path, fileName):
        self.path = path + fileName
        self.client = MongoClient()
        self.workbook = xlsxwriter.Workbook(self.path, {'nan_inf_to_errors': True})  # 处理无穷大

    def buildSheet(self, name='sheet0'):
        worksheet = self.workbook.add_worksheet(name)
        # 设置行头
        for j in range(len(self.fields)):
            worksheet.write(0, j, self.fields[j])
            j = j + 1
        return worksheet

    def export(self, dbName, colName, fields ,filter={},sort =[('_id',1)]):
        start = time.time()
        self.fields = fields
        worksheet = self.buildSheet()
        db = self.client.get_database(dbName)
        col = db.get_collection(colName)
        rlist = col.find(filter).sort(sort)
        rowNum = 1
        for r in rlist:
            rowNum = self.write(r, worksheet, rowNum)
        self.workbook.close()
        print('耗时:', time.time() - start)

    def write(self, record, worksheet, rowNum):
        j = 0
        for j in range(len(fields)):
            worksheet.write(rowNum, j, record[fields[j]])

        return rowNum + 1

    def exportGroupByField(self, dbName, colName, fields, fieldName):
        self.fields = fields
        start = time.time()
        d = {}
        rowNumD = {}
        db = self.client.get_database(dbName)
        col = db.get_collection(colName)
        rlist = col.find()
        for r in rlist:
            key = r[fieldName]
            if (key not in d.keys()):
                d[key] = self.buildSheet(key)
                rowNumD[key] = 1
            rowNumD[key] = self.write(r, d[key], rowNumD[key])
        self.workbook.close()
        print('耗时:', time.time() - start)

if __name__ == '__main__':
    export = MongoExport("E:/Python练习/excel/","job2.xlsx")
    fields = ['jobId', 'jobName', 'arera', 'cAdress', 'cName', 'wage']
    export.buildBook(fields)
    export.export('spider','job')