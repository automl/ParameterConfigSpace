import setuptools

setuptools.setup(name="ParameterConfigSpace",
                 description="parameter configuration space parser for SMAC format",
                 version="0.1dev",
                 packages=setuptools.find_packages(exclude=["*.unittests.*", "unittests.*", "unittests"]),
                 install_requires=["numpy==1.9.2"],
                 package_data={'': ['*.txt', '*.md']},
                 author="Marius Lindauer",
                 author_email="lindauer@cs.uni-freiburg.de",
                 license="GPLv2",
                 platforms=['Linux'],
                 classifiers=[],
                 url="https://github.com/automl/ParameterConfigSpace")
