from jinja2 import Template


def main():
    content = {'name': str(input("Hello, how are you name?: "))}
    template = 'Ok, so hello {{ name }}'
    result = Template(template).render(content)
    print(result)
