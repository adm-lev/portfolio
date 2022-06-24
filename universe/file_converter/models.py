from django.db import models
from django.urls import reverse


class OperationFile(models.Model):
    """
    OperationFile
    """

    unit_file = models.FileField(verbose_name='Документ', help_text='Загрузите документ',
                                 null=True, blank=True, upload_to='converter/files')
    picture = models.ImageField(verbose_name='Изображение', help_text='Загрузите картинку',
                                upload_to='converter/images', null=True, blank=True)

    # def __str__(self):
    #     """
    #
    #     :return:
    #     """
    #     return self.title

    def get_absolute_url(self):
        """

        :return:
        """
        return reverse('file', args=[str(self.id)])
