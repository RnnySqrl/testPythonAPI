# testPythonAPI
A test from pricesearcher company

The code you have in the folder source runs an API in Python3.
You have to install the next dependencies to successfully run the code:
- Python3
- pip3
- tornado
- requests

To install Python3 just go to it's website and find where to download an installer of python or if you are in a linux machine you could also find a command which download and intsall python3.
When you have python3 installed you have to install pip3 ( a comand which download and install different packages).
If you are in a linux machine, run this code in a terminal:

```bash
sudo apt install python3-pip
```
Done that install the tornado and requests packages with the folliwing command:

```bash
sudo pip3 install tornado requests
```

To run our code we just have to run the main.py file with the python3 interpreter, like this:
```bash
python3 main.py
```
if everything goes as it supposed you will see the next lines in the terminal:
```
Data loaded
Running server.... press ctrl+c to stop
```
Now you can do an HTTP request to or server. You have to give a certain id in a json format like this:
```
{
    "id":"d783754511f044c"
}
```
The response should be this:
```
{
    "code": 200,
    "data": {
        "id": "d783754511f044c",
        "name": "underchin",
        "brand": "maizebird",
        "price": 278.93,
        "in_stock": null
    }
}
```
Last but not least here is my favorite git, hope you enjoy it, and of course thanks to give me this opportunity. I enjoy developing this code.

![mygif](bestgif.gif)