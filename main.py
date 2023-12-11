import pandas as pd
from parser2 import Parser

if __name__ == "__main__":
    df = pd.read_csv("core2k_6k.csv", header=None)
    df.columns = ["jp", "furigana", "kana", "en", "audio_1", "pos", "temp_1", "jp_sentence", "jp_sentence_furigana",
                  "jp_sentence_kana", "en_sentence", "miss_word_sentence", "audio_2", "img", "core_2000_step",
                  "core_index", "optimized_voc_index", "optimized_sent_index", "temp_2"]

    clean_furigana_sent = []
    for v in df["jp_sentence_furigana"]:
        v = v.replace("<b>", "").replace("</b>", "").replace(" ", "")
        clean_furigana_sent.append(v)

    clean_jp_sent = []
    for v in df["jp_sentence"]:
        v = v.replace("<b>", "").replace("</b>", "")
        clean_jp_sent.append(v)

    df = pd.DataFrame()
    df["clean_furigana_sent"] = clean_furigana_sent
    df["clean_jp_sent"] = clean_jp_sent

    mistakes = 0

    parser = Parser()

    for i, s in enumerate(df["clean_jp_sent"]):
        if mistakes > 5: break

        try:
            ns = parser.sent2furigana(s)
            if df["clean_furigana_sent"].iloc[i] != ns:
                # print(ns, "\n", new_df["clean_furigana_sent"].iloc[i], "\n", s, "\n\n")
                # mistakes += 1

                # generally these will be because of the tagger eg.) 私 -> わたし -> わたくし
                pass
        except:
            print("error", "\n", df["clean_furigana_sent"].iloc[i], "\n", s, "\n\n")
            mistakes += 1

    print(mistakes)

