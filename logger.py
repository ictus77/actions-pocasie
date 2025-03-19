import logging


### https://realpython.com/python-logging/

#logging.basicConfig(level=logging.DEBUG)

#logging.debug("This is a debug message")
#logging.info("This is an info message")
#logging.warning("This is a warning message")
#logging.error("This is an error message")
#logging.critical("This is a critical message")

###
#print("\nnew\n")
###
#logging.basicConfig(format="%(levelname)s:%(name)s:%(message)s")
#logging.warning("Hello, Warning!")

###
#print("\nnew\n")
###
#logging.basicConfig(format="{levelname}:{name}:{message}", style="{")
#logging.warning("Hello, Warning!")

###
#print("\nnew\n")
###
#logging.basicConfig(
#    format="{asctime} - {levelname} - {message}",
#    style="{",
#    datefmt="%Y-%m-%d %H:%M",
#)

#logging.error("Something went wrong!")

###
#print("\nnew\n")
###

#logging.basicConfig(
#    filename="app.log",
#    encoding="utf-8",
#    filemode="a",
#    format="{asctime} - {levelname} - {message}",
#    style="{",
#    datefmt="%Y-%m-%d %H:%M",
# )
#
#logging.warning("Save me!")


###
#print("\nnew\n")
###
# import logging
# logging.basicConfig(
#     format="{asctime} - {levelname} - {message}",
#     style="{",
#     datefmt="%Y-%m-%d %H:%M",
#     level=logging.DEBUG,
# )
# 
# name = "Samara"
# logging.debug(f"{name=}")

###
#print("\nnew\n")
#custom one
###


import logging
logger = logging.getLogger(__name__)
#logger.warning("Look at my logger!")

#console_handler = logging.StreamHandler()
file_handler = logging.FileHandler("app11.log", mode="a", encoding="utf-8")

#logger.addHandler(console_handler)
logger.addHandler(file_handler)
# print(logger.handlers)
formatter = logging.Formatter(
   "{asctime} - {levelname} - {message}",
    style="{",
    datefmt="%Y-%m-%d %H:%M",
)

file_handler.setFormatter(formatter)
logger.warning("watch out")