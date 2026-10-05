class UndergroundSystem:
    def __init__(self):
        self.customers = {}  # id -> [start_time, start_station]
        self.stations = {}   # end_station -> {start_station: [trip_times]}
    
    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.customers[id] = [t, stationName]
    
    def checkOut(self, id: int, end_station: str, t: int) -> None:
        start_time, start_station = self.customers[id]
        del self.customers[id]  # clean up after checkout

        if end_station not in self.stations:
            self.stations[end_station] = {}
        if start_station not in self.stations[end_station]:
            self.stations[end_station][start_station] = []
        
        self.stations[end_station][start_station].append(t - start_time)
    
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        times = self.stations[endStation][startStation]
        return sum(times) / len(times)
