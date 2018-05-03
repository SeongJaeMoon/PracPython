from sklearn import svm, metrics
from sklearn.model_selection import train_test_split
import pandas as pd
import csv
import re
import os.path, io, sys
import random
import numpy as np

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

DIR = "C:\\Users\\SIST\\Documents\\moonsworld\\iris.csv"
csv_file = pd.read_csv(DIR)

'''
csv = []
with open(DIR, 'r', encoding = 'utf-8') as f:
    # 한 줄씩 읽어 들이기
    for line in f:
        line = line.strip() # 줄바꿈 제거
        cols = line.split(',') # 쉼표로 자르기
        # 문자열 데이터를 숫자로 변환하기
        fn = lambda x: float(x) if re.match(r'^[0-9]\+$', x) else x
        cols = list(map(fn, cols))
        csv.append(cols)

# 가장 앞 줄의 헤더 제거
del csv[0]

# 데이터 셔플(섞기)
random.shuffle(csv)

# 학습 전용 데이터와 테스트 전용 데이터 분할하기 (2:1 비율)
total_len = len(csv)
train_len = int(total_len * 2 / 3)
train_data = []
train_label = []
test_data = []
test_label = []

for i in range(total_len):
    data = csv[i][0:4]
    label = csv[i][4]
    if i  < train_len:
        train_data.append(data)
        train_label.append(label)
    else:
        test_data.append(data)
        test_label.append(label)
# 데이터를 학습시키고 예측하기
clf = svm.SVC()
clf.fit(train_data, train_label)
pre = clf.predict(test_data)
# 정답률 구하기
as_score = metrics.accuracy_score(test_label, pre)
print("정답률=", as_score)
'''

csv_data = csv_file[["SepalLength", "SepalWidth", "PetalLength", "PetalWidth"]]
csv_label = csv_file["Name"]

# 학습 전용 데이터와 테스트 전용 데이터로 나누기
train_data, test_data, train_label, test_label = \
    train_test_split(csv_data, csv_label)
# 데이터 학습시키고 예측하기
clf = svm.SVC()
clf.fit(train_data, train_label)
pre = clf.predict(test_data)

# 정답률 구하기
as_score = metrics.accuracy_score(test_label, pre)
print("정답률=", as_score)
