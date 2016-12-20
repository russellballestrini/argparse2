from os import environ
from argparse import ArgumentParser

class EnvParser(ArgumentParser):

    def _get_env_var_name(self, flag_name):
        """--port becomes PROG_PORT"""
        return '{}_{}'.format(self.prog, flag_name.lstrip('-')).replace('-', '_').upper()

    def add_argument(self, *args, **kwargs):
        flag_name = args[1].lstrip('-') if len(args) == 2 else args[0].lstrip('-')
        env_var = self._get_env_var_name(flag_name)
        default = environ.get(env_var, kwargs.get('default', ''))
        help_text = kwargs.get('help', '') + ', {}={}'.format(env_var, flag_name)
        del kwargs['default']
        del kwargs['help']
        return super(EnvParser, self).add_argument(*args, default=default, help=help_text, **kwargs)

