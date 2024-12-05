df = df.drop("number", axis = 1) #drop cột number vì không có giá trị phân tích
# print(df.isna().sum() / len(df) * 100) #kiểm tra phần trăm giá trị null