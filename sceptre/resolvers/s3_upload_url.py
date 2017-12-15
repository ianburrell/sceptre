# -*- coding: utf-8 -*-

import os

from sceptre.resolvers import Resolver

class S3UploadUrl(Resolver):
    """
    Resolver for S3 upload URL for template and extra files.
    """

    def __init__(self, *args, **kwargs):
        super(S3UploadUrl, self).__init__(*args, **kwargs)

    def resolve(self):
        """
        :returns: S3 upload base URL
        :rtype: str
        """
        if self.stack.s3_details:
            bucket_name = self.stack.s3_details["bucket_name"]
            bucket_key = self.stack.s3_details["bucket_key"]
            url = "https://{0}.s3.amazonaws.com/{1}".format(
                bucket_name, bucket_key
            )
    
