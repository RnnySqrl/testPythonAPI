import tornado.web
import json

class Search_by_id(tornado.web.RequestHandler):

    def initialize(self, data):
        self.data = data

    def post(self):
        try:
            data = json.loads(self.request.body.decode('utf-8'))
            id = data.get("id", None)
            if id:
                value = [x for x in self.data if x['id'] == id][0]

                id_searched = str(value['id'])
                if value['name']:
                    name_searched = str(value['name'])
                else:
                    name_searched = None

                if value["brand"]:
                    brand_searched = str(value["brand"])
                else:
                    brand_searched = None
                if value["price"]:
                    price_searched = float(value["price"])
                else:
                    price_searched = None
                if value["in_stock"] == ("yes" or "y"):
                    in_stock_searched = True
                elif value["in_stock"] == ("no" or "n"):
                    in_stock_searched = False
                else:
                    in_stock_searched = None
                data_dict = {
                    "id":id_searched,
                    "name":name_searched,
                    "brand":brand_searched,
                    "price":price_searched,
                    "in_stock":in_stock_searched,
                }
                self.write({'code': 200, 'data': data_dict})
            else:
                self.write({'code':404, 'data':None})
        except Exception as e:
            print(e)
            self.write({'code': 400})
