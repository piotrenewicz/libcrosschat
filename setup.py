from setuptools import setup

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

print(requirements)
exit()
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