from em_core import core, EPUMgmtOpts
import sys
import traceback

import em_deprecated
import em_optparse
from epumgmt.api.exceptions import *
from epumgmt.api import *
import remote_debug

def main(argv=None):
    if os.name != 'posix':
        print >>sys.stderr, "Only runs on POSIX systems."
        return 3

    # Enabled by a constant in the remote_debug module.
    remote_debug.connect_debugger_if_enabled()
    
    parser = em_optparse.parsersetup()

    if argv:
        (opts, args) = parser.parse_args(argv[1:])
    else:
        (opts, args) = parser.parse_args()
       
    epu = EPUMgmtOpts(cmd_opts=opts)
 
    try:
        dbgmsgs = em_deprecated.deprecated_args(opts)
        
        # From here 'down' there is no concept of a commandline program, only
        # 'args' which could be coming from any kind of protocol based request.
        # To make such a thing, construct an opts objects with the expected
        # member names (see the em_args module) and pass it in.
        core(epu, dbgmsgs=dbgmsgs)

    except InvalidInput, e:
        msg = "\nProblem with input: %s" % e.msg
        print >>sys.stderr, msg
        return 1

    except InvalidConfig, e:
        msg = "\nProblem with configuration: %s" % e.msg
        print >>sys.stderr, msg
        return 2

    except IncompatibleEnvironment, e:
        msg = "\nProblem with environment: %s" % e.msg
        print >>sys.stderr, msg
        return 3

    except UnexpectedError, e:
        msg = "\nProblem executing: %s" % e.msg
        print >>sys.stderr, msg
        return 4
        
    except KeyboardInterrupt, e:
        print >>sys.stderr, "\nCancelled by ctrl-c/signal"
        return 5
        
    except ProgrammingError,e:
        msg = "*** Developer error ***\n"
        msg += "   If this is a non-modified release, please report all\n"
        msg += "   the following output:\n"
        msg += "%s" % e.msg
        print >>sys.stderr, msg
        traceback.print_tb(sys.exc_info()[2])
        return 42
        
    except:
        msg = "\n*** Unexpected error ***\n"
        msg += "   If this is a non-modified release, please report all\n"
        msg += "   the following output:\n"
        print >>sys.stderr, msg
        exception_type = sys.exc_type
        try:
            exceptname = exception_type.__name__ 
        except AttributeError:
            exceptname = exception_type
        errstr = "%s: %s" % (str(exceptname), str(sys.exc_value))
        print >>sys.stderr, errstr
        traceback.print_tb(sys.exc_info()[2])
        return 42
    
    return 0

if __name__ == "__main__":
    exitcode = main()
    if exitcode != 0:
        sys.stderr.write("\nExiting with error code: %d\n\n" % exitcode)
    sys.stderr.flush()
    sys.exit(exitcode)
