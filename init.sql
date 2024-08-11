-- Otorgar todos los privilegios, incluyendo SUPER y REPLICATION
GRANT ALL PRIVILEGES ON *.* TO 'root1'@'%' WITH GRANT OPTION;

-- Otorgar específicamente los privilegios de replicación
GRANT REPLICATION SLAVE, REPLICATION CLIENT ON *.* TO 'root1'@'%';

-- Otorgar el privilegio SUPER
GRANT SUPER ON *.* TO 'root1'@'%';

-- Actualizar los privilegios
FLUSH PRIVILEGES;