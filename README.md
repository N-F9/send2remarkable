# Send2reMarkable

This is a simple python script to send files to the reMarkable via the command line. It can also backup the entire reMarkable with a simple command.

This script relies on the command `rmapi` from [ddvk/rmapi](https://github.com/ddvk/rmapi). Make sure to put the built binary into the `/bin` directory.

Once that is set up, you can put the `s2r` file into the `/bin` directory and you can use the `s2r` command.

## Usage

`s2r [filename].(pdf/rmdoc)` - sends the file to the reMarkable.

`s2r backup ./` - creates a backup in the current directory.
