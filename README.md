# Async Socket server using David Beazley algorithm

## Description

>

## Create virtual environment

``` bash
python3.11 -m venv venv;
source venv/bin/activate;
```

## Open 3 or more terminals 

> CTRL + ALT + T

### First console:

``` bash
python server.py;
```

### Second and third console:

``` bash
python client.py;
```

### OR use NetCat

``` bash
nc 127.0.0.1 8000;
```

> Now you can just write normally messages in **second** and **third** consoles and send them to the server. You will see how it works asynchronously despite the fact that the code contains **blocking functions** and **infinite loops**.