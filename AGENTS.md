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
- Several other view modules also expose `__main__` demos.

### Non-obvious notes
- `tests/test_smoke.py` only imports the top-level `qtpy_robust_views` package,
  which pulls in none of the widget modules. So the suite can pass even if a
  widget module (e.g. `itemviews/baseview.py`) fails to import. When changing the
  widgets, import them explicitly (or run a demo) to catch import-time errors.
- `get_qt_meta_type` lives in `qtpy_robust_views/_compat.py` and backs the
  context-menu editor widgets in `baseview.py` (`_create_input_widget`).
