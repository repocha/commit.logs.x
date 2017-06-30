### Mining commit logs in code repositories

For sw/sys "researchy" projects, we often needs to mine the history (the commit logs) to understand the common mistakes and patterns of changes. This repo provides some simple parsers and kw-based selectors.

It currently supports Git, SVN, and Bazaar repos with `git_parser.py`, `svn_parser.py`, and `bzr_parser.py`; you can easily extend the `base_parser.py` for other SCM tools. The parsing is not relying on any APIs provided by the SCM tools, but the structure of the commit logs (we intentionally do not want to rely on any external APIs).

In general, the input is the commit logs of a given repo, e.g., the output of `git log`.

The parsers and selectors are extremely simple; but that they are sufficient in most use cases we have encountered in the past. On other other hand, if we need more features, we can always extending the code along the way (this is how we maintain the codebase).

In the `app` directory, there're several "apps" we used the parsers and selectors in the past projects.

