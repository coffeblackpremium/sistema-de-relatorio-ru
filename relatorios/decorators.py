from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import user_passes_test


def user_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='contas/login'):
    
    decorator_actual = user_passes_test(
        lambda user: user.is_active and not user.is_staff or not user.is_superuser,
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )

    if function:
        return decorator_actual(function)
    return decorator_actual
