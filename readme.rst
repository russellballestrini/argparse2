argparse2
###########

Works just like `argparse <https://github.com/ThomasWaldmann/argparse/>`_ but also automatically supports environment vars.

for example, myapp:

.. code-block:: python

 #!/usr/bin/env python
 from argparse2 import EnvParser
 
 if __name__ == '__main__':
     parser = EnvParser('myapp')
     parser.add_argument('-a', '--address', default='127.0.0.1', help='address to bind')
     parser.add_argument('-p', '--port', default='8080', help='port to listen')
     args = parser.parse_args()
     print('listening to {}:{}'.format(args.address, args.port))

.. code-block:: bash

 ./myapp.py
 listening to 127.0.0.1:8080

.. code-block:: bash

 ./myapp --port 6060
 listening to 127.0.0.1:6060

.. code-block:: bash

 MYAPP_ADDRESS=0.0.0.0 ./myapp --port 6060
 listening to 0.0.0.0:6060
