import gspread
from google.oauth2.service_account import Credentials
import streamlit as st
import pandas as pd
import os

# XÁC THỰC TRUY CẬP VÀO GOOGLE SHEET
# Đường dẫn đến tệp credentials.json
credentials_path = "C:\\Users\\thong\\Downloads\\vnw.data\\datavnwealth-25a353ea3781.json"

# Phạm vi truy cập của Google Sheets
scope = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']

# Thông tin xác thực API
credentials = Credentials.from_service_account_file(credentials_path, scopes=scope)

# Kết nối đến Google Sheets
client = gspread.authorize(credentials)

import streamlit as st


# XÁC THỰC TRUY CẬP VÀO GOOGLE SHEET
# Đường dẫn đến tệp credentials.json
credentials_path = "C:\\Users\\thong\\Downloads\\vnw.data\\datavnwealth-25a353ea3781.json"

# Thiết lập xác thực và kết nối với Google Sheets
scope = ["https://spreadsheets.google.com/feeds", 
         "https://www.googleapis.com/auth/spreadsheets", 
         "https://www.googleapis.com/auth/drive.file", 
         "https://www.googleapis.com/auth/drive"]

# Thông tin xác thực API
credentials = Credentials.from_service_account_file(credentials_path, scopes=scope)

# Kết nối đến Google Sheets
client = gspread.authorize(credentials)

# Mở Google Sheets bằng URL hoặc tên
sheet = client.open("suggestion_table").sheet1

# Lấy tất cả dữ liệu từ sheet
data = sheet.get_all_records()
df = pd.DataFrame(data)

# Hiển thị dữ liệu trên Streamlit
st.title("Google Sheets Data in Streamlit")
st.write(df)