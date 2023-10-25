from django.contrib.auth.models import UserManager, AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.contrib.postgres.fields import ArrayField

class CustomUserManager(UserManager):
    def _create_user(self, username, email, password, **extra_fields):
        
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user
    
    def create_user(self, username=None, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)

        return self._create_user(username, email, password, **extra_fields)
    
    def create_superuser(self, username=None, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self._create_user(username, email, password, **extra_fields)
    
class User(AbstractBaseUser, PermissionsMixin):
    ROLE = (('Participant','Participant'),('Owner Event','Owner Event'),('Owner Event and Participant','Owner Event and Participant'))
    CATEGORY = {
        "Deportivo",
        "Musical",
        "Gastronomico",
        "Cultural",
        "Ayuda Social",
        "Mascotas",
        "Academico",
        "Tecnologico",
        "CompraVenta",
    }

    username = models.CharField(max_length=255, blank=True, default='', unique=True)
    email = models.EmailField(blank=True, default='')
    role = models.CharField(max_length=255, choices=ROLE, blank=True, default='')
    location = models.CharField(max_length=255, blank=True, default='')
    age = models.CharField(max_length=255, blank=True, default='')
    CategoriaInteres = ArrayField(models.CharField(max_length=255), blank=True, default=list)

    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    date_joined = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(blank=True, null=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'
    ROLE_FIELD = 'role'
    AGE_FIELD = 'age'
    LOCATION_FIELD = 'location'
    REQUIRED_FIELDS = [EMAIL_FIELD, ROLE_FIELD, AGE_FIELD, LOCATION_FIELD]

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def get_full_name(self):
        return self.username
    
    def get_short_name(self):
        return self.username or self.email.split('@')[0]

