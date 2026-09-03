FROM mcr.microsoft.com/playwright/python:v1.49.0-noble

# ワークディレクトの設定
WORKDIR /workspace

# pipの更新とrequirements.txtのインストール
COPY requirements.txt /tmp/pip-tmp/
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r /tmp/pip-tmp/requirements.txt \
    && rm -rf /tmp/pip-tmp

# Edgeを使用する場合、以下を追加してEdge本体をインストール
RUN npx playwright install msedge
