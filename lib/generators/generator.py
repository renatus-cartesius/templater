import j2


class Generator(object):
    """docstring for Generator. Now in development phase"""

    def __init__(self, main, templateName):
        super(Generator, self).__init__()
        self.main = main
        self.template = open("../templates/", str(templateName))

        self.env = j2.Environment(loader=j2.FileSystemLoader("../vagrant/"))
        template = self.env.get_template("Vagrantfile.j2")

        print("Please, input the hostname: ")
        hostname = str(input())

        content = template.render(hostname=hostname)

        print(content)
