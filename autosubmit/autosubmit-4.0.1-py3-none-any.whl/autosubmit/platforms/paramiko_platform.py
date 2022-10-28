import locale
from time import sleep
import sys
import socket
import os
import paramiko
import datetime
import time
import select
import re
from datetime import timedelta
import random
from autosubmit.job.job_common import Status
from autosubmit.job.job_common import Type
from autosubmit.platforms.platform import Platform
from bscearth.utils.date import date2str
from log.log import AutosubmitError, AutosubmitCritical, Log
from paramiko.ssh_exception import (SSHException)
import Xlib.support.connect as xlib_connect
from threading import Thread



class ParamikoPlatform(Platform):
    """
    Class to manage the connections to the different platforms with the Paramiko library.
    """

    def __init__(self, expid, name, config):
        """

        :param config:
        :param expid:
        :param name:
        """

        Platform.__init__(self, expid, name, config)
        self._ssh_output_err = ""
        self.connected = False
        self._default_queue = None
        self.job_status = None
        self._ssh = None
        self._ssh_config = None
        self._ssh_output = None
        self._user_config_file = None
        self._host_config = None
        self._host_config_id = None
        self.submit_cmd = ""
        self._ftpChannel = None
        self.transport = None
        self.channels = {}
        if sys.platform != "linux":
            self.poller = select.kqueue()
        else:
            self.poller = select.poll()
        self._header = None
        self._wrapper = None
        self.remote_log_dir = ""
        #self.get_job_energy_cmd = ""
        display = os.getenv('DISPLAY')
        if display is None:
            display = "localhost:0"
        self.local_x11_display = xlib_connect.get_display(display)

    @property
    def header(self):
        """
        Header to add to job for scheduler configuration

        :return: header
        :rtype: object
        """
        return self._header

    @property
    def wrapper(self):
        """
        Handler to manage wrappers

        :return: wrapper-handler
        :rtype: object
        """
        return self._wrapper

    def reset(self):
        self.connected = False
        self._ssh = None
        self._ssh_config = None
        self._ssh_output = None
        self._user_config_file = None
        self._host_config = None
        self._host_config_id = None
        self._ftpChannel = None
        self.transport = None
        self.channels = {}
        if sys.platform != "linux":
            self.poller = select.kqueue()
        else:
            self.poller = select.poll()
        display = os.getenv('DISPLAY')
        if display is None:
            display = "localhost:0"
        self.local_x11_display = xlib_connect.get_display(display)


    def test_connection(self):
        """
        Test if the connection is still alive, reconnect if not.
        """
        try:
            if not self.connected:
                self.reset()
                try:
                    self.restore_connection()
                    message = "OK"
                except BaseException as e:
                    message = str(e)
                if message.find("t accept remote connections") == -1:
                    transport = self._ssh.get_transport()
                    transport.send_ignore()
                return message
        except EOFError as e:
            self.connected = False
            raise AutosubmitError("[{0}] not alive. Host: {1}".format(
                self.name, self.host), 6002, str(e))
        except (AutosubmitError,AutosubmitCritical,IOError):
            self.connected = False
            raise
        except BaseException as e:
            self.connected = False
            raise AutosubmitCritical(str(e),7051)
            #raise AutosubmitError("[{0}] connection failed for host: {1}".format(self.name, self.host), 6002, e.message)

    def restore_connection(self):
        try:
            self.connected = False
            retries = 2
            retry = 0
            try:
                self.connect()
            except SSHException as e:
                raise
            except Exception as e:
                if ',' in self.host:
                    Log.printlog("Connection Failed to {0}, will test another host".format(
                        self.host.split(',')[0]), 6002)
                else:
                    raise AutosubmitCritical(
                        "First connection to {0} is failed, check host configuration or try another login node ".format(self.host), 7050,str(e))
            while self.connected is False and retry < retries:
                try:
                      self.connect(True)
                except:
                    pass
                retry += 1
            if not self.connected:
                trace = 'Can not create ssh or sftp connection to {0}: Connection could not be established to platform {1}\n Please, check your expid platform.conf to see if there are mistakes in the configuration\n Also Ensure that the login node listed on HOST parameter is available(try to connect via ssh on a terminal)\n Also you can put more than one host using a comma as separator'.format(
                    self.host, self.name)
                raise AutosubmitCritical(
                    'Experiment cant no continue without unexpected behaviour, Stopping Autosubmit', 7050, trace)

        except AutosubmitCritical:
            raise
        except SSHException as e:
            raise
        except Exception as e:
            raise AutosubmitCritical(
                'Cant connect to this platform due an unknown error', 7050, str(e))
    
    def threaded(fn):
        def wrapper(*args, **kwargs):
            thread = Thread(target=fn, args=args, kwargs=kwargs)
            thread.start()
            return thread
        return wrapper

    def connect(self, reconnect=False):
        """
        Creates ssh connection to host

        :return: True if connection is created, False otherwise
        :rtype: bool
        """
        try:
            display = os.getenv('DISPLAY')
            if display is None:
                display = "localhost:0"
            self.local_x11_display = xlib_connect.get_display(display)
            self._ssh = paramiko.SSHClient()
            self._ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            self._ssh_config = paramiko.SSHConfig()

            self._user_config_file = os.path.expanduser("~/.ssh/config")
            if os.path.exists(self._user_config_file):
                with open(self._user_config_file) as f:
                    self._ssh_config.parse(f)
            self._host_config = self._ssh_config.lookup(self.host)
            if "," in self._host_config['hostname']:
                if reconnect:
                    self._host_config['hostname'] = random.choice(
                        self._host_config['hostname'].split(',')[1:])
                else:
                    self._host_config['hostname'] = self._host_config['hostname'].split(',')[
                        0]
            if 'identityfile' in self._host_config:
                self._host_config_id = self._host_config['identityfile']

            if 'proxycommand' in self._host_config:
                self._proxy = paramiko.ProxyCommand(
                    self._host_config['proxycommand'])
                try:
                    self._ssh.connect(self._host_config['hostname'], 22, username=self.user,
                                      key_filename=self._host_config_id, sock=self._proxy, timeout=120 , banner_timeout=120)
                except:
                    self._ssh.connect(self._host_config['hostname'], 22, username=self.user,
                                      key_filename=self._host_config_id, sock=self._proxy, timeout=120,
                                      banner_timeout=120,disabled_algorithms={'pubkeys': ['rsa-sha2-256', 'rsa-sha2-512']})
            else:
                try:
                    self._ssh.connect(self._host_config['hostname'], 22, username=self.user,
                                      key_filename=self._host_config_id, timeout=120 , banner_timeout=120)
                except:
                    self._ssh.connect(self._host_config['hostname'], 22, username=self.user,
                                      key_filename=self._host_config_id, timeout=120 , banner_timeout=120,disabled_algorithms={'pubkeys': ['rsa-sha2-256', 'rsa-sha2-512']})
            self.transport = self._ssh.get_transport()
            #self.transport = paramiko.Transport((self._host_config['hostname'], 22))
            #self.transport.connect(username=self.user)
            window_size = pow(4, 12)  # about ~16MB chunks
            max_packet_size = pow(4, 12)
            #self._ftpChannel = self._ssh.open_sftp()
            self._ftpChannel = paramiko.SFTPClient.from_transport(self.transport,window_size=window_size,max_packet_size=max_packet_size)
            self.connected = True
        except SSHException as e:
            raise
        except IOError as e:
            if "refused" in e.strerror.lower():
                raise SSHException(" {0} doesn't accept remote connections. Check if there is an typo in the hostname".format(self.host))
            elif "name or service not known" in e.strerror.lower():
                raise SSHException(" {0} doesn't accept remote connections. Check if there is an typo in the hostname".format(self.host))
            else:
                raise AutosubmitError("File can't be located due an slow connection", 6016, str(e))
        except BaseException as e:
            self.connected = False
            if "Authentication failed." in str(e):
                raise AutosubmitCritical("Authentication Failed, please check the platform.conf of {0}".format(
                    self._host_config['hostname']), 7050, str(e))
            if not reconnect and "," in self._host_config['hostname']:
                self.restore_connection(reconnect=True)
            else:
                raise AutosubmitError(
                    "Couldn't establish a connection to the specified host, wrong configuration?", 6003, str(e))

    def check_completed_files(self, sections=None):
        if self.host == 'localhost':
            return None
        command = "find %s " % self.remote_log_dir
        if sections:
            for i, section in enumerate(sections.split()):
                command += " -name *%s_COMPLETED" % section
                if i < len(sections.split()) - 1:
                    command += " -o "
        else:
            command += " -name *_COMPLETED"

        if self.send_command(command, True):
            return self._ssh_output
        else:
            return None

    def remove_multiple_files(self, filenames):
        #command = "rm"
        log_dir = os.path.join(self.tmp_path, 'LOG_{0}'.format(self.expid))
        multiple_delete_previous_run = os.path.join(
            log_dir, "multiple_delete_previous_run.sh")
        if os.path.exists(log_dir):
            lang = locale.getlocale()[1]
            if lang is None:
                lang = locale.getdefaultlocale()[1]
                if lang is None:
                    lang = 'UTF-8'
            open(multiple_delete_previous_run, 'wb+').write( ("rm -f" + filenames).encode(lang))
            os.chmod(multiple_delete_previous_run, 0o770)
            self.send_file(multiple_delete_previous_run, False)
            command = os.path.join(self.get_files_path(),
                                   "multiple_delete_previous_run.sh")
            if self.send_command(command, ignore_log=True):
                return self._ssh_output
            else:
                return ""
        return ""

    def send_file(self, filename, check = True):
        """
        Sends a local file to the platform
        :param filename: name of the file to send
        :type filename: str
        """

        if check:
            self.check_remote_log_dir()
            self.delete_file(filename)
        try:
            local_path = os.path.join(os.path.join(self.tmp_path, filename))
            remote_path = os.path.join(
                self.get_files_path(), os.path.basename(filename))
            self._ftpChannel.put(local_path, remote_path)
            self._ftpChannel.chmod(remote_path, os.stat(local_path).st_mode)
            return True
        except IOError as e:
            raise AutosubmitError('Can not send file {0} to {1}'.format(os.path.join(
                self.tmp_path, filename)), os.path.join(self.get_files_path(), filename), 6004, str(e))
        except BaseException as e:
            raise AutosubmitError(
                'Send file failed. Connection seems to no be active', 6004)


    def get_list_of_files(self):
        return self._ftpChannel.get(self.get_files_path)

    # Gets .err and .out
    def get_file(self, filename, must_exist=True, relative_path='', ignore_log=False, wrapper_failed=False):
        """
        Copies a file from the current platform to experiment's tmp folder

        :param filename: file name
        :type filename: str
        :param must_exist: If True, raises an exception if file can not be copied
        :type must_exist: bool
        :param relative_path: path inside the tmp folder
        :type relative_path: str
        :return: True if file is copied successfully, false otherwise
        :rtype: bool
        """

        local_path = os.path.join(self.tmp_path, relative_path)
        if not os.path.exists(local_path):
            os.makedirs(local_path)

        file_path = os.path.join(local_path, filename)
        if os.path.exists(file_path):
            os.remove(file_path)
        remote_path = os.path.join(self.get_files_path(), filename)
        try:
            self._ftpChannel.get(remote_path, file_path)
            return True
        except Exception as e:
            try:
                os.remove(file_path)
            except:
                pass
            if str(e) in "Garbage":
                if not ignore_log:
                    Log.printlog(
                        "File {0} seems to no exists (skipping)".format(filename), 5004)
            if must_exist:
                if not ignore_log:
                    Log.printlog(
                        "File {0} does not exists".format(filename), 6004)
                return False
            else:
                if not ignore_log:
                    Log.printlog(
                        "Log file couldn't be retrieved: {0}".format(filename), 5000)
                return False

    def delete_file(self, filename):
        """
        Deletes a file from this platform

        :param filename: file name
        :type filename: str
        :return: True if successful or file does no exist
        :rtype: bool
        """

        try:
            self._ftpChannel.remove(os.path.join(
                self.get_files_path(), filename))
            return True
        except IOError as e:
            return False
        except BaseException as e:
            Log.error('Could not remove file {0} due a wrong configuration'.format(
                os.path.join(self.get_files_path(), filename)))
            if str(e).lower().find("garbage") != -1:
                raise AutosubmitCritical(
                    "Wrong User or invalid .ssh/config. Or invalid user in platform.conf or public key not set ", 7051, str(e))

    def move_file(self, src, dest, must_exist=False):
        """
        Moves a file on the platform (includes .err and .out)
        :param src: source name
        :type src: str
        :param dest: destination name
        :param must_exist: ignore if file exist or not
        :type dest: str
        """
        try:
            path_root = self.get_files_path()
            src = os.path.join(path_root, src)
            dest = os.path.join(path_root, dest)
            self._ftpChannel.rename(src,dest)
            return True

        except IOError as e:
            if str(e) in "Garbage":
                raise AutosubmitError('File {0} does not exists, something went wrong with the platform'.format(os.path.join(path_root,src)), 6004, str(e))
            if must_exist:
                raise AutosubmitError("File {0} does not exists".format(
                    os.path.join(path_root,src)), 6004, str(e))
            else:
                Log.debug("File {0} doesn't exists ".format(path_root))
                return False
        except Exception as e:
            if str(e) in "Garbage":
                raise AutosubmitError('File {0} does not exists'.format(
                    os.path.join(self.get_files_path(), src)), 6004, str(e))
            if must_exist:
                raise AutosubmitError("File {0} does not exists".format(
                    os.path.join(self.get_files_path(), src)), 6004, str(e))
            else:
                Log.printlog("Log file couldn't be moved: {0}".format(
                    os.path.join(self.get_files_path(), src)), 5001)
                return False

    def submit_job(self, job, script_name, hold=False, export="none"):
        """
        Submit a job from a given job object.

        :param job: job object
        :type job: autosubmit.job.job.Job
        :param script_name: job script's name
        :rtype scriptname: str
        :param hold: send job hold
        :type hold: boolean
        :return: job id for the submitted job
        :rtype: int
        """
        if job is None or not job:
            x11 = False
        else:
            x11 = job.x11

        cmd = self.get_submit_cmd(script_name, job, hold=hold, export=export)
        if cmd is None:
            return None
        if self.send_command(cmd,x11=x11):
            job_id = self.get_submitted_job_id(self.get_ssh_output(),x11=job.x11)
            Log.debug("Job ID: {0}", job_id)
            return int(job_id)
        else:
            return None

    def check_job_energy(self, job_id):
        """
        Checks job energy and return values. Defined in child classes.

        Args:
            job_id (int): ID of Job

        Returns:
            4-tuple (int, int, int, int): submit time, start time, finish time, energy
        """
        check_energy_cmd = self.get_job_energy_cmd(job_id)
        self.send_command(check_energy_cmd)
        return self.get_ssh_output()

    def submit_Script(self, hold=False):
        """
        Sends a Submitfile Script, exec in platform and retrieve the Jobs_ID.
        :param hold: send job hold
        :type hold: boolean
        :return: job id for the submitted job
        :rtype: int
        """
        raise NotImplementedError

    def check_job(self, job, default_status=Status.COMPLETED, retries=5, submit_hold_check=False, is_wrapper=False):
        """
        Checks job running status

        :param retries: retries
        :param job: job
        :type job: autosubmit.job.job.Job
        :param default_status: default status if job is not found
        :type job: class(job)
        :param default_status: status to assign if it can be retrieved from the platform
        :type default_status: autosubmit.job.job_common.Status
        :return: current job status
        :rtype: autosubmit.job.job_common.Status

        """
        job_id = job.id
        job_status = Status.UNKNOWN
        if type(job_id) is not int and type(job_id) is not str:
            Log.error(
                'check_job() The job id ({0}) is not an integer neither a string.', job_id)
            job.new_status = job_status
        sleep_time = 5
        sleep(2)
        self.send_command(self.get_checkjob_cmd(job_id))
        while self.get_ssh_output().strip(" ") == "" and retries > 0:
            retries = retries - 1
            Log.debug(
                'Retrying check job command: {0}', self.get_checkjob_cmd(job_id))
            Log.debug('retries left {0}', retries)
            Log.debug('Will be retrying in {0} seconds', sleep_time)
            sleep(sleep_time)
            sleep_time = sleep_time + 5
            self.send_command(self.get_checkjob_cmd(job_id))
        if retries >= 0:
            Log.debug('Successful check job command: {0}', self.get_checkjob_cmd(job_id))
            job_status = self.parse_job_output(
                self.get_ssh_output()).strip("\n")
            # URi: define status list in HPC Queue Class
            if job_status in self.job_status['COMPLETED'] or retries == 0:
                job_status = Status.COMPLETED
            elif job_status in self.job_status['RUNNING']:
                job_status = Status.RUNNING
                if not is_wrapper:
                    if job.status != Status.RUNNING:
                        job.start_time = datetime.datetime.now() # URi: start time
                    if job.start_time is not None and str(job.wrapper_type).lower() == "none":
                        wallclock = job.wallclock
                        if job.wallclock == "00:00":
                            wallclock == job.platform.max_wallclock
                        if wallclock != "00:00" and wallclock != "00:00:00" and wallclock != "":
                            if job.is_over_wallclock(job.start_time,wallclock):
                                try:
                                    job.platform.get_completed_files(job.name)
                                    job_status = job.check_completion(over_wallclock=True)
                                except:
                                    job_status = Status.FAILED
            elif job_status in self.job_status['QUEUING'] and (not job.hold or job.hold.lower() != "true"):
                job_status = Status.QUEUING
            elif job_status in self.job_status['QUEUING'] and (job.hold or job.hold.lower() == "true"):
                job_status = Status.HELD
            elif job_status in self.job_status['FAILED']:
                job_status = Status.FAILED
            else:
                job_status = Status.UNKNOWN
        else:
            Log.error(
                " check_job(), job is not on the queue system. Output was: {0}", self.get_checkjob_cmd(job_id))
            job_status = Status.UNKNOWN
            Log.error(
                'check_job() The job id ({0}) status is {1}.', job_id, job_status)
        if submit_hold_check:
            return job_status
        else:
            job.new_status = job_status

    def _check_jobid_in_queue(self, ssh_output, job_list_cmd):
        for job in job_list_cmd[:-1].split(','):
            if job not in ssh_output:
                return False
        return True

    def check_Alljobs(self, job_list, as_conf, retries=5):
        """
        Checks jobs running status
        :param job_list: list of jobs
        :type job_list: list
        :param as_conf: autosubmit configuration
        :type as_conf: autosubmitconfigparser.config.config.Config
        :param retries: retries
        :type retries: int
        :return: list of jobs with their status
        :rtype: list

        """
        job_status = Status.UNKNOWN
        remote_logs = as_conf.get_copy_remote_logs()
        job_list_cmd = ""
        for job,job_prev_status in job_list:
            job_list_cmd += str(job.id)+","
        if job_list_cmd[-1] == ",":
            job_list_cmd=job_list_cmd[:-1]
        cmd = self.get_checkAlljobs_cmd(job_list_cmd)
        sleep_time = 5
        sleep(sleep_time)
        self.send_command(cmd)
        while not self._check_jobid_in_queue(self.get_ssh_output(), job_list_cmd) and retries >= 0:
            self.send_command(cmd)
            Log.debug('Retrying check job command: {0}', cmd)
            Log.debug('retries left {0}', retries)
            Log.debug('Will be retrying in {0} seconds', sleep_time)
            retries -= 1
            sleep(sleep_time)
            sleep_time = sleep_time + 5
        job_list_status = self.get_ssh_output()
        if retries >= 0:
            Log.debug('Successful check job command')
            in_queue_jobs = []
            list_queue_jobid = ""
            for job,job_prev_status in job_list:
                job_id = job.id
                job_status = self.parse_Alljobs_output(job_list_status, job_id)
                while len(job_status) <= 0 and retries >= 0:
                    retries -= 1
                    self.send_command(cmd)
                    job_list_status = self.get_ssh_output()
                    job_status = self.parse_Alljobs_output(job_list_status, job_id)
                    if len(job_status) <= 0:
                        Log.debug('Retrying check job command: {0}', cmd)
                        Log.debug('retries left {0}', retries)
                        Log.debug('Will be retrying in {0} seconds', sleep_time)
                        sleep(sleep_time)
                        sleep_time = sleep_time + 5
                # URi: define status list in HPC Queue Class
                if job_status in self.job_status['COMPLETED']:
                    job_status = Status.COMPLETED
                elif job_status in self.job_status['RUNNING']:
                    job_status = Status.RUNNING
                elif job_status in self.job_status['QUEUING']:
                    if job.hold:
                        job_status = Status.HELD  # release?
                    else:
                        job_status = Status.QUEUING
                    list_queue_jobid += str(job.id) + ','
                    in_queue_jobs.append(job)
                elif job_status in self.job_status['FAILED']:
                    job_status = Status.FAILED
                elif retries == 0:
                    job_status = Status.COMPLETED
                    job.update_status(as_conf)

                else:
                    job_status = Status.UNKNOWN
                    Log.error(
                        'check_job() The job id ({0}) status is {1}.', job_id, job_status)
                job.new_status = job_status
            reason = str()
            if self.type == 'slurm' and len(in_queue_jobs) > 0:
                cmd = self.get_queue_status_cmd(list_queue_jobid)
                self.send_command(cmd)
                queue_status = self._ssh_output
                for job in in_queue_jobs:
                    reason = self.parse_queue_reason(queue_status, job.id)
                    if job.queuing_reason_cancel(reason):
                        Log.error(
                            "Job {0} will be cancelled and set to FAILED as it was queuing due to {1}", job.name, reason)
                        self.send_command(
                            self.platform.cancel_cmd + " {0}".format(job.id))
                        job.new_status = Status.FAILED
                        job.update_status(as_conf)
                        return
                    elif reason == '(JobHeldUser)':
                        job.new_status = Status.HELD
                        if not job.hold:
                            # SHOULD BE MORE CLASS (GET_scontrol realease but not sure if this can be implemented on others PLATFORMS
                            self.send_command("scontrol release {0}".format(job.id))
                            job.new_status = Status.QUEUING # If it was HELD and was released, it should be QUEUING next.                                                        
                        else:
                            pass
                    # This shouldn't happen anymore TODO delete
                    elif reason == '(JobHeldAdmin)':
                        Log.debug(
                            "Job {0} Failed to be HELD, canceling... ", job.name)
                        job.new_status = Status.WAITING
                        job.platform.send_command(
                            job.platform.cancel_cmd + " {0}".format(job.id))

        else:
            for job in job_list:
                job_status = Status.UNKNOWN
                Log.warning(
                    'check_job() The job id ({0}) from platform {1} has an status of {2}.', job.id, self.name, job_status)
            raise AutosubmitError("Some Jobs are in Unknown status", 6008)
            # job.new_status=job_status

    def get_jobid_by_jobname(self,job_name,retries=2):
        """
        Get job id by job name
        :param retries: retries
        :type retries: int
        :return: job id
        """
        #sleep(5)
        cmd = self.get_jobid_by_jobname_cmd(job_name)
        self.send_command(cmd)
        job_id_name = self.get_ssh_output()
        while len(job_id_name) <= 0 and retries > 0:
            self.send_command(cmd)
            job_id_name = self.get_ssh_output()
            retries -= 1
            sleep(2)
        if retries >= 0:
            #get id last line
            job_ids_names = job_id_name.split('\n')[1:-1]
            #get all ids by jobname
            job_ids = [job_id.split(',')[0] for job_id in job_ids_names]
        return job_ids







    def get_checkjob_cmd(self, job_id):
        """
        Returns command to check job status on remote platforms

        :param job_id: id of job to check
        :param job_id: int
        :return: command to check job status
        :rtype: str
        """
        raise NotImplementedError

    def get_checkAlljobs_cmd(self, jobs_id):
        """
        Returns command to check jobs status on remote platforms

        :param jobs_id: id of jobs to check
        :param jobs_id: str
        :return: command to check job status
        :rtype: str
        """
        raise NotImplementedError



    def flush_out(self, session):
        while session.recv_ready():
            sys.stdout.write(session.recv(4096))
        while session.recv_stderr_ready():
            sys.stderr.write(session.recv_stderr(4096))

    def x11_handler(self, channel, xxx_todo_changeme):
        '''handler for incoming x11 connections
        for each x11 incoming connection,
        - get a connection to the local display
        - maintain bidirectional map of remote x11 channel to local x11 channel
        - add the descriptors to the poller
        - queue the channel (use transport.accept())'''
        (src_addr, src_port) = xxx_todo_changeme
        x11_chanfd = channel.fileno()
        local_x11_socket = xlib_connect.get_socket(*self.local_x11_display[:4])
        local_x11_socket_fileno = local_x11_socket.fileno()
        self.channels[x11_chanfd] = channel, local_x11_socket
        self.channels[local_x11_socket_fileno] = local_x11_socket, channel
        self.poller.register(x11_chanfd, select.POLLIN)
        self.poller.register(local_x11_socket, select.POLLIN)
        self.transport._queue_incoming_channel(channel)

    def flush_out(self,session):
        while session.recv_ready():
            sys.stdout.write(session.recv(4096))
        while session.recv_stderr_ready():
            sys.stderr.write(session.recv_stderr(4096))
    @threaded
    def x11_status_checker(self, session, session_fileno):
        self.transport.accept()
        while not session.exit_status_ready():
            try:
                if sys.platform != "linux":
                    self.poller = self.poller.kqueue()
                else:
                    self.poller = self.poller.poll()
                # accept subsequent x11 connections if any
                if len(self.transport.server_accepts) > 0:
                    self.transport.accept()
                if not poll:  # this should not happen, as we don't have a timeout.
                    break
                for fd, event in poll:
                    if fd == session_fileno:
                        self.flush_out(session)
                    # data either on local/remote x11 socket
                    if fd in list(self.channels.keys()):
                        channel, counterpart = self.channels[fd]
                        try:
                            # forward data between local/remote x11 socket.
                            data = channel.recv(4096)
                            counterpart.sendall(data)
                        except socket.error:
                            channel.close()
                            counterpart.close()
                            del self.channels[fd]
            except:
                pass


    def exec_command(self, command, bufsize=-1, timeout=None, get_pty=False,retries=3, x11=False):
        """
        Execute a command on the SSH server.  A new `.Channel` is opened and
        the requested command is executed.  The command's input and output
        streams are returned as Python ``file``-like objects representing
        stdin, stdout, and stderr.

        :param str command: the command to execute
        :param int bufsize:
            interpreted the same way as by the built-in ``file()`` function in
            Python
        :param int timeout:
            set command's channel timeout. See `Channel.settimeout`.settimeout
        :return:
            the stdin, stdout, and stderr of the executing command, as a
            3-tuple

        :raises SSHException: if the server fails to execute the command
        """
        while retries > 0:
            try:
                chan = self.transport.open_session()
                if x11 == "true":
                    display = os.getenv('DISPLAY')
                    if display is None or not display:
                        display = "localhost:0"
                    self.local_x11_display = xlib_connect.get_display(display)
                    chan.request_x11(handler=self.x11_handler)
                else:
                    chan.settimeout(timeout)
                if x11 == "true":
                    command = command + " ; sleep infinity"
                    chan.exec_command(command)
                    chan_fileno = chan.fileno()
                    self.poller.register(chan_fileno, select.POLLIN)
                    self.x11_status_checker(chan, chan_fileno)
                else:
                    chan.exec_command(command)
                stdin = chan.makefile('wb', bufsize)
                stdout = chan.makefile('rb', bufsize)
                stderr = chan.makefile_stderr('rb', bufsize)
                return stdin, stdout, stderr
            except paramiko.SSHException as e:
                if str(e) in "SSH session not active":
                    self._ssh = None
                    self.restore_connection()
                timeout = timeout + 60
                retries = retries - 1
        if retries <= 0:
            return False , False, False
    def exec_command_x11(self, command, bufsize=-1, timeout=None, get_pty=False,retries=3, x11=False):
        session = self.transport.open_session()
        session.request_x11(handler=self.x11_handler)
        session.exec_command(command + " ; sleep infinity")
        session_fileno = session.fileno()
        self.poller.register(session_fileno, select.POLLIN)
        self.x11_status_checker(session, session_fileno)
        pass
    def send_command(self, command, ignore_log=False, x11 = False):
        """
        Sends given command to HPC

        :param command: command to send
        :type command: str
        :return: True if executed, False if failed
        :rtype: bool
        """
        lang = locale.getlocale()[1]
        if lang is None:
            lang = locale.getdefaultlocale()[1]
            if lang is None:
                lang = 'UTF-8'
        if "rsync" in command or "find" in command or "convertLink" in command:
            timeout = None  # infinite timeout on migrate command
        elif "rm" in command:
            timeout = 60
        else:
            timeout = 60 * 2
        stderr_readlines = []
        stdout_chunks = []

        try:
            stdin, stdout, stderr = self.exec_command(command, x11=x11)
            channel = stdout.channel
            if not x11:
                channel.settimeout(timeout)
                stdin.close()
                channel.shutdown_write()
            stdout_chunks.append(stdout.channel.recv(len(stdout.channel.in_buffer)))
            while not channel.closed or channel.recv_ready() or channel.recv_stderr_ready():
                # stop if channel was closed prematurely, and there is no data in the buffers.
                got_chunk = False
                readq, _, _ = select.select([stdout.channel], [], [], 2)
                for c in readq:
                    if c.recv_ready():
                        stdout_chunks.append(
                            stdout.channel.recv(len(c.in_buffer)))
                        #stdout_chunks.append(" ")
                        got_chunk = True
                    if c.recv_stderr_ready():
                        # make sure to read stderr to prevent stall
                        stderr_readlines.append(
                            stderr.channel.recv_stderr(len(c.in_stderr_buffer)))
                        #stdout_chunks.append(" ")
                        got_chunk = True
                if x11 == "true":
                    got_chunk = True
                    break
                if not got_chunk and stdout.channel.exit_status_ready() and not stderr.channel.recv_stderr_ready() and not stdout.channel.recv_ready():
                    # indicate that we're not going to read from this channel anymore
                    stdout.channel.shutdown_read()
                    # close the channel
                    stdout.channel.close()
                    break
            # close all the pseudofiles
            if not x11:
                stdout.close()
                stderr.close()


            self._ssh_output = ""
            self._ssh_output_err = ""
            for s in stdout_chunks:
                if s.decode(lang) != '':
                    self._ssh_output += s.decode(lang)
            for errorLineCase in stderr_readlines:
                self._ssh_output_err += errorLineCase.decode(lang)

                errorLine = errorLineCase.lower().decode(lang)
                if "not active" in errorLine:
                    raise AutosubmitError(
                        'SSH Session not active, will restart the platforms', 6005)
                if errorLine.find("command not found") != -1:
                    raise AutosubmitCritical("scheduler is not installed.",7052,self._ssh_output_err)
                elif errorLine.find("syntax error") != -1:
                    raise AutosubmitCritical("Syntax error",7052,self._ssh_output_err)
                elif errorLine.find("refused") != -1 or errorLine.find("slurm_persist_conn_open_without_init") != -1 or errorLine.find("slurmdbd") != -1 or errorLine.find("submission failed") != -1 or errorLine.find("git clone") != -1 or errorLine.find("sbatch: error: ") != -1 or errorLine.find("not submitted") != -1 or errorLine.find("invalid") != -1:
                    if (self._submit_command_name == "sbatch" and (errorLine.find("policy") != -1 or errorLine.find("invalid") != -1) ) or (self._submit_command_name == "sbatch" and errorLine.find("argument") != -1) or (self._submit_command_name == "bsub" and errorLine.find("job not submitted") != -1) or self._submit_command_name == "ecaccess-job-submit" or self._submit_command_name == "qsub ":
                        raise AutosubmitError(errorLine, 7014, "Bad Parameters.")
                    raise AutosubmitError('Command {0} in {1} warning: {2}'.format(command, self.host,self._ssh_output_err, 6005))

            if not ignore_log:
                if len(stderr_readlines) > 0:
                    Log.printlog('Command {0} in {1} warning: {2}'.format(command, self.host,self._ssh_output_err, 6006))
                else:
                    pass
                    #Log.debug('Command {0} in {1} successful with out message: {2}', command, self.host, self._ssh_output)
            return True
        except AttributeError as e:
            raise AutosubmitError(
                'Session not active: {0}'.format(str(e)), 6005)
        except AutosubmitCritical as e:
            raise
        except AutosubmitError as e:
            raise
        except IOError as e:
            raise AutosubmitError(str(e),6016)
        except BaseException as e:
            raise AutosubmitError('Command {0} in {1} warning: {2}'.format(
                command, self.host, '\n'.join(stderr_readlines)), 6005, str(e))

    def parse_job_output(self, output):
        """
        Parses check job command output, so it can be interpreted by autosubmit

        :param output: output to parse
        :type output: str
        :return: job status
        :rtype: str
        """
        raise NotImplementedError

    def parse_Alljobs_output(self, output, job_id):
        """
        Parses check jobs command output, so it can be interpreted by autosubmit
        :param output: output to parse
        :param job_id: select the job to parse
        :type output: str
        :return: job status
        :rtype: str
        """
        raise NotImplementedError

    def open_submit_script(self):
        pass

    def get_submit_script(self):
        pass

    def get_submit_cmd(self, job_script, job_type, hold=False, export= ""):
        """
        Get command to add job to scheduler

        :param job_type:
        :param job_script: path to job script
        :param job_script: str
        :param hold: submit a job in a held status
        :param hold: boolean
        :param export: modules that should've downloaded
        :param export: string
        :return: command to submit job to platforms
        :rtype: str
        """
        raise NotImplementedError

    def get_mkdir_cmd(self):
        """
        Gets command to create directories on HPC

        :return: command to create directories on HPC
        :rtype: str
        """
        raise NotImplementedError

    def parse_queue_reason(self, output):
        raise NotImplementedError

    def get_ssh_output(self):
        """
        Gets output from last command executed

        :return: output from last command
        :rtype: str
        """
        #Log.debug('Output {0}', self._ssh_output)

        #Log.debug('Output {0}', self._ssh_output)
        if self._ssh_output is None or not self._ssh_output:
            self._ssh_output = ""
        return self._ssh_output

    def get_ssh_output_err(self):
        return self._ssh_output_err

    def get_call(self, job_script, job, export="none",timeout=-1):
        """
        Gets execution command for given job

        :param job: job
        :type job: Job
        :param job_script: script to run
        :type job_script: str
        :return: command to execute script
        :rtype: str
        """
        executable = ''
        if job.type == Type.BASH:
            executable = 'bash'
        elif job.type == Type.PYTHON:
            executable = 'python'
        elif job.type == Type.R:
            executable = 'Rscript'
        remote_logs = (job.script_name + ".out."+str(job.fail_count), job.script_name + ".err."+str(job.fail_count))
        if timeout < 1:
            command = export + ' nohup ' + executable + ' {0} > {1} 2> {2} & echo $!'.format(
                os.path.join(self.remote_log_dir, job_script),
                os.path.join(self.remote_log_dir, remote_logs[0]),
                os.path.join(self.remote_log_dir, remote_logs[1]),
            )
        else:
            command = export + "timeout {0}".format(timeout) + ' nohup ' + executable + ' {0} > {1} 2> {2} & echo $!'.format(
                os.path.join(self.remote_log_dir, job_script),
                os.path.join(self.remote_log_dir, remote_logs[0]),
                os.path.join(self.remote_log_dir, remote_logs[1]),
            )
        return command


    @staticmethod
    def get_pscall(job_id):
        """
        Gets command to check if a job is running given process identifier

        :param job_id: process indentifier
        :type job_id: int
        :return: command to check job status script
        :rtype: str
        """
        return 'nohup kill -0 {0} > /dev/null 2>&1; echo $?'.format(job_id)

    def get_submitted_job_id(self, output, x11 = False):
        """
        Parses submit command output to extract job id
        :param output: output to parse
        :type output: str
        :return: job id
        :rtype: str
        """
        raise NotImplementedError

    def get_header(self, job):
        """
        Gets header to be used by the job

        :param job: job
        :type job: Job
        :return: header to use
        :rtype: str
        """
        if str(job.processors) == '1':
            header = self.header.SERIAL
        else:
            header = self.header.PARALLEL
        str_datetime = date2str(datetime.datetime.now(), 'S')
        if str(job.wrapper_type).lower() != "vertical":
            out_filename = "{0}.cmd.out.{1}".format(job.name,job.fail_count)
            err_filename = "{0}.cmd.err.{1}".format(job.name,job.fail_count)
        else:
            out_filename = "{0}.cmd.out".format(job.name)
            err_filename = "{0}.cmd.err".format(job.name)
        header = header.replace('%OUT_LOG_DIRECTIVE%', out_filename)
        header = header.replace('%ERR_LOG_DIRECTIVE%', err_filename)

        if hasattr(self.header, 'get_queue_directive'):
            header = header.replace(
                '%QUEUE_DIRECTIVE%', self.header.get_queue_directive(job))
        if hasattr(self.header, 'get_partition_directive'):
            header = header.replace(
                '%PARTITION_DIRECTIVE%', self.header.get_partition_directive(job))
        if hasattr(self.header, 'get_tasks_per_node'):
            header = header.replace(
                '%TASKS_PER_NODE_DIRECTIVE%', self.header.get_tasks_per_node(job))
        if hasattr(self.header, 'get_threads_per_task'):
            header = header.replace(
                '%THREADS_PER_TASK_DIRECTIVE%', self.header.get_threads_per_task(job))
        if job.x11 == "true":
            header = header.replace(
                '%X11%', "SBATCH --x11=batch")
        else:
            header = header.replace(
                '%X11%', "")
        if hasattr(self.header, 'get_scratch_free_space'):
            header = header.replace(
                '%SCRATCH_FREE_SPACE_DIRECTIVE%', self.header.get_scratch_free_space(job))
        if hasattr(self.header, 'get_custom_directives'):
            header = header.replace(
                '%CUSTOM_DIRECTIVES%', self.header.get_custom_directives(job))
        if hasattr(self.header, 'get_exclusivity'):
            header = header.replace(
                '%EXCLUSIVITY_DIRECTIVE%', self.header.get_exclusivity(job))
        if hasattr(self.header, 'get_account_directive'):
            header = header.replace(
                '%ACCOUNT_DIRECTIVE%', self.header.get_account_directive(job))
        if hasattr(self.header, 'get_memory_directive'):
            header = header.replace(
                '%MEMORY_DIRECTIVE%', self.header.get_memory_directive(job))
        if hasattr(self.header, 'get_memory_per_task_directive'):
            header = header.replace(
                '%MEMORY_PER_TASK_DIRECTIVE%', self.header.get_memory_per_task_directive(job))
        if hasattr(self.header, 'get_hyperthreading_directive'):
            header = header.replace(
                '%HYPERTHREADING_DIRECTIVE%', self.header.get_hyperthreading_directive(job))
        return header
    def parse_time(self,wallclock):
        regex = re.compile(r'(((?P<hours>\d+):)((?P<minutes>\d+)))(:(?P<seconds>\d+))?')
        parts = regex.match(wallclock)
        if not parts:
            return
        parts = parts.groupdict()
        time_params = {}
        for name, param in parts.items():
            if param:
                time_params[name] = int(param)
        return timedelta(**time_params)

    def closeConnection(self):
        if self._ftpChannel is not None and len(str(self._ftpChannel)) > 0:
            self._ftpChannel.close()
        if self._ssh is not None and len(str(self._ssh)) > 0:
            self._ssh.close()
            self.transport.close()
            self.transport.stop_thread()
            try:
                del self._ssh
                del self._ftpChannel
                del self.transport
            except:
                pass

    def check_tmp_exists(self):
        try:
            if self.send_command("ls {0}".format(self.temp_dir)):
                if "no such file or directory" in self.get_ssh_output_err().lower():
                    return False
                else:
                    return True
            else:
                return False
        except Exception as e:
            return False
    
    def check_remote_permissions(self):
        try:
            path = os.path.join(self.scratch, self.project, self.user, "permission_checker_azxbyc")
            try:
                self._ftpChannel.mkdir(path)
                self._ftpChannel.rmdir(path)
            except IOError as e:
                self._ftpChannel.rmdir(path)
                self._ftpChannel.mkdir(path)
                self._ftpChannel.rmdir(path)
            return True
        except:
            return False
    
    def check_remote_log_dir(self):
        """
        Creates log dir on remote host
        """


        try:
            if self.send_command(self.get_mkdir_cmd()):
                Log.debug('{0} has been created on {1} .',
                          self.remote_log_dir, self.host)
            else:
                Log.debug('Could not create the DIR {0} to HPC {1}'.format(
                    self.remote_log_dir, self.host))
        except BaseException as e:
            raise AutosubmitError("Couldn't send the file {0} to HPC {1}".format(
                self.remote_log_dir, self.host), 6004, str(e))


class ParamikoPlatformException(Exception):
    """
    Exception raised from HPC queues
    """

    def __init__(self, msg):
        self.message = msg
