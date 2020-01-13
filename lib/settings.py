# BESS install location
DEFAULT_BESSDIR = '~/bess'

# directory to hold (temporal) output files
TMP_DIR = '/tmp/'

# file containing profiler results (produced by profiler.py)
PROFILER_FILE = 'profiler_results.json'

# enable if 'show pipeline' statistics are required
ENABLE_OGATE_TRACKING = False

# enable 'stop-the-world' assumption of the controller
ENABLE_STOPTHEWORLD = False

# extra controller deadtime in seconds
EXTRA_CONTROLLER_DEADTIME = 0

# tolerance for various SLO violations
# currently applied for the overdelay-bound and the rate-limit check
DEFAULT_TOLERANCE = 0.05

# default batch size
BATCH_SIZE = 32
DELTA_TRIGGER_MAX = BATCH_SIZE

# default size of the bursts generated by the bulk source
# avoid powers of two setting to avoid determinism in packet generation
DEFAULT_BULK_SOURCE_BURST_SIZE = 31

# weight limits
WEIGHT_MAX = 1024
DELTA_WEIGHT_MAX = 8

# size of queues between tasks
# conservative setting: small delay, lower speed
#DEFAULT_QUEUE_SIZE = 1 * BATCH_SIZE
# optimistic setting: double the delay but somewhat larger speed
DEFAULT_QUEUE_SIZE = 2 * BATCH_SIZE

# default rate limit for tasks/flows
DEFAULT_RATE_LIMIT_RESOURCE = 'packet'
DEFAULT_RATE_LIMIT = int(1e9)

# latency statistic percentile to control
DELAY_MAX_PERC = '95'
DEFAULT_DELAY_BOUND = int(1e11)    # infinite delay

# module statistic querying method
# supported types are: 'full', 'partial'
MODULE_GET_STAT_METHOD = 'full'

# default task controller: RTC
DEFAULT_TASK_TYPE = 'RTC'

# resource shared by the scheduler between tasks
SCHEDULER_DOMAIN = 'count'

# resource shared by the scheduler between WFQ tasks
WFQ_SCHEDULER_DOMAIN = 'cycle'

# share of QoS tasks at worker's top-level 'weighted-fair'
DEFAULT_TC_QOS_SHARE = 1

# toggle task-level backpressure
ENABLE_BACKPRESSURE = True

# batchiness bound for modules: module is controllable if batchiness is
# smaller than the cound
CONTROLLABLE_BOUND = 0.5

# default pull of fractional buffers: min_q + X
DEFAULT_BUFFER_PULL = 4

# push a module back to q_v=0 if it already receives large batches
DEFAULT_PUSH_RATIO = 0.7

# default T0, T1 values are used when profiling data can not be read
DEFAULT_T0 = 0
DEFAULT_T1 = 0

# set controller aggressiveness: larger settings will make the controller
# overshoot the delay bound, allows to account for inaccurate gradient
# estimates
EXTRA_TRIGGER = 0
EXTRA_WEIGHT = 0
WEIGHT_GRADIENT = 1

# consider flow CBR if it reached its limit
CBR_RATIO = 1.0 + DEFAULT_TOLERANCE/2.0

# flow considered seriously overdelayed if violation is at least this ratio
# of the delay bound
OVERDELAY_BOUND = 1.0 + DEFAULT_TOLERANCE

# a relative SLO violation larger than the below will result in a resource
# reallocation step
CRITICAL_SLO_VIOLATION_RATIO = 1.5

# how much time to wait for warmup
DEFAULT_WARMUP_PERIOD = 2

# how much time to wait before applying control
DEFAULT_CONTROL_PERIOD = 0.5

# after how many task control rounds to call the batchy controller
DEFAULT_TASK_CONTROL_ROUNDS = 10

# number of gradient projection iterations
MAX_PROJGRAD_ITERATIONS = 3

# number of extra workers that can be used by batchy controllers to decompose pipelines
DECOMP_EXTRA_WORKERS = 2

# task controller type of new tasks created during decomposition by batchy controller
DECOMP_EXTRA_TASK_CONTROLLER = 'projgradient'

BYPASS_RATIO = 2.5

# flow measure parameters
DEFAULT_MEASURE_LATENCY_NS_MAX = 250_000_000
DEFAULT_MEASURE_LATENCY_NS_RESOLUTION = 50

# timestamp offsets
FLOW_TIMESTAMP_OFFSET = 18 + 20 + 8 + 0     # eth/ip/udp-or-tcp/0
BULK_TIMESTAMP_OFFSET = 18 + 20 + 8 + 16    # eth/ip/udp-or-tcp/16