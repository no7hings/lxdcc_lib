# coding:utf-8
name = 'lxdcc_lib'

version = '0.0.15'

description = ''

authors = ['']

tools = []

requires = []


def commands():
    import platform
    # utility-package
    env.PYTHONPATH.append('{root}/lib/python-2.7/site-packages')
    # linux-package
    if platform.system() == 'Linux':
        env.PYTHONPATH.append('{root}/lib/linux-python-2.7/site-packages')
        env.PYTHONPATH.append('{root}/lib/linux-x64-python-2.7/site-packages')
    else:
        pass


timestamp = 1608028331

format_version = 2
