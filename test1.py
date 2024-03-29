# coding=utf-8
import pandas as pd
import jieba.posseg


w1 = '美对华商品将大规模加征关税 我驻美大使：奉陪到底。当地时间22日，美国总统特朗普宣布将对从中国进口的商品大规模征收关税，涉税商品达600亿美元。我驻美大使崔天凯回应：中国从来不想与任何国家进行贸易战，但若其他国家非要对中国施加贸易战，中国一定会予以还击、奉陪到底。'
w2 = '《流浪地球》最大的硬伤：洛希极限竟是错的！地球真会被木星撕碎吗？'
w3 = '重点指出为了构建普适性的且可理解的智能生长机制，需要颠覆传统科学的科学观和方法论对人工智能研究的统领地位，确立信息科学的科学观和方法论对人工智能研究的统领。探究了人工智能理论的核心问题：智能是怎样生成的？结果表明，普适性的智能生成机制乃是“信息转换与智能创生”定律。'
w4 = '一种基于深度学习的遥感图像分类及农田识别方法,为解决便于发现我国基本农田被非法侵占的问题,针对现有神经网络收敛速度慢、识别准确率不高的缺点,提出一种基于卷积神经网络的遥感图像农田分类及识别方法。该算法使用较大的卷积核,有效地提取梯度信息;设计深度为6层的卷积神经网络,提高了网络的分类效果,且大大降低了网络的训练次数。实验结果表明,利用该识别模型对农田、建筑、荒漠以及植被的识别准确率达到98.15%,比经典AlexNet网络模型提高了6.1%;训练网络所需的迭代次数由1.49×106次左右降低到4 500次。因此,与经典AlexNet网络相比,改进的AlexNet网络用于遥感图像分类和目标图像识别,耗时更短、识别准确率更高。 '
w5 = '卷积神经网络'
w6 = '深度学习（英语：deep learning）是机器学习的分支，是一种以人工神经网络为架构，对数据进行表征学习的算法。[1][2][3][4][5]深度学习是机器学习中一种基于对数据进行表征学习的算法。观测值（例如一幅图像）可以使用多种方式来表示，如每个像素强度值的向量，或者更抽象地表示成一系列边、特定形状的区域等。而使用某些特定的表示方法更容易从实例中学习任务（例如，人脸识别或面部表情识别[6]）。深度学习的好处是用非监督式或半监督式的特征学习和分层特征提取高效算法来替代手工获取特征。[7]表征学习的目标是寻求更好的表示方法并创建更好的模型来从大规模未标记数据中学习这些表示方法。表示方法来自神经科学，并松散地创建在类似神经系统中的信息处理和对通信模式的理解上，如神经编码，试图定义拉动神经元的反应之间的关系以及大脑中的神经元的电活动之间的关系。[8]至今已有数种深度学习框架，如深度神经网络、卷积神经网络和深度置信网络和递归神经网络已被应用在计算机视觉、语音识别、自然语言处理、音频识别与生物信息学等领域并获取了极好的效果。另外，“深度学习”已成为类似术语，或者说是神经网络的品牌重塑'
w7 = '阿图尔·叔本华（德语：Arthur Schopenhauer，1788年2月22日－1860年9月21日），著名德国哲学家，唯意志论主义的开创者，其思想对近代的学术界、文化界影响极为深远。不同于同时代的费希特、谢林、黑格尔，叔本华并无取消物自体，他继承了康德对物自体和表象之间的区分，认为它是可以透过直观而被认识的，并且将其确定为意志。叔本华认为，意志是独立于时间和空间的，它同时亦包括所有的理性与知识，我们只能透过沉思来摆脱它。叔本华把他著名的悲观主义哲学与此学说联系在一起，认为被意志所支配最终只会带来虚无和痛苦。他对心灵屈从于器官、欲望和冲动的压抑、扭曲的理解启发了日后的精神分析学和心理学。'
w8 = '纳什均衡'


seg = jieba.posseg.cut("智慧医疗")
for i in seg:
    print(i.word, i.flag)

keys = jieba.lcut('强化学习')
for key in keys:
    print(key)