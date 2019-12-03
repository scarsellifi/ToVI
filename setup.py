from setuptools import setup

setup(name='tovi',
      version='0.1',
      description='upload video from different source in easy way',
      url='https://#',
      author='Marco Scarselli',
      author_email='scarselli@gmail.com',
      license='MIT',
      packages=['tovi'],
      install_requires=[
          'pytube',
          'video_indexer==0.1.6'
      ],
      zip_safe=False)