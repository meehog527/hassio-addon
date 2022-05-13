echo "Installing python packages"
sudo pip3 install -r requirements.txt
sudo apt-get remove git -y
sudo apt-get clean

echo "Initilizing container"
python3 gateway.py
