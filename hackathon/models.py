
import uuid

# from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from stdimage.models import StdImageField


class UsuarioManager(BaseUserManager):

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('O e-mail é obrigatório')
        email = self.normalize_email(email)
        user = self.model(email=email, username=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        # extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser precisa ter is_superuser=True')

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser precisa ter is_staff=True')

        return self._create_user(email, password, **extra_fields)


def get_file_path(_instace, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return filename


class Estado(models.Model):
    nome = models.CharField('Nome', max_length=80)
    descricao = models.CharField('Sub Título', max_length=280)
    banner = StdImageField('Banner', upload_to=get_file_path,)
    iframe_url = models.URLField('Link 3D', null=True, blank=True)

    class Meta:
        verbose_name = 'Estado'

    def __str__(self):
        return self.nome


class Lugar(models.Model):
    estado = models.ForeignKey(
        Estado, verbose_name='Estado', on_delete=models.CASCADE)
    preco = models.DecimalField(
        'Preço', null=True, blank=True, max_digits=19, decimal_places=2)
    nome = models.CharField('Titulo', max_length=160)
    descricao = models.CharField('Sub Título', max_length=280)
    bio = models.TextField('Texto de apresentação', null=True, blank=True)
    banner = StdImageField('Banner', upload_to=get_file_path,)
    iframe_url = models.URLField('Link 3D', null=True, blank=True)

    class Meta:
        verbose_name = 'Lugar'

    def __str__(self):
        return self.nome


class Atividade(models.Model):
    lugar = models.ForeignKey(
        Lugar, verbose_name='Lugar', on_delete=models.CASCADE)
    nome = models.CharField('Nome', max_length=80)
    descricao = models.CharField('Sub Título', max_length=280)
    preco = models.DecimalField(
        'Preço', null=True, blank=True, max_digits=19, decimal_places=2)
    banner = StdImageField('Banner', upload_to=get_file_path,)
    iframe_url = models.URLField('Link 3D', null=True, blank=True)

    class Meta:
        verbose_name = 'Atividade'

    def __str__(self):
        return self.nome


class Hospedagem(models.Model):
    lugar = models.ForeignKey(
        Lugar, verbose_name='Lugar', on_delete=models.CASCADE)
    nome = models.CharField('Nome', max_length=80)
    descricao = models.CharField('Sub Título', max_length=280)
    preco = models.DecimalField(
        'Preço', null=True, blank=True, max_digits=19, decimal_places=2)
    banner = StdImageField('Banner', upload_to=get_file_path,)
    iframe_url = models.URLField('Link 3D', null=True, blank=True)

    class Meta:
        verbose_name = 'Hospedagem'

    def __str__(self):
        return self.nome


class Restaurante(models.Model):
    lugar = models.ForeignKey(
        Lugar, verbose_name='Lugar', on_delete=models.CASCADE)
    preco = models.DecimalField(
        'Preço', null=True, blank=True, max_digits=19, decimal_places=2)
    nome = models.CharField('Nome', max_length=80)
    descricao = models.CharField('Sub Título', max_length=280)
    banner = StdImageField('Banner', upload_to=get_file_path,)
    iframe_url = models.URLField('Link 3D', null=True, blank=True)

    class Meta:
        verbose_name = 'Restaurante'

    def __str__(self):
        return self.nome


class Viagem(models.Model):
    salario = models.DecimalField(
        'Salario', null=True, blank=True, max_digits=19, decimal_places=2)
    porcentagem = models.DecimalField(
        'Porcentagem', null=True, blank=True, max_digits=19, decimal_places=0)
    estado = models.ForeignKey(
        Estado, verbose_name='Estado', on_delete=models.CASCADE)
    lugar = models.ForeignKey(
        Lugar, verbose_name='Lugar', on_delete=models.CASCADE)

    def __str__(self):
        return 'viajem'


class Extras(models.Model):
    viagem = models.ForeignKey(
        Viagem, verbose_name='Viagem', on_delete=models.CASCADE, default="")
    ativadade = models.ForeignKey(
        Atividade, verbose_name='Atividade', on_delete=models.CASCADE, default="")
    hospedagem = models.ForeignKey(
        Hospedagem, verbose_name='Hospedagem', on_delete=models.CASCADE, default="")
    restaurante = models.ForeignKey(
        Restaurante, verbose_name='Restaurante', on_delete=models.CASCADE, default="")

    def __str__(self):
        return 'extras'


class CustomUsuario(AbstractUser):
    email = models.EmailField('E-mail', unique=True)
    salario = models.DecimalField(
        'Salario', null=True, blank=True, max_digits=19, decimal_places=2)
    porcentagem = models.DecimalField(
        'Porcentagem', null=True, blank=True, max_digits=19, decimal_places=0)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return self.email

    objects = UsuarioManager()
