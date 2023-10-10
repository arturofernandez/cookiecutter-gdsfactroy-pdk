# {{cookiecutter.package_name}}
{{cookiecutter.package_description}}

# PDK Quick Set Up:
1. Replace or develop your PDKs `.lyp` and `.lyt` files (a template is provided)
2. Run `{{cookiecutter.pdk_name}}\install_tech.py`. If you are using anaconda you can do:
```
conda activate $your_env_name$
python {{cookiecutter.pdk_name}}\install_tech.py
```
3. To check the PDK is working correcly run `example\activate_pdk.py` where one of the outputs must be:
```
gdsfactory.pdk:activate:316 - '{{cookiecutter.pdk_name}}' PDK is now active
```