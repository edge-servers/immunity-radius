#!/usr/bin/env python
import os
import sys

from setuptools import find_packages, setup

from immunity_radius import get_version

if sys.argv[-1] == 'publish':
    # delete any *.pyc, *.pyo and __pycache__
    os.system('find . | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs rm -rf')
    os.system('python setup.py sdist bdist_wheel')
    os.system('twine upload -s dist/*')
    os.system('rm -rf dist build')
    args = {'version': get_version()}
    print('You probably want to also tag the version now:')
    print("  git tag -a %(version)s -m 'version %(version)s'" % args)
    print('  git push --tags')
    sys.exit()


setup(
    name='immunity-radius',
    version=get_version(),
    license='GPL3',
    author='Immunity',
    author_email='support@immunity.io',
    description='Immunity Radius',
    long_description=open('README.rst').read(),
    url='https://immunity.org',
    download_url='https://github.com/edge-servers/immunity-radius/releases',
    platforms=['Platform Independent'],
    keywords=['django', 'freeradius', 'networking', 'immunity'],
    packages=find_packages(exclude=['tests*', 'docs*']),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        (
            'immunity-users '
            '@ https://github.com/edge-servers/immunity-users/tarball/master'
        ),
        (
            'immunity-utils[rest,celery] @ '
            'https://github.com/edge-servers/immunity-utils/tarball/master'
        ),
        'passlib~=1.7.1',
        'djangorestframework-link-header-pagination~=0.1.1',
        'weasyprint~=59.0',
        'dj-rest-auth~=4.0.1',
        'django-sendsms~=0.5.0',
        'jsonfield~=3.1.0',
        'django-private-storage~=3.1.0',
        'django-ipware~=5.0.0',
        'pyrad~=2.4',
    ],
    extras_require={
        'saml': ['djangosaml2~=1.9.2'],
        'openvpn_status': ['openvpn-status~=0.2.1'],
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: System :: Networking',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
        'Framework :: Django',
        'Programming Language :: Python :: 3',
    ],
)
