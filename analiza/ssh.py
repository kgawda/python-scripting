import fabric

with open('haslo.txt') as f:
    password = f.read().strip()

connection = fabric.Connection(
    '54.75.110.104',
    user='konrad',
    port=7501,
    connect_kwargs={"password": password}
)

connection.run('ls -al logs')
# result.stdout
# result.ok

connection.get('/config/logs/openssh/current', local='openssh.log')
