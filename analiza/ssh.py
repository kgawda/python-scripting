import fabric

with open('haslo.txt') as f:
    password = f.read().strip()

result = fabric.Connection(
    '54.75.110.104',
    user='konrad',
    port=7501,
    connect_kwargs={"password": password}
).run('df -h')

# result.stdout
# result.ok