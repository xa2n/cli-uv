# src/cli_uv/main.py

# module_1からfoo関数をインポート
from cli_uv.utils.module_1 import foo


def main():
    # foo関数を呼び出し
    message = foo()
    print(message)


if __name__ == "__main__":
    main()
