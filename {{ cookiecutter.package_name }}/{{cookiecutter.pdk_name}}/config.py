__all__ = ["PATH"]

import pathlib

home = pathlib.Path.home()
cwd = pathlib.Path.cwd()

cwd_config = cwd / "config.yml" # TODO: Delete if not needed

home_config = home / ".config"  # TODO: Delete if not needed
config_dir = home / ".config"   # TODO: Delete if not needed
config_dir.mkdir(exist_ok=True)
module_path = pathlib.Path(__file__).parent.absolute()
repo_path = module_path.parent

class Path:
    module = module_path
    repo = repo_path

    tech_dir = module_path / "klayout"
    lyp = module_path / tech_dir / "{{ cookiecutter.pdk_lyp_name }}.lyp"
    lyt = module_path / tech_dir / "{{ cookiecutter.pdk_lyt_name }}.lyt"

    lyp_2_yaml = module_path / "{{ cookiecutter.pdk_layers_yaml_name }}.yaml"

    ip_blocks_dir = module_path / "ip_blocks"
    examples_dir = module_path / "examples"
    components_dir = module_path / "components"

PATH = Path()

if __name__ == "__main__":
    print(PATH)
