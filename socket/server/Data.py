class Data(object):
    def __init__(self,method,information,information_bullet):
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
                self.information["health"]=information.health
                self.information_bullet={}
                self.information_bullet["x"] = information_bullet.x
                self.information_bullet["y"] = information_bullet.y
                self.information_bullet["width"] = information_bullet.width
                self.information_bullet["height"] = information_bullet.height
                self.information_bullet["vel"] = information_bullet.vel
                self.information_bullet["angle"] = information_bullet.angle
                self.information_bullet["show"]=information_bullet.show
            except Exception as e:
                print(e)
        else:
            self.information = information    
            self.information_bullet=information_bullet
