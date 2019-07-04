install env and activate:
```bash
sudo pip install virtualenv
python3 -m venv env
source env/bin/activate

pip3 install requests
pip3 install kivy
```

compile android:
```bash
buildozer android debug deploy run
```
