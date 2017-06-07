argparse2
###########

Works just like `argparse <https://github.com/ThomasWaldmann/argparse/>`_ but also automatically supports environment vars.

For example, `myapp`:

.. code-block:: python

 #!/usr/bin/env python
 from argparse2 import EnvParser
 
 if __name__ == '__main__':
     parser = EnvParser('myapp')
     parser.add_argument('-a', '--address', default='127.0.0.1', help='address to bind')
     parser.add_argument('-p', '--port', default='8080', help='port to listen')
     args = parser.parse_args()
     print('listening to {}:{}'.format(args.address, args.port))

No arguments, flags, or environment vars:

.. code-block:: bash

 ./myapp.py
 listening to 127.0.0.1:8080

A flag:

.. code-block:: bash

 ./myapp --port 6060
 listening to 127.0.0.1:6060

A flag and an environment var:

.. code-block:: bash

 MYAPP_ADDRESS=0.0.0.0 ./myapp --port 6060
 listening to 0.0.0.0:6060

A flag overiding an environment var:

 MYAPP_ADDRESS=0.0.0.0 ./myapp --address 192.168.1.21
 listening to 192.168.1.21:8080

We also add the environment vars to the help texts:

.. code-block:: bash

 ./myapp --help
 usage: myapp [-h] [-a ADDRESS] [-p PORT]

 optional arguments:
   -h, --help            show this help message and exit, MYAPP_HELP=help
   -a ADDRESS, --address ADDRESS
                         address to bind, MYAPP_ADDRESS=address
   -p PORT, --port PORT  port to listen, MYAPP_PORT=port
