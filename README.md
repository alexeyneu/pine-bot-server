# pine-bot-server
pine-script compiler. can answer buy or sell out of script  
working fork for a robot
  
  
robots are in `examples` of `solcpp`  
also running `serum-history` required for all this to work
![Screen1](/Untitled.png)  
  
(ofc it's not original script here)
  
```
python3.8 -m pip install ta-lib
python3.8 -m pip install numpy
sudo apt install python3.8-dev -y
python3.8 -m pip install mprpc
python3.8 -m pip install "plotly==3.4.2" --force-reinstall
python3.8 -m pip install flask
python3.8 -m pip install ply
python3.8 -m pip install msgpack-rpc-python
python3.8 -m pip install pandas
python3.8 -m pip install webcolors
python3.8 -m pip install matplotlib
python3.8 -m pip install Pillow --force-reinstall
python3.8 -m pip install mpl_finance
```


Install Python 3.8  

curl -OL https://www.python.org/ftp/python/3.8.12/Python-3.8.12.tar.xz  

Extract the Python archive. Remember, change the version number if you downloaded a newer one:  

tar -xf Python-3.8.12.tar.xz  
mv Python-3.8.12 /opt/Python3.8.12  

Now install the dependencies required to install Python 3.8:  

sudo apt install build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libsqlite3-dev libreadline-dev libffi-dev curl libbz2-dev -y  

Navigate to the directory and run the ./configure –enable-optimizations command:  

cd /opt/Python3.8.12/  
./configure --enable-optimizations --enable-shared  

Note, The script performs several checks to make sure all of the dependencies on your system are present. The ./configure –enable-optimizations will optimize the Python binary by running multiple tests, which will make the build process slower.  

Now that you have built and configured the environment, it is time to compile it with the command make.  
  
make  
  
A handy trick is to specify the -j <number of cpu> as this can significantly increase compiling speed if you have a powerful server. For example, the LinuxCapable server has 6 CPUs, and I can use all 6 or at least use 4 to 5 to increase speed.  
  
make -j 6  

Once you have finished building, install Python binaries as follows:  

sudo make altinstall  

Note, it’s advised to use the make altinstall command NOT to overwrite the default Python 3 binary system.  

Next, after the installation, you need to configure the dynamic linker run-time bindings:  

sudo ldconfig /opt/Python3.8.12  

Note, do not skip this, or you will face issues. You will also need to replace the path with your directory name and version.  

