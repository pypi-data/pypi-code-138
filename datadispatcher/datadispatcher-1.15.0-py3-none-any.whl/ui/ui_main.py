import time

from data_dispatcher.api import DataDispatcherClient
from data_dispatcher import Version
from metacat.webapi import MetaCatClient 
import sys, getopt, os, json

from .cli import CLI, CLICommand, InvalidArguments
from .ui_project import ProjectCLI
from .ui_file import FileCLI
from .ui_worker import WorkerCLI
from .ui_rse import RSECLI
from .ui_lib import pretty_json

class LoginCommand(CLICommand):
    
    Usage = """<mechanism> <args>...             -- log in
        login x509 <user> <cert> <key>                  - use X.509 authentication
        login password <user>                           - password authentication
    """
    MinArgs = 2
    
    def __call__(self, command, client, opts, args):
        mech, rest = args[0], args[1:]
        if mech == "x509":
            username, cert, key = rest
            user, expiration = client.login_x509(username, cert, key)
        elif mech == "password":
            import getpass
            username = rest[0]
            password = getpass.getpass("Password:")
            user, expiration = client.login_password(username, password)
        else:
            raise InvalidArguments(f"Unknown authentication mechanism {mech}\n")

        print ("User:   ", user)
        print ("Expires:", time.ctime(expiration))
        

class VersionCommand(CLICommand):
    
    def __call__(self, command, client, opts, args):
        print("Server URL:    ", client.ServerURL)
        print("Server version:", client.version())
        print("Client version:", Version)

class DDCLI(CLI):
    
    Opts = "s:a:"
    Usage = """[-s <server URL>] [-a <auth server URL>]
                Both server and auth server URLs must be specified either using -s and -a or 
                via environment variables DATA_DISPATCHER_URL and DATA_DISPATCHER_AUTH_URL
            """
    
    def __init__(self):
        
        CLI.__init__(self,
            "login",    LoginCommand(),
            "version",  VersionCommand(),
            "project",  ProjectCLI,
            "file",     FileCLI,
            "worker",   WorkerCLI,
            "rse",      RSECLI
        )
            
    def update_context(self, context, command, opts, args):
        if context is None:
            server_url = opts.get("-s") or os.environ.get("DATA_DISPATCHER_URL")
            auth_server_url = opts.get("-a") or os.environ.get("DATA_DISPATCHER_AUTH_URL")

            if not server_url:
                print("Server address must be specified either using -s option or using environment variable DATA_DISPATCHER_URL", file=sys.stderr)
                sys.exit(2)

            if not auth_server_url:
                print("Authentication server address must be specified either using -a option or using environment variable DATA_DISPATCHER_AUTH_URL", file=sys.stderr)
                sys.exit(2)
    
            context = DataDispatcherClient(server_url, auth_server_url)       # return the client as context
        return context



my_name = sys.argv[0]

Usage = f"""
Data Dispatcher version: {Version}

Usage:

dd <commnd> <subcommand> <options> <args>

Commands:

    worker [-n|<worker id>]                                - set or print my worker_id 
                                                             -n generates new one
                                                             worker id will be saved in <CWD>/.worker_id
    create project ...
    show project ...
    list projects ...

    delete project <project_id>
    cancel project [-j] <project_id>                       - cancel project, -j - print project info as JSON

    show file [-j] <namespace>:<name>

    show handle [-j] <project_id> <namespace>:<name>       - show file handle, -j - as JSON

    next [-j] [-t <timeout>] [-c <cpu_site>] <project_id>  - get next available file
                                                             -c - choose the file according to the CPU/RSE proximity map for the CPU site
                                                             -j - as JSON
                                                             -t - wait for next file until "timeout" seconds, 
                                                                  otherwise, wait until the project finishes
    done <project_id> <namespace>:<name>                   - mark the file as successfully processed
    failed [-f] <project_id> <namespace>:<name>            - mark the file as failed, -f means "final", no retries

    list rses [-j]                                         - list RSEs, -j: print as JSON
    show rse [-j] <rse>                                    - show information about RSE
    set rse -a (up|down) <rse>                             - set RSE availability (requires admin privileges)
    
    login x509 <user> <cert> <key>
    login password <user>
"""


def junk():

    if command == "login":
        if len(rest) < 2:
            print(Usage)
            sys.exit(2)
        subcommand, rest = rest[0], rest[1:]
        if subcommand == "x509":
            username, cert, key = rest
            user, expiration = client.login_x509(username, cert, key)
        elif subcommand == "password":
            import getpass
            username = rest[0]
            password = getpass.getpass("Password:")
            user, expiration = client.login_password(username, password)
        else:
            print(f"Unknown authentication mechanism {subcommand}\n")
            print(Usage)
            sys.exit(2)

        print ("User:   ", user)
        print ("Expires:", time.ctime(expiration))
    
    else:
        print(Usage)
        sys.exit(2)

def main():
    cli = DDCLI()
    cli.run(sys.argv, argv0="dd")
        
if __name__ == "__main__":
    main()
        
    
            
            
        
        
        
        
        
