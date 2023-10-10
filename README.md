# cookiecutter-gdsfactroy-pdk
Cookiecutter Template for GDS Factory PDKs

# Quick Set up
1. Clone this repository
2. Run `cookiecutter cookiecutter-gdsfactroy-pdk` on the command promt
3. Answare all the questions:
```
package_name [your_package_name]: test_pdk
pdk_name [your_PDK]: gtest
pdk_lyt_name [your_PDK]: gtest_lyt
pdk_layers_yaml_name [your_PDK]: gtest_yaml
package_version [0.0.1]: 0
package_description [your package description. What is this package for?]: This is a test PDK
package_url [https://github.com/]: test_pdk
author_email [your_email@gmail.com]: helo@test_pdk.com
Select cicd:
1 - github
2 - gitlab
Choose from 1, 2 [1]: 1
```