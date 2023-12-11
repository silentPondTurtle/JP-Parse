from collections import deque
import re
from fugashi import Tagger

from tempName import kata2hira

kanji_uni = r'[㐀-䶵一-鿋豈-頻]'
ascii_char = r'[ -~]'

tagger = Tagger('-Owakati')

def extract_unicode_block(unicode_block, s):
    return re.findall(unicode_block, s)


def remove_unicode_block(unicode_block, s):
    return re.sub(unicode_block, "", s)


class Parser:
    def __init__(self):
        pass

    def clean(self, s1, s2):
        # something like "食べる", "たべる" would return an incorrect result
        # print("clean", "\t", s1)
        if s1.isnumeric():
            return s1 + "[" + s2 + "]"

        if len(extract_unicode_block(kanji_uni, s1)) == 0:
            return s2

        if len(extract_unicode_block(kanji_uni, s1)) == len(s1):
            return s1 + "[" + s2 + "]"

        i = 0

        res = ""

        s1 = deque(list(s1))
        s2 = deque(list(s2))
        while s1 or s2:
            if s1 and s2 and len(extract_unicode_block(kanji_uni, (s1[0]))) == 1:
                res += s1.popleft() + "[" + s2.popleft()
            elif s1 and s2 and s1[0] == s2[0] and i != 0:
                res += "]" + s2.popleft()
                if s1:
                    s1.popleft()
            else:
                # this might have bugs...
                if s1 and s2:
                    res += s2.popleft()
                    # s1.popleft()
                elif s2:
                    res += s2.popleft()
                else:
                    res += s1.popleft()

            i += 1

        if "]" not in res:
            res += "]"

        return res

    def sent2furigana(self, text):
        arr = []
        for word in tagger(text):
            arr.append((word.feature.orth, word.feature.lemma, word.pos, word.feature.kana, word.feature.kanaBase,
                        word.feature.pos1))

        i, N, s, isOpen = 0, len(arr), "", False
        while i < N:
            temp = ""
            # print(arr[i][0], arr[i][4])

            # checking arr[i][0] instead of arr[i][3] might also break something because arr[i][0] might not contain katakana like arr[i][3] does
            if arr[i][0] == "。":
                s += arr[i][0]
            elif arr[i][0] != arr[i][4] and arr[i][5] not in ["助詞", "助動詞"]:
                s += self.clean(arr[i][0], kata2hira(arr[i][3]))
                temp = self.clean(arr[i][0], kata2hira(arr[i][3]))

            else:
                # s += clean(arr[i][0], kata2hira(arr[i][3]))
                s += arr[i][0]
                temp = arr[i][0]

            # print(temp, "\t", arr[i][3], arr[i][5])

            i += 1

        return s


if __name__ == "__main__":
    parser = Parser()

    s1 = "暑い"
    s2 = "あつい"
    res = parser.clean(s1, s2)
    print(res)

    s1 = "天の川"
    s2 = "あまのがわ"
    res = parser.clean(s1, s2)
    print(res)

    s1 = "食べ"
    s2 = "たべ"
    res = parser.clean(s1, s2)
    print(res)

    s = ""
    print(s)



