from django.db import models


class BaseModelAbstract(models.Model):
    note = models.TextField(blank=True, verbose_name='Примечание')
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    date_deleted = models.DateTimeField(auto_now=True, verbose_name='Дата удаления')
    date_updated = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    class Meta:
        abstract = True


class BaseDictionaryModelAbstract(BaseModelAbstract):
    name = models.CharField(max_length=150, verbose_name='Наименование')
    photo_location = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    hierarchy = models.ForeignKey('ModelsHierarchy', on_delete=models.PROTECT, null=True, verbose_name='Номер иерархии')

    class Meta:
        abstract = True


class ModelsHierarchy(BaseModelAbstract):
    hierarchy_number = models.PositiveIntegerField(blank=True, verbose_name='Номер иерархии')

    class Meta:
        verbose_name = 'Номер иерархии'
        verbose_name_plural = 'Номера иерархии'

class Productions(BaseDictionaryModelAbstract):
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Производство'
        verbose_name_plural = 'Производства'


class Workshops(BaseDictionaryModelAbstract):

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Цех'
        verbose_name_plural = 'Цеха'


class Compartments(BaseDictionaryModelAbstract):

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Участок'
        verbose_name_plural = 'Участки'


class Locations(BaseModelAbstract):
    production_id = models.ForeignKey('Productions', on_delete=models.PROTECT, null=True, verbose_name='Производство',
                                      related_name='Productions')
    workshop_id = models.ForeignKey('Workshops', on_delete=models.PROTECT, null=True, verbose_name='Цех')
    compartment_id = models.ForeignKey('Compartments', on_delete=models.PROTECT, null=True, verbose_name='Участок')
    photo_location = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)

    class Meta:
        verbose_name = 'Местоположение оборудования'
        verbose_name_plural = 'Местоположения оборудования'
