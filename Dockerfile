# このイメージ内にchroniumが含まれるので
# playwrightのライブラリのバージョンと合わせる必要がある(requirements.txt)
FROM mcr.microsoft.com/playwright/python:v1.49.0-noble

# ワークディレクトの設定
WORKDIR /workspace

# pipの更新とrequirements.txtのインストール
COPY requirements.txt /tmp/pip-tmp/
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r /tmp/pip-tmp/requirements.txt \
    && rm -rf /tmp/pip-tmp

# プログラムファイルをコピー
COPY main.py /workspace

# 画像置くフォルダを作る
RUN mkdir -p /workspace/images

# Edgeを使用する場合、以下を追加してEdge本体をインストール
# RUN npx playwright install msedge

# コンテナ起動時に main.py を実行し、完了後に常駐させる
CMD ["sh", "-c", "python main.py && tail -f /dev/null"]

