from django.contrib.auth.tokens import PasswordResetTokenGenerator
# from django.utils import six

# https://docs.djangoproject.com/en/2.2/_modules/django/utils/six/
class TokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return (
            str(user.pk) + str(timestamp) +
            str(user.is_active)
        )
account_activation_token = TokenGenerator()