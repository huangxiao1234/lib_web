#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User


class Reader(models.Model):
    class Meta:
        verbose_name = '读者信息'
        verbose_name_plural = '读者信息'

    user = models.OneToOneField(User)
    name = models.CharField(max_length=16, unique=True)
    phone = models.IntegerField(unique=True)
    max_borrowing = models.IntegerField(default=5)
    balance = models.FloatField(default=0.0)
    photo = models.ImageField(blank=True, upload_to='images/')
    email = models.EmailField(default='wonghiu45@163.com')

    STATUS_CHOICES = (
        (0, 'normal'),
        (-1, 'overdue')
    )
    status = models.IntegerField(
        choices=STATUS_CHOICES,
        default=0,
    )

    def __str__(self):
        return self.name


class Book(models.Model):
    class Meta:
        verbose_name = '图书信息'
        verbose_name_plural = '图书信息'

    ISBN = models.CharField(max_length=13, primary_key=True)
    title = models.CharField(max_length=128)
    author = models.CharField(max_length=32)
    press = models.CharField(max_length=64)

    description = models.CharField(max_length=1024, default='')
    price = models.CharField(max_length=20, null=True)

    category = models.CharField(max_length=64, default=u'文学')
    cover = models.ImageField(null=True)
    index = models.CharField(max_length=16, null=True)
    location = models.CharField(max_length=64, default=u'图书馆1楼')
    quantity = models.IntegerField(default=1)

    state=models.CharField(max_length=20,default=u'no_borrow')#借阅状态。1.be_borrow 已借出2.no 不可借3.be_order 被预约4.no_borrow 还可借
    ordering_id=models.CharField(max_length=20,default=u'null')#若书被预约，则保存预约读者号。其余时候为null
    manager_id = models.CharField(max_length=20,default=u'无')#入库管理员编号

    def __str__(self):
        return self.title + self.author


class Borrowing(models.Model):
    class Meta:
        verbose_name = '借阅记录'
        verbose_name_plural = '借阅记录'

    reader = models.ForeignKey(Reader)
    ISBN = models.ForeignKey(Book, on_delete=models.CASCADE)
    date_issued = models.DateField()
    date_due_to_returned = models.DateField()
    date_returned = models.DateField(null=True)
    amount_of_fine = models.FloatField(default=0.0)

    def __str__(self):
        return '{} 借了 {}'.format(self.reader, self.ISBN)

class Ordering(models.Model):
    class Meta:
        verbose_name = '预约记录'
        verbose_name_plural = '预约记录'

    reader = models.ForeignKey(Reader)
    ISBN = models.ForeignKey(Book, on_delete=models.CASCADE)
    date_issued = models.DateField(default='2018-5-16')
    date_due_to_returned = models.DateField(default='2018-5-16')
    date_returned = models.DateField(null=True)
    amount_of_fine = models.FloatField(default=0.0)

    def __str__(self):
        return '{} 预约了 {}'.format(self.reader, self.ISBN)