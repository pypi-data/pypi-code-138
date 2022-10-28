"""Tornado handler for bodo cluster management."""

import json

from jupyter_server.base.handlers import APIHandler
from jupyter_server.utils import url_path_join
from tornado import web

from .auto_attach import should_auto_attach
from .platform import PlatformClusterManager
from .remote_ikernels_manager import (
    cleanup_kernelspecs,
    get_remote_kernel_name_for_cluster,
)
from .ssh_keys_manager import cleanup_ssh_keys, get_cluster_ssh_key_fname
from .config import BASTION_IP, BASTION_USER, CLUSTER_USER


class ClusterRemoteIKernelHandler(APIHandler):
    """
    Handler for Remote IKernels on Clusters
    """

    @web.authenticated
    async def post(self, cluster_id: str) -> None:
        """
        Create a remote kernel on one of the hosts and return its name.
        """
        logging_prefix = f"[ClusterRemoteIKernelHandler.post][UUID: {cluster_id}]"
        self.log.info(f"{logging_prefix} Starting...")

        error = None
        try:
            hostlist = PlatformClusterManager.get_cluster_hostlist(
                cluster_id, logger=self.log
            )
            self.log.info(f"{logging_prefix} hostlist: {hostlist}")

            if BASTION_IP:
                ssh_key_fname = None
            else:
                ssh_key_fname: str = get_cluster_ssh_key_fname(
                    cluster_id, logger=self.log, hard_refresh=False,
                )
            self.log.info(f"{logging_prefix} ssh_key_fname: {ssh_key_fname}")

            tunnel_host: str = BASTION_IP
            tunnel_host_user: str = BASTION_USER
            cluster_user: str = CLUSTER_USER
            self.log.info(f"{logging_prefix} tunnel_host: {tunnel_host}")
            self.log.info(f"{logging_prefix} tunnel_host_user: {tunnel_host_user}")
            self.log.info(f"{logging_prefix} cluster_user: {cluster_user}")
            remote_kernel_name: str = get_remote_kernel_name_for_cluster(
                cluster_id,
                hostlist,
                logger=self.log,
                tunnel_host=tunnel_host,
                tunnel_host_user=tunnel_host_user,
                cluster_user=cluster_user,
                ssh_key_fname=ssh_key_fname,
            )
            self.log.info(f"{logging_prefix} remote_kernel_name: {remote_kernel_name}")
        except Exception as e:
            self.log.error(f"{logging_prefix} Error: {e}")
            remote_kernel_name = None
            error = str(e)

        self.log.info(f"{logging_prefix} Finishing...")
        self.finish(json.dumps({"remote_kernel_name": remote_kernel_name, "e": error}))


class PlatformClusterListHandler(APIHandler):
    @web.authenticated
    async def get(self):
        """
        Get list of clusters from the platform.
        Also do a kernelspec and ssh keys cleanup after.
        """
        logging_prefix = "[PlatformClusterListHandler.get]"
        # Parameter is parsed from URL and parsed to a boolean to be used in PlatformClusterManager.get_clusters_list
        force_refresh = self.get_argument("forceRefresh", "false").lower() == "true"
        self.log.info(f"{logging_prefix} Starting...")
        error = None
        try:
            clusters = PlatformClusterManager.get_clusters_list(
                logger=self.log, force_refresh=force_refresh
            )
            cluster_uuids = [cluster["uuid"] for cluster in clusters]
            cluster_uuids_set = frozenset(cluster_uuids)
            PlatformClusterManager.clusters_backup = clusters
            self.log.info(f"{logging_prefix} clusters: {clusters}")
        except Exception as e:
            self.log.error(f"{logging_prefix} Error: {e}")
            cluster_uuids_set = frozenset([])
            clusters = PlatformClusterManager.clusters_backup
            error = str(e)

        if error is None:
            try:
                self.log.info(f"{logging_prefix} Calling KernelSpec cleanup...")
                cleanup_kernelspecs(self.log, cluster_uuids_set)
                self.log.info(
                    f"{logging_prefix} Successfully finished KernelSpec cleanup..."
                )
            except Exception as e:
                self.log.warning(
                    f"{logging_prefix} Error during KernelSpec cleanup: {e}"
                )

            if not BASTION_IP:
                try:
                    self.log.info(f"{logging_prefix} Calling SSH Keys cleanup...")
                    cleanup_ssh_keys(self.log, cluster_uuids_set)
                    self.log.info(
                        f"{logging_prefix} Successfully finished SSH Keys cleanup..."
                    )
                except Exception as e:
                    self.log.warning(
                        f"{logging_prefix} Error during SSH Keys cleanup: {e}"
                    )

        self.log.info(f"{logging_prefix} Finishing...")
        self.finish(json.dumps({"clusters": clusters, "e": error}))


class AutoAttachHandler(APIHandler):
    """
    Determine whether a cluster should be auto attached to a notebook.
    """

    @web.authenticated
    async def get(self):
        logging_prefix = "[AutoAttachHandler.get]"
        self.log.info(f"{logging_prefix} Starting...")
        error = None

        try:
            auto_attach = should_auto_attach()
            self.log.info(f"{logging_prefix} auto_attach: {auto_attach}")

        except Exception as e:
            self.log.error(f"{logging_prefix} Error: {e}")
            auto_attach = None
            error = str(e)

        self.log.info(f"{logging_prefix} Finishing...")
        self.finish(json.dumps({"auto_attach": auto_attach, "e": error}))


class ResumeClusterHandler(APIHandler):
    @web.authenticated
    async def put(self, cluster_id: str) -> None:
        """
        Resume a specified cluster.
        """
        logging_prefix = "[PlatformResumeClusterHandler.put]"
        self.log.info(f"{logging_prefix} Starting...")
        error = None
        try:
            PlatformClusterManager.resume_cluster(cluster_id, logger=self.log)
            self.log.info(f"{logging_prefix} resuming cluster with id: {cluster_id}")
        except Exception as e:
            self.log.error(f"{logging_prefix} Error: {e}")
            error = str(e)

        self.log.info(f"{logging_prefix} Finishing...")
        self.finish(json.dumps({"e": error}))


class PauseClusterHandler(APIHandler):
    @web.authenticated
    async def put(self, cluster_id: str) -> None:
        """
        Pause a specified cluster.
        """
        logging_prefix = "[PlatformPauseClusterHandler.put]"
        self.log.info(f"{logging_prefix} Starting...")
        error = None
        try:
            PlatformClusterManager.pause_cluster(cluster_id, logger=self.log)
            self.log.info(f"{logging_prefix} pausing cluster with id: {cluster_id}")
        except Exception as e:
            self.log.error(f"{logging_prefix} Error: {e}")
            error = str(e)

        self.log.info(f"{logging_prefix} Finishing...")
        self.finish(json.dumps({"e": error}))


def setup_handlers(web_app):
    base_url = web_app.settings["base_url"]
    cluster_id_regex = r"(?P<cluster_id>[\w-]+)"
    remote_ikernel_cluster_path = url_path_join(
        base_url, rf"/cluster-remote-ikernel/{cluster_id_regex}"
    )
    cluster_list_path = url_path_join(base_url, r"/bodo/cluster")
    resume_cluster_path = url_path_join(
        base_url, rf"/bodo/cluster/{cluster_id_regex}/resume"
    )
    pause_cluster_path = url_path_join(
        base_url, rf"/bodo/cluster/{cluster_id_regex}/pause"
    )

    auto_attach_path = url_path_join(base_url, r"/bodo/autoattach")

    handlers = [
        (remote_ikernel_cluster_path, ClusterRemoteIKernelHandler),
        (cluster_list_path, PlatformClusterListHandler),
        (auto_attach_path, AutoAttachHandler),
        (resume_cluster_path, ResumeClusterHandler),
        (pause_cluster_path, PauseClusterHandler),
    ]
    web_app.add_handlers(".*$", handlers)
