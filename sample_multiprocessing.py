import multiprocessing
import argparse
import time
import os

def worker(process_id):
    """
    子プロセスで実行される関数。
    ここでは簡単なメッセージを表示して少し待機します。
    """
    print(f"子プロセス {process_id} が実行されました。PID: {os.getpid()}")
    time.sleep(1)
    print(f"子プロセス {process_id} が終了しました。")
    return f"プロセス {process_id} の結果"  # 結果を返すように変更

def get_default_parallelism():
    """
    デフォルトの並列度として multiprocessing.cpu_count() を返す。
    """
    return multiprocessing.cpu_count()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="multiprocessing.Pool を利用して複数の子プロセスを実行するサンプルプログラム")
    parser.add_argument(
        "-p", "--parallelism",
        type=int,
        default=get_default_parallelism(),
        help=f"並列実行するプロセス数 (デフォルト: multiprocessing.cpu_count() = {get_default_parallelism()})"
    )
    args = parser.parse_args()

    parallelism = args.parallelism
    num_processes_to_execute = 100

    print(f"並列度: {parallelism}")
    print(f"{num_processes_to_execute} 個のタスクを処理します。")

    with multiprocessing.Pool(processes=parallelism) as pool:
        results = []
        for i in range(1, num_processes_to_execute + 1):
            result = pool.apply_async(worker, (i,))
            results.append(result)

        # 全てのタスクの完了を待機し、結果を取得
        for result in results:
            print(f"結果: {result.get()}")

    print("全てのタスクが完了しました。")
