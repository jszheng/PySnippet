from jinja2 import Template, Environment, FileSystemLoader

string = """\
Hello {{ name }}!"""

template = Template(string)
out = template.render(name='jszheng')
print(out)

env = Environment(loader=FileSystemLoader('./templates'))
template = env.get_template('test1.txt')
print(template.render(name='Jason'))