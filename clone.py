import subprocess

REPOSITORY_COUNT = 12

names = (
    '_proto3',
    'binary_keyboard',
    'comp',
    'formula_finder',
    'ip',
    'json_deser',
    'miarka',
    'mki2',
    'proxy',
    'system_stuff',
    'Budzik',
    'Kalkulator',
)
assert len(names) == REPOSITORY_COUNT

def get_addr_from_name(name):
    return "git://github.com/marekw2143/%s.git" % name

for name in names:
    subprocess.call(['git', 'clone', get_addr_from_name(name)])
