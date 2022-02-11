# recoll-webui

An interface for Recoll to search for your data from the web.

## usage

```shell
install ./contrib/systemd/recollindex@.service /etc/systemd/user/recollindex@.service
install ./contrib/systemd/recoll-webui.service /etc/systemd/user/recoll-webui.service
systemctl enable recollindex@user.service
systemctl enable recoll-webui.service
```
