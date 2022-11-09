# Async Socket server using David Beazley algorithm

## Description

> This project is a copy of David Beasley's algorithm that he showed at PyCon 2015 (OOP rework). 
> It shows us how we can write asynchronous Python code using sync sockets, 
> generators to control program execution, and an event loop.

## Create virtual environment

``` bash
python3.11 -m venv venv;
source venv/bin/activate;
```

## Open 3 or more terminals 

### First terminal:

``` bash
python server.py;
```

### Second and third terminal:

``` bash
python client.py;
```

### OR use NetCat:

``` bash
nc 127.0.0.1 8000;
```

> Now you can write messages in the **second** and **third** terminal and send them to the server. 
> You will see how it works asynchronously, despite the fact that the code 
> contains **blocking functions** and **infinite loops**.