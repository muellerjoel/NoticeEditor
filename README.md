# Clone git of NoticeEditor

git clone https://github.com/muellerjoel/noticeeditor.git

# Go in Folder of NoticeEditor

cd NoticeEditor

# Download -> Install python3 (Windows Installer 64bit)

https://www.python.org/ftp/python/3.12.3/python-3.12.3-amd64.exe

# Install of virtualenv requirements

pip install virtualenv

# Install of virtualenv

python -m venv .venv

# Activation of virtualenv 1. Windows 1.1 CMD 1.2 Powershell

.venv/Scripts/activate.bat 
.venv/Scripts/Activate.ps1 


# Install of NoticeEditor requirements

pip install -r requirements.txt

# Execute

python main.py
