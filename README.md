### parsing commit logs in code repos

For sw/sys research, we often needs to search the history (record by the commit logs) to understand the mistakes and changes. This repo provides some simple parsers and kw-based selectors.

The input is the commit logs of a given repo. For example, if the repo is maintained using Git, you can use 
```
git -C $repo_path log > repo.log
```
where `$repo_path` is the file path of the repo.

We support Git, SVN, and Bazaar repos with `git_parser.py`, `svn_parser.py`, and `bzr_parser.py`
The parser are extremely simple and only support the default log format. 
But it turns out that they are sufficient in most use cases.

If we need more features (e.g., recording more information), we can always extending these parsers along the way.

