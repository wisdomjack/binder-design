# 💫 Binder Design Pipeline — Modular Singularity Containers for Protein Binder Design

This repository contains a quality-of-life mod for the modern protein engineer.

The tools used in this pipeline — **RFdiffusion**, **ProteinMPNN**, and **AlphaFold2** — were originally integrated in the [dl_binder_design](https://github.com/nrbennet/dl_binder_design) workflow using Conda environments and monolithic setups. While effective, that structure can be difficult to reproduce or adapt in scientific computing environments, where software restrictions and lack of root access are common.

Here, each tool is packaged in a standalone **Singularity container**, making the pipeline easier to run, modify, and deploy on shared HPC systems without relying on Docker or Conda. 

This restructuring makes the workflow:
- Easier to deploy in real-world cluster environments
- More modular and transparent for debugging or retooling
- Better suited for labs working between computation and experiment


## RFdiffusion Container (Singularity)

This container runs [RFdiffusion](https://github.com/RosettaCommons/RFdiffusion) using Singularity and is intended for use on HPC clusters with NVIDIA GPUs. It supports protein structure generation using diffusion-based modeling.

### Features

- CUDA 11.6.2 and cuDNN 8 support
- Python 3.9 with PyTorch 1.12.1 and DGL (CUDA 11.6)
- Includes SE3Transformer and RFdiffusion source installation
- Modular setup: works with a locally cloned RFdiffusion repo

---

### Requirements

- NVIDIA GPU with CUDA 11.6 support
- Singularity version 3.7 or higher
- Local clone of the RFdiffusion GitHub repository
- Internet connection for downloading model weights

---

### Instalation

Clone the official RFdiffusion repository into the same directory as your Singularity definition file:

```bash
git clone https://github.com/RosettaCommons/RFdiffusion.git
singularity build RFdiffusion.sif RFdiffusion.def
```

## ProteinMPNN Container (Singularity)

This container builds and runs [ProteinMPNN](https://github.com/dauparas/ProteinMPNN) using Singularity for use on HPC clusters with NVIDIA GPUs. The container includes a pre-configured Conda environment and can optionally support PyRosetta integration (if licensed credentials are available).

### Features

- CUDA 11.6.1 and cuDNN 8 development environment
- Pre-installed Conda environment based on `proteinmpnn_fastrelax.yml`
- PyRosetta configuration support (optional)
- Designed to work with the `dl_binder_design` fork or standalone MPNN modules

---

### Requirements

- NVIDIA GPU with CUDA 11.6 support
- Singularity version 3.7 or higher
- Local clone of [dl_binder_design](https://github.com/nrbennet/dl_binder_design) or equivalent MPNN-compatible repo
- Internet connection for model/environment setup
- (Optional) PyRosetta credentials for full Relax support

---

### Installation

Place the cloned `dl_binder_design` repo in the same directory as your `proteinmpnn.def` file, then build the container:

The bootstrap.sh script is used to unpack and inject Rosetta binaries (brians_score_jd2 and extract_pdbs) into the correct location within the dl_binder_design repository. This is necessary because, these Rosetta binaries are not included in the public dl_binder_design repo.


```bash
git clone https://github.com/nrbennet/dl_binder_design.git
./bootstrap.sh
singularity build proteinmpnn.sif proteinmpnn.def
```
