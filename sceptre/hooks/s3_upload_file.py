from __future__ import print_function

from sceptre.hooks import Hook
import os.path

class S3UploadFile(Hook):
    """ Uploads file (argument) to the configured S3 bucket.
        Requires template_bucket_name to be set.
    """
    def run(self):
        path = self.argument
        bucket_name = self.stack.s3_details["bucket_name"]
        bucket_prefix = self.stack.s3_details["bucket_prefix"]
        key = "/".join([ bucket_prefix, os.path.basename(path) ])
        
        fd = open(path, 'r+b')
        self.stack.connection_manager.call(
            service='s3',
            command='put_object',
            kwargs={
                'Bucket': bucket,
                'ServerSideEncryption': 'AES256',
                'Key': key,
                'Body': fd
            }
        )

        
