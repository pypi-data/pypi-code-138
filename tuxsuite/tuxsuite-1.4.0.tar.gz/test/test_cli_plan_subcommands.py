# -*- coding: utf-8 -*-

import sys
import json
import pytest
import tuxsuite


@pytest.fixture
def plan_json():
    plan = {
        "project": "tuxsuite/senthil",
        "uid": "1qsx3P3UROY9DwTUV48cEre3UO7",
        "name": "i386 kernel",
        "description": "Build and test i386 with every toolchains",
        "user": None,
        "user_agent": None,
        "provisioning_time": "2021-11-01T19:38:31.142790",
        "builds": {
            "count": 6,
            "results": [
                # Watch the error counts and warning counts which differ in
                # each build / test.
                {
                    "project": "tuxsuite/senthil",
                    "uid": "1qsx3vvpbsyQS7gVwfdwBHZzcCX",
                    "plan": "1qsx3P3UROY9DwTUV48cEre3UO7",
                    "kconfig": ["defconfig"],
                    "target_arch": "x86_64",
                    "toolchain": "clang-nightly",
                    "build_name": "",
                    "client_token": "537c0a39-5919-48a3-96c2-31773aaae988",
                    "environment": {},
                    "make_variables": {},
                    "targets": [],
                    "git_repo": "https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git",
                    "git_ref": "master",
                    "git_sha": "454859c552da78b0f587205d308401922b56863e",
                    "download_url": "https://builds.tuxbuild.com/1qsx3vvpbsyQS7gVwfdwBHZzcCX/",
                    "kernel_image": "",
                    "user": "senthil.kumaran@linaro.org",
                    "user_agent": None,
                    "state": "provisioning",  # case: status provisioning
                    "result": "pass",
                    "waited_by": ["1qsx5iBMtsjD24OgjWW9tatj4HE"],
                    "errors_count": 0,  # case: error count 0
                    "warnings_count": 0,  # case: warning count 0
                    "kernel_patch_file": None,
                    "provisioning_time": "2021-11-01T19:38:31.161747",
                    "running_time": None,
                    "finished_time": None,
                    "git_short_log": "454859c552da (\"Merge tag 'arc-5.12-rc7'\")",
                    "kernel_image_name": "bzImage",
                    "duration": 409,
                    "build_status": "pass",
                    "tuxbuild_status": "complete",
                    "kernel_version": "5.12.0-rc6",
                    "status_message": "build completed",
                },
                {
                    "project": "tuxsuite/senthil",
                    "uid": "1qsx3vvpbsyQS7gVwfdwBHZzcCX",
                    "plan": "1qsx3P3UROY9DwTUV48cEre3UO7",
                    "kconfig": ["defconfig"],
                    "target_arch": "x86_64",
                    "toolchain": "clang-nightly",
                    "build_name": "",
                    "client_token": "537c0a39-5919-48a3-96c2-31773aaae988",
                    "environment": {},
                    "make_variables": {},
                    "targets": [],
                    "git_repo": "https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git",
                    "git_ref": "master",
                    "git_sha": "454859c552da78b0f587205d308401922b56863e",
                    "download_url": "https://builds.tuxbuild.com/1qsx3vvpbsyQS7gVwfdwBHZzcCX/",
                    "kernel_image": "",
                    "user": "senthil.kumaran@linaro.org",
                    "user_agent": None,
                    "state": "finished",
                    "result": "pass",
                    "waited_by": ["1qsx5iBMtsjD24OgjWW9tatj4HE"],
                    "errors_count": 0,  # case: error count 0
                    "warnings_count": 1,  # case: warning count 1
                    "kernel_patch_file": None,
                    "provisioning_time": "2021-11-01T19:38:31.161747",
                    "running_time": None,
                    "finished_time": None,
                    "git_short_log": "454859c552da (\"Merge tag 'arc-5.12-rc7'\")",
                    "kernel_image_name": "bzImage",
                    "duration": 409,
                    "build_status": "pass",
                    "tuxbuild_status": "complete",
                    "kernel_version": "5.12.0-rc6",
                    "status_message": "build completed",
                },
                {
                    "project": "tuxsuite/senthil",
                    "uid": "1qsx3vvpbsyQS7gVwfdwBHZzcCX",
                    "plan": "1qsx3P3UROY9DwTUV48cEre3UO7",
                    "kconfig": ["defconfig"],
                    "target_arch": "x86_64",
                    "toolchain": "clang-nightly",
                    "build_name": "",
                    "client_token": "537c0a39-5919-48a3-96c2-31773aaae988",
                    "environment": {},
                    "make_variables": {},
                    "targets": [],
                    "git_repo": "https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git",
                    "git_ref": "master",
                    "git_sha": "454859c552da78b0f587205d308401922b56863e",
                    "download_url": "https://builds.tuxbuild.com/1qsx3vvpbsyQS7gVwfdwBHZzcCX/",
                    "kernel_image": "",
                    "user": "senthil.kumaran@linaro.org",
                    "user_agent": None,
                    "state": "running",  # case: status running
                    "result": "pass",
                    "waited_by": ["1qsx5iBMtsjD24OgjWW9tatj4HE"],
                    "errors_count": 0,  # case: error count 0
                    "warnings_count": 2,  # case: warning count 2
                    "kernel_patch_file": None,
                    "provisioning_time": "2021-11-01T19:38:31.161747",
                    "running_time": None,
                    "finished_time": None,
                    "git_short_log": "454859c552da (\"Merge tag 'arc-5.12-rc7'\")",
                    "kernel_image_name": "bzImage",
                    "duration": 409,
                    "build_status": "pass",
                    "tuxbuild_status": "complete",
                    "kernel_version": "5.12.0-rc6",
                    "status_message": "build completed",
                },
                {
                    "project": "tuxsuite/senthil",
                    "uid": "1qsx3vvpbsyQS7gVwfdwBHZzcCX",
                    "plan": "1qsx3P3UROY9DwTUV48cEre3UO7",
                    "kconfig": ["defconfig"],
                    "target_arch": "x86_64",
                    "toolchain": "clang-nightly",
                    "build_name": "",
                    "client_token": "537c0a39-5919-48a3-96c2-31773aaae988",
                    "environment": {},
                    "make_variables": {},
                    "targets": [],
                    "git_repo": "https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git",
                    "git_ref": "master",
                    "git_sha": "454859c552da78b0f587205d308401922b56863e",
                    "download_url": "https://builds.tuxbuild.com/1qsx3vvpbsyQS7gVwfdwBHZzcCX/",
                    "kernel_image": "",
                    "user": "senthil.kumaran@linaro.org",
                    "user_agent": None,
                    "state": "finished",
                    "result": "fail",  # case: result fail with errors/warnings
                    "waited_by": ["1qsx5iBMtsjD24OgjWW9tatj4HE"],
                    "errors_count": 2,
                    "warnings_count": 4,
                    "kernel_patch_file": None,
                    "provisioning_time": "2021-11-01T19:38:31.161747",
                    "running_time": None,
                    "finished_time": None,
                    "git_short_log": "454859c552da (\"Merge tag 'arc-5.12-rc7'\")",
                    "kernel_image_name": "bzImage",
                    "duration": 409,
                    "build_status": "fail",
                    "tuxbuild_status": "complete",
                    "kernel_version": "5.12.0-rc6",
                    "status_message": "build completed",
                },
                {
                    "project": "tuxsuite/senthil",
                    "uid": "1qsx3vvpbsyQS7gVwfdwBHZzcCX",
                    "plan": "1qsx3P3UROY9DwTUV48cEre3UO7",
                    "kconfig": ["defconfig"],
                    "target_arch": "x86_64",
                    "toolchain": "clang-nightly",
                    "build_name": "",
                    "client_token": "537c0a39-5919-48a3-96c2-31773aaae988",
                    "environment": {},
                    "make_variables": {},
                    "targets": [],
                    "git_repo": "https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git",
                    "git_ref": "master",
                    "git_sha": "454859c552da78b0f587205d308401922b56863e",
                    "download_url": "https://builds.tuxbuild.com/1qsx3vvpbsyQS7gVwfdwBHZzcCX/",
                    "kernel_image": "",
                    "user": "senthil.kumaran@linaro.org",
                    "user_agent": None,
                    "state": "finished",
                    "result": "fail",  # case: result fail with 1 error
                    "waited_by": ["1qsx5iBMtsjD24OgjWW9tatj4HE"],
                    "errors_count": 1,
                    "warnings_count": 4,
                    "kernel_patch_file": None,
                    "provisioning_time": "2021-11-01T19:38:31.161747",
                    "running_time": None,
                    "finished_time": None,
                    "git_short_log": "454859c552da (\"Merge tag 'arc-5.12-rc7'\")",
                    "kernel_image_name": "bzImage",
                    "duration": 409,
                    "build_status": "fail",
                    "tuxbuild_status": "complete",
                    "kernel_version": "5.12.0-rc6",
                    "status_message": "build completed",
                },
                {
                    "project": "tuxsuite/senthil",
                    "uid": "1qsx3vvpbsyQS7gVwfdwBHZzcCX",
                    "plan": "1qsx3P3UROY9DwTUV48cEre3UO7",
                    "kconfig": ["defconfig"],
                    "target_arch": "x86_64",
                    "toolchain": "clang-nightly",
                    "build_name": "",
                    "client_token": "537c0a39-5919-48a3-96c2-31773aaae988",
                    "environment": {},
                    "make_variables": {},
                    "targets": [],
                    "git_repo": "https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git",
                    "git_ref": "master",
                    "git_sha": "454859c552da78b0f587205d308401922b56863e",
                    "download_url": "https://builds.tuxbuild.com/1qsx3vvpbsyQS7gVwfdwBHZzcCX/",
                    "kernel_image": "",
                    "user": "senthil.kumaran@linaro.org",
                    "user_agent": None,
                    "state": "finished",
                    "result": "error",  # case: result error with 1 error
                    "waited_by": ["1qsx5iBMtsjD24OgjWW9tatj4HE"],
                    "errors_count": 1,
                    "warnings_count": 4,
                    "kernel_patch_file": None,
                    "provisioning_time": "2021-11-01T19:38:31.161747",
                    "running_time": None,
                    "finished_time": None,
                    "git_short_log": "454859c552da (\"Merge tag 'arc-5.12-rc7'\")",
                    "kernel_image_name": "bzImage",
                    "duration": 409,
                    "build_status": "error",
                    "tuxbuild_status": "complete",
                    "kernel_version": "5.12.0-rc6",
                    "status_message": "build completed",
                },
            ],
            "next": None,
        },
        "tests": {
            "count": 6,
            "results": [
                {
                    "project": "tuxsuite/senthil",
                    "device": "qemu-x86_64",
                    "uid": "1qsx5iBMtsjD24OgjWW9tatj4HE",
                    "kernel": "https://builds.tuxbuild.com/1qsx3vvpbsyQS7gVwfdwBHZzcCX/bzImage",
                    "ap_romfw": None,
                    "mcp_fw": None,
                    "mcp_romfw": None,
                    "modules": None,
                    "parameters": None,
                    "rootfs": None,
                    "scp_fw": None,
                    "scp_romfw": None,
                    "fip": None,
                    "tests": ["boot", "ltp-smoke"],
                    "user": None,
                    "user_agent": None,
                    "state": "waiting",  # case: status waiting
                    "result": "pass",  # case: result pass
                    "results": {"boot": "pass", "ltp-smoke": "pass"},
                    "plan": "1qsx3P3UROY9DwTUV48cEre3UO7",
                    "waiting_for": "1qsx3vvpbsyQS7gVwfdwBHZzcCX",
                    "boot_args": None,
                    "provisioning_time": "2021-04-08T11:46:53.297621",
                    "running_time": "2021-04-08T11:46:54.355808",
                    "finished_time": "2021-04-08T11:47:39.082080",
                    "duration": 45,
                },
                {
                    "project": "tuxsuite/senthil",
                    "device": "qemu-x86_64",
                    "uid": "1qsx5iBMtsjD24OgjWW9tatj4HE",
                    "kernel": "https://builds.tuxbuild.com/1qsx3vvpbsyQS7gVwfdwBHZzcCX/bzImage",
                    "ap_romfw": None,
                    "mcp_fw": None,
                    "mcp_romfw": None,
                    "modules": None,
                    "parameters": None,
                    "rootfs": None,
                    "scp_fw": None,
                    "scp_romfw": None,
                    "fip": None,
                    "tests": ["boot", "ltp-smoke"],
                    "user": None,
                    "user_agent": None,
                    "state": "provisioning",  # case: status provisioning
                    "result": "fail",  # case: result fail
                    "results": {"boot": "fail", "ltp-smoke": "pass"},
                    "plan": "1qsx3P3UROY9DwTUV48cEre3UO7",
                    "waiting_for": "1qsx3vvpbsyQS7gVwfdwBHZzcCX",
                    "boot_args": None,
                    "provisioning_time": "2021-04-08T11:46:53.297621",
                    "running_time": "2021-04-08T11:46:54.355808",
                    "finished_time": "2021-04-08T11:47:39.082080",
                    "duration": 45,
                },
                {
                    "project": "tuxsuite/senthil",
                    "device": "qemu-x86_64",
                    "uid": "1qsx5iBMtsjD24OgjWW9tatj4HE",
                    "kernel": "https://builds.tuxbuild.com/1qsx3vvpbsyQS7gVwfdwBHZzcCX/bzImage",
                    "ap_romfw": None,
                    "mcp_fw": None,
                    "mcp_romfw": None,
                    "modules": None,
                    "parameters": None,
                    "rootfs": None,
                    "scp_fw": None,
                    "scp_romfw": None,
                    "fip": None,
                    "tests": ["boot", "ltp-smoke"],
                    "user": None,
                    "user_agent": None,
                    "state": "running",  # case: status running
                    "result": "error",  # case: result error
                    "results": {"boot": "fail", "ltp-smoke": "pass"},
                    "plan": "1qsx3P3UROY9DwTUV48cEre3UO7",
                    "waiting_for": "1qsx3vvpbsyQS7gVwfdwBHZzcCX",
                    "boot_args": None,
                    "provisioning_time": "2021-04-08T11:46:53.297621",
                    "running_time": "2021-04-08T11:46:54.355808",
                    "finished_time": "2021-04-08T11:47:39.082080",
                    "duration": 45,
                },
                {
                    "project": "tuxsuite/senthil",
                    "device": "qemu-x86_64",
                    "uid": "1qsx5iBMtsjD24OgjWW9tatj4HE",
                    "kernel": "https://builds.tuxbuild.com/1qsx3vvpbsyQS7gVwfdwBHZzcCX/bzImage",
                    "ap_romfw": None,
                    "mcp_fw": None,
                    "mcp_romfw": None,
                    "modules": None,
                    "parameters": None,
                    "rootfs": None,
                    "scp_fw": None,
                    "scp_romfw": None,
                    "fip": None,
                    "tests": ["boot", "ltp-smoke"],
                    "user": None,
                    "user_agent": None,
                    "state": "finished",
                    "result": "pass",  # case: result pass
                    "results": {"boot": "pass", "ltp-smoke": "pass"},
                    "plan": "1qsx3P3UROY9DwTUV48cEre3UO7",
                    "waiting_for": None,  # case: standalone test
                    "boot_args": None,
                    "provisioning_time": "2021-04-08T11:46:53.297621",
                    "running_time": "2021-04-08T11:46:54.355808",
                    "finished_time": "2021-04-08T11:47:39.082080",
                    "duration": 45,
                },
                {
                    "project": "tuxsuite/senthil",
                    "device": "qemu-x86_64",
                    "uid": "1qsx5iBMtsjD24OgjWW9tatj4HE",
                    "kernel": "https://builds.tuxbuild.com/1qsx3vvpbsyQS7gVwfdwBHZzcCX/bzImage",
                    "ap_romfw": None,
                    "mcp_fw": None,
                    "mcp_romfw": None,
                    "modules": None,
                    "parameters": None,
                    "rootfs": None,
                    "scp_fw": None,
                    "scp_romfw": None,
                    "fip": None,
                    "tests": ["boot", "ltp-smoke"],
                    "user": None,
                    "user_agent": None,
                    "state": "finished",
                    "result": "fail",  # case: result fail
                    "results": {"boot": "fail", "ltp-smoke": "pass"},
                    "plan": "1qsx3P3UROY9DwTUV48cEre3UO7",
                    "waiting_for": None,  # case: standalone test
                    "boot_args": None,
                    "provisioning_time": "2021-04-08T11:46:53.297621",
                    "running_time": "2021-04-08T11:46:54.355808",
                    "finished_time": "2021-04-08T11:47:39.082080",
                    "duration": 45,
                },
                {
                    "project": "tuxsuite/senthil",
                    "device": "qemu-x86_64",
                    "uid": "1qsx5iBMtsjD24OgjWW9tatj4HE",
                    "kernel": "https://builds.tuxbuild.com/1qsx3vvpbsyQS7gVwfdwBHZzcCX/bzImage",
                    "ap_romfw": None,
                    "mcp_fw": None,
                    "mcp_romfw": None,
                    "modules": None,
                    "parameters": None,
                    "rootfs": None,
                    "scp_fw": None,
                    "scp_romfw": None,
                    "fip": None,
                    "tests": ["boot", "ltp-smoke"],
                    "user": None,
                    "user_agent": None,
                    "state": "finished",
                    "result": "error",  # case: result error
                    "results": {"boot": "fail", "ltp-smoke": "pass"},
                    "plan": "1qsx3P3UROY9DwTUV48cEre3UO7",
                    "waiting_for": None,  # case: standalone test
                    "boot_args": None,
                    "provisioning_time": "2021-04-08T11:46:53.297621",
                    "running_time": "2021-04-08T11:46:54.355808",
                    "finished_time": "2021-04-08T11:47:39.082080",
                    "duration": 45,
                },
            ],
            "next": None,
        },
        "oebuilds": {"count": 0, "results": [], "next": None},
    }
    return json.dumps(plan).encode("utf-8")


@pytest.fixture
def bake_plan_json():
    bake_plan = {
        "project": "tuxsuite/alok",
        "uid": "29EbSmPfjpbYQj8ZuaBpsiA8CbW",
        "name": "armv7 validation",
        "description": "Build and test linux kernel for armv7",
        "user": "alok.ranjan@linaro.org",
        "user_agent": "tuxsuite/0.43.10",
        "provisioning_time": "2022-05-16T06:06:33.830964",
        "oebuilds": {
            "count": 2,
            "results": [
                {
                    "project": "tuxsuite/alok",
                    "uid": "29EbSyjM7FZgX1X2FDvpq0hxomz",
                    "plan": "29EbSmPfjpbYQj8ZuaBpsiA8CbW",
                    "distro": "rpb",
                    "machine": "ledge-multi-armv7",
                    "container": "ubuntu-20.04",
                    "environment": {},
                    "local_conf": [],
                    "bblayers_conf": [],
                    "artifacts": [],
                    "target": "rpb-console-image rpb-console-image-test rpb-desktop-image rpb-desktop-image-test",
                    "envsetup": "setup-environment",
                    "user": "alok.ranjan@linaro.org",
                    "user_agent": "tuxsuite/0.43.10",
                    "download_url": "https://oebuilds.tuxbuild.com/29EbSyjM7FZgX1X2FDvpq0hxomz/",
                    "sources": {
                        "repo": {
                            "branch": "qcom/dunfell",
                            "manifest": "default.xml",
                            "url": "https://github.com/96boards/oe-rpb-manifest.git",
                        }
                    },
                    "state": "finished",
                    "result": "fail",
                    "waited_by": [],
                    "errors_count": 0,
                    "warnings_count": 0,
                    "running_time": "2022-05-16T06:09:04.713320",
                    "finished_time": "2022-05-16T06:09:46.534596",
                    "manifest_file": "None",
                    "provisioning_time": "2022-05-16T06:06:35.312535",
                    "duration": 43,
                    "status_message": "",
                },
                {
                    "project": "tuxsuite/alok",
                    "uid": "29EbSycpmLu8Nut5SoZFCwJaRER",
                    "plan": "29EbSmPfjpbYQj8ZuaBpsiA8CbW",
                    "distro": "rpb",
                    "machine": "dragonboard-845c",
                    "container": "ubuntu-20.04",
                    "environment": {},
                    "local_conf": [],
                    "bblayers_conf": [],
                    "artifacts": [],
                    "target": "rpb-console-image rpb-console-image-test rpb-desktop-image rpb-desktop-image-test",
                    "envsetup": "setup-environment",
                    "user": "alok.ranjan@linaro.org",
                    "user_agent": "tuxsuite/0.43.10",
                    "download_url": "https://oebuilds.tuxbuild.com/29EbSycpmLu8Nut5SoZFCwJaRER/",
                    "sources": {
                        "repo": {
                            "branch": "qcom/dunfell",
                            "manifest": "default.xml",
                            "url": "https://github.com/96boards/oe-rpb-manifest.git",
                        }
                    },
                    "state": "finished",
                    "result": "pass",
                    "waited_by": [],
                    "errors_count": 0,
                    "warnings_count": 0,
                    "running_time": "2022-05-16T06:09:04.709211",
                    "finished_time": "2022-05-16T08:06:04.740891",
                    "manifest_file": "None",
                    "provisioning_time": "2022-05-16T06:06:35.312683",
                    "duration": 7021,
                    "status_message": "",
                },
            ],
            "next": None,
        },
        "builds": {"count": 0, "results": [], "next": None},
        "tests": {"count": 0, "results": [], "next": None},
    }
    return json.dumps(bake_plan).encode("utf-8")


@pytest.fixture
def plan_list_json():
    plan_list = {
        "count": 1,
        "results": [
            {
                "project": "tuxsuite/senthil",
                "uid": "1zjHLXHufFpOd5XjuhkWpYZfK0y",
                "name": "linux stable",
                "description": "Build linux stable",
                "user": "senthil.kumaran@linaro.org",
                "user_agent": "tuxsuite/0.35.0",
                "provisioning_time": "2021-10-19T14:42:01.896219",
            },
        ],
        "next": None,
    }
    return json.dumps(plan_list).encode("utf-8")


def test_plan_handle_get(mocker, plan_json, config, response, monkeypatch):
    monkeypatch.setattr(
        sys, "argv", ["tuxsuite", "plan", "get", "1tOhlD2nkPsRNNTMB5Lj09n1IVQ"]
    )
    response.status_code = 200
    response._content = plan_json
    get_req = mocker.patch("requests.get", return_value=response)
    tuxsuite.cli.main()
    assert get_req.call_count == 1

    # Test json out
    mocker.resetall()
    monkeypatch.setattr(
        sys,
        "argv",
        ["tuxsuite", "plan", "get", "1tOhlD2nkPsRNNTMB5Lj09n1IVQ", "--json"],
    )
    response.status_code = 200
    response._content = plan_json
    get_req = mocker.patch("requests.get", return_value=response)
    tuxsuite.cli.main()
    assert get_req.call_count == 1

    # Test failure case when the response is not 200
    response.status_code = 500
    get_req = mocker.patch("requests.get", return_value=response)
    with pytest.raises(NotImplementedError):
        tuxsuite.cli.main()
    assert get_req.call_count == 1

    mocker.resetall()
    response.status_code = 200
    response._content = plan_json
    get_req = mocker.patch("requests.get", return_value=response)
    monkeypatch.setattr(
        sys,
        "argv",
        ["tuxsuite", "plan", "get", "1tOhlD2nkPsRNNTMB5Lj09n1IVQ", "--json"],
    )
    tuxsuite.cli.main()


def test_plan_handle_list(mocker, plan_list_json, config, response, monkeypatch):
    monkeypatch.setattr(sys, "argv", ["tuxsuite", "plan", "list"])
    monkeypatch.setattr("sys.stdout.isatty", lambda: True)
    response.status_code = 200
    response._content = plan_list_json
    list_req = mocker.patch("requests.get", return_value=response)
    with pytest.raises(SystemExit) as exit:
        tuxsuite.cli.main()
    assert exit.value.code == 0
    assert list_req.call_count == 2

    # Test json out
    monkeypatch.setattr(sys, "argv", ["tuxsuite", "plan", "list", "--json"])
    response.status_code = 200
    response._content = plan_list_json
    list_req = mocker.patch("requests.get", return_value=response)
    tuxsuite.cli.main()
    assert exit.value.code == 0
    assert list_req.call_count == 1

    # Test failure case when the response is not 200
    response.status_code = 500
    list_req = mocker.patch("requests.get", return_value=response)
    with pytest.raises(NotImplementedError):
        tuxsuite.cli.main()
    assert list_req.call_count == 1

    mocker.resetall()
    response.status_code = 200
    response._content = plan_list_json
    list_req = mocker.patch("requests.get", return_value=response)
    monkeypatch.setattr(
        sys,
        "argv",
        ["tuxsuite", "plan", "list"],
    )
    with pytest.raises(SystemExit):
        tuxsuite.cli.main()
    assert list_req.call_count == 2


def test_bake_plan_handle_get(mocker, bake_plan_json, config, response, monkeypatch):
    monkeypatch.setattr(
        sys, "argv", ["tuxsuite", "plan", "get", "29EbSmPfjpbYQj8ZuaBpsiA8CbW"]
    )
    response.status_code = 200
    response._content = bake_plan_json
    get_req = mocker.patch("requests.get", return_value=response)
    tuxsuite.cli.main()
    assert get_req.call_count == 1

    # Test json out
    mocker.resetall()
    monkeypatch.setattr(
        sys,
        "argv",
        ["tuxsuite", "plan", "get", "29EbSmPfjpbYQj8ZuaBpsiA8CbW", "--json"],
    )
    response.status_code = 200
    response._content = bake_plan_json
    get_req = mocker.patch("requests.get", return_value=response)
    tuxsuite.cli.main()
    assert get_req.call_count == 1

    # Test failure case when the response is not 200
    response.status_code = 500
    get_req = mocker.patch("requests.get", return_value=response)
    with pytest.raises(NotImplementedError):
        tuxsuite.cli.main()
    assert get_req.call_count == 1
