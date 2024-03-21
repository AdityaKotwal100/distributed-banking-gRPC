# gRPC Distributed Banking System

## Overview

This project develops a distributed banking system utilizing gRPC for communication between customer and branch processes. The system manages money transactions such as deposits and withdrawals across multiple bank branches, ensuring consistency across replicas of account balances. Each customer interacts with a specific branch, identified by a unique ID, to perform transactions on a shared bank account, without concurrent updates. This setup uses Python and gRPC technology to facilitate RPC communication for transaction requests and propagation of updates across branch replicas.


Installation Steps:

1. Install Python 3.11.X

```bash
$ sudo add-apt-repository ppa:deadsnakes/ppa
```

```bash
$ sudo apt update
```

```bash
$ sudo apt install python3.11
```

To verify the installation

```bash
$ python3.11 --version
> Python 3.11.5
```

1. Install Python Package manager

```bash
$ sudo apt install python3-pip
```

1. Install Python virtual environment and activate it

```bash
$ sudo apt install python3-virtualenv
$ virtualenv venv
$ source venv/bin/activate
> (venv) user@user: ~path
$ python -m pip install --upgrade pip
```

1. Install requirements
    1. Inside your virtual environment run the following commands
    
    ```bash
    > pip3 install -r requirements.txt
    ```
    
2. Run server using `run_branch.py`
    
    ```bash
    > python3 run_branch.py
    ```
    
    This starts the server and all the Branch objects are instantiated with the data provided in `input.json`
    
3. In another terminal, run client using `run_client.py`
    
    ```bash
    > python3 run_customer.py
    ```
    
    This reads `input.json` and instantiates the Customer processes, calling `executeEvents()` to process the list of events provided
    
4. Results are stored in `output.json`
5. Customer processes debug logs are stored in `customerDebug.txt`
6. Branch processes debug logs are stored in `branchDebug.txt`