import os
from .base import * 
import environ
env  = environ.Env()
environ.Env.read_env()


SECRET_KEY = env.str('DJANGO_SECRET_KEY', '%p8#dko(q2l2d+9-k(f)6w-1p$(*3*y2v#+^ebjxka@og*oocd')

DEBUG = False

ALLOWED_HOSTS = ['portfolioag.herokuapp.com']