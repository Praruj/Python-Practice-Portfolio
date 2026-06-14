 Python Practice Portfolio

<div style="margin: 20px 0;">
  <button onclick="toggleLang('en')" id="btn-en" 
    style="padding: 8px 16px; margin-right: 8px; font-weight: bold; background: #00ff9d; color: #000; border: none; border-radius: 4px; cursor: pointer;">
    🇬🇧 English
  </button>
  <button onclick="toggleLang('ja')" id="btn-ja" 
    style="padding: 8px 16px; background: transparent; color: #00ff9d; border: 1px solid #00ff9d; border-radius: 4px; cursor: pointer;">
    🇯🇵 日本語
  </button>
</div>

<div id="content-en">

**Welcome to my Python Practice Portfolio!**  
This repository showcases my journey in learning Python programming and data analysis through a variety of practical exercises and projects. It demonstrates my growing proficiency in Python core concepts, data structures, JSON handling, and algorithm problem-solving.

## About Me
I am an aspiring Software Developer and Python/Data Analyst enthusiast eager to learn and grow. This portfolio reflects my commitment to mastering programming fundamentals and applying them to real-world problems.

## Key Skills Demonstrated
- Python basics: data types, variables, control flow
- Data structures: lists, dictionaries, sets
- JSON handling with `json.dumps()` and `json.loads()`
- Regular Expressions and API with `FastAPI()`

## How to Use
1. Clone the repository:
   ```bash
   git clone https://github.com/Praruj/Python-Practice-Portfolio.git
   cd Python-Practice-Portfolio
   ```
2. Create a virtual environment:
   ```bash
   python -m venv .venv
   ```
3. Activate the virtual environment:

   **Windows**
   ```bash
   .venv\Scripts\activate
   ```

   **macOS / Linux**
   ```bash
   source .venv/bin/activate
   ```
4. Install dependencies (if `requirements.txt` exists):
   ```bash
   pip install -r requirements.txt
   ```
5. Launch Jupyter Notebook:
   ```bash
   jupyter notebook
   ```
6. Open the notebooks to explore and run the exercises.

## Future Plans
- Expand coverage of advanced Python topics
- Add more real-world Python projects
- Improve documentation and explanations
- Include structured learning paths

---

Thank you for visiting my portfolio! Feel free to reach out if you'd like to collaborate or discuss Python programming.

[Visit my GitHub Profile](https://github.com/Praruj)
</div>

<!-- Japanese Version -->
<div id="content-ja" style="display: none;">

**Python練習ポートフォリオへようこそ！**  
このリポジトリは、Pythonプログラミングとデータ分析を学ぶためのさまざまな実践演習とプロジェクトを集めたものです。Pythonの基礎概念、データ構造、JSON処理、アルゴリズム問題解決などのスキルを着実に向上させている過程を示しています。

## 自己紹介
私はソフトウェア開発者を目指すPython/データアナリスト愛好家です。このポートフォリオは、プログラミングの基礎を習得し、実世界の問題に応用することへの私の取り組みを示しています。

## 習得した主なスキル
- Python基礎：データ型、変数、制御構文
- データ構造：リスト、辞書、セット
- JSON処理（`json.dumps()` / `json.loads()`）
- 正規表現と `FastAPI()` を使ったAPI開発

## 使い方
1. リポジトリをクローン：
   ```bash
   git clone https://github.com/Praruj/Python-Practice-Portfolio.git
   cd Python-Practice-Portfolio
   ```
2. 仮想環境を作成：
   ```bash
   python -m venv .venv
   ```
3. 仮想環境を有効化：

   **Windows**
   ```bash
   .venv\Scripts\activate
   ```

   **macOS / Linux**
   ```bash
   source .venv/bin/activate
   ```
4. 依存関係をインストール：
   ```bash
   pip install -r requirements.txt
   ```
5. Jupyter Notebookを起動：
   ```bash
   jupyter notebook
   ```
6. ノートブックを開いて演習を実行してください。

## 今後の予定
- 高度なPythonトピックの拡張
- より実践的なPythonプロジェクトの追加
- ドキュメントと説明の改善
- 体系的な学習パスの作成

---

ポートフォリオをご覧いただきありがとうございます！  
協力やPythonに関する議論を希望される場合はお気軽にご連絡ください。

[GitHubプロフィールを見る](https://github.com/Praruj)
</div>

<script>
function toggleLang(lang) {
  const en = document.getElementById('content-en');
  const ja = document.getElementById('content-ja');
  const btnEn = document.getElementById('btn-en');
  const btnJa = document.getElementById('btn-ja');

  if (lang === 'en') {
    en.style.display = 'block';
    ja.style.display = 'none';
    btnEn.style.fontWeight = 'bold';
    btnJa.style.fontWeight = 'normal';
  } else {
    en.style.display = 'none';
    ja.style.display = 'block';
    btnEn.style.fontWeight = 'normal';
    btnJa.style.fontWeight = 'bold';
  }
}

// Default to English
toggleLang('en');
</script>
