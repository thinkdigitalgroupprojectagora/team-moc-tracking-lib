from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='tracking_lib',
    version='0.1.0',
    url='https://github.com/thinkdigitalgroupprojectagora/team-moc-tracking-lib',
    author='Damianos Damianidis',
    author_email='damianosd@projectagora.com',
    description='A library for tracking transactions in Flask and FastAPI applications.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=find_packages(),    
    install_requires=[
        'fastapi==0.103.1', 
        'Flask==2.2.3',
        'functions-framework==3.5.0',
        'requests==2.31.0'
    ]
)