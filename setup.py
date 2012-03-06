from setuptools import setup

setup(name='Bebop',
      version='0.1',
      author='Zach Kelling',
      packages=['bebop'],
      description='WebSocket web app reloader for rapid development',
      install_requires=['autobahn', 'twisted', 'watchdog']
)