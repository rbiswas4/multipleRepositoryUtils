#!/usr/bin/env python
import multiplicity as m
def islsstsims(g):
    if 'github.com:lsst' in g:
        return True

# main
mydir = '/Users/rbiswas/src/LSST'
repos = m.absPathsIn(mydir)

lsstRepos = list(m.remoteChar(repos, islsstsims)) 
dirtyRepos = list(m.listDirtyRepos(lsstRepos))
if len(dirtyRepos) != 0:
    raise ValueError('repos should all be clean for the following process')
print('DIRTY', dirtyRepos)

for repo in lsstRepos:
    if repo not in dirtyRepos:
        tablename = m.eupsPkgName(repo)
        if tablename != []:
            print tablename
