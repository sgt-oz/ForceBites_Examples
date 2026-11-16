# ForceBites Examples

[ForceBites](https://pypi.org/project/forcebites/) moves pandas DataFrames in and out of Salesforce
in one line of code:

```python
successful, failed = sf.insert(df, "Contact")
```

You get back the rows that made it, with their new Ids, and the rows that didn't, with the reason
why. Under the hood, it picks between the REST and Bulk APIs, tunes batch size and threads while the
job runs, and keeps retrying until only the truly bad records are left.

This repo has example scripts in `examples/` for each method. For every method and setting, see
the [ForceBites README on PyPI](https://pypi.org/project/forcebites/). The source is at
[sgt-oz/ForceBites](https://github.com/sgt-oz/ForceBites).

## Running them

```
pip install -r requirements.txt
```

Copy `.env.example` to `.env`, fill in your connected app's details, then run a script:

```
python examples/query.py
```

The others create and change the made-up Contacts in `examples/data/contacts.csv`, all with the
first name "ForceBites", so use a sandbox. Each one deletes its Contacts again when it finishes, so
they run in any order. If one stops partway, `delete.py` removes whatever it left behind.
