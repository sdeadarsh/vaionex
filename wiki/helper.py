from rest_framework.response import Response


class ResponseProcess:

    def __init__(self,data,message,count=None):
        self.data=data
        self.message=message
        self.count = count

    def successfull_response(self):
        if self.count==None:
            return Response({"message":self.message,"data":self.data,"error":False})
        return Response({"message":self.message,"data":self.data,"error":False,'total_count':self.count})

    def errord_response(self):
        if self.count==None:
            return Response({"message": self.message, "data": self.data, "error": True})
        return Response({"message": self.message, "data": self.data, "error": True,'total_count':self.count})

class Data:
    def dummy_data(self):
        document_data = [{"title_id": 1, "content": "dummy conntent one", 'timestamp': "2022-05-19 05:36:43"},
                         {"title_id": 2, "content": "dummy conntent two", 'timestamp': "2022-05-19 06:46:41"},
                         {"title_id": 2, "content": "dummy new conntent two", 'timestamp': "2022-05-19 09:16:23"},
                         ]
        title_data = [{"id": 1, "title": "title one"},
                      {"id": 2, "title": "title two"}]
        return document_data, title_data
