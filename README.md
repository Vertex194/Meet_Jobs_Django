### 版本號
-	git --version

### 設定全域變數
-	git config  --global user.name eric
-	git config  --global user.email eric@lungmei.com.tw

### 目前設定值
-	git config --list

### 初始倉庫(回溯功能)
-	git init

### 加入檔案至暫存區
-	git add<filename>

### 檢視所有的狀態
- 	git status 

### 查看Object內容
-	git cat-file  -s sha1
	-s  (size)
	-p (內容)
	-t  (型態)

### 查看暫存區控管的檔案
-	git ls-files
-	git ls-files -s
	    -查看完整資訊

### 修改後 A==>M (M==>D)
-	git add <filename>
		  -確認修改(刪除)
-	git restore <filename>
		  -反悔修改		

### 儲存至倉庫區(-a代表新增 -m修改)；Message內容不多
-	git commit -am "Message" 

### 儲存至倉庫區(-a代表新增 -m修改)；Message內容很多；進入vim模式
-	git commit 
						esc➔切換normal/insert
						:w  ➔代表寫入= 儲存
						:q  ➔代表離開程式
						:!   ➔代表強制執行
						:q! ➔回到上一個動作
						i    ➔insert
						a   ➔append
						o   ➔new line

### 將檔案一併移至暫存區
-	git add. 

### 檢視commit的完整紀錄
-	git log 

### 檢視commit的單行完整記錄
-	git log --oneline

### 修改最後一次的commit
-	git commit --amend

### 手動刪除(暫存區/倉庫區)(紅字)
-	git restore <filename>
		  -恢復
-	git add <filename>
		  - 確認(綠字)
		  - git restore --staged<filename>
								-恢復到手動刪除狀態(變回紅字)

### 倉庫區的刪除
- 手動同上
- git rm
		- git commit
		- git restore --staged<filename>
				-恢復到刪除狀態(變回紅字)
							-	git restore <filename>
									  -恢復
							-	git add <filename>
									  - 確認(綠字

### 暫存/倉庫移到工作區
- git rm --cachen <filename>

### 檢視目前分支
- git branch
		 - 產生新分支
		 - git branch <branch-name>
		 - 切換分支
		 - git check out <branch-name>

			