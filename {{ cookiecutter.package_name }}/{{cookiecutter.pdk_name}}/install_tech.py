"""Symlink tech to klayout."""
import os
import pathlib
import shutil
import sys

def remove_path_or_dir(dest: pathlib.Path):
    if dest.is_dir():
        os.unlink(dest)
    else:
        os.remove(dest)

def make_link(src, dest, overwrite: bool = True) -> None:
    dest = pathlib.Path(dest)
    if dest.exists() and not overwrite:
        print(f"{dest} already exists")
        return
    if dest.exists() or dest.is_symlink():
        print(f"removing {dest} already installed")
        remove_path_or_dir(dest)
    try:
        os.symlink(src, dest, target_is_directory=True)
    except OSError:
        shutil.copy(src, dest)
    print("link made:")
    print(f"From: {src}")
    print(f"To:   {dest}")

if __name__ == "__main__":
    import gdsfactory as gf
    from gdsfactory.technology.klayout_tech import KLayoutTechnology
    from gdsfactory.technology import  LayerViews

    from config import PATH
    
    {%+ if cookiecutter.pdk_tech_files == "From GDSFactory LayerViews Python Class generate KLayout Files" %}
    # TODO: Export using somethink similar to to_lyp
    
    {%+ elif cookiecutter.pdk_tech_files == "From existing KLayout Files generate GDSFactory LayerViews Python Class" %}
    LAYER_VIEWS = LayerViews(filepath=PATH.lyp)
    LAYER_VIEWS.to_yaml(layer_file=PATH.yaml)
    print(LAYER_VIEWS)

    {%+ elif cookiecutter.pdk_tech_files == "From GDSFactory YMAL generate KLayout Files" %}
    LAYER_VIEWS = LayerViews(filepath=PATH.yaml)
    LAYER_VIEWS.to_lyp(filepath=PATH.lyp)
    print(LAYER_VIEWS)
    {% endif %}


    # TODO: Revise code below
    # klayout_folder = "KLayout" if sys.platform == "win32" else ".klayout"
    # cwd = pathlib.Path(__file__).resolve().parent
    # home = pathlib.Path.home()
    # src = cwd / "{{ cookiecutter.pdk_name }}" / "klayout"
    # dest_folder = home / klayout_folder / "tech"
    # dest_folder.mkdir(exist_ok=True, parents=True)
    # dest = dest_folder / "{{ cookiecutter.pdk_name }}"
    # make_link(src=src, dest=dest)