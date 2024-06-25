from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# Create your models here.
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class Chude(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='ID Chủ đề')
    name = models.CharField(max_length=200, verbose_name='Tên chủ đề')

    class Meta:
        verbose_name = 'Chủ đề'
        verbose_name_plural = 'Các chủ đề'

    def __str__(self):
        return self.name

class Theloai(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='ID Thể loại')
    chude = models.ForeignKey(Chude, on_delete=models.CASCADE, verbose_name='ID Chủ đề')
    name = models.CharField(max_length=200, verbose_name='Tên thể loại')
    image = models.ImageField(null=True, blank=True)

    class Meta:
        verbose_name = 'Thể loại'
        verbose_name_plural = 'Các thể loại'

    def __str__(self):
        return self.name

    @property
    def ImageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url 


class Album(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='ID Album')
    name = models.CharField(max_length=200, verbose_name='Tên Album')
    casi_album = models.CharField(max_length=200, verbose_name='Tên Ca Sĩ Album')
    image = models.ImageField(null=True, blank=True)

    class Meta:
        verbose_name = 'Album'
        verbose_name_plural = 'Các Album'

    def __str__(self):
        return self.name

    @property
    def ImageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url 


class Playlist(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='ID Playlist')
    name = models.CharField(max_length=200, verbose_name='Tên Playlist')
    image = models.ImageField(null=True, blank=True)
    songs = models.ManyToManyField('self', related_name='playlists', blank=True, symmetrical=False)

    class Meta:
        verbose_name = 'Playlist'
        verbose_name_plural = 'Các Playlists'

    def __str__(self):
        return self.name
    
    @property
    def ImageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url 

class Baihat(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='ID Bài hát')
    album = models.ForeignKey(Album, on_delete=models.CASCADE, verbose_name='ID Album')
    theloai = models.ForeignKey(Theloai, on_delete=models.CASCADE, verbose_name='ID Thể loại')
    playlist = models.ForeignKey(Playlist, on_delete=models.CASCADE, verbose_name='ID Playlist')
    ten = models.CharField(max_length=200, verbose_name='Tên Bài hát')
    image = models.ImageField(null=True, blank=True)
    casi = models.CharField(max_length=200, verbose_name='Ca sĩ')
    audio = models.FileField(upload_to='audios/', default='', null=True, blank=True)
    luotthich = models.IntegerField(default=0, verbose_name='Lượt thích')

    

    class Meta:
        verbose_name = 'Bài hát'
        verbose_name_plural = 'Các Bài hát'

    def __str__(self):
        return self.ten
    
    @property
    def ImageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url 
    @property
    def AudioURL(self):
        try:
            url = self.audio.url
        except:
            url = ''
        return url 



class Quangcao(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='ID Quảng cáo')
    image = models.ImageField(null=True, blank=True)
    baihat = models.ForeignKey(Baihat, on_delete=models.CASCADE, verbose_name='ID Bài hát')

    class Meta:
        verbose_name = 'Quảng cáo'
        verbose_name_plural = 'Các Quảng cáo'

    def __str__(self):
        return f"Quảng cáo {self.id}"

    @property
    def ImageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url










