# coding=utf-8
import numpy as np
import gensim
import pandas as pd
import jieba.posseg
import codecs
from collections import Counter

model = gensim.models.Word2Vec.load('data/wiki.zh.text.model')


# 此函数计算某词对于模型中各个词的转移概率p(wk|wi)
def predict_proba(oword, iword):
    #获取输入词的词向量
    iword_vec = model[iword]
    #获取保存权重的词的词库
    oword = model.wv.vocab[oword]
    oword_l = model.trainables.syn1[oword.point].T
    dot = np.dot(iword_vec, oword_l)
    lprob = -sum(np.logaddexp(0, -dot) + oword.code*dot)
    return lprob

# 各个词对于某词wi转移概率的乘积即为p(content|wi)，
# 如果p(content|wi)越大就说明在出现wi这个词的条件下，此内容概率越大，
# 那么把所有词的p(content|wi)按照大小降序排列，越靠前的词就越重要，越应该看成是本文的关键词。


def keywords(s):
    # 抽出s中和与训练的model重叠的词,去停用词
    s = [w for w in s if w in model]
    ws = {w: sum([predict_proba(u, w) for u in s]) for w in s}
    return Counter(ws).most_common()


w1 = '美对华商品将大规模加征关税 我驻美大使：奉陪到底。当地时间22日，美国总统特朗普宣布将对从中国进口的商品大规模征收关税，涉税商品达600亿美元。我驻美大使崔天凯回应：中国从来不想与任何国家进行贸易战，但若其他国家非要对中国施加贸易战，中国一定会予以还击、奉陪到底。'
w2 = u'你可以在微博微信喜马拉雅b站等平台找到我们，请问你觉得这个视频难做吗什么都做之前我不知道为什么我会认识繁体字丹肠道感觉也还行就，就算这句话中可能有你不熟悉的繁体字你只要读出其中所有的传承字然后再根据上下文语境就能自动地不熟悉的繁体字翻译过来，你好能顺畅的读书这段话因为你已经识别出这一段歌词及时你的老师从来没教过你这些字应该怎么读，其实都是繁体字幕三简体汉字同根同源高度相似的字形结构以及大量传承字的存在是繁简转换器存在的外部因素而人脑匪夷所思的信息重建能力就是反向转换器存在的内部因素，比如大部分人在阅读的时候都采取了整体阅读的方式无论一段文字中掺杂的繁体字yy文字或者干脆脱掉这些文字都不会影响信息的获取而改变文字顺序或者大小也不会影响正常阅读，2013年正式颁布的通用规范汉字表一共收入了8105个汉字其中有2546个左右的汉字是由繁体字简化得到的简体字，还有一大批汉字只保留了猿繁体字中的一部分另外还有一批轮廓子也就是保留的袁繁体字的轮廓特征值的具体的笔画进行简化，从字形结构上看绝大多数简体字都保留的原繁体字中最重要的形态特征上过学的中国人联盟太太就有很高的正确率除了简体字以外通用规范汉字表中有超过三分之二的汉字都是传承字也就是历史上留存下来并且在各地沿用至今的汉字它们既不属于繁体字也不属于简体字还是各类汉字系统中的共同组成部分是连接繁简字之间的桥梁，1956年1月31日人民日报全文发表了国务院制定的汉字简化方案公布了第一批简化汉字其中一大批文字的字形结构梅便只是把繁体字中比较复杂的部分改成了简单的符号，永远不要低估大脑的信息进口能力别说繁体字就连阅读根本不存在的火星文都不是什么难事趁着同学阅读好几种型号都不在话下，类似原则大量的汉字被简化其中的一批简化字还可以当作其它汉字的偏旁由此就得到了更多的偏旁类推简化字汉字是一种象形文字，那么为什么中国人会自带繁简转换器呢财之道在知识的海洋里狗刨，这个过程重复多次之后老师没教过的繁体字也就逐渐认识英语感慨文化产品的强是你从小接触繁体字的次数可能远远超出自己的想象一至于你可能没有意识到有多少大陆群众喜闻乐见的文化产品，3301，'

# 定义选取的词性(名词、专有名词、机构团体、人名、地名)
pos = ['n', 'nz', 'nt', 'nr', 'ns']
stop_key = [w.strip() for w in codecs.open('data/stopWord.txt', 'r', encoding='utf-8').readlines()]
seg = jieba.posseg.cut(w1)  # 分词
words = []
for i in seg:
    if i.word not in words and i.word not in stop_key and i.flag in pos:  #去重 + 去停用词 + 词性筛选
        words.append(i.word)
x = pd.Series(keywords(words))

# 输出最重要的前10个词
print(x[0:10])
keys = [x[0:10][i][0] for i in range(10)]
result = " ".join(keys)
print(result)
