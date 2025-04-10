from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=32, db_comment='书名')
    author = models.CharField(max_length=32, blank=True, null=True, db_comment='作者')
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, db_comment='价格')
    create_time = models.DateTimeField(db_comment='创建时间')
    update_time = models.DateTimeField(db_comment='更新时间')

    class Meta:
        managed = False
        db_table = 'book'


class PurchaseRecord(models.Model):
    book_id = models.IntegerField(db_comment='购买的书id')
    name = models.CharField(max_length=32, blank=True, null=True, db_comment='购买人姓名')
    phone = models.CharField(max_length=16, blank=True, null=True, db_comment='购买人电话')
    create_time = models.DateTimeField(db_comment='购买时间')

    class Meta:
        managed = False
        db_table = 'purchase_record'
