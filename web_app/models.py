from django.db import models
# Create your models here.
class UserArea(models.Model):
    area_no = models.CharField('區域編號',max_length=32)
    area_name = models.CharField('區域名稱',max_length=32)
    memo = models.CharField('備註',max_length=32,null=True,blank=True)
    # flag = models.CharField()
    
    def __str__(self):
        return self.area_name

    class Meta:
        verbose_name = '所屬區域資料檔'
        verbose_name_plural = '所屬區域資料檔'

class UserUnit(models.Model):
    unit_no = models.CharField('編號',max_length=32)
    unit_name = models.CharField('名稱',max_length=32)
    memo = models.CharField('備註',max_length=32,null=True,blank=True)
    # flag = models.CharField()
    
    def __str__(self):
        return self.unit_name

    class Meta:
        verbose_name = '所屬單位資料檔'
        verbose_name_plural = '所屬單位資料檔'

class AssetBasic(models.Model):
    no = models.CharField('資產編號',max_length=32)
    form = models.CharField('資產類別',max_length=32,null=True,blank=True)
    name = models.CharField('名稱',max_length=32,null=True,blank=True)
    style = models.CharField('規格',max_length=32,null=True,blank=True)
    nums = models.CharField('數量',max_length=32,null=True,blank=True)
    put_place = models.CharField('放置地點',max_length=32)
    price = models.CharField('財產價值',max_length=32,null=True,blank=True)
    dept = models.CharField('財產部門',max_length=32)
    syid = models.CharField('員編(保管人)',max_length=32)
    buydate = models.DateTimeField('購置日期',null=True,blank=True)
    chgdate = models.DateTimeField('異動日期')
    memo = models.CharField('備註',max_length=32,null=True,blank=True)
    # flag = models.CharField()
    
    def __str__(self):
        return self.no

    class Meta:
        verbose_name = '資產基本檔'
        verbose_name_plural = '資產基本檔'

class AssetMove(models.Model):
    moving_no = models.CharField('移轉單號',max_length=32)
    createDate = models.DateTimeField('建立日')
    moveDate = models.DateTimeField('移轉日')
    createNo = models.CharField('員編(建立者)',max_length=32)
    moveToDept = models.CharField('轉出部門',max_length=32)
    moveToSyId = models.CharField('轉出員編',max_length=32)
    moveToAssetNo = models.CharField('轉出資產編號',max_length=32)
    moveToNums = models.CharField('轉出數量',max_length=32)
    moveInDept = models.CharField('轉入部門',max_length=32)
    moveInSyId = models.CharField('轉入員編',max_length=32)
    moveInAssetNo = models.CharField('轉入資產編號',max_length=32)
    moveInNums = models.CharField('轉入數量',max_length=32)
    moveInPlace = models.CharField('轉入放置地點',max_length=32)
    memo = models.CharField('備註',max_length=32,null=True,blank=True)
    # flag = models.CharField()
    
    def __str__(self):
        return self.moving_no

    class Meta:
        verbose_name = '資產移轉單'
        verbose_name_plural = '資產移轉單'

class SyUser(models.Model):
    syid = models.CharField('員編',max_length=6)
    username = models.CharField('姓名',max_length=16)
    area = models.ForeignKey(
        UserArea, verbose_name='所屬區域', on_delete=models.CASCADE,null=True)
    workunit = models.ForeignKey(
        UserUnit, verbose_name='所屬單位', on_delete=models.CASCADE,null=True)
    # flag = models.CharField()
    def __str__(self):
        return self.syid

    class Meta:
        verbose_name = '員工基本檔'
        verbose_name_plural = '員工基本檔'