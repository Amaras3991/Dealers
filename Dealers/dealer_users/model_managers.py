from django.contrib.auth.models import BaseUserManager


class CustomUserManager(BaseUserManager):
    def _create_user(self, username, email, password,
        is_staff, is_superuser, is_admin, is_dealer, **extra_fields):
        """
        Creates and saves a User with the given username, email and password.
        """
        if not username:
            raise ValueError('The given username must be set')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, is_admin=is_admin,
            is_staff=is_staff, is_active=True,
            is_superuser=is_superuser, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user


    def create_user(self, username, email=None, password=None,
                    **extra_fields):
        return self._create_user(username, email, password, False, False, False, False, **extra_fields)


    def create_superuser(self, username, email, password,
                         **extra_fields):
        return self._create_user(username, email, password, True, True, True, True,  **extra_fields)

    def create_dealer(self, username, email, password,
                      **extra_fields):
        return self._create_user(username, email, password, False, False, False, True, **extra_fields)