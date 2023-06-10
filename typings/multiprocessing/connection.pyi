# https://github.com/python/typeshed/blob/main/stdlib/multiprocessing/connection.pyi
import sys
from types import TracebackType
from typing import Any, Generic, SupportsIndex, TypeVar

from _typeshed import ReadableBuffer
from typing_extensions import Self

_T1 = TypeVar("_T1")
_T2 = TypeVar("_T2")


class _ConnectionBase(Generic[_T1, _T2]):
    def __init__(self, handle: SupportsIndex, readable: bool = True, writable: bool = True) -> None: ...
    @property
    def closed(self) -> bool: ...  # undocumented
    @property
    def readable(self) -> bool: ...  # undocumented
    @property
    def writable(self) -> bool: ...  # undocumented
    def fileno(self) -> int: ...
    def close(self) -> None: ...
    def send_bytes(self, buf: ReadableBuffer, offset: int = 0, size: int | None = None) -> None: ...
    def send(self, obj: _T1) -> None: ...
    def recv_bytes(self, maxlength: int | None = None) -> bytes: ...
    def recv_bytes_into(self, buf: Any, offset: int = 0) -> int: ...
    def recv(self) -> _T2: ...
    def poll(self, timeout: float | None = 0.0) -> bool: ...
    def __enter__(self) -> Self: ...

    def __exit__(
        self, exc_type: type[BaseException] | None, exc_value: BaseException | None, exc_tb: TracebackType | None,
    ) -> None: ...


class Connection(_ConnectionBase[_T1, _T2]): ...


if sys.platform == "win32":
    class PipeConnection(_ConnectionBase[_T1, _T2]): ...
    def Pipe(duplex=True) -> tuple[PipeConnection[_T1, _T2], PipeConnection[_T2, _T1]]: ...
else:
    def Pipe(duplex: bool = True) -> tuple[Connection[_T1, _T2], Connection[_T2, _T1]]: ...