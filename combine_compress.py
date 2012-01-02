import subprocess
import simplejson
import sys
import shutil


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


def combine_compress(confobj):
    js_compressor_cmd = confobj['compressor_js']
    css_compressor_cmd = confobj['compressor_css']
    css_outputs = confobj.get('css', {})
    js_outputs = confobj.get('js', {})
    
    
if __name__ == "__main__":
    conffile = sys.argv[1]
    confobj = simplejson.load(conffile)
    
    
