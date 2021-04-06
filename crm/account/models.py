from django.db import models
from django.contrib.auth.models import AbstractUser
from account.accountmanager import AccountManager
from tenant.models import Tenant
from django.utils.timezone import now

class Account(AbstractUser):
    email = models.EmailField(
        unique=True,
        blank=False,
        null=False,
        max_length=255
    )
    username = models.CharField(
        null=False,
        blank=False,
        max_length=255,
        unique=True
    )

    fullname = models.CharField(
        null=False,
        blank=False,
        max_length=300
    )
    created_at = models.DateTimeField(default=now)

    updated_at = models.DateTimeField(default=now)

    tenant = models.ForeignKey(Tenant, related_name='accounts', null=True, on_delete=models.CASCADE)

    is_tenant = models.BooleanField(default=False)

    is_active = models.BooleanField(default=True)

    is_super_admin = models.BooleanField(default=False)

    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['username', 'fullname']

    objects = AccountManager()

    excludes = 'password'

    def __str__(self):
        if self.fullname == 'null':
            return self.email
        return self.fullname

    def get_email_fullname_all(self):
        user = {'fullname': self.fullname, 'username': self.username}

        return user

    @property
    def is_tenant_user(self):
        return self.is_tenant

    @property
    def is_admin_user(self):
        return self.is_super_admin
