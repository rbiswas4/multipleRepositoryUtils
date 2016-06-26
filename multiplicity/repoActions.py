"""
"""
import git

__all__ = ['listDirtyRepos']
def listDirtyRepos(repos):
    """
    return a sequence of dirty repositorieso

    Parameters
    ----------
    repos : sequence of abs path to repos 
    """
    for repo in repos:
        gitRepo = git.Repo(repo)
        if gitRepo.is_dirty():
            yield repo
