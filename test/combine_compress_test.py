import unittest
import simplejson
import tempfile
import combine_compress

class CombineCompressTestCase(unittest.TestCase):
    def test_file_combine(self):
        files = []
        for c in range(10):
            files.append(tempfile.NamedTemporaryFile('w+'))
            files[-1].write(str(c))
            files[-1].flush()
        output_file = tempfile.NamedTemporaryFile('w+')
        combine_compress.cat(output_file.name,
                                 [x.name for x in files])
        output_file.seek(0)
        data = output_file.read()
        assert data == ''.join([str(c) for c in range(10)])

    def test_file_min(self):
        test_data = \
        """
        function(x){
        return x;
        }
        """
        testjs = tempfile.NamedTemporaryFile('w+')
        testjs.write(test_data)
        testjs.flush()
        outfile = tempfile.NamedTemporaryFile('w+')
        combine_compress.minfile(
            outfile.name, testjs.name,
            'java -jar test/support/yuicompressor-2.4.7.jar --type=js')
        outfile.seek(0)
        output_data = outfile.read()
        assert len(output_data) > 0
        
                            
    
