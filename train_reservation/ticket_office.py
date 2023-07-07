import cherrypy
import urllib.request
import json


url = "http://127.0.0.1:8083"

class TicketOffice(object):

    def reserve(self):
        form_data = {"train_id": "express_2000", "seat_count": 4}
        data = urllib.parse.urlencode(form_data)
        req = urllib.request.Request(url + "/reserve", bytes(data, encoding="ISO-8859-1"))
        response = urllib.request.urlopen(req).read().decode("ISO-8859-1")
        reservation = json.loads(response)
        print(reservation)
        assert "express_2000" == reservation["train_id"]


if __name__ == "__main__":
    """Deploy this class as a web service using CherryPy"""
    TicketOffice.reserve.exposed = True
    cherrypy.config.update({"server.socket_port": 8083})
    cherrypy.quickstart(TicketOffice())
    TicketOffice().reserve()

