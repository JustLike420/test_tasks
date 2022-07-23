def task(array):
    for i, a in enumerate(array):
        if a == '0':
            return i


def main():
    print(task('111111111110000000000000000'))  # 11
    print(task('111111111111111111111111100000000'))  # 25


if __name__ == '__main__':
    main()
