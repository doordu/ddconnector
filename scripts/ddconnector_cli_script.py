import configparser
import socket

import click
from raven import Client
from raven_aiohttp import AioHttpTransport


@click.group()
@click.option("--ini_file", default='/etc/ddconnector.ini', help='ddconnector配置文件绝对路径', type=click.Path(exists=True))
@click.pass_context
def cli(ctx, ini_file):
    config = configparser.ConfigParser()
    config.read(ini_file)
    ctx.obj['config'] = config
    

@cli.command()
@click.argument('level', type=int)
@click.pass_context  
def debug(ctx, level):
    config = ctx.obj['config']
    enabled = bool(level)
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((config.get('general', 'server_ip'), 
                  config.getint('general', 'listen_port')))
    
    try:
        message = None
        if enabled:
            message = b'eyJjbWQiOiAiZGVidWciLCAiZW5hYmxlZCI6IHRydWV9*'
        else:
            message = b'eyJjbWQiOiAiZGVidWciLCAiZW5hYmxlZCI6IGZhbHNlfQ==*'

        sock.sendall(message)
        response = sock.recv(2046)
        click.echo("Response: %r" % response)
    finally:
        sock.close()
        
        
@cli.command()
@click.pass_context  
def total(ctx):
    config = ctx.obj['config']
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((config.get('general', 'server_ip'), 
                  config.getint('general', 'listen_port')))
    try:
        message = b"eyJjbWQiOiAidG90YWwifQ==*"

        sock.sendall(message)
        response = sock.recv(2046)
        click.echo(response)
    finally:
        sock.close()        
        
@cli.command()
@click.pass_context  
def gc(ctx):
    config = ctx.obj['config']
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((config.get('general', 'server_ip'), 
                  config.getint('general', 'listen_port')))
    try:
        message = b"eyJjbWQiOiAiZ2MifQ==*"

        sock.sendall(message)
        response = sock.recv(2046)
        click.echo(response)
    finally:
        sock.close()          
        
def main():
    client = Client('https://ca252a631c4b437cac81ea0ad3e545ff:d31c83bc53b644138831c7c7d41ba661@sdlog.doordu.com:8205/17', transport=AioHttpTransport)
    cli(obj={})