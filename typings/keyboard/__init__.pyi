"""
This type stub file was generated by pyright.
"""
from __future__ import print_function as _print_function
from typing import Any, Optional, Union
from collections.abc import Callable

from threading import Lock as _Lock
from ._keyboard_event import KEY_DOWN, KEY_UP, KeyboardEvent
from ._generic import GenericListener as _GenericListener
from ._canonical_names import all_modifiers, normalize_name, sided_modifiers
__all__ = ["all_modifiers", "normalize_name", "sided_modifiers", "KEY_DOWN", "KEY_UP", "KeyboardEvent"]

__all__ = [
    "KEY_DOWN",
    "KEY_UP",
    "KeyboardEvent",
    "_GenericListener",
    "all_modifiers",
    "normalize_name",
    "sided_modifiers"]

try:
    # Python2
    # threading.Event is a function in Python2 wrappin _Event (?!).
    from threading import _Event as _UninterruptibleEvent  # type: ignore
except NameError:
    # Python3
    import queue as _queue
    from threading import Event as _UninterruptibleEvent


Callback = Callable[[KeyboardEvent], None]

version: str
_is_str = Callable[[Any], bool]
_is_number = Callable[[Any], bool]
_is_list: Callable[[Any], bool]


class _State:
    ...


class _Event(_UninterruptibleEvent):
    def wait(self) -> None:
        ...


_modifier_scan_codes: set


def is_modifier(key) -> bool:
    ...


_pressed_events_lock: _Lock
_pressed_events: dict
_physically_pressed_keys: dict
_logically_pressed_keys: dict


class _KeyboardListener(_GenericListener):
    transition_table = {
        ('free', KEY_UP, 'modifier'): (False, True, 'free'),
        ('free', KEY_DOWN, 'modifier'): (False, False, 'pending'),
        ('pending', KEY_UP, 'modifier'): (True, True, 'free'),
        ('pending', KEY_DOWN, 'modifier'): (False, True, 'allowed'),
        ('suppressed', KEY_UP, 'modifier'): (False, False, 'free'),
        ('suppressed', KEY_DOWN, 'modifier'): (False, False, 'suppressed'),
        ('allowed', KEY_UP, 'modifier'): (False, True, 'free'),
        ('allowed', KEY_DOWN, 'modifier'): (False, True, 'allowed'),

        ('free', KEY_UP, 'hotkey'): (False, None, 'free'),
        ('free', KEY_DOWN, 'hotkey'): (False, None, 'free'),
        ('pending', KEY_UP, 'hotkey'): (False, None, 'suppressed'),
        ('pending', KEY_DOWN, 'hotkey'): (False, None, 'suppressed'),
        ('suppressed', KEY_UP, 'hotkey'): (False, None, 'suppressed'),
        ('suppressed', KEY_DOWN, 'hotkey'): (False, None, 'suppressed'),
        ('allowed', KEY_UP, 'hotkey'): (False, None, 'allowed'),
        ('allowed', KEY_DOWN, 'hotkey'): (False, None, 'allowed'),

        ('free', KEY_UP, 'other'): (False, True, 'free'),
        ('free', KEY_DOWN, 'other'): (False, True, 'free'),
        ('pending', KEY_UP, 'other'): (True, True, 'allowed'),
        ('pending', KEY_DOWN, 'other'): (True, True, 'allowed'),
        # Necessary when hotkeys are removed after beign triggered, such as
        # TestKeyboard.test_add_hotkey_multistep_suppress_modifier.
        ('suppressed', KEY_UP, 'other'): (False, False, 'allowed'),
        ('suppressed', KEY_DOWN, 'other'): (True, True, 'allowed'),
        ('allowed', KEY_UP, 'other'): (False, True, 'allowed'),
        ('allowed', KEY_DOWN, 'other'): (False, True, 'allowed'),
    }

    def init(self) -> None:
        ...

    def pre_process_event(self, event):
        ...

    def direct_callback(self, event):
        ...

    def listen(self) -> None:
        ...


_listener: _KeyboardListener


def key_to_scan_codes(key: Union[int, str, list[Union[int, str]]], error_if_missing: bool = ...) -> list[int]:
    ...


def parse_hotkey(hotkey) -> tuple[
        tuple[tuple[int] | int | tuple[()] | tuple[int, ...]]
        | tuple[tuple[tuple[int] | int | tuple[()] | tuple[int, ...], ...]]
        | tuple[int, ...]]:
    ...


def send(hotkey: Union[str, int], do_press: bool = ..., do_release: bool = ...) -> None:
    ...


press_and_release = send


def press(hotkey) -> None:
    ...


def release(hotkey) -> None:
    ...


def is_pressed(hotkey) -> bool:
    ...


def call_later(fn, args=..., delay=...) -> None:
    ...


_hooks: dict[Callable, Unknown]


def hook(callback: Callback, suppress=..., on_remove=...) -> Callable[[], None]:
    ...


def on_press(callback: Callback, suppress=...) -> Callable[[], None]:
    ...


def on_release(callback: Callback, suppress=...) -> Callable[[], None]:
    ...


def hook_key(key: Union[int, str, list[Union[int, str]]],
             callback: Callback,
             suppress: bool = ...
             ) -> Callable[[], None]:
    ...


def on_press_key(key, callback: Callback, suppress=...) -> Callable[[], None]:
    ...


def on_release_key(key, callback: Callback, suppress=...) -> Callable[[], None]:
    ...


def unhook(remove: Callable[[], None]) -> None:
    ...


unhook_key = unhook


def unhook_all() -> None:
    ...


def block_key(key) -> Callable[[], None]:
    ...


unblock_key = unhook_key


def remap_key(src, dst) -> Callable[[], None]:
    ...


unremap_key = unhook_key


def parse_hotkey_combinations(hotkey) -> tuple[tuple[tuple[Unknown, ...], ...], ...]:
    ...


_hotkeys: dict


def add_hotkey(hotkey,
               callback: Callable,
               args=...,
               suppress=...,
               timeout=...,
               trigger_on_release=...
               ) -> Callable[[], None]:
    ...


register_hotkey = add_hotkey


def remove_hotkey(hotkey_or_callback) -> None:
    ...


unregister_hotkey = clear_hotkey = remove_hotkey


def unhook_all_hotkeys() -> None:
    ...


unregister_all_hotkeys = remove_all_hotkeys = clear_all_hotkeys = unhook_all_hotkeys


def remap_hotkey(src, dst, suppress=..., trigger_on_release=...) -> Callable[[], None]:
    ...


unremap_hotkey = remove_hotkey


def stash_state() -> list[Unknown]:
    ...


def restore_state(scan_codes) -> None:
    ...


def restore_modifiers(scan_codes) -> None:
    ...


def write(text, delay=..., restore_state_after=..., exact=...):
    ...


def wait(hotkey=..., suppress=..., trigger_on_release=...) -> None:
    ...


def get_hotkey_name(names=...) -> str:
    ...


def read_event(suppress: bool = ...) -> KeyboardEvent:
    ...


def read_key(suppress=...):
    ...


def read_hotkey(suppress=...) -> str:
    ...


def get_typed_strings(events, allow_backspace=...):
    ...


_recording: Optional[tuple[Unknown | _queue.Queue[Unknown], Callable[[], None]]]


def start_recording(recorded_events_queue=...) -> tuple[Unknown | _queue.Queue[Unknown], Callable[[], None]]:
    ...


def stop_recording() -> list[Unknown | Any]:
    ...


def record(until=..., suppress=..., trigger_on_release=...) -> list[Unknown | Any]:
    ...


def play(events, speed_factor=...):
    ...


replay = play
_word_listeners: dict


def add_word_listener(
    word,
    callback: Callback,
    triggers=...,
    match_suffix=...,
    timeout=...
) -> Callable[[], None]:
    ...


def remove_word_listener(word_or_handler) -> None:
    ...


def add_abbreviation(source_text,
                     replacement_text,
                     match_suffix=...,
                     timeout=...
                     ) -> Callable[[], None]:
    ...


register_word_listener = add_word_listener
register_abbreviation = add_abbreviation
remove_abbreviation = remove_word_listener
