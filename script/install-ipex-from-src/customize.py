from cmind import utils
import os

def preprocess(i):

    os_info = i['os_info']

    if os_info['platform'] == 'windows':
        return {'return':1, 'error': 'Windows is not supported in this script yet'}

    env = i['env']

    env['IPEX_DIR'] = env['CM_IPEX_SRC_REPO_PATH']

    if env.get('CM_USE_LLVM_FOR_IPEX', '') == 'yes':
        env['DNNL_GRAPH_BUILD_COMPILER_BACKEND'] = 1
        env['USE_LLVM'] = env['CM_LLVM_INSTALLED_PATH']
        env['LLVM_DIR'] = os.path.join(env['CM_LLVM_INSTALLED_PATH'], "lib", "cmake", "llvm")

    run_cmd="python setup.py clean && python setup.py install"

    env['CM_RUN_DIR'] = env['IPEX_DIR']
    env['CM_RUN_CMD'] = run_cmd

    return {'return':0}

def postprocess(i):

    env = i['env']

    return {'return':0}
