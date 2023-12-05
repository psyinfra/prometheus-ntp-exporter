from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()
long_description = (here / "README.md").read_text(encoding="utf-8")

setup(
    name='prometheus_ntp_exporter',
    version='1.0.0',
    description='Python-based Prometheus exporter for NTP response offset',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/psyinfra/prometheus-ntp-exporter",
    project_urls={
        "Bug Reports":
            "https://github.com/psyinfra/prometheus-ntp-exporter/issues",
        "Source":
            "https://github.com/psyinfra/prometheus-ntp-exporter",
    },
    author='Niels Reuter',
    author_email='n.reuter@fz-juelich.de',
    keywords="ntp, monitoring, prometheus",
    packages=find_packages(),
    license='ISC',
    install_requires=[
        'ntplib',
        'prometheus_client'
    ],
    python_requires=">=3.7, <4",
    entry_points={
        'console_scripts': [
            'prometheus_ntp_exporter=prometheus_ntp_exporter.main:main'
        ],
    },
)
