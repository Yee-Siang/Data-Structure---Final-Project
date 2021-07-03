class Data(object):
    def __init__(self,method,information):
        self.method = method                  #string
        if self.method == "get_game":         #傳player的資訊給server
            try:
                self.information = {}         #dict
                self.information["x"] = information.x
                self.information["y"] = information.y
                self.information["width"] = information.width
                self.information["height"] = information.height
                self.information["vel"] = information.vel
                self.information["angle"] = information.angle
            except Exception as e:
                print(e)
        else:
            self.information = information    
