## ホストPCに用意するもの
- Docker

## とにかく起動
```sh
IMAGE_NAME=scraper-sample
CONTAINER_NAME=scrap-container
VERSION=v0.0.1
docker stop $(docker ps -aq -f name=$CONTAINER_NAME)
docker rm $(docker ps -aq -f name=$CONTAINER_NAME)
docker build -t $IMAGE_NAME:$VERSION .
docker run --name $CONTAINER_NAME -d -v "./images:/workspace/images" $IMAGE_NAME:$VERSION

docker logs $CONTAINER_NAME
docker exec -it $CONTAINER_NAME sh
```

## イメージをビルド
```sh
# dokcer build -t {イメージ名}:{バージョン名} {Dockerfileへのパス}
docker build -t scraper-test:v0.0.1 .
docker build -t scraper-test:latest .
docker build -t scraper-sample:v0.0.1 .
# など
```

## コンテナ起動
```sh
# -d デタッチ（バックグラウンド）起動
# -p ホスト側のポート:コンテナ側のポート
# -v マウント。バインドマウントだとホスト-コンテナ間でフォルダを共有するイメージ
docker run \
    --name コンテナ名 \
    -d \
    -p 8080:8080 \
    -v "$(pwd)/../ホストのフォルダ:/asset/コンテナ内のフォルダ" \
    イメージ名:タグ名
docker run --name scrap-container -d -v "../images:/workspace" scraper-test:v0.0.1
```


## 確認や削除
```sh
# イメージ一覧
docker images

# 起動中のコンテナ一覧
docker ps -a

# 起動中のコンテナの中のshellに入る
docker exec -it {コンテナ名} sh

# コンテナを停止
docker stop {コンテナID}

# コンテナ名指定でコンテナ停止
docker stop $(docker ps -aq -f name=コンテナ名)

# コンテナを削除
docker rm {id1} {id2} ...

# コンテナ名指定でコンテナ削除
docker rm $(docker ps -aq -f name=NAME)

# イメージを削除
docker rmi {id1} {id2} ...
```

