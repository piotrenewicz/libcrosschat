from setuptools import setup
import os

req_path = os.path.join(os.path.dirname(__file__), "requirements.txt")
with open(req_path) as f:
    requirements = f.read().splitlines()

setup(
    name='libcrosschat',
    packages=['libcrosschat'],
    version='1.0.0',
    install_requires=requirements,
    description="Python module to make chatbots for multiple Platforms",
    author='Piotr Morel, Konrad Maciejczyk, Mykhailo Marchenko',
    author_email='piotr.morel@smcebi.edu.pl',
    url='https://github.com/piotrenewicz/libcrosschatrepo',
    keywords=['chatbot', 'chatbots', 'chat-bot', 'chatbot-framework', 'discord', 'telegram', 'facebook messenger', 'python', 'bot'],
    classifiers=[],
)

