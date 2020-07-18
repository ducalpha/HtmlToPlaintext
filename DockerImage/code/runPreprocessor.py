"""Copy crawed privacy policies into a flattened directory and process by HtmlToText.
"""
from __future__ import print_function

from pathlib2 import Path
import os
import shutil

from dotenv import load_dotenv

from Preprocessor import processDirectory

load_dotenv()
processed_data_dir_str = os.getenv('PROCESSED_DATA_DIR')
assert processed_data_dir_str is not None
processed_data_dir = Path(processed_data_dir_str)
assert processed_data_dir.exists()

# root_dir = processed_data_dir / '2020-05-31'
# root_dir = processed_data_dir / '2020-06-02'

# root_dir = processed_data_dir / '2020-06-27'
# in_dir = root_dir / 'policy_crawl'
# flat_dir = root_dir / 'policy_crawl_flat'
# plain_dir = flat_dir.parent / 'policy_crawl_plain'
root_dir = processed_data_dir / '2020-07-18'
in_dir = root_dir / 'policy_crawl_new_apps_2020-07-18'
flat_dir = root_dir / 'policy_crawl_new_apps_2020-07-18_flat'
plain_dir = flat_dir.parent / 'policy_crawl_new_apps_2020-07-18_plain'

### Copy to a flat directory.
assert in_dir.exists()
flat_dir.mkdir(exist_ok=True)

for file_path in in_dir.glob('*/policy.full.html'):
    package_name = file_path.parent.name
    out_file = flat_dir / '{}.html'.format(package_name)
    if not out_file.exists():
        shutil.copy(str(file_path), str(out_file))
        # print('Copied {} -> {}'.format(file_path, out_file))
print('Copied all privacy policies from {} -> {}'.format(in_dir, flat_dir))


# Run Preprocessor, input:the flat dir and output: /ext dir.
plain_dir.mkdir(exist_ok=True)
processDirectory(str(flat_dir), str(plain_dir))
