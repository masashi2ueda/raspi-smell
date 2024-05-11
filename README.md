# raspi-smell

## 背景
- 鼻が悪いので赤ちゃんのうんちにきづけない...  
- ラズパイでうんちをけんちできるのではないか？  
    →ラズパイ+臭気センサを使ってみる


## 用意するもの
- [Raspberry Pi Zero WH](https://akizukidenshi.com/catalog/g/g112958/)
- [ADRSZOD ゼロワン 臭気センサ拡張基板](https://bit-trade-one.co.jp/adrszod/)
- sandiskのSDカード
- ラズパイ用の電源


## ラズパイの設定
1. [こちら](https://www.raspberrypi.com/software/)よりimagerを取得
1. "CHOOSE DEVICE"で"RASPBERRY PI ZERO"を選択
1. osは"RASPBERRY PI OS(32-BIT)"を選択
1. "would you like to apply OS customization settings?"と出るのでやっておく
    1. 一般: ホスト名やwifi設定をあらかじめやっておく(ホスト名はsmellpiにする) 
        ＊5Ghzのwifiは最初に設定しても使えないので注意(詳細は[こちら](https://qiita.com/ymktmk/items/424a34191585db25bdab))
    1. サービス: sshを有効化しておく
1. 書き込みを実行→結構時間かかる
1. sdをラズパイにさす+電源もさす→ラズパイのライトが光る
1. sshで接続する
1. sudo raspi-configコマンドを打って、
    1. 「3.Interface Options」>「P5 I2C」> 「はい」 > 「了解」　> 「Finish」
        * SPIは上記のI2CをSPIにする
1. pip install --break-system-packages flask flask-cors
1. sudo apt-get update
1. sudo apt-get install -y nodejs npm
1. sudo npm cache clean
1. sudo npm install npm n -g
1. sudo n stable
1. git clone https://github.com/masashi2ueda/raspi-smell.git
1. cd frontend
1. npm install
1. npm run build
1. cd ../backend
1. nohup python app.py
1. スマホでbedpi:5053にアクセス

## 参考
- [ADRSZOD-臭気センサ拡張基板](https://github.com/bit-trade-one/RasPi-Zero-One-Series/tree/master/5th/ADRSZOD_Odd_Sensor)
- [Raspberry Pi 4BでI2C、SPIを使用する際の覚書](https://qiita.com/airpocket/items/c0bb5bfdcc5a2c4ec19b)
- [Raspberry Pi 4 5GHzのWi-Fiに接続する](https://qiita.com/ymktmk/items/424a34191585db25bdab)
- [Raspberry Pi OSでもbookwormでpipインストールエラー「externally-managed-environment」](https://raspida.com/pip-error-pep668/)
- [Raspberry PiにNode.jsとnpmの最新版をインストールする](https://qiita.com/mascii/items/77c685df65c4cbca9315)