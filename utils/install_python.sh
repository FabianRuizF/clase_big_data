wget https://repo.anaconda.com/miniconda/Miniconda3-py39_23.1.0-1-Linux-x86_64.sh
bash ~/Miniconda3-py39_23.1.0-1-Linux-x86_64.sh -b -p $HOME/miniconda
$HOME/miniconda/bin/conda init
source ~/.bashrc

pip install pyspark==3.3.2
pip install pandas
