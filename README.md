# Python Monorepo using Poetry v1.1

Welcome!

## Tools used

- Python:
    - `pipx`, installed via `pip install pipx`.
    - `poetry`, installed via `pipx install poetry`. This should give you `poetry` with version 1.1.X.
        - Ran `poetry config virtualenvs.in-project true`
    - `pre-commit`, installed via `pipx install pre-commit`.
    - `black`, installed via `pipx install black`.

## How is this monorepo structured?

- `libs`: Contains Python packages that function as libraries, i.e., packages that every project can depend upon. Libraries can also depend upon each other.
- `apps`: Actual applications that can be deployed elsewhere.

## How was this monorepo created?

- Root folders are created manually.
- Within folder `libs`, create libraries using command `poetry new xyz_lib_a`, etc. Within folder `projects`, create projects using command `poetry new xyz_proj_a`, etc.
- Added dependencies and code to relevant libraries/projects.
- Added a basic pre-commit hook configuration in `.pre-commit-config.yaml`.
- Run `pre-commit install` and `pre-commit run --all-files`.
- Check that everything works in shell using `poetry install`, `poetry update`, `poetry run pytest tests`, etc.
- Added a `.gitignore` to deal with unwanted folders, Python caches, venvs, etc.
- Added a `pyproject.toml` for the end-to-end integration tests.

# Poetry comments

- It seems that Poetry just unions the normal and dev dependencies and then tries to resolve them. So if you have `lib_b = 0.1.0` in your normal dependencies and `lib_b = { path = "../lib_b", develop = true}` in your dev dependencies, then this will correctly work with the local version if its version in the `pyproject.toml` is 0.1.0.
- You can depend on a local package, but it will only install the normal dependencies of that local package, not its development dependencies.
- This means that chaining multiple local packages is not possible, since only the normal dependency will be looked at and it will most likely not be found. E.g., if you have `lib_a -> lib_b -> lib_c`, then `lib_a` will find the local development version of `lib_b` just fine, but not `lib_c`.
- One way to solve this chaining issue is to add the local development versions to the top of the chain. E.g., adding `lib_c` as a dev dependency to the `lib_a` `pyproject.toml`. Note that it does not need to be added as an official package.
- Note that for some reason the dependencies need to be ordered in a specific way: dependencies lower down the chain should be placed above higher dependencies.
- The `poetry.lock` will contain the packages of the development environment, so it should/will contain the local development packages, not the official releases!

# PyCharm setup

- Create a project at the root of the repo, in this case `python-monorepo-poetry`.
- Configure your base Python installation as the interpreter for this project. I think it will not be used.
- Configure content sources and exclude temporary folders.
- At this point, check that imports from libraries and applications are correctly working. If not, remove the `.idea` folder at the repo root and try again. Note that at this point the lib/app imports are working because of the content roots, but any dependencies will not be recognized yet.
- Now add additional projects to the existing project for every app and library. These seem to have their own content roots, that they may or may not inherit from the root project. At least they will only get roots limited to their own folder. So at this point the imports may stop working again.
- Create VENVs for every lib and app and add them in PyCharm. You probably have to rename them a bit.
- Associate every sub-project with its correct interpreter from the VENVs you just made. Add this point everything should start working again.
- Note: the sub-projects automatically add sources roots outside their folder structures based on the path installs you do in the VENV. But that is fine.
- Create run configurations for every library and application. Also create a compound configuration to run them all. Save as a project file so it can be added to Git. Don't forget to set a `--cov=...` additional argument to get code coverage in the report.
- The default arguments added for Pytest caused my coverage not to show up, so remove them in the advanced settings.
- Add `black` as an external tool by following the steps in [this](https://black.readthedocs.io/en/stable/integrations/editors.html#pycharm-intellij-idea) link. Basically just add it as an external tool. I also like to map the invocation to `ctrl + \ `.

# Flake8

Lints your code, i.e., make sure that is syntactically correct. Black will also kind of do this already since it will fail if cannot run due to syntax errors.
Flake8 is alot more extensive though. Use [this](https://flake8.pycqa.org/en/latest/user/configuration.html) link for the configuration details.

I've added a `.flake8` config file in the root of the repo that the pre-commit hook will use. My settings are mostly based on the Poetry repository, which is a treasure trove https://github.com/python-poetry/poetry/blob/master/.pre-commit-config.yaml. This list is also pretty good: https://github.com/DmytroLitvinov/awesome-flake8-extensions.

Plugins:

- `flake8-docstrings`: https://github.com/pycqa/flake8-docstrings. Adds pydocstyle to Flake8. Checks that your docstrings are correctly configured. Use https://www.pydocstyle.org/en/latest/error_codes.html#grouping.
- `flake8-bugbear`: https://github.com/PyCQA/flake8-bugbear. Finds bugs and design problems.
- `pep8-naming`: https://github.com/PyCQA/pep8-naming. Checks that names adhere to PEP8 standards.
- `flake8-bultins`: https://github.com/gforcada/flake8-builtins. Checks that variable names are not built-in keywords.
