
#!/bin/bash

apt-get update && apt-get install -y build-essential
apt-get install openslide-tools -y
pip install openslide-python
