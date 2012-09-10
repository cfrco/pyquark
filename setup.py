from distutils.core import setup

from pyquark import __version__

setup(
        name = 'pyquark',
        description = 'A Python base web develop,admin and deploy tool kit',
        version = __version__,
        author = 'cfrco',
        author_email='z82206.cat@gmail.com',
        packages = ['pyquark','pyquark.admin','pyquark.web','pyquark.dev']
)
