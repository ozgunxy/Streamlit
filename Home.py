# main.py
import streamlit as st
import pyodbc
import pandas as pd
import matplotlib.pyplot as plt

# MS SQL Server bağlantı bilgileri
server = 'DESKTOP-D3NN4GU\SQLEXPRESS'
database = 'streamlit_db'
trusted_connection = 'yes'  # Bu, Windows Authentication kullanılacağını belirtir

# Bağlantı dizesi oluştur
connection_string = f'DRIVER=SQL Server;SERVER={server};DATABASE={database};Trusted_Connection={trusted_connection}'

# MS SQL Server bağlantısını kur
conn = pyodbc.connect(connection_string)
cursor = conn.cursor()

# Streamlit uygulama başlat
def main():
# main.py

# main.py



    # main.py

# main.py




    st.sidebar.title("Yan Menü")

    if st.sidebar.button("Ana Sayfa"):
        show_home_page()
    if st.sidebar.button("Duygu Durum Analizi"):
        show_new_page()
    if st.sidebar.button("Veritabanı"):
        show_page_3()
    if st.sidebar.button("gfsdgdfgd"):
        show_page_4()
    if st.sidebar.button("Çıkış yap"):
        show_page_5()

def show_home_page():
    st.title("Ana Sayfa")
    
    # Kullanıcı adı ve şifre girişi için text input alanları
    username = st.text_input("Kullanıcı Adı")
    password = st.text_input("Şifre", type="password")

    # Giriş ve İptal butonları
    if st.button("Giriş"):
        # Kullanıcı giriş işlemleri burada gerçekleştirilebilir
        if authenticate_user(username, password):
            st.success("Başarıyla giriş yaptınız.")
           
            # Veritabanından verileri çekmek ve diğer işlemleri burada gerçekleştirin
        else:
            st.error("Geçersiz kullanıcı adı veya şifre. Lütfen tekrar deneyin.")

    if st.button("İptal"):
        st.warning("İptal edildi.")

# Kullanıcıyı doğrula
def authenticate_user(username, password):
    query = f"SELECT * FROM users WHERE UserName1='{username}' AND UserPW='{password}'"
    result = cursor.execute(query).fetchone()
def show_new_page():
    st.title("Yeni Sayfa")
    st.write("Bu yeni sayfa içeriğidir.")

def show_page_3():
    st.title("Verileriniz")
    '---'
   







# main.py

import streamlit as st
import pyodbc
import pandas as pd

server = 'DESKTOP-D3NN4GU\SQLEXPRESS'
database = 'streamlit_db'
trusted_connection = 'yes'  # Bu, Windows Authentication kullanılacağını belirtir

# Bağlantı dizesi oluştur
connection_string = f'DRIVER=SQL Server;SERVER={server};DATABASE={database};Trusted_Connection={trusted_connection}'

# MS SQL Server bağlantısını kur
conn = pyodbc.connect(connection_string)
cursor = conn.cursor()

# SQL sorgusu ile verileri çek
sql_query = sql_query = 'SELECT duygular.Duygular, Duygular_Oranlar.Oran,Duygular_Oranlar.DuyguID FROM Duygular_Oranlar INNER JOIN duygular ON duygular.DuyguID = Duygular_Oranlar.DuyguID;'

# Tablo adını ve sorguyu kendi veritabanınıza uygun şekilde değiştirin
df = pd.read_sql(sql_query, conn)

# Varsayılan indeksi olan sütunları kaldır
df = df.set_index("DuyguID")

# Varsayılan indeksi olan sütunları kaldır
df = df.reset_index(drop=True)




# Veri çerçevesini göster
st.write("Çekilen Veriler:")
st.dataframe(df)

st.bar_chart(df.set_index("Duygular")[["Oran"]])


# Veritabanı bağlantısını kapat
conn.close()












def show_page_4():
    st.title("Sayfa 4")
 
st.components.v1.html(
        """
        <iframe srcdoc='<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>Camera Access</title></head><body><h1>Camera Access</h1><video id="camera" width="640" height="480" autoplay></video><script>document.addEventListener("DOMContentLoaded", function() {const video = document.getElementById("camera");navigator.mediaDevices.getUserMedia({ video: true }).then(function (stream) {video.srcObject = stream;}).catch(function (error) {console.error("Error accessing camera:", error);});});</script></body></html>' width="700" height="500"></iframe>
        """,
        height=550,
    )




def show_page_5():
    st.title("Sayfa 5")
    st.write("Bu 5. sayfa içeriğidir.")


  


 

    
    return result is not None

if __name__ == "__main__":
    main()
