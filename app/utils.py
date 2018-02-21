import string, random

def generator_code(size=6,chars = string.ascii_lowercase+ string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def create(instance, size = 6):
    new_code = generator_code(size=size)
    Shortner = instance.__class__
    sh_exist = Shortner.objects.filter(shortcode = new_code).exists()

    if sh_exist:
        return create(size=size)
    return new_code