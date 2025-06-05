from django.db import models

class People(models.Model):
    image = models.ImageField()
    name = models.CharField(max_length=20)
    patronymic = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    
    def __str__(self):
        return f'{self.name} {self.patronymic} {self.surname}'
    
class Program(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    supervisor = models.ForeignKey(People, related_name='supervised_programs', on_delete=models.CASCADE) # нельзя пустым - удалит о программе
    manager = models.ForeignKey(People, null=True, related_name='managed_programs', blank=True, on_delete=models.SET_NULL) # можно пустым

    def __str__(self):
        return self.name

class ProgramPoints(models.Model):
    program = models.ForeignKey(Program, null=True, blank=True, on_delete=models.SET_NULL, related_name='points') # имя в html
    text = models.TextField()
    class Meta:
        verbose_name = "За счет чего достигается программа"
        verbose_name_plural = "За счет чего достигается программа"
        ordering = ("-pk", )