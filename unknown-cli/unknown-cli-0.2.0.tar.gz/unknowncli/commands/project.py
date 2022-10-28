import time 
import sys, os
import requests
import logging
import socket
from tabulate import tabulate
from pathlib import Path
from pprint import pprint
from ..utils import dumps, abort
from subprocess import check_call
from P4 import P4
import shutil

log = logging.getLogger(__name__)

from typer import Context, launch, echo, secho, Option, Typer, confirm, prompt, style, progressbar

app = Typer()

hostname = socket.gethostname().lower()
SUBST_DRIVE = "S:"
STREAMS = ["//project/sn2-main", "//project/sandbox"]
is_windows = (os.name == 'nt')
DEFAULT_FOLDER = "C:\Perforce" if is_windows else "~/Perforce"
MIN_FREE_GB = 200

def get_clientspecs(p4):
    try:
        specs = p4.run_clients("-u", p4.user)
    except Exception as e:
        abort(str(e))
    ret = {}
    for s in specs:
        host = s["Host"].lower()
        if host == hostname or not host:
            ret[s["Stream"].lower()] = s
    return ret

def get_sync_stats(p4, force=False):
    # gah, p4 wrapper just returns text
    if force:
        ret = p4.run_sync("-N", "-f")
    else:
        ret = p4.run_sync("-N")
    lst = ret[0].split("=")
    ret = {"files": {"added": 0, "updated": 0, "deleted": 0, "total": 0}, "mbytes": {"added": 0, "updated": 0, "total": 0}}
    lst2 = [int(l) for l in lst[1].split(",")[0].split("/")]
    ret["files"]["added"] = lst2[0]
    ret["files"]["updated"] = lst2[1]
    ret["files"]["deleted"] = lst2[2]
    ret["files"]["total"] = sum(lst2)

    lst2 = [int(l) // 1024 // 1024 for l in lst[-1].split(",")[0].split("/")]
    ret["mbytes"]["added"] = lst2[0]
    ret["mbytes"]["updated"] = lst2[1]
    ret["mbytes"]["total"] = sum(lst2)

    return ret

@app.command()
def setup(perforce_path: str = Option(DEFAULT_FOLDER, prompt="Perforce path"), force: bool = Option(False)):
    """
    Creates the virtual drive and perforce workspaces from 
    //Project/[stream] -> s:/[stream]
    """
    p4 = P4()
    if not p4.port or p4.port == "perforce:1666" or force:
        secho("Perforce connection has not been established.", fg="yellow")
        host = prompt("Perforce connection string (ssl:[url]:1666):", default=p4.port)
        lst = host.split(":")
        if len(lst) != 3 or lst[0] != "ssl" or not lst[2].isdigit():
            abort("Perforce connection string is mangled. Expecting ssl:[url]:[port]")

        username = prompt("Perforce username (same as UWE)", default=p4.user)

        p4.port = host
        p4.user = username
        config_filename = "p4config.txt"
        echo(f"Saving {config_filename}")
        config_file = Path("~").expanduser() / config_filename
        contents = {}
        if config_file.exists():
            with config_file.open("r") as f:
                contents = {ll[0]: ll[1] for ll in [l.strip().split("=") for l in f.readlines()]}
                #print(contents)
        contents["P4PORT"] = host
        contents["P4USER"] = username
        with config_file.open("w") as f:
            for k, v in contents.items():
                f.write(f"{k}={v}\n")

    try:
        p4.connect()
    except Exception as e:
        abort(f"Cannot establish connection with Perforce server: {e}")

    perforce_path = Path(perforce_path).expanduser().resolve()
    _, _, free = shutil.disk_usage(perforce_path)
    free_gb = free // 1024 // 1024 // 1024
    if free_gb < MIN_FREE_GB:
        abort(f"You need to have at least {MIN_FREE_GB} GB free disk space but you have only {free_gb} GB")

    subst_cmd = f"subst {SUBST_DRIVE} {perforce_path}"
    if not perforce_path.exists():
        ret = prompt(f"Path {perforce_path} not found. Would you like to create it [y/n]?")
        if ret == "y":
            perforce_path.mkdir(parents=True, exist_ok=True)
        else:
            abort("Path not found")

    if is_windows:
        s_path = Path(SUBST_DRIVE)
        if s_path.exists():
            s_path_resolve = str(s_path.resolve()).lower()
            if s_path_resolve == str(perforce_path).lower():
                secho(f"{SUBST_DRIVE} virtual drive is already set up and pointing to {s_path_resolve}.", fg="green")
            elif not force:
                abort(f"{SUBST_DRIVE} virtual drive is pointing to another folder: {s_path_resolve}.")
        
        if not s_path.exists() or force:
            try:
                check_call(f"subst {SUBST_DRIVE} /D")
            except:
                pass
            check_call(subst_cmd)

        import winreg
        echo(f"Adding Virtual Drive {SUBST_DRIVE} -> {perforce_path} to startup")
        h = winreg.CreateKey(winreg.HKEY_CURRENT_USER, "Software\Microsoft\Windows\CurrentVersion\Run")
        winreg.SetValueEx(h, "Unknown Worlds Perforce Work Drive", 0, winreg.REG_SZ, subst_cmd)

        if not perforce_path.exists():
            abort(f"Failed to add subst for {SUBST_DRIVE}")
        root_path = SUBST_DRIVE
    else:
        root_path = str(perforce_path)

    try:
        all_client_specs = p4.run_clients("-u", p4.user)
    except Exception as e:
        if "P4PASSWD" in str(e):
            passwd = prompt(f"Please enter perforce password for {p4.user}", hide_input=True)
            try:
                p4.password = passwd
                p4.run_login()
                all_client_specs = p4.run_clients("-u", p4.user)
            except Exception as e:
                abort(str(e))
        else:
            abort(str(e))
    computer_name = prompt("What would you like to call this computer in Perforce (work, home, laptop, etc)", default="work")
    if not computer_name.isalpha() or computer_name != computer_name.lower():
        abort("Computer name must be lowercase with no symbols")
    for stream in STREAMS:
        stream_name = stream.split("/")[-1]
        mapping = f"{root_path}/{stream_name}"
        found = False
        for r in all_client_specs:
            root = r["Root"].lower()
            client = r["client"]
            host = r["Host"].lower()
            if root == mapping.lower() and host == hostname:
                if force:
                    secho(f"Deleting workspace {client} which was mapped to {root}", fg="yellow")
                    p4.run_client("-d", client)
                else:
                    secho(f"Workspace {client} already mapped to {root}", fg="green")
                    found = True
        if not found:
            client_spec = f"{p4.user}_{computer_name}_{stream_name}"
            echo(f"Creating workspace {client_spec} -> {mapping}")
            client = p4.fetch_client(client_spec)
            client["Root"] = mapping
            client["Stream"] = stream
            p4.save_client(client)
            p = Path(mapping)
            p.mkdir(parents=True, exist_ok=True)

    if prompt("Would you like to sync the workspaces now [y/n]", default="n") == "y":
        sync_workspaces()

@app.command()
def sync(stream: str = Option(""), force: bool = Option(False)):
    """
    Runs a full Perforce sync of the Project streams. Intented for initial project sync
    """
    sync_workspaces(stream, force)

def sync_workspaces(stream="", force=False):
    files_completed = 0
    old_files_completed = 0
    files_remaining = 0
    num_files = 0

    p4 = P4()
    p4.connect()
    specs = get_clientspecs(p4)
    stream = stream.lower()
    for s in STREAMS:
        if stream in s and s not in specs:
            abort(f"Stream {s} has no workspace. Please run init")

    for s in STREAMS:
        if stream not in s:
            continue
        echo(f"Syncing {s}...")
        p4.client = specs[s]["client"]
        stats = get_sync_stats(p4, force)
        num_files = stats['files']['total']
        batch_size = 200
        threads = 10

        if force:
            secho(f"Refetching all files in {s} (this will take a while)...")
            ret = p4.run_sync("--parallel", threads, "-f")
            num_files = get_sync_stats(p4)['files']['total']

        if num_files > 0:
            echo(f"Syncing {num_files} files...")
            with progressbar(length=num_files, show_pos=True) as progress:
                batch_size = 1000
                threads = 10
                for i in range(num_files//batch_size):
                    p4.run_sync("-m", batch_size, "--parallel", threads, "-q")
                    progress.update(batch_size)
            p4.run_sync()
            files_remaining = get_sync_stats(p4)['files']['total']
            if files_remaining == 0:
                secho(f"{s} is now up-to-date", fg="green")
            else:
                abort(f"{s} is not up to date after sync. Please sync manually")
        else:
            secho(f"{s} is already up-to-date", fg="green")

@app.command()
def workspaces():
    """
    Shows a list of your perforce workspaces
    """
    p4 = P4()
    p4.connect()
    try:
        ret = p4.run_clients("-u", p4.user)
    except Exception as e:
        if "P4PASSWD" in str(e):
            abort("Please log into perforce with p4 login")
    rows = []
    for r in ret:
        h = r["Host"]
        if h.lower() == socket.gethostname().lower():
            h = style(h, bold=True)
        else:
            h = style(h, fg="red")
        rows.append([r["client"], r["Stream"], r["Root"], h])
    tbl = tabulate(rows, headers=["Client", "Stream", "Root", "Host"])
    echo(tbl)
