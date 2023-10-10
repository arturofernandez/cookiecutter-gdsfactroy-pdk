import gdsfactory as gf

from {{ cookiecutter.pdk_name }}.config import PATH

import gdsfactory as gf
from pydantic import BaseModel
from gdsfactory.typings import Layer
from functools import partial
from gdsfactory.technology import LayerLevel, LayerStack, LayerViews
from gdsfactory.cross_section import cross_section, Section

# Define PDK Materials
class LayerMap(BaseModel):
    WG: Layer = (1, 0)
    
LAYER = LayerMap()

nm = 1e-3

def get_layer_stack_{{ cookiecutter.pdk_name }}(
    wg_thickness: float = 300 * nm,

) -> LayerStack:
    """Returns {{ cookiecutter.pdk_name }} LayerStack"""

    class {{ cookiecutter.pdk_name }}LayerStack(LayerStack):
        Si = LayerLevel(
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