import requests
import os
import subprocess

url = "https://www.apachefriends.org/xampp-files/7.4.33/xampp-windows-x64-7.4.33-0-VC15-installer.exe"
r = requests.get(url, stream=True)
with open("xampp_installer.exe", "wb") as f:
    for chunk in r.iter_content(chunk_size=8192):
        f.write(chunk)

if os.path.exists("C:\\xampp"):
    print("O XAMPP já tá instalado")
else:
  subprocess.run(["xampp_installer.exe", "/S"]) # O '/S' é pra fazer uma instalação silenciosa.

subprocess.run("git", "clone", "https:\\link-do-repositório")
subprocess.run([
    "C:\\xampp\\mysql\\bin\\mysql.exe",
    "-u", "root",
    "-e", "CREATE DATABASE IF NOT EXISTS mvc_biblioteca; USE mvc_biblioteca; SOURCE C:\\xampp\\htdocs\\mvc-biblioteca\\mvc-biblioteca.sql"
])

