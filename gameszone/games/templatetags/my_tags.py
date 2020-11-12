from django import template
register = template.Library()

@register.filter(nam='get_urls')
def get_url_list(images):
    urls=[]
    for image in images:
        urls.append(image.image.url)
    return urls