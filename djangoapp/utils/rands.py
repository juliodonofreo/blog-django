import random
import string

from django.utils.text import slugify


def random_letters(length=5):
    if length < 0:
        raise ValueError("O tamanho não pdoe ser negativo.")

    return "".join(random.choices(string.ascii_lowercase, k=length))


def random_slugify(text, extra_length):
    return slugify(text) + "-" + random_letters(length=extra_length)


if __name__ == "__main__":
    random_string = random_letters(length=10)
    print(random_string)
    
    random_slug = random_slugify("bla bla bla", 5)
    print(random_slug)