import jieba.posseg as pseg

sentence = "我来到北京清华大学"
words = pseg.cut(sentence)  # 同时进行分词和词性标注
for word, flag in words:
    print(f'{word}/{flag}', end=' ')