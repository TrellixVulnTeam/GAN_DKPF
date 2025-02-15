#----------------------------------------------
# -*- encoding=utf-8 -*-                      #
# __author__:'xiaojie'                        #
# CreateTime:                                 #
#       2019/4/30 10:12                       #
#                                             #
#               天下风云出我辈，                 #
#               一入江湖岁月催。                 #
#               皇图霸业谈笑中，                 #
#               不胜人生一场醉。                 #
#----------------------------------------------
# https://blog.csdn.net/qq_25737169/article/details/78532719
# impl1：
# 在dataset中没有unlabeled的数据，传入的y都是有意义的，代表X的真实标签
#     没有特别声明无监督学习的loss，如果数据集中只要100条有标签的数据，则
#     相当于用这100条数据训练一个分类器
#     没有无监督学习的损失(真实X)。(无监督学习的loss在判别器的第一个loss中)

# impl2：同上
# impl3:
#     虽然数据集中的数据全是labeled，但是，把有些数据当成unlabeled数据来训练
#     适合dataset中既有label又有unlabeled的数据的情形，似乎是真正的半监督学习，如果是真正的既有labeled又有unlabeled
#     的dataset，在feed的时候应该注意区分。
#     真实X和生成的X都用到了无监督学习
#     真实X和生成的X也都用到了监督学习，只是生成的X的loss没用上，
#     根据文章中理论，监督学习的loss只有真实的X，无监督的loss采用X和X_gen

# 实际应用时，应该是在dataset中，既有labeled的数据，又有unlabeled的数据，且unlabeled的数据远远大于labeled的数据，
# 这个时候，如果想训练一个分类器，可以采用半监督学习GAN，但是在传入label的时候应该注意区分

# 当既有labeled数据又有unlabeled的数据时，只使用labeled数据，虽然可以训练，但是丢失了很多那些是真实只是没有label
# 的数据的信息

# 注意:半监督学习GAN中，传入给模型的label中，有标签的和没有标签的数据应该是分开传给模型的。有标签的数据可以当做
# 无标签的的数据传给模型，训练无监督学习，也可以训练监督学习。