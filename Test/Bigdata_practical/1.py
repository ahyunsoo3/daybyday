
import pandas as pd
df = pd.read_csv('data/mtcars.csv', index_col=0)

qsec = df.loc[:, 'qsec']
qsec_min, qsec_max = qsec.min(), qsec.max()
# print(qsec)
res = (qsec-qsec_min)/(qsec_max-qsec_min)
print(res)

a = res>0.5
b = df[a]
print('record:', len(b))

# reference :
# https://blog.naver.com/statstorm/222364100877

# https://dataq.goorm.io/exam/116674/%EC%B2%B4%ED%97%98%ED%95%98%EA%B8%B0/quiz/2