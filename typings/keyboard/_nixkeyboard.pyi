from collections import defaultdict
from collections.abc import Callable, Generator

from keyboard._canonical_names import all_modifiers as all_modifiers, normalize_name as normalize_name
from keyboard._keyboard_event import KEY_DOWN as KEY_DOWN, KEY_UP as KEY_UP, KeyboardEvent as KeyboardEvent
from keyboard._nixcommon import (EV_KEY as EV_KEY, AggregatedEventDevice, EventDevice,
                                 aggregate_devices as aggregate_devices, ensure_root as ensure_root)

#


def cleanup_key(name: str) -> tuple[str, bool]: ...
def cleanup_modifier(modifier: str) -> str: ...


to_name: defaultdict[tuple[int, tuple[str, ...]], list[str] | str]
from_name: defaultdict[str, list[tuple[int, tuple[str, ...]]]]
keypad_scan_codes: set[str]


def register_key(key_and_modifiers: tuple[int, tuple[str, ...]], name: str) -> None: ...
def build_tables() -> None: ...


device: AggregatedEventDevice | EventDevice | None


def build_device() -> None: ...
def init() -> None: ...


pressed_modifiers: set[str]


def listen(callback: Callable[[KeyboardEvent], None]) -> None: ...
def write_event(scan_code: int, is_down: bool | int) -> None: ...
def map_name(name: str) -> Generator[tuple[int, tuple[str, ...]], None, None]: ...
def press(scan_code: int) -> None: ...
def release(scan_code: int) -> None: ...
def type_unicode(character: str | bytes | bytearray) -> None: ...