# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 09:17:29 2024

@author: DinhHoa
"""
########################################################
# GIAI ĐOẠN 1: NẠP DỮ LIỆU GỐC (PRIMARY INPUT DATA LOAD)
########################################################
#######################################
# Bước 1: Nạp các thư viện cần thiết
#######################################

import numpy as np #Numeric Python: Thư viện về Đại số tuyến tính tính

import pandas as pd #Python Analytic on Data System: For data processing (Thư viện xử lý dữ liệu)
from sklearn.preprocessing import MinMaxScaler
from scipy import stats # thư viện cung cấp các công cụ thống kê [statistics] sub-lib của science python [các công cụ khoa học] 

from sklearn import preprocessing # Thư viện tiền xử lý DL (XL ngoại lệ: Isolated)
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_selection import SelectKBest, chi2 # Nạp hàm Thư viện hỗ trợ Mô hình phân tích dữ liệu thăm dò
###############################################################
# Bước 2: Tải tập dữ liệu: Load the data set (Nạp tập dữ liệu)
# ./pokemon.csv
##############################################################
df = pd.read_csv('./G213NTD_EDA/pokemon_combined.csv')
df = df.drop(columns=['Abilities', 'Growth Rate', 'Gender'])
# Display the shape of the data set (xem lượng dòng & cột dữ liệu của tập DL gốc)
print("--------------BƯỚC 2----------------")
print('Độ lớn của bảng [frame] dữ liệu pokemon:',df.shape)
#Display data (Hiển thị dữ liệu dạng mảng 5 dòng đầu của tập DL gốc)
print(df[0:5])

###############################################
# # GIAI ĐOẠN 2: TIỀN XỬ LÝ (PRE-PROCESSING)
###############################################
############################################################################
# # Bước 3: Xử lý CỘT dữ liệu NULL quá nhiều OR không có giá trị phân tích
############################################################################
# Checking for null values (Kiểm tra giá trị null = đếm số dòng có dữ liệu ứng từng thuộc# tính)
print("--------------BƯỚC 3----------------")
print(df.count().sort_values()) #df.count(): đếm số lượng dòng có dữ liệu của df, .sort_values() sx tăng dân

#
# df = df.drop("number", axis = 1) #drop cột number vì không có giá trị phân tích
# print(df.isna().sum() / len(df) * 100) #kiểm tra phần trăm giá trị null
#

#df = df.drop(columns=['type2'],axis=1) có thể drop cột type2
# thay đổi giá trị null của cột type2 thành 'PST' để đảm bảo phân tích toàn bộ dữ liệu
# 
# df["type2"].fillna("PST", inplace = True)   # PST viết tắt của pure-single-type pokemon (pokemon chỉ có 1 )
# 
# kiểm tra lại sự tồn tại của giá trị null
print(df.isna().sum())
print(df.shape) # kiểm tra lại số lượng cột & dòng của df sau khi XL NULL cột


#####################################
# # Bước 4: Xử lý DÒNG dữ liệu NULL 
###################################
# Removing null values (Xóa tất cả các dòng có giá trị null trong tập FRAME dữ liệu.)
print("--------------BƯỚC 4----------------")

df = df.dropna(how='any')
print(df.shape) # kiểm tra lại số lượng cột & dòng của df sau khi XL NULL các dòng DL
# =>(1014,17) không NULL 

# ##############################################################################
# # # Bước 5: RR THEO Mã hóa trược tiếp: Thay thế các vị trí giá trị  0 và 1 bởi CÓ (Yes) và KHÔNG (No).
# ##############################################################################
# # #Thay thế vị trí giá trị 1 (Y) và 0 (N) tương ứng cột|biến legendary]
print("--------------BƯỚC 5----------------")
df['Type'] = df['Type'].map({'Fire': 'Có'})  # Chuyển True/False thành 1/0
print(df[['Name', 'Type']].head(10))
# print(df[0:10])
# # số hóa cột type1 và type2
# # Khởi tạo LabelEncoder
label_encoder = LabelEncoder()

# # Số hóa cột type1 và type2
# df['type1_encoded'] = label_encoder.fit_transform(df['type1'])
# df['type2_encoded'] = label_encoder.fit_transform(df['type2'])
# print(df)
# ##################################################################
# # # Bước 6: Xử lý loại bỏ các giá trị ngoại lệ (cá biệt): isolated
# ##################################################################
# # #kiểm tra tập dữ liệu có bất kỳ ngoại lệ nào không
print("--------------BƯỚC 6----------------")
z = np.abs(stats.zscore(df._get_numeric_data())) # Dò tìm và lấy các giá trị cá biệt trong tập dữ liệu gốc thông qua điểm z (z_score)
print('MA TRAN Z-SCORE\n')
print(z) # in ra tập (ma trận) các giá trị z-score từ tập dữ liệu gốc
df= df[(z < 3).all(axis=1)] # kiểm tra và chỉ giữ lại trong df các giá trị số liệu tưng ứng với z-score < 3  # {loại các giá trị >= 3} vì các giá trị z-score >=3 tướng ứng với số liệu quá khác biệt so với các số liệu còn lại (“cá biệt” = “ngoại lệ” = isolated}
print(df.shape) # xác định số dòng & cột dữ liệu sau khu xử lý các giá trị cá biệt
# ####################################################################
# # #Bước 7: RR hóa theo khoảng / đoạn = Chuẩn hóa (Rời rạc hóa) tập dữ liệu Input dùng ..MaxMin
# ####################################################################
print("--------------BƯỚC 7----------------")
# # Tách các cột không cần chuẩn hóa (ví dụ: cột 'name')
columns_to_exclude = ['Name', 'Type', 'Species']
columns_to_scale = [col for col in df.columns if col not in columns_to_exclude]

# Rời rạc hóa các cột số
# xác định thang đo sẽ dùng để RR hóa theo khoảng đều 
scaler = MinMaxScaler()
# Áp dụng thang đo vào data frame [df] của đề tài (đã tiền xử lý đến Bước 5)
df_scaled = pd.DataFrame(scaler.fit_transform(df[columns_to_scale]), columns=columns_to_scale, index=df.index)
# Kết hợp lại DataFrame
df = pd.concat([df[columns_to_exclude], df_scaled], axis=1)

df.iloc[4:10]
print(df)
# # # GIAI ĐOẠN 3: PHÂN TÍCH DỮ LIỆU THĂM DÒ : EDA [CƠ SỞ = HỌC CÁC MÔN data Science, AI, ML và DeepML,... ]
# # #Bước 8: Xác định mô hình trích lọc các thuộc tính đặc trưng: EDA 
# # xác định các thuộc tính đặc trưng của legendary pokemon (pokemon huyền thoại)
# # dựa trên tập dữ liệu đã được rời rạc hóa ở bước 7
print("--------------BƯỚC 8----------------")
X = df_scaled.loc[:,df_scaled.columns!='Catch rate'] # xác định tập DL Input (X) = All trừ (chú ý !=) cột DL đoán đầu ra legendary
y = df_scaled[['Catch rate']] # xác định tập DL ra legendary

selector = SelectKBest(chi2, k=5) # sd các hàm SelectKBest trong thư viện sklearn = Mô hình xác định các Thuộc tính quan trọng quyết định việc dự đoàn DL output = trích lọc Đặc trưng = Feature Extraction: k = 5 (đ/v bài này)
selector.fit(X, y) # Áp dụng mô hình trên vào SelectKBest
X_new = selector.transform(X) # Chuyên DL Input theo mô hình
print('Ma tran input sau khi ao dung chi so k Best')
print(X_new)
print('Vector output sau khi ap dung chi so K Best')
print(y)
# #########################################
print('k cot quan trong nhat quet dinh Vector Output')
print(X.columns[selector.get_support(indices=True)]) # in ds các tt đặc trưng
# #Bước 9: Xác định mô hình trích lọc các thuộc tính đặc trưng 
# # XĐ data frame = Chiếu lấy các thuộc tính đặc trưng đã xđ trong B8
df = df[['HP', 'Attack', 'Sp. Atk', 'Sp. Def', 'Speed']] # tổng chỉ số, tấn công, tấn công đặc biệt, phòng thủ đặc biệt, tốc độ

# #Bước 10: EDA theo nhu cầu thực tế => input vào các mô hình AI, ML,...
# # Đơn giản nhất là lấy 1 thuộc tính đầu vào (total) để XD Mô hình
X = df[['HP']]
y = df[['Attack']]

print('COT INPUT CAN XEM XET TINH PHU THUOC CUA OUTPUT')
print(X)
print('COT OUTPUT VECTOR KET QUA')
print(y)
# # ############CÁC KQ TRÊN SẼ INPUT VÀO CÁC  MÔ HÌNH AI & ML,...


#ĐỒ ÁN HỌC PHẦN: LẬP TRÌNH PYTHON
#SV THỰC HIỆN: NGUYỄN THÀNH ĐẠT, STT: 13, MSSV: 22110129
#TRƯỜNG: HCMUTE, KHOA: CNTT, 2024


