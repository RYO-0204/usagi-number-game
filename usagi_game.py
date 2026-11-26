import random

MIN_NUMBER = 1
MAX_NUMBER = 100


def show_title():
    """タイトルと遊び方を表示する。"""
    line = "━" * 28
    print(line)
    print("🐰 うさぎの数当てゲーム 🥕")
    print(line)
    print("1〜100の数字を当ててね！")
    print()


def read_guess():
    """1〜100の整数を受け取る。不正な入力のときは None を返す。"""
    text = input("🐰 予想した数字を入れてね > ").strip()

    if not text.isdigit():
        return None

    number = int(text)
    if number < MIN_NUMBER or number > MAX_NUMBER:
        return None

    return number


def main():
    answer = random.randint(MIN_NUMBER, MAX_NUMBER)
    count = 0

    show_title()

    while True:
        guess = read_guess()

        if guess is None:
            print("🐰 1〜100の数字を入れてね")
            continue

        count += 1

        if guess < answer:
            print("⬆️ もっと大きいよ！")
        elif guess > answer:
            print("⬇️ もっと小さいよ！")
        else:
            print(f"🎉 大正解！ {count}回で当てたよ！")
            break


main()
