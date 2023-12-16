from __future__ import annotations

import gdsfactory as gf
from gdsfactory.get_factories import get_cells
from gdsfactory.cross_section import get_cross_section_factories
from gdsfactory.pdk import Pdk, constants

from {{ cookiecutter.pdk_name }} import components
from {{ cookiecutter.pdk_name }}.config import PATH
from {{ cookiecutter.pdk_name }}.tech import LAYER

from gdsfactory.technology import LayerView, LayerViews

cells = get_cells([components])
cross_sections = get_cross_section_factories(LAYER)

PDK = Pdk(
    name="{{ cookiecutter.pdk_name }}",
    cells=cells,
    cross_sections=cross_sections,
    layers=LAYER.dict(),
    layer_stack=None,
    {%- if cookiecutter.pdk_tech_files == "From GDSFactory LayerViews Python Class generate KLayout Files" -%}
    layer_views={{ cookiecutter.pdk_name }}.tech.LAYER_VIEWS,
    {%- elif cookiecutter.pdk_tech_files == "From existing KLayout Files generate GDSFactory LayerViews Python Class" -%}
    layer_views= LayerViews(filepath=PATH.lyp),
    {%- elif cookiecutter.pdk_tech_files == "From GDSFactory YMAL generate KLayout Files" -%}
    layer_views= LayerViews(filepath=PATH.yaml),
    {% endif %}

    # layer_transitions=LAYER_TRANSITIONS,
    # sparameters_path=PATH.sparameters,
    constants=constants,
)

# TODO: Remove if not needed
gf.routing.all_angle.LOW_LOSS_CROSS_SECTIONS = [
    {"cross_section": "rib", "settings": {"width": 2.5}},
    {"cross_section": "strip", "settings": {"width": 6.0}},
    {"cross_section": "strip", "settings": {"width": 3.0}},
]

PDK.activate()
__version__ = "0.0.1"

if __name__ == "__main__":
    # layer_views = LayerViews(filepath=PATH.lyp_yaml)
    # layer_views.to_lyp(PATH.lyp)
    print(PDK.name)