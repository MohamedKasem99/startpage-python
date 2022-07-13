# startpage-python
perform websearch via startpage search engine which is powered by google.com results.
This package should in theory return identical results as you would expect from google search without being caught by google's bot detection algorithms

<img src="https://i.ibb.co/pxbCQdm/Untitled-Diagram.png" alt="Untitled-Diagram" border="0" width="600" height="150" align=center>

### INSTALL

* from pip
```
$ pip install startpage-python
```
* from source
```
$ git clone https://github.com/mohamedkasem99/startpage-python
$ cd startpage-python
$ pip install -e .
```

***

### examples

```python
from startpage import Startpage

task = Startpage()
results = task.search("Hello World")
for res in results:
    print(res)
"""
https://en.wikipedia.org/wiki/%22Hello,_World!%22_program
https://en.wikipedia.org/wiki/Hello_World_(film)
https://www.youtube.com/watch?v=u7JMhVI7taQ
https://www.youtube.com/watch?v=Yw6u6YkTgQ4
https://code.org/helloworld
https://helloworld.raspberrypi.org/
https://www.imdb.com/title/tt9418812/
https://www.techtarget.com/whatis/definition/Hello-World
https://www.programiz.com/c-programming/examples/print-sentence
http://www.helloworld.com/
"""
```