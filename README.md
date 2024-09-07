# Credit-Card-Fraud-Detection
Achieving high prediction accuracy in this context means creating models that effectively distinguish between legitimate and fraudulent transactions while minimizing false positives.

Output Of Credit-Card-Fraud-Detection-:

<class 'pandas.core.frame.DataFrame'>
RangeIndex: 1296675 entries, 0 to 1296674
Data columns (total 23 columns):
 #   Column                 Non-Null Count    Dtype  
---  ------                 --------------    -----  
 0   Unnamed: 0             1296675 non-null  int64  
 1   trans_date_trans_time  1296675 non-null  object 
 2   cc_num                 1296675 non-null  int64  
 3   merchant               1296675 non-null  object 
 4   category               1296675 non-null  object 
 5   amt                    1296675 non-null  float64
 6   first                  1296675 non-null  object 
 7   last                   1296675 non-null  object 
 8   gender                 1296675 non-null  object 
 9   street                 1296675 non-null  object 
 10  city                   1296675 non-null  object 
 11  state                  1296675 non-null  object 
 12  zip                    1296675 non-null  int64  
 13  lat                    1296675 non-null  float64
 14  long                   1296675 non-null  float64
 15  city_pop               1296675 non-null  int64  
 16  job                    1296675 non-null  object 
 17  dob                    1296675 non-null  object 
 18  trans_num              1296675 non-null  object 
 19  unix_time              1296675 non-null  int64  
 20  merch_lat              1296675 non-null  float64
 21  merch_long             1296675 non-null  float64
 22  is_fraud               1296675 non-null  int64  
dtypes: float64(5), int64(6), object(12)
memory usage: 227.5+ MB

None
Unnamed: 0               0
trans_date_trans_time    0
cc_num                   0
merchant                 0
category                 0
amt                      0
first                    0
last                     0
gender                   0
street                   0
city                     0
state                    0
zip                      0
lat                      0
long                     0
city_pop                 0
job                      0
dob                      0
trans_num                0
unix_time                0
merch_lat                0
merch_long               0
is_fraud                 0
dtype: int64

is_fraud
0    1289169
1       7506
Name: count, dtype: int64

Normal transactions shape: (1289169, 23)
Fraud transactions shape: (7506, 23)

Normal transactions amount statistics:
count    1.289169e+06
mean     6.766711e+01
std      1.540080e+02
min      1.000000e+00
25%      9.610000e+00
50%      4.728000e+01
75%      8.254000e+01
max      2.894890e+04
Name: amt, dtype: float64

Fraud transactions amount statistics:
count    7506.000000
mean      531.320092
std       390.560070
min         1.060000
25%       245.662500
50%       396.505000
75%       900.875000
max      1376.040000
Name: amt, dtype: float64

New data shape: (15012, 23)

is_fraud
0    7506
1    7506
Name: count, dtype: int64

<class 'pandas.core.frame.DataFrame'>
Index: 15012 entries, 9584 to 1295733
Data columns (total 22 columns):
 #   Column      Non-Null Count  Dtype  
---  ------      --------------  -----  
 0   Unnamed: 0  15012 non-null  int64  
 1   cc_num      15012 non-null  int64  
 2   merchant    15012 non-null  int32  
 3   category    15012 non-null  int32  
 4   amt         15012 non-null  float64
 5   first       15012 non-null  int32  
 6   last        15012 non-null  int32  
 7   gender      15012 non-null  int32  
 8   street      15012 non-null  int32  
 9   city        15012 non-null  int32  
 10  state       15012 non-null  int32  
 11  zip         15012 non-null  int64  
 12  lat         15012 non-null  float64
 13  long        15012 non-null  float64
 14  city_pop    15012 non-null  int64  
 15  job         15012 non-null  int32  
 16  unix_time   15012 non-null  int64  
 17  merch_lat   15012 non-null  float64
 18  merch_long  15012 non-null  float64
 19  dob_year    15012 non-null  int32  
 20  dob_month   15012 non-null  int32  
 21  dob_day     15012 non-null  int32  
dtypes: float64(5), int32(12), int64(5)
memory usage: 1.9 MB

None
Training set shape: (9007, 22)
Testing set shape: (6005, 22)

Model accuracy: 0.8591174021648627
