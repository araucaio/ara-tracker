from setuptools import setup, find_packages

long_description = """Multiple objects tracking with Dlib."""

setup(
    name="ara-tracker",
    version="0.0.1",
    author="Tung Pham",
    author_email="phsontung@gmail.com",
    url="https://github.com/araucaio/ara-tracker",
    download_url="https://github.com/araucaio/ara-tracker/archive/0.0.1.tar.gz",
    install_requires=[
        "six",
        "numpy>=1.15",
        "scipy",
        "Pillow",
        "matplotlib",
        "scikit-image>=0.14.2",
        "opencv-python-headless",
        "dlib"
    ],
    packages=find_packages(),
    include_package_data=True,
    package_data={
        "": ["LICENSE", "README.md", "requirements.txt"],
    },
    license="MIT",
    description="Multiple objects tracking with Dlib",
    long_description=long_description,
    keywords=["dlib", "tracker", "computer vision", "yolov3", "mot", "opencv", "multithread"]
)
