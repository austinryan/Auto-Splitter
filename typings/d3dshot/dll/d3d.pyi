import ctypes

import comtypes
from _typeshed import Incomplete
from typing_extensions import TypeAlias

Pointer: TypeAlias = Incomplete


class DXGI_SAMPLE_DESC(ctypes.Structure):
    ...


class D3D11_BOX(ctypes.Structure):
    ...


class D3D11_TEXTURE2D_DESC(ctypes.Structure):
    ...


class ID3D11DeviceChild(comtypes.IUnknown):
    ...


class ID3D11Resource(ID3D11DeviceChild):
    ...


class ID3D11Texture2D(ID3D11Resource):
    ...


class ID3D11DeviceContext(ID3D11DeviceChild):
    ...


class ID3D11Device(comtypes.IUnknown):
    ...


def initialize_d3d_device(dxgi_adapter: Pointer) -> tuple[Pointer, Pointer]: ...
def describe_d3d11_texture_2d(d3d11_texture_2d: Pointer) -> D3D11_TEXTURE2D_DESC: ...
def prepare_d3d11_texture_2d_for_cpu(d3d11_texture_2d: Pointer, d3d_device: Pointer) -> Pointer: ...