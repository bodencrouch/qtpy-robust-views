# AGENTS.md

## Cursor Cloud specific instructions

`qtpy-robust-views` is a pure-Python library of hardened `qtpy` item views
(`RobustTreeView`/`RobustTableView`/`RobustListView` and related widgets). There is
no server or long-running service. The only runnable "apps" are the per-module
`__main__` demo blocks (e.g. `src/qtpy_robust_views/itemviews/treeview.py`).

### Environment
- Dependencies are installed into a project-local virtualenv at `.venv` by the
  startup update script (`qtpy` + the `PyQt5` binding, matching CI, plus `pytest`,
  and an editable install of this package). Activate it with `. .venv/bin/activate`.
- System packages already provisioned in the VM (needed once; not in the update
  script): `python3.12-venv`, and — only for on-screen GUI runs — the xcb libs
  `libxcb-icccm4 libxcb-image0 libxcb-keysyms1 libxcb-randr0 libxcb-render-util0
  libxcb-shape0 libxcb-xinerama0 libxcb-cursor0 libxkbcommon-x11-0`.

### Test
- Tests run headless: `QT_QPA_PLATFORM=offscreen pytest -q tests`. Without the
  `offscreen` platform Qt will abort. This mirrors `.github/workflows/ci.yml`.
- No linter/type-checker is configured in `pyproject.toml`; CI only runs pytest.
  (Source uses `# noqa` comments, but there is no ruff/flake8/mypy config.)

### Run the GUI demos
- Use the XFCE desktop on `DISPLAY=:1` with the xcb platform, e.g.
  `DISPLAY=:1 QT_QPA_PLATFORM=xcb python -m qtpy_robust_views.itemviews.treeview`.

### Known blocking source bug (non-obvious)
- `src/qtpy_robust_views/itemviews/baseview.py:57` has an incomplete import
  (`from qtpy_robust_views._compat import`) and `get_qt_meta_type` (used later in
  that file) is missing from `_compat.py`, which is only a stub. This `SyntaxError`
  makes every core view (`treeview`/`tableview`/`listview`/`headerview`/
  `stacked_view`) unimportable. The `tests/test_smoke.py` test still passes because
  it only imports the top-level package, which pulls in none of the widget modules.
  To import or run any view, complete that import and implement `get_qt_meta_type`
  in `_compat.py` (map Python `int`/`float`/`bool`/`str` to `QMetaType.Type`).
