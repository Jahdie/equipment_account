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

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class ModelsHierarchy(BaseModelAbstract):
    hierarchy_number = models.PositiveIntegerField(blank=True, verbose_name='Номер иерархии')

    def __str__(self):
        return self.note

    class Meta:
        verbose_name = 'Номер иерархии'
        verbose_name_plural = 'Номера иерархии'


class Productions(BaseDictionaryModelAbstract):
    class Meta:
        verbose_name = 'Производство'
        verbose_name_plural = 'Производства'


class Workshops(BaseDictionaryModelAbstract):
    production_id = models.ForeignKey('Productions', on_delete=models.PROTECT, null=True, verbose_name='Производство',
                                      related_name='production_id')

    class Meta:
        verbose_name = 'Цех'
        verbose_name_plural = 'Цеха'


class Compartments(BaseDictionaryModelAbstract):
    production_id = models.ForeignKey('Productions', on_delete=models.PROTECT, null=True, verbose_name='Производство',
                                      related_name='production')
    workshop_id = models.ForeignKey('Workshops', on_delete=models.PROTECT, null=True, verbose_name='Цех')

    class Meta:
        verbose_name = 'Участок'
        verbose_name_plural = 'Участки'


class Stations(BaseDictionaryModelAbstract):
    ip_adress = models.CharField(max_length=15, verbose_name='IP адресс')
    production_id = models.ForeignKey('Productions', on_delete=models.PROTECT, null=True, verbose_name='Производство')
    workshop_id = models.ForeignKey('Workshops', on_delete=models.PROTECT, null=True, verbose_name='Цех')
    compartment_id = models.ForeignKey('Compartments', on_delete=models.PROTECT, null=True, verbose_name='Участок')

    class Meta:
        verbose_name = 'Станция'
        verbose_name_plural = 'Станции'


class Locations(BaseModelAbstract):
    production_id = models.ForeignKey('Productions', on_delete=models.PROTECT, null=True, verbose_name='Производство',
                                      related_name='Productions')
    workshop_id = models.ForeignKey('Workshops', on_delete=models.PROTECT, null=True, verbose_name='Цех')
    compartment_id = models.ForeignKey('Compartments', on_delete=models.PROTECT, null=True, verbose_name='Участок')
    photo_location = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)

    class Meta:
        verbose_name = 'Местоположение оборудования'
        verbose_name_plural = 'Местоположения оборудования'


class SwitchCabinets(BaseDictionaryModelAbstract):
    production_id = models.ForeignKey('Productions', on_delete=models.PROTECT, null=True, verbose_name='Производство')
    workshop_id = models.ForeignKey('Workshops', on_delete=models.PROTECT, null=True, verbose_name='Цех')
    compartment_id = models.ForeignKey('Compartments', on_delete=models.PROTECT, null=True, verbose_name='Участок')

    class Meta:
        verbose_name = 'Коммутационный шкаф'
        verbose_name_plural = 'Коммутационные шкафы'


class SwitchModels(BaseDictionaryModelAbstract):
    ports_num = models.PositiveIntegerField(verbose_name='Количество портов')

    class Meta:
        verbose_name = 'Модель свитча'
        verbose_name_plural = 'Модели свитчей'


class Switches(BaseDictionaryModelAbstract):
    ip_adress = models.CharField(max_length=15, verbose_name='IP адресс')
    switch_cabinet_id = models.ForeignKey('SwitchCabinets', on_delete=models.PROTECT, null=True,
                                          verbose_name='Коммутационный шкаф')
    model_id = models.ForeignKey('SwitchModels', on_delete=models.PROTECT, null=True, verbose_name='Модель свитча')

    class Meta:
        verbose_name = 'Свитч'
        verbose_name_plural = 'Свитчи'


class SwitchPorts(BaseModelAbstract):
    port_num = models.PositiveIntegerField(verbose_name='Номер порта')
    # Проверка транк это или хост
    is_trunc = models.BinaryField(verbose_name='Транк или хост')
    # Если is_trunc = 0, ставим id станции, если is_trunk = 1, ставим id порта свитча с которым связан этот порт
    station_id_or_ports_id = models.ForeignKey('Stations', on_delete=models.PROTECT, null=True,
                                               verbose_name='Станция или порт свитча')
    switch_id = models.ForeignKey('Switches', on_delete=models.PROTECT, null=True, verbose_name='Свитч')

    class Meta:
        verbose_name = 'Порт свитча'
        verbose_name_plural = 'Порты свитчей'


class ControllerFamilies(BaseDictionaryModelAbstract):
    class Meta:
        verbose_name = 'Семейство контроллеров'
        verbose_name_plural = 'Семейства контроллеров'


class ModulesModels(BaseDictionaryModelAbstract):
    class Meta:
        verbose_name = 'Модель модуля'
        verbose_name_plural = 'Модели модулей'


class ModulesTypes(BaseDictionaryModelAbstract):
    class Meta:
        verbose_name = 'Тип модуля'
        verbose_name_plural = 'Типы модулей'


class ModulesInStations(BaseModelAbstract):
    module_type_id = models.ForeignKey('ModulesTypes', on_delete=models.PROTECT, null=True, verbose_name='Тип модуля')
    controller_family_id = models.ForeignKey('ControllerFamilies', on_delete=models.PROTECT, null=True,
                                             verbose_name='Семейство контроллеров')
    model_id = models.ForeignKey('ModulesModels', on_delete=models.PROTECT, null=True, verbose_name='Модель модуля')

    class Meta:
        verbose_name = 'Модуль в станции'
        verbose_name_plural = 'Модули в станциях'


class SignalsTypes(BaseDictionaryModelAbstract):
    class Meta:
        verbose_name = 'Тип сигнала'
        verbose_name_plural = 'Типы сигналов'


class EquipmentsTypes(BaseDictionaryModelAbstract):
    class Meta:
        verbose_name = 'Тип оборудования'
        verbose_name_plural = 'Типы оборудования'


class EquipmentsNames(BaseDictionaryModelAbstract):
    class Meta:
        verbose_name = 'Наименование оборудования'
        verbose_name_plural = 'Наименования оборудования'


class Signals(BaseDictionaryModelAbstract):
    marking = models.CharField(max_length=15, verbose_name='Маркировка')
    signal_type_id = models.ForeignKey('SignalsTypes', on_delete=models.PROTECT, null=True, verbose_name='Тип сигнала')
    module_id = models.ForeignKey('ModulesInStations', on_delete=models.PROTECT, null=True,
                                  verbose_name='Модуль в станции')
    equipment_type_id = models.ForeignKey('EquipmentsTypes', on_delete=models.PROTECT, null=True,
                                          verbose_name='Тип оборудования')
    equipment_name_id = models.ForeignKey('EquipmentsNames', on_delete=models.PROTECT, null=True,
                                          verbose_name='Наименование оборудования')

    class Meta:
        verbose_name = 'Сигнал'
        verbose_name_plural = 'Сигналы'
