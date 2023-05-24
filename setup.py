from pathlib import Path
from setuptools import setup, find_packages

def readme():
  with open('README.md', 'r') as f:
    return f.read()

ROOT_DIR = Path(__file__).resolve().parent
REQUIREMENTS_DIR = ROOT_DIR / "requirements"
def list_reqs(fname="requirements.txt"):
    with open(REQUIREMENTS_DIR / fname) as fd:
        return fd.read().splitlines()

setup(
  name='RealEstate_package',
  version='1.3.0',
  license="BSD-3",
  author='Клейменов А., Толстенко Л.',
  author_email='notmy@gmail.com',
  description='МЛ-модель, предсказывающая стоимость недвижимости по её параметрам.',
  long_description=readme(),
  long_description_content_type='text/markdown',
  url='https://github.com/Lada-Rom/RealEstate_package',
  packages=find_packages(),
  include_package_data=True,
  install_requires=list_reqs(),
  extras_require={},
  classifiers=[
    'Programming Language :: Python :: 3.8',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent'
  ],
  keywords='lightgbm python real_estate price',
  project_urls={
    'Documentation': 'https://github.com/Lada-Rom/RealEstate_package'
  },
  python_requires='>=3.7'
)
