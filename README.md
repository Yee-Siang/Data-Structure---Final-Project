# Data-Structure---Final-Project
A simplified social network for meeting, coupling, and making friends

## 介面操作 (前台)
在一開始，我們會提供兩個選擇給用戶: 登入 or 註冊
### 註冊
使用者選擇註冊，我們會提供填寫資訊欄位，其中'name'僅能輸入英文，不能超過十個字母，'age'僅能輸入不超過三位數的數字，
gender要讓使使用者填入自己的性別，interest是選擇自己興趣的欄位，注意一定要勾選三項(如果勾選一項不甚喜歡，可以再按一次即取消該項)。
除此之外，註冊者要填入自己理想對象的性別和年齡，以便配對對象的篩選。以上這些選填一項之後都要按enter才能操作下一項。
全部確定好後，會浮出"Sign Up"按鈕以供選填，為進去的資料會產出一個user，顯示新的在id在介面中，以後id是作為登入的重要數字，必須謹記。
使用者按下'pair'後就會關掉初始介面，進行匈牙利演算法的配對得到一個獲取之對象後可以進行互動

### 登入
給過去註冊過帳戶的用戶，輸入id後一樣可以再次進行配對

### 遊戲
進入遊戲介面之後可以使用wasd來操控人物走迷宮，按下e可以發射箭，透過移動滑鼠可以改變發射的方向，請注意人與箭都不會穿牆，要接近對方才能互相攻擊。

## 資料蒐集與整理 (後台)
在後台架設好後，首先要做的事情是:載入過去的使用者資料。因此，我們需要先進行reload動作，將過去使用者的資訊從 storage.json 中抓取下來。
抓取後重新把用戶id大小排到binary tree裡(也寫好了avl tree的實作)，當用戶登入時，就從tree中做search即可獲取該用戶之資料

## 時間複雜度作圖
Open Directory -> Time Analysis
#### AVL Tree  
By typing the command python avltree_analysis.py
#### Binary Tree 
By typing the command python btree_analysis.py
