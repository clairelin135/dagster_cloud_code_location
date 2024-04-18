from setuptools import find_packages, setup

setup(
    name="quickstart_etl",
    packages=find_packages(exclude=["quickstart_etl_tests"]),
    install_requires=[
        "dagster==1.7.2rc3",
        "dagster-cloud==1.7.2rc3",
        "boto3",
        "pandas",
        "matplotlib",
        "gql",
        "requests_toolbelt",
        "dagster-gcp==0.23.2rc3",
        "dagster-dbt==0.23.2rc3",
    ],
    extras_require={"dev": ["dagster-webserver", "pytest"]},
)
