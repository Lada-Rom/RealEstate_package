from setuptools import setup, find_packages

def readme():
  with open('README.md', 'r') as f:
    return f.read()

setup(
  name='RealEstate_model',
  version='1.0.0',
  author='Клейменов А., Толстенко Л.',
  author_email='8)',
  description='МЛ-модель, предсказывающая стоимость недвижимости по её параметрам.',
  long_description=readme(),
  long_description_content_type='text/markdown',
  url='https://github.com/Lada-Rom/RealEstate_model',
  packages=find_packages(),
  install_requires=[
  	'anyio==3.6.2', 'click==8.1.3', 'fastapi==0.95.2',
	'h11==0.14.0', 'idna==3.4', 'joblib==1.2.0',
	'lightgbm==3.3.5', 'numpy==1.24.3', 'pandas==2.0.1',
	'pydantic==1.10.7', 'python-dateutil==2.8.2', 'pytz==2023.3',
	'scikit-learn==1.2.2', 'scipy==1.10.1', 'six==1.16.0',
	'sniffio==1.3.0', 'starlette==0.27.0', 'threadpoolctl==3.1.0',
	'typing_extensions==4.5.0', 'tzdata==2023.3', 'uvicorn==0.22.0'],
  classifiers=[
    'Programming Language :: Python :: 3.8',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent'
  ],
  keywords='lightgbm python real_estate price',
  project_urls={
    'Documentation': 'https://github.com/Lada-Rom/RealEstate_model'
  },
  python_requires='>=3.7'
)
