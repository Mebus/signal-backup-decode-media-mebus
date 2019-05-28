# Signal messenger backup decoder for media

## About

This Python script is an addon to [signal-backup-code](https://github.com/pajowu/signal-backup-decode). It can sort the uploaded media by threads, that means by chats and groups. 

Please use the [SQLiteBrowser](https://sqlitebrowser.org/) to determine the thread IDs and please edit the main.py file in some places.

To extract the Signal-Backup a command similiar to the following can be used:

```
~/.cargo/bin/signal-backup-decode signal-2019-05-28-15-32-37.backup --password "12345678.." --sqlite-path signal-2019-05-28-15-32-37.sqlite.sqlite
``` 

## Author

Mebus, https://mebus.github.io/

## License

MIT License