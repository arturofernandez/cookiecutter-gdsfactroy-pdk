import gdsfactory as gf

from {{ cookiecutter.pdk_name }}.config import PATH

import gdsfactory as gf
from pydantic import BaseModel
from gdsfactory.typings import Layer
from functools import partial
from gdsfactory.technology import LayerLevel, LayerStack, LayerView, LayerViews
from gdsfactory.cross_section import cross_section, Section

# Define PDK Materials
class LayerMap(BaseModel):
    WG: Layer = (1, 0)
    
LAYER = LayerMap()

{%- if cookiecutter.pdk_tech_files == "From GDSFactory LayerViews Python Class generate KLayout Files" -%}

class LayerViews(LayerViews):
    WG_CORE: LayerView = LayerView(color='blue')

LAYER_VIEWS = LayerViews(layer_map=LAYER.dict())

{% endif %}

nm = 1e-3

def get_layer_stack_{{ cookiecutter.pdk_name }}(
    wg_thickness: float = 300 * nm,

) -> LayerStack:
    """Returns {{ cookiecutter.pdk_name }} LayerStack"""

    class {{ cookiecutter.pdk_name }}LayerStack(LayerStack):
        Si : LayerLevel = LayerLevel(
            layer=LAYER.WG,
            thickness=wg_thickness,
            zmin=0,
            material="Si",
        )
               
    return {{ cookiecutter.pdk_name }}LayerStack()

LAYER_STACK = get_layer_stack_{{ cookiecutter.pdk_name }}()

# Define PDKs Crossections

wg = partial(gf.cross_section.cross_section, layer=LAYER.WG)
cross_sections = dict(
    wg = wg,
)