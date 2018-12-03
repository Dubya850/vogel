from distutils.core import setup

setup(name='vogel',
      version='0.1',
      author=['Robert Dohner', 'Michael Waldmeier'],
      url='https://github.com/usaa/',
      packages=['vogel', 'vogel.preprocessing', 'vogel.train', 'vogel.utils'],
      description='Vogel is a ML project flow tool, with the primary objective of simplifying actuarial ML processes. It tracks and manages model development from data preparation to results analysis and visualization.',
      install_requires =[
          'scikit-learn>=0.19',
          'statsmodels>=0.9.0',
          'matplotlib>=2.0.2',
          'pandas>=0.20.3',
	  'xgboost>=0.80',
	  'catboost>=0.10.2' 
      ]
)