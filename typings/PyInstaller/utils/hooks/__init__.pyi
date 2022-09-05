""" # noqa: Y021
This type stub file was generated by pyright.
"""
from collections.abc import Callable
from typing import Any, Literal

logger = ...
PY_IGNORE_EXTENSIONS: set
hook_variables: dict


def exec_statement(statement):
    ...


def exec_statement_rc(statement):
    ...


def exec_script(script_filename, *args, env=...):
    ...


def exec_script_rc(script_filename, *args, env=...):
    ...


def eval_statement(statement) -> Any | Literal[""]:
    ...


def eval_script(scriptfilename, *args, env=...) -> Any | Literal[""]:
    ...


def get_pyextension_imports(modname) -> Any | list:
    ...


def get_homebrew_path(formula=...) -> str | None:
    ...


def remove_prefix(string, prefix):
    ...


def remove_suffix(string, suffix):
    ...


def remove_file_extension(filename):
    ...


def can_import_module(module_name):
    ...


def get_module_attribute(module_name, attr_name):
    ...


def get_module_file_attribute(package):
    ...


def is_module_satisfies(requirements, version=..., version_attr=...):
    ...


def is_package(module_name) -> Literal[False]:
    ...


def get_package_paths(package) -> tuple[str, str]:
    ...


def collect_submodules(package: str, filter: Callable[[str], bool] | None = ...) -> list[str]:
    ...


def is_module_or_submodule(name, mod_or_submod):
    ...


PY_DYLIB_PATTERNS: str


def collect_dynamic_libs(package: str, destdir: str | None = ...) -> list[tuple[str, str]]:
    ...


def collect_data_files(package: str, include_py_files: bool = ..., subdir: str = ...,
                       excludes: list[str] = ..., includes: list[str] = ...) -> list[tuple[str, str]]:
    ...


def collect_system_data_files(path, destdir=..., include_py_files=...):
    ...


def copy_metadata(package_name, recursive=...) -> list:
    ...


def get_installer(module) -> str | None:
    ...


def requirements_for_package(package_name) -> list:
    ...


def collect_all(package_name, include_py_files=..., filter_submodules=...,
                exclude_datas=..., include_datas=...) -> tuple[list, list, list]:
    ...


def collect_entry_point(name: str) -> tuple[list, list]:
    ...


def get_hook_config(hook_api, module_name, key) -> None:
    ...