import multiprocessing
import argparse
import subprocess
import time
import os

COMMANDS_FILE = "commands.txt"

def worker(command):
    """
    与えられたコマンドを実行する。
    """
    try:
        print(f"子プロセス (PID: {os.getpid()}) がコマンドを実行します: {command}")
        subprocess.run(command, shell=True, check=True)
        print(f"子プロセス (PID: {os.getpid()}) がコマンドの実行を完了しました: {command}")
        return f"コマンド '{command}' の実行が完了しました。"
    except subprocess.CalledProcessError as e:
        return f"エラー: コマンド '{command}' の実行に失敗しました (終了コード: {e.returncode})"
    except Exception as e:
        return f"予期しないエラーが発生しました: {e}"

def get_default_parallelism():
    """
    デフォルトの並列度として multiprocessing.cpu_count() を返す。
    """
    return multiprocessing.cpu_count()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=f"{COMMANDS_FILE} に記述されたコマンドを multiprocessing.Pool を利用して並列実行するサンプルプログラム")
    parser.add_argument(
        "-p", "--parallelism",
        type=int,
        default=get_default_parallelism(),
        help=f"並列実行するプロセス数 (デフォルト: multiprocessing.cpu_count() = {get_default_parallelism()})"
    )
    args = parser.parse_args()

    parallelism = args.parallelism

    try:
        with open(COMMANDS_FILE, "r") as f:
            commands = [line.strip() for line in f.readlines()]
    except FileNotFoundError:
        print(f"エラー: ファイル {COMMANDS_FILE} が見つかりません。")
        exit(1)

    num_commands = len(commands)
    print(f"並列度: {parallelism}")
    print(f"{num_commands} 個のコマンドを実行します。")

    start_time = time.time()
    with multiprocessing.Pool(processes=parallelism) as pool:
        results = pool.map(worker, commands)

        # 全てのタスクの結果を表示
        for result in results:
            print(result)

    end_time = time.time()
    print(f"全てのコマンドの実行が完了しました (実行時間: {end_time - start_time:.2f} 秒)。")
