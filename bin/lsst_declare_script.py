# IPython log file

import multiplicity
lsstRepos = multiplicity.LocalLSSTRepos('/Users/rbiswas/src/LSST/')
lsstRepos.declareEupsWithTag(versionName='rbiswas', tag='rbiswas')
get_ipython().magic(u'logstart ')
exit()
