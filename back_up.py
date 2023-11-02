import subprocess
import datetime

# MySQL数据库连接信息
db_host = 'localhost'  # MySQL服务器IP地址
db_port = '3306'       # MySQL服务器端口
db_user = 'your_username'  # MySQL用户名
db_password = 'your_password'  # MySQL密码
db_name = 'your_database_name'  # 要备份的数据库名称

# 备份文件的保存路径和文件名
backup_dir = '/path/to/backup/directory'  # 备份文件保存的目录
current_time = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
backup_file = f'{db_name}_{current_time}.sql'  # 备份文件名

# 构建备份命令
backup_command = [
    'mysqldump',
    f'--host={db_host}',
    f'--port={db_port}',
    f'--user={db_user}',
    f'--password={db_password}',
    db_name,
]

# 执行备份命令
try:
    subprocess.run(backup_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
except subprocess.CalledProcessError as e:
    print(f"Error during backup: {e.stderr}")
else:
    with open(f'{backup_dir}/{backup_file}', 'w') as backup:
        backup.write(e.stdout)
    print(f"Backup completed. File saved as {backup_file} in {backup_dir}")


https://windll.com/dll/the-openssl-project-httpswwwopensslorg/libcrypto-1-1-x64
