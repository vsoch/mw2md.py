FarmShare 2 is intended for use in coursework and unsponsored research; users participating in sponsored research should investigate the [https://sherlock.stanford.edu/mediawiki/index.php/Main_Page Sherlock] service, instead. Like the legacy FarmShare environment, FarmShare 2 is ''not'' approved for use with [https://dataclass.stanford.edu high-risk] data, and is subject to University [[Policy | policies]] on acceptable use.

== Cluster description ==

=== rice.stanford.edu ===

These are the login nodes for the new environment, which replace <code>corn.stanford.edu</code>. There are currently 14 systems in service; each has 8 cores and 48 GB of memory. Like <code>corn</code> systems they can be used for interactive work, but some resource limits are enforced to ensure multiple users can comfortably share a node:

* 1 core and 8 GB of memory are reserved for the system
* Each user is currently allowed:
::- an equal share of CPU under load
::- 12 GB of memory, some of which may be swap under memory pressure
::- 128 GB of <code>/tmp</code> storage, with space regularly reclaimed from files older than 7 days
* No single user may consume more than 75% of total CPU time under any conditions

Interactive sessions that require resources in excess of these limits, exclusive access to resources, or access to a feature not available on <code>rice</code> (e.g., a GPU), must be submitted to a compute node:

<source lang="sh">
srun --pty --qos=interactive $SHELL -l
srun --pty --partition=gpu --gres=gpu:1 --qos=interactive $SHELL -l
srun --pty --partition=bigmem --mem=96G --qos=interactive $SHELL -l
</source>

These are the only systems with access to AFS in the new environment; see below.

=== wheat.stanford.edu ===

These are managed (compute) nodes similar to <code>barley.stanford.edu</code> in the old environment. There are currently 17 systems:

* 10 nodes with 16 cores and 128 GB of memory
* 2 large-memory nodes with 16 cores and 768 GB of memory

To submit to the large-memory nodes you need to run on the <code>bigmem</code> partition (see below), and request a minimum of 96 GB of memory:

<source lang="sh">
srun --partition=bigmem --qos=bigmem --mem=96G
sbatch --partition=bigmem --qos=bigmem --mem=96G
</source>

=== oat.stanford.edu ===

These are GPU nodes similar to <code>rye.stanford.edu</code> in the old environment. There are currently 10 systems, each with 16 cores, 128 GB of memory, and one Tesla K40 GPU. Unlike the <code>rye</code> systems, these nodes are managed: you must submit a job to run on <code>oat</code> systems, and you must explicitly request access to a GPU when doing so:

<source lang="sh">
srun --partition=gpu --qos=gpu --gres=gpu:1
sbatch --partition=gpu --qos=gpu --gres=gpu:1
</source>

== Slurm ==

The new environment uses [https://slurm.schedmd.com Slurm] rather than Grid Engine for job management. If you have used [https://sherlock.stanford.edu/mediawiki/index.php/Main_Page Sherlock] the system should be familiar to you. A package that provides limited compatibility with GE commands has been installed, but we encourage users to learn and use the native [https://slurm.schedmd.com/pdfs/summary.pdf Slurm commands] whenever possible.

=== Partitions and Qualities-of-Service ===

There are separate Slurm partitions for the standard compute nodes (<code>normal</code>), the large-memory nodes (<code>bigmem</code>), and the GPU nodes (<code>gpu</code>); there are corresponding Slurm qualities-of-service, as well as qualities-of-service for long-running (<code>long</code>) and interactive (<code>interactive</code>) jobs. Normal jobs have a maximum runtime of 2 days and long jobs a maximum of 7. Each user is currently allowed one interactive session with a maximum runtime of 1 day.

Be sure to request explicitly the resources you need when submitting a job.

== Remote display ==

X11 forwarding is supported using the <code>-X</code> or <code>-Y</code> options for <code>ssh</code>. FarmVNC is no longer supported, but TurboVNC server is installed as a module, and we hope to have better support for VNC use-cases in the future.

== AFS and scratch space ==

[https://uit.stanford.edu/service/afs AFS] is accessible on the <code>rice</code> systems ''only'', and is ''not'' used for home directories. Instead, home directories are served from a dedicated file server, and per-user quota is currently 48 GB. A link to users’ AFS home directories, <code>~/afs-home</code>, is provided as a convenience, for transferring data between the old and new environments, but locations in AFS should not be used as working directories for batch jobs. <code>/farmshare/user_data</code> is mounted everywhere, and can be used for additional (scratch) storage.
