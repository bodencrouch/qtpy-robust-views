"""Compatibility helpers.

Small utilities that the widgets rely on but that originated in the upstream
project this package was extracted from.
"""

from __future__ import annotations

from typing import Any

from qtpy.QtCore import QDate, QDateTime, QMargins, QMetaType, QSize, QTime
from qtpy.QtGui import QColor


def get_qt_meta_type(param_type: type | None, current_value: Any = None):
    """Map a Python/Qt type (or a value's type) to a ``QMetaType.Type``.

    Used to choose an appropriate editor widget for a value. ``QMargins`` is
    returned as the class itself, matching how callers compare against it.
    """
    resolved = param_type if isinstance(param_type, type) else type(current_value)

    # ``bool`` must be checked before ``int`` (``bool`` subclasses ``int``).
    if resolved is bool:
        return QMetaType.Type.Bool
    if resolved is int:
        return QMetaType.Type.Int
    if resolved is float:
        return QMetaType.Type.Double
    if resolved is str:
        return QMetaType.Type.QString
    if issubclass(resolved, QColor):
        return QMetaType.Type.QColor
    if issubclass(resolved, QDateTime):
        return QMetaType.Type.QDateTime
    if issubclass(resolved, QDate):
        return QMetaType.Type.QDate
    if issubclass(resolved, QTime):
        return QMetaType.Type.QTime
    if issubclass(resolved, QSize):
        return QMetaType.Type.QSize
    if issubclass(resolved, QMargins):
        return QMargins
    return QMetaType.Type.QString
