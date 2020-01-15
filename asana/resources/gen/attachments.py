# coding=utf-8
class _Attachments:

    def __init__(self, client=None):
        self.client = client

    def create_attachment_for_task(self, task_gid, params={}, **options):
        """Upload an attachment
        :param str task_gid: (required) The task to operate on.
        :param Object params: Parameters for the request
        :return: Object
        """
        path = "/tasks/{task_gid}/attachments".replace("{task_gid}", task_gid)
        return self.client.post(path, params, **options)


    def delete_attachment(self, attachment_gid, params={}, **options):
        """Delete an attachment
        :param str attachment_gid: (required) Globally unique identifier for the attachment.
        :param Object params: Parameters for the request
        :return: Object
        """
        path = "/attachments/{attachment_gid}".replace("{attachment_gid}", attachment_gid)
        return self.client.delete(path, params, **options)


    def get_attachment(self, attachment_gid, params={}, **options):
        """Get an attachment
        :param str attachment_gid: (required) Globally unique identifier for the attachment.
        :param Object params: Parameters for the request
            - opt_fields {list[str]}:  Defines fields to return. Some requests return *compact* representations of objects in order to conserve resources and complete the request more efficiently. Other times requests return more information than you may need. This option allows you to list the exact set of fields that the API should be sure to return for the objects. The field names should be provided as paths, described below. The id of included objects will always be returned, regardless of the field options.
            - opt_pretty {bool}:  Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.
        :return: Object
        """
        path = "/attachments/{attachment_gid}".replace("{attachment_gid}", attachment_gid)
        return self.client.get(path, params, **options)


    def get_attachments_for_task(self, task_gid, params={}, **options):
        """Get attachments for a task
        :param str task_gid: (required) The task to operate on.
        :param Object params: Parameters for the request
            - offset {str}:  Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. 'Note: You can only pass in an offset that was returned to you via a previously paginated request.'
            - limit {int}:  Results per page. The number of objects to return per page. The value must be between 1 and 100.
            - opt_fields {list[str]}:  Defines fields to return. Some requests return *compact* representations of objects in order to conserve resources and complete the request more efficiently. Other times requests return more information than you may need. This option allows you to list the exact set of fields that the API should be sure to return for the objects. The field names should be provided as paths, described below. The id of included objects will always be returned, regardless of the field options.
            - opt_pretty {bool}:  Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.
        :return: Object
        """
        path = "/tasks/{task_gid}/attachments".replace("{task_gid}", task_gid)
        return self.client.get_collection(path, params, **options)

