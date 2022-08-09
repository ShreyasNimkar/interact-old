from atexit import register
from django import template

register=template.Library()


def index(indexable, i):
    return indexable[i]

def same(a,b):
    return a==b

register.filter('index',index)
register.filter('same',same)