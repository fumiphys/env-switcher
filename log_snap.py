'''save logs
'''

import config
import os
import json
import datetime
import codecs


def save_snapshot():
    '''save snapshot for context
    '''
    LOG_DIR = config.get_log_dir()
    if not os.path.exists(LOG_DIR):
        os.mkdir(LOG_DIR)
    if not os.path.exists("{}/snapshot".format(LOG_DIR)):
        os.mkdir("{}/snapshot".format(LOG_DIR))

    now = datetime.datetime.now()
    log_file = "{}/snapshot/{}{}{}_{}{}{}.json".format(
        LOG_DIR,
        now.year,
        now.month,
        now.day,
        now.hour,
        now.minute,
        now.second
    )

    with codecs.open(log_file, 'w', 'utf-8') as writer:
        json.dump(dict(os.environ), writer)


if __name__ == '__main__':
    save_snapshot()
