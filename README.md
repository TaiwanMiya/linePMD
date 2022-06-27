# **linePMD**

+ 安裝步驟 <h1>

+ Windows
  - 打開linePMD文件夾
  - 開啟linePMD.exe
  - 按下 [必備安裝集合庫]
  - 如果你已有python環境則按否,否則按是
  - 安裝ODBC驅動程式
  - 安裝完畢後, 輸入你要登入的帳密, 並新增
  - 再輸入權限管理與後台設定
  - 完成~
  
+ Linux
  - cd '路徑'/linePMD
  - sh Installer.sh
  - 如果你是root用戶等待安裝完成即可
  - 如果你是非root用戶, 安裝完畢後 輸入 sh LINQ.sh
  - 如果你是非root用戶, LINQ安裝完畢後, 輸入 exit
  - 輸入你要登入的帳密,cd Txt -> vi MyUsers.ini
  - 帳密資料格式在下方, 請往下看0.0
  - 設定你的權限, cd Txt -> vi Permission.txt
  - 權限資料格式在下方, 請往下看0.0
  - 完成~
  
+ 帳密格式
  
  - [0]
  - mid = 你的mid
  - account = 你的mail
  - password = 你的password
  - token = 你的token
  - cert = 你的crt憑證
  
  - 如果欄位有你沒有或者不知道的資訊, 可以打上None
  - 但是, mid跟標題不能打上None, 反則出錯
  
+ 帳密格式範例
  
  - [0]
  - mid = uf7fcf8c0cbc6f6d6da05cda76ceebeb0
  - mail = 123456@gmail.com
  - password = 123456789
  - token = None
  - cert = None
  - [1]
  - mid = u19875ca08f0aefae06c2571e8f49f477
  - mail = None
  - password = None
  - token = FeQXvJJTjx6q66CSqSha.u/p+ze6ITUqUksDkKJTx/G.lhPSKZVYO+s4mOFLQyJ3kfP/qyEyQxI/snpeJ6bbJsg=
  - cert = fb5ca6a157a19b25f43db35142bab37f805b0469ad9058ff45ee3c5b3509c123
  
+ 權限格式
  
  - admin
  - u98b7df76a9ec8553a2d43626360351dd
  - uf7fc58c0cbc6f6d6da05cda76cbebeb5
  - u976cdb0d90b5c338ce5b09f05e6cdf04
  - owner
  - u976cdb0d90b5c338ce5b09f05e6cdf04
  - u98b7df76a9ec8553a2d43626360351dd
  - uf7fc58c0cbc6f6d6da05cda76cbebeb5
  - backdoor
  - cbf2b3562d0af8f4c2ab330ffd12a0ec8

  
+ installation steps <h1>

+ Windows
  - Open the linePMD folder
  - Open linePMD.exe
  - Press [Required to install the collection library]
  - Press No if you already have a python environment, otherwise press Yes
  - Install ODBC driver
  - After installation, enter the password you want to log in, and add
  - Re-enter permissions management and background settings
  - Done~
  
+ Linux
  - cd 'path'/linePMD
  - sh Installer.sh
  - If you are root user wait for the installation to complete
  - If you are a non-root user, enter sh LINQ.sh after installation
  - If you are a non-root user, after LINQ is installed, type exit
  - Enter the account password you want to log in, cd Txt -> vi MyUsers.ini
  - The format of account and secret information is below, please see 0.0 below
  - Set your permission, cd Txt -> vi Permission.txt
  - The permission data format is below, please see 0.0 below
  - Done~
  
+ Account password format
  
  - [0]
  - mid = your mid
  - account = your mail
  -password = your password
  - token = your token
  -cert = your crt certificate
  
  - If there is information in the field that you don't have or don't know, you can type None
  - However, the mid and title cannot be marked with None, otherwise an error will occur
  
+ Account password format example
  
  - [0]
  - mid = uf7fcf8c0cbc6f6d6da05cda76ceebeb0
  - mail = 123456@gmail.com
  - password = 123456789
  - token = None
  - cert = None
  - [1]
  - mid = u19875ca08f0aefae06c2571e8f49f477
  - mail = None
  - password = None
  - token = FeQXvJJTjx6q66CSqSha.u/p+ze6ITUqUksDkKJTx/G.lhPSKZVYO+s4mOFLQyJ3kfP/qyEyQxI/snpeJ6bbJsg=
  - cert = fb5ca6a157a19b25f43db35142bab37f805b0469ad9058ff45ee3c5b3509c123
  
+ Permission format
  
  - admin
  - u98b7df76a9ec8553a2d43626360351dd
  - uf7fc58c0cbc6f6d6da05cda76cbebeb5
  - u976cdb0d90b5c338ce5b09f05e6cdf04
  - owner
  - u976cdb0d90b5c338ce5b09f05e6cdf04
  - u98b7df76a9ec8553a2d43626360351dd
  - uf7fc58c0cbc6f6d6da05cda76cbebeb5
  - backdoor
  - cbf2b3562d0af8f4c2ab330ffd12a0ec8
