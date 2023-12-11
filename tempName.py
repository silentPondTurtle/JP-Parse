

hira_start = int("3041", 16)
hira_end = int("3096", 16)
kata_start = int("30a1", 16)

kata_to_hira = dict()
for i in range(hira_start, hira_end + 1):
    kata_to_hira[chr(i - hira_start + kata_start)] = chr(i)

hira_to_kata = dict()
for i in range(hira_start, hira_end + 1):
    hira_to_kata[chr(i)] = chr(i - hira_start + kata_start)


def kata2hira(s):
    return "".join([kata_to_hira[c] for c in s])


if __name__ == "__main__":
    print(hira_to_kata["あ"])
    print(kata_to_hira["ア"])

    print(kata2hira("リンゴ"))
