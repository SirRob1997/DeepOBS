from setuptools import setup, find_packages

setup(name='deepobs',
      version='1.0.1',
      description='Deep Optimization Benchmark Suite',
      url='https://github.com/fsschneider/DeepOBS',
      author='Frank Schneider, Lukas Balles',
      author_email='frank.schneider@tuebingen.mpg.de',
      license='MIT',
      packages=find_packages(),
      install_requires=[
          'argparse',
          'importlib',
          'numpy',
          'seaborn',
          'matplotlib2tikz',
          'pandas'],
      scripts=['scripts/deepobs_prepare_data.sh',
               'scripts/deepobs_run_sgd.py',
               'scripts/deepobs_run_momentum.py',
               'scripts/deepobs_run_adam.py',
               'scripts/deepobs_plot_results.py',
               'scripts/deepobs_estimate_runtime.py'],
      package_data={
          # txt files in baselines folder
          '': ['*.pickle', 'events.*']},
      zip_safe=False)
