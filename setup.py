from setuptools import setup

setup(
    name='jwst_planning_tools',
    version='0.0.1',
    packages=['jwst_planning_tools'],
    url='https://github.com/patapisp/jwst_planning_tools',
    license='MIT',
    author='Polychronis Patapis',
    author_email='chronispatapis@gmail.com',
    description='Toolkit for planning JWST/MIRI MRS observations',
    install_requires=["jwst >= 1.12.5",
                      "astropy",
                      "spectres",
                      "matplotlib",
                      "jwst-gtvt",
                      "webbpsf",
                      "photutils",
                      "scipy"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Astronomy",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
)
