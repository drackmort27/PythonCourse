from setuptools import setup

setup(
    name="mensajes",
    version="2.0",
    description='Un paquete para saludar y despedir',
    author='Luciano somare',
    author_email='luciano@somare',
    url='https://lucianosoma.com.ar',
    packages=["mensajes", "mensajes.hola"],
    scripts=['test.py']
)   