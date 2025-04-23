# Python によるプロセスベースの並列化のサンプルコード

## Usage

```bash
python sample_multiprocessing.py [-p <# of parallelism>]
```

実行すると 1 秒待つサブプロセスを 100 個作成します。

`p` オプションで並列度を指定できます。
デフォルトは OS から見える CPU の個数です。

