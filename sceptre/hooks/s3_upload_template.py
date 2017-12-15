from __future__ import print_function

from sceptre.hooks import Hook
import posixpath
import os.path

class S3UploadTemplate(Hook):
    """ Uploads file (argument) to the configured S3 bucket.
        Requires template_bucket_name to be set.
    """
    def run(self):
        path = self.argument
        template = Template(
            path = path,
            sceptre_user_data=self.stack.sceptre_user_data,
            s3_details=self.stack.s3_details,
            connection_manager=self.stack.connection_manager
        )

        template.upload_to_s3()

