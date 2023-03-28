# MuJoCo Map Maker

MuJoCo Map Maker is a tool for creating maps for the MuJoCo physics engine.

## Installation

Follow the next steps for installing the simulation on your device.

**Requirements:**
- Python 3.10.0 or higher


### Install miniconda (highly-recommended)
It is highly recommended to install all the dependencies on a new virtual environment. For more information check the conda documentation for [installation](https://conda.io/projects/conda/en/latest/user-guide/install/index.html) and [environment management](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html). For creating the environment use the following commands on the terminal.

```bash
conda create -n map_maker python==3.10.9
conda activate map_maker
```
### Install from pip
The MuJoCo Map Maker is available as a pip package. For installing it just use:
```
pip install mujoco-map-maker
```

### Install from source
Firstly, clone the repository in your system.
```bash
git clone https://github.com/vistormu/mujoco_map_maker.git
```

Then, enter the directory and install the required dependencies
```bash
cd mujocon_map_maker
pip install -r requirements.txt
```

## Documentation
The official documentation of the package is available on [Read the Docs](https://mujoco-map-maker.readthedocs.io/en/latest/). Here you will find the [installation instructions](https://mujoco-map-maker.readthedocs.io/en/latest/src/installation.html), the [API reference](https://mujoco-map-maker.readthedocs.io/en/latest/src/api_reference.html) and some [minimal working examples](https://mujoco-map-maker.readthedocs.io/en/latest/src/examples.html).
