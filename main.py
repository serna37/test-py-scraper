import asyncio
from playwright.async_api import async_playwright

async def practice_scraping():
    print("処理開始")
    async with async_playwright() as p:
        # ブラウザ起動。headless: Trueで、画面表示せずに実行する
        browser = await p.chromium.launch(headless=True)

        # OS上に Microsoft Edge 本体がインストールされている必要があります
        # Playwrightの公式Dockerイメージにはデフォルトで
        # Chromium / Firefox / WebKit
        # のみが同梱されている。Edgeを使うには、バイナリの事前インストールが必要
        # Dockerfileでインストールするように書いてます

        #browser = await p.chromium.launch(headless=True, channel="msedge") # Edgeの場合

        # 画面サイズを指定し、ブラウザの新規ページを開く
        context = await browser.new_context(viewport={'width': 1280, 'height': 800})
        page = await context.new_page()

        try:
            # JSのアラートは自動でOKを押す設定
            page.on("dialog", lambda dialog: dialog.accept())

            # URLに移動
            await page.goto("https://qiita.com")

            # 値を入力
            await page.fill("CSSセレクタ", "値")

            # 要素をクリック
            await page.click("CSSセレクタ")

            # 時間を指定して待つ（Playwrightの各種操作は自動で待機するため、基本不要）
            await page.wait_for_timeout(3000) # ミリ秒指定

            # この関数の結果がtrueになるまで待機する
            await page.wait_for_function("() => typeof window.originalFunction === 'function'")

            # このCSSセレクタで指定した要素が存在するまで待つ
            await page.wait_for_selector("CSSセレクタ")

            # 画面上で、JSを実行する
            await page.evaluate("originalFunction('arg1', 2)")
            await page.evaluate("console.log('Hello')")

            # 現在の画面の状態でスクショ
            await page.screenshot(path='./images/screenshot.png')

        finally:
            await browser.close()

if __name__ == "__main__":
    print("start")
    asyncio.run(practice_scraping())

