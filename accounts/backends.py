from django.contrib.auth.backends import ModelBackend as BaseModeBackend
from .models import User

class ModelBackend(BaseModeBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        if not username is None:
            try:
                user = User.objects.get(email=username)
                if user.check_password(password):
                    return user
            except User.DoesNotExist:
                pass
