# INT6181 Tutorial 7

Tutorial 7: Automate Tests with GitHub Actions

In this tutorial you will set up a GitHub Actions workflow so the provided teacher tests run automatically on every pull request.

The modules under `tutorial_7` (`password_validator.py`, `triangle.py`, `parking_fee.py`) and all `test_*` teacher test files are already provided in this repository on GitHub.

---

## Task: Set Up GitHub Actions

Create a GitHub Actions workflow that runs the provided teacher tests on pull requests.

### Specification

1. Place the workflow under `.github/workflows/` at the **repository root** (the folder that contains both `tutorial_6` and `tutorial_7`), not inside `tutorial_7`.
2. The workflow must trigger on `pull_request` events.
3. Define a single job that runs on the latest Ubuntu runner.
4. Set the jobs default working directory to `tutorial_7`.
5. The job must:
  - Check out the repository code.
  - Set up Python version 3.12.
  - Run the provided unit tests with Python `unittest` discovery, matching files named like `test_*.py`.
6. Commit and push your workflow, make a small change under `tutorial_7`, then open a **pull request** so the workflow runs and all tests pass.

---

## Expected Results

![Expected Result](expected_results.png)