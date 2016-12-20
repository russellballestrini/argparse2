argparse2
###########

Works just like `argparse <https://github.com/ThomasWaldmann/argparse/>` but also automatically supports environment vars.

for example:

.. code-block:: python

 from argparse2 import EnvParser
 
 if __name__ == '__main__':
     parser = EnvParser('myapp')
     parser.add_argument('-a', '--address', default='127.0.0.1', help='address to bind')
     parser.add_argument('-p', '--port', default='8080', help='port to listen')
     args = parser.parse_args()
     print('listening to {}:{}'.format(args.address, args.port))
