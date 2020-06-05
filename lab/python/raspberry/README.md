install [PyInstaller](https://pyinstaller.readthedocs.io/en/stable/index.html)

install [UPX](https://upx.github.io/)

```shell
$ PYTHONOPTIMIZE=1 pyinstaller --upx-dir ../bin/upx-3.96-arm_linux/ dht_thingsboard.py 
$ sudo cp -r dist/dht_thingsboard /usr/local/bin

$ sudo cp dht.service /etc/systemd/system
$ sudo systemctl start myscript.service
$ sudo systemctl status dht.service
$ sudo systemctl enable dht.service
````

