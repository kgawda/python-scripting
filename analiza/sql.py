import pymysql
import datetime
# pip install PyMySQL

create_table = """CREATE TABLE `temp` (
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `time` DATETIME NOT NULL,
    `temperature` INTEGER NOT NULL,
    PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin
AUTO_INCREMENT=1 ;"""

connection = pymysql.connect(
    host='54.75.110.104',
    port=3306,
    user='root',
    password="pythonALX",
    db="db"
)

save_to_table = "INSERT INTO `temp` (`time`, `temperature`) VALUES (%s, %s)"
read_form_table = "SELECT `id`, `time`, `temperature` FROM `temp`"

with connection:
    with connection.cursor() as cursor:
        #cursor.execute(create_table)
        cursor.execute(save_to_table, (datetime.datetime.now(), 24))
    connection.commit()
    with connection.cursor() as cursor:
        cursor.execute(read_form_table)
        print(cursor.fetchall())
