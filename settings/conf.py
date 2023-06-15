from decouple import config


SECRET_KEY = config('SECRET_KEY', cast=str)
DEBUG = config('DEBUG', cast=bool)
print("[INFO]", config('TEST_MESSAGE'))
