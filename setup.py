import setuptools

from portfolio import __version__

with open('README.md', 'r', encoding='utf-8') as fp:
    long_description = fp.read()

requirements = set()
with open(f'requirements/prod.txt', encoding='utf-8') as fp:
    for line in fp:
        line = line.strip()
        if line.startswith('git'):  # handle private repositories
            requirements.add(f'{line.split("/")[-1].split(".git")[0]} @ {line}')
        elif not line or line.startswith('-') or line.startswith('#'):
            continue  # ignore other files including and comments
        else:
            requirements.add(line)

setuptools.setup(
    name='portfolio',
    version=__version__,
    author='Ihar Yazerski',
    author_email='ihar.yazerski@gmail.com',
    description='My modest portfolio',
    include_package_data=True,
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://iyazerski.me/',
    packages=setuptools.find_packages(exclude=('tests*',)),
    install_requires=sorted(requirements),
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.9'
)
