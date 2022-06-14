from pathlib import Path

from setuptools import setup

CURRENT_DIR = Path(__file__).parent


def get_long_description():
    readme_md = CURRENT_DIR / "README.md"
    with open(readme_md, encoding="utf8") as ld_file:
        return ld_file.read()


setup(
    name="objerve",
    version="0.1.0",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    description="Tiny observer for the attributes of Python objects.",
    keywords=["monitoring", "hook", "observer"],
    author="Furkan Onder",
    author_email="furkanonder@protonmail.com",
    url="https://github.com/furkanonder/objerve",
    license="MIT",
    python_requires=">=3.0",
    py_modules=["objerve"],
    install_requires=[],
    extras_require={},
    zip_safe=False,
    include_package_data=False,
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: End Users/Desktop",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities",
        "Operating System :: POSIX :: Linux",
        "Operating System :: Unix",
        "Operating System :: Microsoft :: Windows",
    ],
)
