from cmind import utils
import os
import shutil

def preprocess(i):

    os_info = i['os_info']

    if os_info['platform'] == 'windows':
        return {'return':1, 'error': 'Windows is not supported in this script yet'}
    env = i['env']
    env['CM_TMP_CURRENT_SCRIPT_PATH'] = os.getcwd()

    return {'return':0}

def postprocess(i):

    env = i['env']
    state = i['state']

    env['CM_MLC_INFERENCE_SOURCE'] = os.path.join(os.getcwd(), 'inference')
    env['CM_MLC_INFERENCE_VISION_PATH'] = os.path.join(os.getcwd(), 'inference', 'vision', 'classification_and_detection')
    valid_models = get_valid_models(env['CM_MLC_LAST_RELEASE'], env['CM_MLC_INFERENCE_SOURCE'])
    state['CM_MLPERF_INFERENCE_MODELS'] = valid_models

    return {'return':0}

def get_valid_models(mlc_version, mlc_path):
    import sys
    submission_checker_dir = os.path.join(mlc_path, "tools", "submission")
    sys.path.append(submission_checker_dir)
    if not os.path.exists(os.path.join(submission_checker_dir, "submission_checker.py")):
        shutil.copy(os.path.join(submission_checker_dir,"submission-checker.py"), os.path.join(submission_checker_dir,
        "submission_checker.py"))
    import submission_checker as checker
    config = checker.MODEL_CONFIG
    valid_models = config[mlc_version]["models"]
    return valid_models