#密碼重試程式

#先在程式碼中 設定好密碼 password = 'a123456'
#讓使用者重複最多輸入3次
#不對的話，印出"密碼錯誤! 還有幾次機會
#對的話，就印出"登入成功"

password = 'a123456'
i = 3 #剩餘機會
while True:
	pwd = input('請輸入密碼')#設使用者的密碼變數為pwd
	if pwd == password:#如果 pwd是密碼就登入成功
		print('登入成功')
		break#也逃出迴圈
	else:#反之 錯的話 i 要減少
		i = i - 1 
		print('密碼錯誤!還有', i ,'機會')
		if i == 0: #剩餘次數=0，
		 break#就跳出迴圈