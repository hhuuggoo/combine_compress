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


def combine_confobjs(confobjs):
    for confobj in confobjs:
        cat(confobj['output'], confobj['inputs'])
        
def combine_compress(confobjs):
    for confobj in confobjs:
        cat(confobj['output'], confobj['inputs'])
        minfile(confobj['output'], confobj['output'], confobj['compressor'])
    
if __name__ == "__main__":
    conffile = sys.argv[1]
    confobj = simplejson.load(conffile)
    
    
