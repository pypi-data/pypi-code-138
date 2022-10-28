def _reset_sys_path():
    # Clear generic sys.path[0]
    import os
    import sys

    resources = os.environ["RESOURCEPATH"]
    while sys.path[0] == resources:
        del sys.path[0]


_reset_sys_path()


"""
sys.argv emulation

This module starts a basic event loop to collect file- and url-open
AppleEvents. Those get converted to strings and stuffed into sys.argv.
When that is done we continue starting the application.

This is a workaround to convert scripts that expect filenames on the
command-line to work in a GUI environment. GUI applications should not
use this feature.

NOTE: This module uses ctypes and not the Carbon modules in the stdlib
because the latter don't work in 64-bit mode and are also not available
with python 3.x.
"""

import ctypes
import struct
import sys
import time


class AEDesc(ctypes.Structure):
    _fields_ = [
        ("descKey", ctypes.c_int),
        ("descContent", ctypes.c_void_p),
    ]


class EventTypeSpec(ctypes.Structure):
    _fields_ = [
        ("eventClass", ctypes.c_int),
        ("eventKind", ctypes.c_uint),
    ]


def _ctypes_setup():
    carbon = ctypes.CDLL("/System/Library/Carbon.framework/Carbon")

    # timer_func = ctypes.CFUNCTYPE(
    #        None, ctypes.c_void_p, ctypes.c_long)

    ae_callback = ctypes.CFUNCTYPE(
        ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p
    )
    carbon.AEInstallEventHandler.argtypes = [
        ctypes.c_int,
        ctypes.c_int,
        ae_callback,
        ctypes.c_void_p,
        ctypes.c_char,
    ]
    carbon.AERemoveEventHandler.argtypes = [
        ctypes.c_int,
        ctypes.c_int,
        ae_callback,
        ctypes.c_char,
    ]

    carbon.AEProcessEvent.restype = ctypes.c_int
    carbon.AEProcessEvent.argtypes = [ctypes.c_void_p]

    carbon.ReceiveNextEvent.restype = ctypes.c_int
    carbon.ReceiveNextEvent.argtypes = [
        ctypes.c_long,
        ctypes.POINTER(EventTypeSpec),
        ctypes.c_double,
        ctypes.c_char,
        ctypes.POINTER(ctypes.c_void_p),
    ]

    carbon.AEGetParamDesc.restype = ctypes.c_int
    carbon.AEGetParamDesc.argtypes = [
        ctypes.c_void_p,
        ctypes.c_int,
        ctypes.c_int,
        ctypes.POINTER(AEDesc),
    ]

    carbon.AECountItems.restype = ctypes.c_int
    carbon.AECountItems.argtypes = [
        ctypes.POINTER(AEDesc),
        ctypes.POINTER(ctypes.c_long),
    ]

    carbon.AEGetNthDesc.restype = ctypes.c_int
    carbon.AEGetNthDesc.argtypes = [
        ctypes.c_void_p,
        ctypes.c_long,
        ctypes.c_int,
        ctypes.c_void_p,
        ctypes.c_void_p,
    ]

    carbon.AEGetDescDataSize.restype = ctypes.c_int
    carbon.AEGetDescDataSize.argtypes = [ctypes.POINTER(AEDesc)]

    carbon.AEGetDescData.restype = ctypes.c_int
    carbon.AEGetDescData.argtypes = [
        ctypes.POINTER(AEDesc),
        ctypes.c_void_p,
        ctypes.c_int,
    ]

    carbon.FSRefMakePath.restype = ctypes.c_int
    carbon.FSRefMakePath.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint]

    return carbon


def _run_argvemulator(timeout=60):

    # Configure ctypes
    carbon = _ctypes_setup()

    # Is the emulator running?
    running = [True]

    timeout = [timeout]

    # Configure AppleEvent handlers
    ae_callback = carbon.AEInstallEventHandler.argtypes[2]

    (kAEInternetSuite,) = struct.unpack(">i", b"GURL")
    (kAEISGetURL,) = struct.unpack(">i", b"GURL")
    (kCoreEventClass,) = struct.unpack(">i", b"aevt")
    (kAEOpenApplication,) = struct.unpack(">i", b"oapp")
    (kAEOpenDocuments,) = struct.unpack(">i", b"odoc")
    (keyDirectObject,) = struct.unpack(">i", b"----")
    (typeAEList,) = struct.unpack(">i", b"list")
    (typeChar,) = struct.unpack(">i", b"TEXT")
    (typeFSRef,) = struct.unpack(">i", b"fsrf")
    FALSE = b"\0"
    TRUE = b"\1"
    eventLoopTimedOutErr = -9875

    (kEventClassAppleEvent,) = struct.unpack(">i", b"eppc")
    kEventAppleEvent = 1

    @ae_callback
    def open_app_handler(message, reply, refcon):
        # Got a kAEOpenApplication event, which means we can
        # start up. On some OSX versions this event is even
        # sent when an kAEOpenDocuments or kAEOpenURLs event
        # is sent later on.
        #
        # Therefore don't set running to false, but reduce the
        # timeout to at most two seconds beyond the current time.
        timeout[0] = min(timeout[0], time.time() - start + 2)
        return 0

    carbon.AEInstallEventHandler(
        kCoreEventClass, kAEOpenApplication, open_app_handler, 0, FALSE
    )

    @ae_callback
    def open_file_handler(message, reply, refcon):
        listdesc = AEDesc()
        sts = carbon.AEGetParamDesc(
            message, keyDirectObject, typeAEList, ctypes.byref(listdesc)
        )
        if sts != 0:
            print("argvemulator warning: cannot unpack open document event")
            running[0] = False
            return

        item_count = ctypes.c_long()
        sts = carbon.AECountItems(ctypes.byref(listdesc), ctypes.byref(item_count))
        if sts != 0:
            print("argvemulator warning: cannot unpack open document event")
            running[0] = False
            return

        desc = AEDesc()
        for i in range(item_count.value):
            sts = carbon.AEGetNthDesc(
                ctypes.byref(listdesc), i + 1, typeFSRef, 0, ctypes.byref(desc)
            )
            if sts != 0:
                print("argvemulator warning: cannot unpack open document event")
                running[0] = False
                return

            sz = carbon.AEGetDescDataSize(ctypes.byref(desc))
            buf = ctypes.create_string_buffer(sz)
            sts = carbon.AEGetDescData(ctypes.byref(desc), buf, sz)
            if sts != 0:
                print("argvemulator warning: cannot extract open document event")
                continue

            fsref = buf

            buf = ctypes.create_string_buffer(1024)
            sts = carbon.FSRefMakePath(ctypes.byref(fsref), buf, 1023)
            if sts != 0:
                print("argvemulator warning: cannot extract open document event")
                continue

            if sys.version_info[0] > 2:
                sys.argv.append(buf.value.decode("utf-8"))
            else:
                sys.argv.append(buf.value)

        running[0] = False
        return 0

    carbon.AEInstallEventHandler(
        kCoreEventClass, kAEOpenDocuments, open_file_handler, 0, FALSE
    )

    @ae_callback
    def open_url_handler(message, reply, refcon):
        listdesc = AEDesc()
        ok = carbon.AEGetParamDesc(
            message, keyDirectObject, typeAEList, ctypes.byref(listdesc)
        )
        if ok != 0:
            print("argvemulator warning: cannot unpack open document event")
            running[0] = False
            return

        item_count = ctypes.c_long()
        sts = carbon.AECountItems(ctypes.byref(listdesc), ctypes.byref(item_count))
        if sts != 0:
            print("argvemulator warning: cannot unpack open url event")
            running[0] = False
            return

        desc = AEDesc()
        for i in range(item_count.value):
            sts = carbon.AEGetNthDesc(
                ctypes.byref(listdesc), i + 1, typeChar, 0, ctypes.byref(desc)
            )
            if sts != 0:
                print("argvemulator warning: cannot unpack open URL event")
                running[0] = False
                return

            sz = carbon.AEGetDescDataSize(ctypes.byref(desc))
            buf = ctypes.create_string_buffer(sz)
            sts = carbon.AEGetDescData(ctypes.byref(desc), buf, sz)
            if sts != 0:
                print("argvemulator warning: cannot extract open URL event")

            else:
                if sys.version_info[0] > 2:
                    sys.argv.append(buf.value.decode("utf-8"))
                else:
                    sys.argv.append(buf.value)

        running[0] = False
        return 0

    carbon.AEInstallEventHandler(
        kAEInternetSuite, kAEISGetURL, open_url_handler, 0, FALSE
    )

    # Remove the funny -psn_xxx_xxx argument
    if len(sys.argv) > 1 and sys.argv[1].startswith("-psn_"):
        del sys.argv[1]

    start = time.time()
    now = time.time()
    eventType = EventTypeSpec()
    eventType.eventClass = kEventClassAppleEvent
    eventType.eventKind = kEventAppleEvent

    while running[0] and now - start < timeout[0]:
        event = ctypes.c_void_p()

        sts = carbon.ReceiveNextEvent(
            1,
            ctypes.byref(eventType),
            start + timeout[0] - now,
            TRUE,
            ctypes.byref(event),
        )

        if sts == eventLoopTimedOutErr:
            break

        elif sts != 0:
            print("argvemulator warning: fetching events failed")
            break

        sts = carbon.AEProcessEvent(event)
        if sts != 0:
            print("argvemulator warning: processing events failed")
            break

    carbon.AERemoveEventHandler(
        kCoreEventClass, kAEOpenApplication, open_app_handler, FALSE
    )
    carbon.AERemoveEventHandler(
        kCoreEventClass, kAEOpenDocuments, open_file_handler, FALSE
    )
    carbon.AERemoveEventHandler(kAEInternetSuite, kAEISGetURL, open_url_handler, FALSE)


def _argv_emulation():
    import os

    # only use if started by LaunchServices
    if os.environ.get("_PY2APP_LAUNCHED_"):
        _run_argvemulator()


_argv_emulation()


def _chdir_resource():
    import os

    os.chdir(os.environ["RESOURCEPATH"])


_chdir_resource()


def _disable_linecache():
    import linecache

    def fake_getline(*args, **kwargs):
        return ""

    linecache.orig_getline = linecache.getline
    linecache.getline = fake_getline


_disable_linecache()


import re
import sys

cookie_re = re.compile(rb"coding[:=]\s*([-\w.]+)")
if sys.version_info[0] == 2:
    default_encoding = "ascii"
else:
    default_encoding = "utf-8"


def guess_encoding(fp):
    for _i in range(2):
        ln = fp.readline()

        m = cookie_re.search(ln)
        if m is not None:
            return m.group(1).decode("ascii")

    return default_encoding


def _run():
    global __file__
    import os
    import site  # noqa: F401

    sys.frozen = "macosx_app"
    base = os.environ["RESOURCEPATH"]

    argv0 = os.path.basename(os.environ["ARGVZERO"])
    script = SCRIPT_MAP.get(argv0, DEFAULT_SCRIPT)  # noqa: F821

    path = os.path.join(base, script)
    sys.argv[0] = __file__ = path
    if sys.version_info[0] == 2:
        with open(path, "rU") as fp:
            source = fp.read() + "\n"
    else:
        with open(path, "rb") as fp:
            encoding = guess_encoding(fp)

        with open(path, "r", encoding=encoding) as fp:
            source = fp.read() + "\n"

        BOM = b"\xef\xbb\xbf".decode("utf-8")
        if source.startswith(BOM):
            source = source[1:]

    exec(compile(source, path, "exec"), globals(), globals())


def _setup_ctypes():
    import os
    from ctypes.macholib import dyld

    frameworks = os.path.join(os.environ["RESOURCEPATH"], "..", "Frameworks")
    dyld.DEFAULT_FRAMEWORK_FALLBACK.insert(0, frameworks)
    dyld.DEFAULT_LIBRARY_FALLBACK.insert(0, frameworks)


_setup_ctypes()


def _boot_multiprocessing():
    import sys
    import multiprocessing.spawn

    orig_get_command_line = multiprocessing.spawn.get_command_line
    def wrapped_get_command_line(**kwargs):
        orig_frozen = sys.frozen
        del sys.frozen
        try:
            return orig_get_command_line(**kwargs)
        finally:
            sys.frozen = orig_frozen
    multiprocessing.spawn.get_command_line = wrapped_get_command_line

_boot_multiprocessing()


import pkg_resources, zipimport, os

def find_eggs_in_zip(importer, path_item, only=False):
    if importer.archive.endswith('.whl'):
        # wheels are not supported with this finder
        # they don't have PKG-INFO metadata, and won't ever contain eggs
        return

    metadata = pkg_resources.EggMetadata(importer)
    if metadata.has_metadata('PKG-INFO'):
        yield Distribution.from_filename(path_item, metadata=metadata)
    for subitem in metadata.resource_listdir(''):
        if not only and pkg_resources._is_egg_path(subitem):
            subpath = os.path.join(path_item, subitem)
            dists = find_eggs_in_zip(zipimport.zipimporter(subpath), subpath)
            for dist in dists:
                yield dist
        elif subitem.lower().endswith(('.dist-info', '.egg-info')):
            subpath = os.path.join(path_item, subitem)
            submeta = pkg_resources.EggMetadata(zipimport.zipimporter(subpath))
            submeta.egg_info = subpath
            yield pkg_resources.Distribution.from_location(path_item, subitem, submeta)  # noqa: B950

def _fixup_pkg_resources():
    pkg_resources.register_finder(zipimport.zipimporter, find_eggs_in_zip)
    pkg_resources.working_set.entries = []
    list(map(pkg_resources.working_set.add_entry, sys.path))

_fixup_pkg_resources()



def _setup_openssl():
    import os
    resourcepath = os.environ["RESOURCEPATH"]
    os.environ["SSL_CERT_FILE"] = os.path.join(
        resourcepath, "openssl.ca", "no-such-file")
    os.environ["SSL_CERT_DIR"] = os.path.join(
        resourcepath, "openssl.ca", "no-such-file")

_setup_openssl()


def _boot_tkinter():
    import os

    resourcepath = os.environ["RESOURCEPATH"]
    os.putenv("TCL_LIBRARY", os.path.join(resourcepath, "lib/tcl8"))
    os.putenv("TK_LIBRARY", os.path.join(resourcepath, "lib/tk8.6"))
_boot_tkinter()


DEFAULT_SCRIPT='bull-code.py'
SCRIPT_MAP={}
_run()
