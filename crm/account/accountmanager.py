from django.contrib.auth.models import BaseUserManager


class AccountManager(BaseUserManager):
    def create_user(self, email, username, password=None, fullname=None, **kwargs):
        if not email:
            raise ValueError('email is required')

        if not username:
            raise ValueError('username is required')

        if not password:
            raise ValueError('password is required')

        user = self.model(
            email=self.normalize_email(email),
            username=username.lower(),
            fullname=fullname.title()
        )

        user.set_password(password)

        user.save(using=self._db)

        return user

    def create_tenant_user(self, email, username, password, fullname):
        if not fullname:
            raise ValueError('fullname is required for tenant accounts')

        user = self.create_user(
            email,
            username,
            password,
            fullname
        )

        user.is_tenant = True

        user.save(using=self._db)

        return user

    def create_superuser(self, email, username, password, fullname):
        if not fullname:
            raise ValueError('fullname is required for admin accounts')

        user = self.create_user(
            email,
            username,
            password,
            fullname
        )

        user.is_super_admin = True

        user.is_admin = True

        user.is_superuser = True

        user.is_staff = True

        user.is_tenant = False

        user.save(using=self._db)

        return user
