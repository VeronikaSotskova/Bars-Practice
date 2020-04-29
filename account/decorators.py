from django.contrib.auth.decorators import user_passes_test

from account.models import CustomUser


def manager_perm_required(function=None, login_url=None):
    """
    Decorator for views that checks that the user is manager
    """
    decorator = user_passes_test(
        lambda u: u.is_manager(),
        login_url=login_url,
    )
    if function:
        return decorator(function)
    return decorator
