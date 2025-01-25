from django.contrib.auth.password_validation import (
    MinimumLengthValidator,
    CommonPasswordValidator,
    NumericPasswordValidator,
    UserAttributeSimilarityValidator,
)

class SilentMinimumLengthValidator(MinimumLengthValidator):
    def get_help_text(self):
        return ""

class SilentCommonPasswordValidator(CommonPasswordValidator):
    def get_help_text(self):
        return ""

class SilentNumericPasswordValidator(NumericPasswordValidator):
    def get_help_text(self):
        return ""

class SilentUserAttributeSimilarityValidator(UserAttributeSimilarityValidator):
    def get_help_text(self):
        return ""