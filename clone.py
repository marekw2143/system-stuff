import subprocess

names = (
	'_proto3',
	'proxy',
	'miarka',
	'ip',
	'Kalkulator',
	'comp',
	'formula_finder',
	'binary_keyboard',
	'mki2',
)

def get_addr_from_name(name):
	return "git://github.com/marekw2143/%s.git" % name

for name in names:
	subprocess.call(['git', 'clone', get_addr_from_name(name)])
