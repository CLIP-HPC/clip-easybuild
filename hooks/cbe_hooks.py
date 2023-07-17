import os

def pre_configure_hook(self, *args, **kwargs):

    if self.name == 'OpenMPI':
	    extra_opts = ""
	    extra_opts += "--with-pmi=/usr --with-slurm"

            self.log.info("[pre-configure hook] Adding CBE spec %s" % extra_opts)
	    self.cfg.update('configopts', extra_opts)

