from .key import rand_key


class Config:
    SECRET_KEY = rand_key(0, 256)
