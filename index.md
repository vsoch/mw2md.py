Transforming MediWiki from '/home/vanessa/Documents/Dropbox/Code/srcc/rst2md.py/index.rst' to MarkDown syntax...
FarmShare 2 is intended for use in coursework and unsponsored research; users participating in sponsored research should investigate the [Sherlock](https://sherlock.stanford.edu/mediawiki/index.php/Main_Page) service, instead. Like the legacy FarmShare environment, FarmShare 2 is *not* approved for use with [high-risk](https://dataclass.stanford.edu) data, and is subject to University [Policy](policies.md) on acceptable use.

## Cluster description
### rice.stanford.edu
These are the login nodes for the new environment, which replace `corn.stanford.edu`. There are currently 14 systems in service; each has 8 cores and 48 GB of memory. Like `corn` systems they can be used for interactive work, but some resource limits are enforced to ensure multiple users can comfortably share a node:

* 1 core and 8 GB of memory are reserved for the system
* Each user is currently allowed:
  - an equal share of CPU under load
  - 12 GB of memory, some of which may be swap under memory pressure
  - 128 GB of `/tmp` storage, with space regularly reclaimed from files older than 7 days
* No single user may consume more than 75% of total CPU time under any conditions

Interactive sessions that require resources in excess of these limits, exclusive access to resources, or access to a feature not available on `rice` (e.g., a GPU), must be submitted to a compute node:

```sh
srun --pty --qos=interactive $SHELL -l
srun --pty --partition=gpu --gres=gpu:1 --qos=interactive $SHELL -l
srun --pty --partition=bigmem --mem=96G --qos=interactive $SHELL -l
```

These are the only systems with access to AFS in the new environment; see below.

### wheat.stanford.edu
These are managed (compute) nodes similar to `barley.stanford.edu` in the old environment. There are currently 17 systems:

* 10 nodes with 16 cores and 128 GB of memory
* 2 large-memory nodes with 16 cores and 768 GB of memory

To submit to the large-memory nodes you need to run on the `bigmem` partition (see below), and request a minimum of 96 GB of memory:

```sh
srun --partition=bigmem --qos=bigmem --mem=96G
sbatch --partition=bigmem --qos=bigmem --mem=96G
```

### oat.stanford.edu
These are GPU nodes similar to `rye.stanford.edu` in the old environment. There are currently 10 systems, each with 16 cores, 128 GB of memory, and one Tesla K40 GPU. Unlike the `rye` systems, these nodes are managed: you must submit a job to run on `oat` systems, and you must explicitly request access to a GPU when doing so:

```sh
srun --partition=gpu --qos=gpu --gres=gpu:1
sbatch --partition=gpu --qos=gpu --gres=gpu:1
```

## Slurm
The new environment uses [Slurm](https://slurm.schedmd.com) rather than Grid Engine for job management. If you have used [Sherlock](https://sherlock.stanford.edu/mediawiki/index.php/Main_Page) the system should be familiar to you. A package that provides limited compatibility with GE commands has been installed, but we encourage users to learn and use the native [Slurm commands](https://slurm.schedmd.com/pdfs/summary.pdf) whenever possible.

### Partitions and Qualities-of-Service
There are separate Slurm partitions for the standard compute nodes (`normal`), the large-memory nodes (`bigmem`), and the GPU nodes (`gpu`); there are corresponding Slurm qualities-of-service, as well as qualities-of-service for long-running (`long`) and interactive (`interactive`) jobs. Normal jobs have a maximum runtime of 2 days and long jobs a maximum of 7. Each user is currently allowed one interactive session with a maximum runtime of 1 day.

Be sure to request explicitly the resources you need when submitting a job.

## Remote display
X11 forwarding is supported using the `-X` or `-Y` options for `ssh`. FarmVNC is no longer supported, but TurboVNC server is installed as a module, and we hope to have better support for VNC use-cases in the future.

## AFS and scratch space
[AFS](https://uit.stanford.edu/service/afs) is accessible on the `rice` systems *only*, and is *not* used for home directories. Instead, home directories are served from a dedicated file server, and per-user quota is currently 48 GB. A link to users’ AFS home directories, `~/afs-home`, is provided as a convenience, for transferring data between the old and new environments, but locations in AFS should not be used as working directories for batch jobs. `/farmshare/user_data` is mounted everywhere, and can be used for additional (scratch) storage.

