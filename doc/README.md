This is a set of tools to handle multiple git repositories such as the repositories in LSST. The sort of features required are:

- Obtaining a set of sub-directories under a top level directory that belong to the list of LSST repositories by using a certain set of criteria. The criteria might involve being
    - a directory
    - having a remote origin at a repository called lsst at github.
    - having a name that starts with `sims`
- Given the paths to such a local set of repositories, use gitpython to verify that none of the local repositories are dirty (ie. non-empty git-diff returns), and return the list of dirty repositories.
- Given the paths to such a local set of repositories, verify that the repositories are clean and switch to a branch of choice. The default is master, but if a branch name is provided, all repositories should try to switch to this branch. If multiple branches are provided in a list, this should be done in order.
- eups Declare all of the repositories with a certain tag
