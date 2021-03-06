from epumgmt.api.actions import ACTIONS
from epumgmt.main import ControlArg

a = []
ALL_EC_ARGS_LIST = a

################################################################################
# EM ARGUMENTS
#
# The following cmdline arguments may be queried via Parameters, using either
# the 'name' as the argument or simply the object like:
#   
#   params.get_arg_or_none(em_args.GRACE_PERIOD)
# 
################################################################################

actionlist = str(ACTIONS().all_actions())
actionlist = actionlist[1:] # remove '['
actionlist = actionlist[:-1] # remove ']'
ACTION = ControlArg("action", "-a")
a.append(ACTION)
ACTION.help = "Action for the program to take: %s" % actionlist

CONF = ControlArg("conf", "-c", metavar="PATH")
a.append(CONF)
CONF.help = "Absolute path to main.conf.  Required (shell script adds the default)."

DRYRUN = ControlArg("dryrun", None, noval=True)
#a.append(DRYRUN)
DRYRUN.help = "Do as little real things as possible, will still affect filesystem, for example logs and information persistence. (not implemented yet)"

KILLNUM = ControlArg("killnum", "-k", metavar="NUM")
a.append(KILLNUM)
KILLNUM.help = "For the fetchkill action, number of VMs to terminate."

NAME = ControlArg("name", "-n", metavar="RUN_NAME")
a.append(NAME)
NAME.help = "Unique run name for logs and management.  Can use across multiple invocations for launches that belong together."

GRAPH_NAME = ControlArg("graphname", "-r", metavar="GRAPH_NAME")
a.append(GRAPH_NAME)
GRAPH_NAME.help = "For the generate-graph action, name of graph to generate: stacked-vms or job-tts."

GRAPH_TYPE = ControlArg("graphtype", "-t", metavar="GRAPH_TYPE")
a.append(GRAPH_TYPE)
GRAPH_TYPE.help = "For the generate-graph action, output file type: eps or png."

WORKLOAD_FILE = ControlArg("workloadfilename", "-f", metavar="WORKLOAD_FILE")
a.append(WORKLOAD_FILE)
WORKLOAD_FILE.help = "For the execute-workload-test action, file name of workload definition file."

CLOUDINITD_DIR = ControlArg("cloudinitdir", "-C", metavar="PATH")
a.append(CLOUDINITD_DIR)
CLOUDINITD_DIR.help = "Path to the directory where cloudinit databases are kept.  default is ~/.cloudinit"

REPORT_INSTANCE = ControlArg("instance-report", None, metavar="COLUMNS")
#a.append(REPORT_INSTANCE)
REPORT_INSTANCE.help = "Used with '--action %s'. Batch mode for machine parsing instance status. Report selected columns from choice of the following separated by comma: service,instanceid,iaas_state,iaas_state_time,heartbeat_time,heartbeat_state" % ACTIONS.STATUS

REPORT_SERVICE = ControlArg("service-report", None, metavar="COLUMNS")
#a.append(REPORT_SERVICE)
REPORT_SERVICE.help = "Used with '--action %s'. Batch mode for machine parsing service status. Report selected columns from choice of the following separated by comma: service,last_queuelen_size,last_queuelen_time,de_state,de_conf" % ACTIONS.STATUS

STATUS_NOUPDATE = ControlArg("no-update", None, noval=True)
a.append(STATUS_NOUPDATE)
STATUS_NOUPDATE.help = "Used with '--action %s'.  If used, %s does not try to find any new information." % (ACTIONS.STATUS, ACTIONS.STATUS)

NEWN = ControlArg("newn", None)
a.append(NEWN)
NEWN.help = "Used with '--action %s'. Syntax is controller_name:N[,controller_name:N,...]" % ACTIONS.RECONFIGURE_N

CONTROLLER = ControlArg("controller", None)
a.append(CONTROLLER)
CONTROLLER.help = "Some actions only work on a specific controller"
