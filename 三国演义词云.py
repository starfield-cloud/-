from wordcloud import WordCloud
import jieba.posseg as pseg
from matplotlib import pyplot as plt

def load_stopword(path):
    with open(path, 'r', encoding='GBK', errors='ignore') as f:
        data = f.read()
        stopword = data.split('\n')
    print("加载停用词数量:", len(stopword))  # 调试输出
    return stopword

def load_text(path):
    with open(path, 'r', encoding='GBK', errors='ignore') as f:
        data = f.read()
    print("加载文本长度:", len(data))  # 调试输出
    return data

def word_freq(word_list, stopword, wordflag=None):
    cout = {}
    for w in word_list:
        if w.word in stopword:
            continue
        name = None
        if '刘玄德' in w.word or '玄德' in w.word or '刘豫州' in w.word or '备' in w.word or '大耳贼' in w.word or '先主' in w.word or '刘皇叔' in w.word or '皇叔' in w.word or '大耳' in w.word or '玄德公' in w.word:
            name = '刘备'
        elif '孔明' in w.word or '卧龙' in w.word or '卧龙先生' in w.word or '亮' in w.word or '武侯' in w.word or '武乡侯' in w.word or '诸葛丞相' in w.word or '相父' in w.word or '诸葛孔明' in w.word:
            name = '诸葛亮'
        elif '曹孟德' in w.word or '曹公' in w.word or '曹贼' in w.word or '操' in w.word or '曹丞相' in w.word or '曹操' in w.word or '魏公' in w.word or '魏王' in w.word or '阿瞒' in w.word or '曹阿瞒' in w.word or '孟德' in w.word or '操军' in w.word:
            name = '曹操'
        elif '关云长' in w.word or '云长' in w.word or '关二爷' in w.word or '关公' in w.word or '关将军' in w.word or '美髯公' in w.word or '汉寿亭侯' in w.word or '关云' in w.word or '关某' in w.word or '关羽' in w.word:
            name = '关羽'
        elif '赵云' in w.word or '子龙' in w.word or '常山' in w.word or '赵将军' in w.word:
            name = '赵子龙'
        elif '张翼德' in w.word or '三弟' in w.word or '翼德' in w.word or '张翼' in w.word or '张飞' in w.word:
            name = '张飞'
        elif '吕奉先' in w.word or '奉先' in w.word or '布' in w.word or '吕将军' in w.word or '三姓家奴' in w.word:
            name = '吕布'
        elif '卓' in w.word or '仲颖' in w.word or '董老贼' in w.word:
            name = '董卓'
        elif '瑜' in w.word or '公瑾' in w.word or '周郎' in w.word or '周瑜' in w.word:
            name = '周瑜'
        elif '仲达' in w.word or '司马仲达' in w.word or '懿' in w.word:
            name = '司马懿'
        elif '刘景升' in w.word or '景升' in w.word or '刘表' in w.word:
            name = '刘表'
        elif '超' in w.word or '孟起' in w.word or '马孟起' in w.word:
            name = '马超'
        elif '阿斗' in w.word or '刘禅' in w.word:
            name = '刘禅'
        elif '仲谋' in w.word or '吴王' in w.word or '吴主孙权' in w.word or '孙权' in w.word:
            name = '孙权'
        elif '瓒' in w.word:
            name = '公孙瓒'
        elif '伯约' in w.word or '姜维' in w.word:
            name = '姜维'
        elif '肃' in w.word or '子敬' in w.word:
            name = '鲁肃'
        elif '绍' in w.word or '本初' in w.word or '袁本初' in w.word:
            name = '袁绍'
        elif len(wordflag) > 0 and w.flag in wordflag:
            name = w.word
        if name is not None:
            cout[name] = cout.get(name, 0) + 1
    items = list(cout.items())
    items.sort(key=lambda x: x[1], reverse=True)
    return items, cout

def create_wordcloud(cout):
    if not cout:
        print("没有足够的数据生成词云")
        return
    wc = WordCloud(
        width=1000,
        height=500,
        background_color='white',
        max_words=30,
        font_path=r"C:\Windows\Fonts\simkai.ttf"
    )
    wc.generate_from_frequencies(cout)
    plt.figure(figsize=(10, 5))
    plt.imshow(wc, interpolation='bilinear')
    plt.axis('off')
    plt.show()

if __name__ == '__main__':
    stopwords = load_stopword('stop_words.txt')
    text = load_text('三国演义.txt')
    word_list = pseg.cut(text)
    wordflag = ['nr']
    result, cout = word_freq(list(word_list), stopwords, wordflag)

    if not result:
        print("没有数据可以显示")
    else:
        print(type(result[0][1]))
        for i in range(min(30, len(result))):
            w = result[i]
            print("%-4s: %4d" % w, end=' ')
            if (i + 1) % 5 == 0:
                print("\n")

    create_wordcloud(cout)