# Port Scanner

The following is a port-scanner network script that checks for open-ports in a specified IP machine. Internally creates and perform a `TCP socket communication` between the `client` and the specific host and checks for the availability.

In order to optimize performance, the script uses execution `threads` for each connection established.

## Usage

Preferable, use an isolated environment with `virtualenv`, because the `termcolor` package is required.

`port-scan.py -H <your target> -p <ports>`

You can also set a range of ports with a comma separation.

## Set up

Simple, just.

`virtualenv -p python3 <name_of_the_env>`

## Credits

 - [David E Lares](https://twitter.com/davidlares3)

## License

 - [MIT](https://opensource.org/licenses/MIT)
