
import serial
port="COM7"
conn=serial(port,115200)
message=input("Message:")
conn.write(message.encode())

