from wordcloud import WordCloud
import jieba.posseg as pseg
from matplotlib import pyplot as plt

# 定义函数：加载停用词
def load_stopword(path):
    with open(path, 'r', encoding='GBK', errors='ignore') as f:  # 读取停用词文件
        data = f.read()
        stopword = data.split('\n')  # 将文件内容按行分割成列表
    print("加载停用词数量:", len(stopword))  # 打印加载的停用词数量
    return stopword

# 定义函数：加载文本数据
def load_text(path):
    with open(path, 'r', encoding='GBK', errors='ignore') as f:  # 读取文本文件
        data = f.read()
    print("加载文本长度:", len(data))  # 打印加载的文本长度
    return data

# 定义函数：计算词频
def word_freq(word_list, stopword, wordflag=None):
    cout = {}
    for w in word_list:  # 遍历分词结果
        if w.word in stopword:
            continue  # 如果是停用词，则跳过
        name = None
        # 以下为判断词汇的系列条件，将特定词汇映射为统一名称
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
            name = w.word  # 如果符合特定词性，则使用原词
        # 进行词频统计
        if name is not None:
            cout[name] = cout.get(name, 0) + 1
    # 对统计结果进行排序
    items = list(cout.items())
    items.sort(key=lambda x: x[1], reverse=True)
    return items, cout

# 定义函数：生成词云
def create_wordcloud(cout):
    if not cout:  # 如果词频字典为空，则不生成词云
        print("没有足够的数据生成词云")
        return
    wc = WordCloud(
        width=1000,  # 设置词云图的宽度
        height=500,  # 设置词云图的高度
        background_color='white',  # 设置词云图的背景颜色
        max_words=30,  # 设置词云图中显示的最大单词数量
        font_path=r"C:\Windows\Fonts\simkai.ttf"  # 设置字体路径
    )
    wc.generate_from_frequencies(cout)  # 根据词频生成词云
    plt.figure(figsize=(10, 5))  # 设置图像大小
    plt.imshow(wc, interpolation='bilinear')  # 显示词云
    plt.axis('off')  # 不显示坐标轴
    plt.show()  # 显示图像

# 主程序
if __name__ == '__main__':
    stopwords = load_stopword('stop_words.txt')  # 加载停用词
    text = load_text('三国演义.txt')  # 加载文本
    word_list = pseg.cut(text)  # 使用 jieba 进行分词和词性标注
    wordflag = ['nr']  # 定义需要统计的词性
    result, cout = word_freq(list(word_list), stopwords, wordflag)  # 计算词频

    if not result:  # 如果结果为空
        print("没有数据可以显示")
    else:
        print(type(result[0][1]))  # 打印结果中第一个词频的类型
        for i in range(min(30, len(result))):  # 打印前30个最高频的词
            w = result[i]
            print("%-4s: %4d" % w, end=' ')
            if (i + 1) % 5 == 0:
                print("\n")

    create_wordcloud(cout)  # 生成词云
