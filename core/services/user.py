from django.contrib.auth import get_user_model


User = get_user_model()


def is_active_email(email: str) -> bool:
    return User.objects.filter(email=email).exists()
