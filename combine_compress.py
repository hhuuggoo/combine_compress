import subprocess
import simplejson
import sys
import shutil
import os
import os.path
import re


def minfile(out_name, in_name, mincommand):
    subproc = subprocess.Popen("%s %s" % (mincommand, in_name),
                               shell=True,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)
    retval = subproc.stdout.read()
    with open(out_name, 'w+') as outfile:
        outfile.write(retval)
    
                               
    
def cat(output, inputs):
    with open(output, 'wb+') as outfile:
        for fname in inputs:
            with open(fname, 'rb') as infile:
                shutil.copyfileobj(infile, outfile)

def replace_html_file(key, replacement, html):
    start_key = "<!-- start %s -->" % key
    end_key = "<!-- end %s -->" % key
    regexstring = "%s(\s*)([\w\W]*?)%s" % (start_key, end_key)
    regobj = re.compile(regexstring)
    replacement = "%s\g<1>%s\g<1>%s" % (start_key, replacement, end_key)
    replacement = regobj.sub(replacement, html)
    return replacement

def replace_html_dir(key, newfile, path, css_or_js):
    if css_or_js == 'css':
        replacement = '<link rel="stylesheet" href="%s" type="text/css" >'
    else:
        replacement = '<script src="%s" type="text/javascript"></script>'
    replacement = replacement % newfile
    for dirpath, dirname, filenames in os.walk(path):
        for fname in filenames:
            fname = os.path.join(dirpath, fname)
            with open(fname) as f:
                html = f.read()
                html = replace_html_file(key, replacement, html)
            with open(fname, "w") as f:
                f.write(html)
        

def combine_confobjs(confobjs):
    for confobj in confobjs:
        cat(confobj['output'], confobj['inputs'])
        
def combine_compress_confobjs(confobjs):
    for confobj in confobjs:
        cat(confobj['output'], confobj['inputs'])
        minfile(confobj['output'], confobj['output'], confobj['compressor'])

def html_replace_confobjs(confobjs):
    for confobj in confobjs:
        for htmldir in confobj['html_dirs']:
            replace_html_dir(confobj['name'], confobj['output_link'],
                             htmldir, confobj['type'])
    
if __name__ == "__main__":
    conffile = sys.argv[1]
    with open(conffile) as f:
        data = f.read()
        print data
        confobjs = simplejson.loads(data)
    combine_compress_confobjs(confobjs)
    html_replace_confobjs (confobjs)
    
    
