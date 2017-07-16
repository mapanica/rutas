from fabric.api import *
import fabric.contrib.project as project
import os
import shutil
import sys
import SocketServer
import livereload

from pelican.server import ComplexHTTPRequestHandler

# Local path configuration (can be absolute or relative to fabfile)
env.deploy_path = 'output'
DEPLOY_PATH = env.deploy_path
theme_path = 'themes/mombacho'

# Port for `serve`
PORT = 8000

def clean():
    """Remove generated files"""
    if os.path.isdir(DEPLOY_PATH):
        # Don't remove folder because local web server get's affected
        local('rm -rf ' + DEPLOY_PATH + '/*')
        # shutil.rmtree(DEPLOY_PATH)
        # os.makedirs(DEPLOY_PATH)

def build():
    """Build local version of site"""
    local('make html')

def rebuild():
    """`clean` then `build`"""
    clean()
    build()

def regenerate():
    """Automatically regenerate site upon file modification"""
    local('pelican -r -s pelicanconf.py')
    local('cp -r extra/* '+ DEPLOY_PATH + '/')

def serve():
    """Serve site at http://localhost:8000/"""
    os.chdir(env.deploy_path)

    class AddressReuseTCPServer(SocketServer.TCPServer):
        allow_reuse_address = True

    server = AddressReuseTCPServer(('', PORT), ComplexHTTPRequestHandler)

    sys.stderr.write('Serving on port {0} ...\n'.format(PORT))
    server.serve_forever()

def reserve():
    """`build`, then `serve`"""
    build()
    serve()

@hosts(production)
def publish():
    """Publish to production via rsync"""
    local('lessc ' + theme_path + '/static/css/style.less -x > ' + theme_path + '/static/css/style.min.css')
    local('pelican -s publishconf.py')
    local('cp -r extra/* '+ DEPLOY_PATH + '/')
    project.rsync_project(
        remote_dir=dest_path,
        exclude=".DS_Store",
        local_dir=DEPLOY_PATH.rstrip('/') + '/',
        delete=True,
        extra_opts='-c',
    )


def make_entry(title):
    today = datetime.today()
    slug = title.lower().strip().replace(' ', '-')
    f_create = "content/{}_{:0>2}_{:0>2}_{}.rst".format(
        today.year, today.month, today.day, slug)
    t = TEMPLATE.strip().format(title=title,
                                hashes='#' * len(title),
                                year=today.year,
                                month=today.month,
                                day=today.day,
                                hour=today.hour,
                                minute=today.minute,
                                slug=slug)
    with open(f_create, 'w') as w:
        w.write(t)
    print("File created -> " + f_create)


def serve_livereload():
    local('make clean')
    local('make html')
    os.chdir('output')
    server = livereload.Server()
    server.watch('../content/*.rst',
        livereload.shell('pelican -s ../pelicanconf.py -o ../output'))
    server.watch('../naffy/',
        livereload.shell('pelican -s ../pelicanconf.py -o ../output'))
    server.watch('*.html')
    server.watch('*.css')
    server.serve(liveport=35729, port=PORT)
