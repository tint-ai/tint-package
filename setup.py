from setuptools import setup

setup(name='tintpkg',
      version='0.1',
      description='tint.ai utils package',
      url='https://github.com/tint-ai/tint-package',
      author='Chedhli Bourguiba',
      author_email='chedly@tint.ai',
      license='MIT',
      packages=['tintpkg'],
      install_requires=[
          'datarobot ',
          'pandas',
          'boto3',
      ],
      zip_safe=False)