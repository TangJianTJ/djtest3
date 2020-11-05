
import mongoengine
from mongoengine import connect


#connect('test', host='127.0.0.1', port=27017) #连接数据库
# Create your models here.


class Classify(mongoengine.Document):
    uid = mongoengine.SequenceField(primary_key=True)  # 自增id ,主码
    classifyName = mongoengine.StringField(max_length=30, verbose_name='分类名称')
    createdTime = mongoengine.DateTimeField(verbose_name='创建时间')
    updateTime = mongoengine.DateTimeField(verbose_name='修改时间')
    meta = {'collection': 'classify'}  # 数据库中的集合
