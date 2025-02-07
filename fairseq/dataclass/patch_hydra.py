# patch_hydra.py
from dataclasses import field
from hydra.conf import JobConf

def get_default_override_dirname():
    return JobConf.JobConfig.OverrideDirname(
        kv_sep=":",
        item_sep="__",
        exclude_keys=["fb_run_config", "distributed_training.distributed_port"]
    )

# Patch the JobConfig class
JobConf.JobConfig.override_dirname = field(default_factory=get_default_override_dirname)