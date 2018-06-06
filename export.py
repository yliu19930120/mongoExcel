import datetime
import xlsxwriter
from pymongo import MongoClient
import time

time_start = time.time()

time_str = '2017-01-01 00:00:00'

start = datetime.datetime.strptime(time_str, '%Y-%m-%d %H:%M:%S')

client = MongoClient()

db = client.spider

factor = db.job

# filter = {'date':{'$gte':start}}

# sort = [('date', 1)]

rlist = factor.find()

keys = ['jobId', 'jobName', 'arera','cAdress', 'cName', 'wage']

path = 'E:/Python练习/excel/job.xlsx'

workbook = xlsxwriter.Workbook(path, {'nan_inf_to_errors': True})  # 处理无穷大

worksheet = workbook.add_worksheet()
# 设置行头
for j in range(len(keys)):
    worksheet.write(0, j, keys[j])
i = 1
for r in rlist:
    j = 0
    for j in range(len(keys)):
        worksheet.write(i, j, r[keys[j]])
    i = i + 1

workbook.close()
time_end = time.time()
print('OK! totally cost', time_end - time_start)


