@echo off
setlocal

rem MySQL数据库连接信息
set mysql_host=127.0.0.1
set mysql_port=3306
set mysql_user=root
set mysql_password=your_mysql_password
set mysql_database=your_database_name

rem 备份文件存放路径
set backup_folder=C:\Backup

rem 创建备份文件夹
if not exist "%backup_folder%" mkdir "%backup_folder%"

rem 获取当前日期和时间
for /f "tokens=2-4 delims=/ " %%a in ('date /t') do (
    set day=%%a
    set month=%%b
    set year=%%c
)
for /f "tokens=1-2 delims=: " %%a in ('time /t') do (
    set hour=%%a
    set minute=%%b
)

rem 生成备份文件名
set backup_filename=%mysql_database%_%year%%month%%day%_%hour%%minute%.sql

rem 使用 mysqldump 命令备份数据库
mysql\bin\mysqldump -h %mysql_host% -P %mysql_port% -u %mysql_user% -p%mysql_password% %mysql_database% > "%backup_folder%\%backup_filename%"

if %errorlevel% equ 0 (
    echo 数据库备份成功，备份文件已保存到 "%backup_folder%\%backup_filename%"
) else (
    echo 数据库备份失败
)

endlocal
