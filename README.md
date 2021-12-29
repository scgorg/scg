# scg

Send Your Custom Gmail with Python

## 第一步

開啟 Google 低安全性 https://myaccount.google.com/lesssecureapps
![](https://i.imgur.com/nN5MqgO.png)


## 第二步

在 `config.py` 輸入你的帳號密碼

## 第三步

在 `send_mail.py` 修改你要使用的 csv 檔案

## 第四步

在 `helper.py` 修改你所要寄信的內容，如果需要使用 html 可以在 HackMD 打完內容後，使用下載成 **純HTML**。

![](https://i.imgur.com/DPtOJOS.png)

把內容複製貼上 `get_mail_content` 函數中。

## 第五步

```python
python3 send_mail.py
```
