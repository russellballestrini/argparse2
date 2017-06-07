from os import environ
from argparse import ArgumentParser

class EnvParser(ArgumentParser):

    def _get_env_var_name(self, flag_name):
        """port becomes PROG_PORT"""
        return '{}_{}'.format(self.prog, flag_name).replace('-', '_').upper()

    def add_argument(self, *args, **kw):
        flag_name = args[1].lstrip('-') if len(args) == 2 else args[0].lstrip('-')
        env_var = self._get_env_var_name(flag_name)
        kw['default'] = environ.get(env_var, kw.get('default', ''))
        kw['help'] = kw.get('help', '') + ', {}={}'.format(env_var, flag_name)
        return super(EnvParser, self).add_argument(*args, **kw)

