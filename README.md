# Python によるプロセスベースの並列化のサンプルコード

## メソッドを並列実行する場合

### Usage

```bash
python sample_multiprocessing.py [-p <# of parallelism>]
```

実行すると 1 秒待つサブプロセスを 100 個作成します。

`p` オプションで並列度を指定できます。
デフォルトは OS から見える CPU の個数です。

## 外部ファイルから読み込んだコマンドを並列実行する場合

### Usage

```bash
python sample_exec_commandlist_in_parallel.py [-p <# of parallelism>]
```

実行すると `commands.txt` に記述されたコマンド列を並列に実行します。
`commands.txt` には `sleep 1` が 100 行書かれています。

`p` オプションで並列度を指定できます。
デフォルトは OS から見える CPU の個数です。
