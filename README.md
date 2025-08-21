# 4Gamers 每日任務自動化腳本

這是一個使用 Python 和 Selenium 開發的網頁自動化腳本，用於自動執行 4Gamers 網站上的每日簽到與互動任務。

## 功能

此腳本透過模擬使用者操作，自動登入 4Gamers 網站並執行以下任務：

- **每日轉蛋** (`gacha.Gacha`)
- **參與投票** (`vote.vote`)
- **領取獎勵** (`zgetMoney.earnMoney`)

此外，專案中還包含了以下可擴充的功能模組（在 `zMain.py` 中預設為註解狀態）：

- **匿名聊天室互動**:
    - 自動發文 (`ztalkPost`)
    - 自動留言 (`ztalkComments`)
    - 斗內 (`zTalkDonate`)
- **大賢者專區互動**:
    - 瀏覽與按讚 (`zBigMasterbrowse`)
    - 留言 (`zBigMasterComments`)
- **新聞留言** (`znewsComments`)

## 專案結構

- `zMain.py`: 主執行檔，負責初始化 Selenium WebDriver、登入網站並依序呼叫各個任務模組。
- `chromedriver.exe`: Chrome 瀏覽器的 WebDriver。
- **任務模組** (位於 `4gamerScript/`):
    - `Gacha.py`
    - `Vote.py`
    - `getMoney.py`
    - `talkPost.py`
    - `talkComments.py`
    - `TalkDonate.py`
    - `BigMasterbrowse.py`
    - `BigMasterComments.py`
    - `newsComments.py`

## 如何使用

1.  **環境設定**:
    - 確認已安裝 Python。
    - 安裝 Selenium 套件: `pip install selenium`
2.  **登入資訊**:
    - 此腳本設計為透過 Facebook 登入。首次執行前，可能需要手動處理登入流程以儲存 cookies (`cookies.pkl`)，或在程式碼中設定帳號密碼。
3.  **執行**:
    - 執行主腳本 `zMain.py` 來啟動自動化流程。

**注意**: 網頁結構時常變動，若腳本無法正常運作，可能需要更新 Selenium 的元素定位器 (Selectors)。

