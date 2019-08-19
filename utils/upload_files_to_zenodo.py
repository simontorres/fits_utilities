import requests
import json
import os
import urllib.parse
import glob
import logging

from astropy.io import fits

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

ACCESS_TOKEN = ''

SANDBOX_ZENODO_TOKEN = ''

zenodo_api_url = 'https://zenodo.org/api/'
sandobox_api_url = 'https://sandbox.zenodo.org/api/'


def upload_to_zenodo(path, file, meta, api_url, access_token):
    headers = {"Content-Type": "application/json"}
    params = {'access_token': access_token}
    r = requests.get(urllib.parse.urljoin(api_url, 'deposit/depositions'),
                     params=params)
    if r.status_code == 200:
        try:
            existing_files = [_item['files'][0]['filename'] for _item in r.json()]
            if file in existing_files:
                logger.error("File Exists")
        except KeyError:
            logger.error("No files uploaded yet.")

        rc = requests.post(
            urllib.parse.urljoin(api_url, 'deposit/depositions'),
            params=params,
            json={},
            headers=headers)
        if rc.status_code == 201:
            dep_id = rc.json()['id']
            data = {'filename': file}
            files = {'file': open(os.path.join(path, file), 'rb')}

            ru = requests.post(
                urllib.parse.urljoin(
                    api_url, 'deposit/depositions/{}/files'.format(dep_id)),
                params=params,
                data=data,
                files=files)
            logger.debug("Upload file status code: {}".format(ru.status_code))

            rmeta = requests.put(
                urllib.parse.urljoin(api_url,
                                     'deposit/depositions/{}'.format(dep_id)),
                params=params,
                data=json.dumps(meta),
                headers=headers)

            if rmeta.status_code == 200:
                r = requests.post(
                    urllib.parse.urljoin(
                        api_url,
                        'deposit/depositions/{}/actions/publish'.format(dep_id)),
                    params=params)

                if r.status_code == 202:
                    result = {'filename': file, 'id': r.json()['id']}
                    logger.info("Success: {}".format(result))
                    return result
                else:
                    logger.error("Publish failed, status code: {}"
                                 "".format(r.status_code))
            # print(ru.json())

        else:
            print("Returned status code: {}".format(rc.status_code))
            print(rc.json()['message'])





    else:
        print("API returned status code: {}".format(r.status_code))


def zenodo(path, sandbox=True):
    if sandbox:
        api_url = sandobox_api_url
        access_token = SANDBOX_ZENODO_TOKEN
    else:
        api_url = zenodo_api_url
        access_token = ACCESS_TOKEN

    all_results = []

    for _file in glob.glob(os.path.join(path, '*.fits')):
        print(_file)

        header = fits.getheader(_file)
        header_info = "Using the mode {} " \
                      "and slit {} " \
                      "exposed {} seconds".format(header['WAVMODE'],
                                                  header['SLIT'],
                                                  header['EXPTIME'])

        metadata = {
            'metadata': {
                'title': os.path.basename(_file),
                'upload_type': 'dataset',
                'description': 'Reference lamp library for the '
                               'Goodman Pipeline {}'.format(header_info),
                'creators': [{'name': 'Torres, Simon',
                              'affiliation': 'SOAR Telescope',
                              'orcid': '0000-0002-2726-6971'}],
                'keywords': ['spectroscopy', 'template', 'soar', 'telescope']
            }
        }
        result = upload_to_zenodo(path=path,
                                  file=os.path.basename(_file),
                                  meta=metadata,
                                  api_url=api_url,
                                  access_token=access_token)

        all_results.append(result)
    for _line in all_results:
        print(_line)


if __name__ == '__main__':
    zenodo(path='/user/simon/development/soar/goodman_pipeline/'
                'goodman_pipeline/data/ref_comp', sandbox=False)