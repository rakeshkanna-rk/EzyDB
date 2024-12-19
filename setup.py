from setuptools import setup, find_packages
import json

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("config.json","r") as jfh:
    data = json.load(jfh)

name = data["name"] 
version = data["version"]
desc = data["description"]
auth = data["author"]
auth_mail = data["author_email"]
kw = data["keywords"]
dependency = data["install_requires"]
urls = data["project_urls"]
classifiers = data["classifiers"]

setup(
    name= name,
    version= version,
    description= desc,
    author= auth,
    author_email= auth_mail,
    license="MIT",
    python_requires=">=3.6",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    project_urls= urls,
    keywords= kw,
    install_requires= dependency,
    entry_points={"console_scripts": ["ezydb = EzyDB:cmd_cli"]},
    classifiers= classifiers
)
