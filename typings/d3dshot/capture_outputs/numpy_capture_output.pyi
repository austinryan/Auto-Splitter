import numpy as np
import numpy.typing as npt
from _typeshed import Incomplete
from d3dshot.capture_output import CaptureOutput as CaptureOutput
from PIL.Image import Image
from typing_extensions import TypeAlias

Pointer: TypeAlias = Incomplete
NDArray: TypeAlias = npt.NDArray[np.int32]


class NumpyCaptureOutput(CaptureOutput):
    def __init__(self) -> None: ...

    def process(
        self, pointer: Pointer, size: int, width: int, height: int, region: tuple[int, int, int, int], rotation: int
    ) -> NDArray: ...
    def to_pil(self, frame: NDArray) -> Image: ...
    def stack(self, frames: list[NDArray] | NDArray, stack_dimension: int) -> NDArray: ...