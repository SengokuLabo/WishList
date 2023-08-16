from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.utils.translation import gettext_lazy as _

class CustomUser(AbstractUser):
    # ここにユーザーアカウントに関するカスタムフィールドを追加できます
    groups = models.ManyToManyField(
        Group,
        verbose_name=_('groups'),
        blank=True,
        related_name='custom_user_set',  # ここでrelated_nameを変更
        help_text=_('The groups this user belongs to. A user will get all permissions granted to each of their groups.'),
        related_query_name='user',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('user permissions'),
        blank=True,
        related_name='custom_user_set',  # ここでrelated_nameを変更
        help_text=_('Specific permissions for this user.'),
        related_query_name='user',
    )
