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

### Folder Setup

Clone the official RFdiffusion repository into the same directory as your Singularity definition file:

```bash
git clone https://github.com/RosettaCommons/RFdiffusion.git
singularity build RFdiffusion.sif RFdiffusion.def
