Ubuntu

sudo rabbitmq-server start			- включение message broker RabbitMQ

sudo invoke-rc.d rabbitmq-server stop		- отключение message broker RabbitMQ

http://localhost:15672/#/			- для наблюдения


# java 

javac -cp rabbitmq-client.jar Send.java Recv.java 			     - для создания классов Send and Recv

java -cp .:commons-io-1.2.jar:commons-cli-1.1.jar:rabbitmq-client.jar Send   - запуск Send

java -cp .:commons-io-1.2.jar:commons-cli-1.1.jar:rabbitmq-client.jar Recv   - запуск Recv


# Python

python send.py		- запуск Send

python receive.py	- запуск Recv
