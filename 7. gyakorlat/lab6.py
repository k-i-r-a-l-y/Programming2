
class City:

    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def __str__(self):
        return self.__name

class Time:

    def __init__(self, hour, min):
        self.__hour = hour
        self.__min = min

    def get_hour(self):
        return self.__hour

    def get_min(self):
        return self.__min

    def __str__(self):
        return self.__hour + ":" + self.__min

class Station(City, Time):

    def __init__(self, name, hour, min):
        City.__init__(self, name)
        Time.__init__(self, hour, min)

    def __str__(self):
        return Time.__str__(self) + "; " + City.__str__(self)

    def __lt__(self, other):
        if isinstance(other, Station):
            if self.get_hour() == other.get_hour():
                if self.get_min() == other.get_min():
                    return self.get_name() < other.get_name()
                else:
                    return self.get_min() < other.get_min()
            else:
                return self.get_hour() < other.get_hour()
        else:
            return "A ket objektum nem ooszehasonlithato!"

    def __gt__(self, other):
        if isinstance(other, Station):
            if self.get_hour() == other.get_hour():
                if self.get_min() == other.get_min():
                    return self.get_name() > other.get_name()
                else:
                    return self.get_min() > other.get_min()
            else:
                return self.get_hour() > other.get_hour()
        else:
            return "A ket objektum nem ooszehasonlithato!"

    def __le__(self, other):
        if isinstance(other, Station):
            if self.get_hour() == other.get_hour():
                if self.get_min() == other.get_min():
                    return self.get_name() <= other.get_name()
                else:
                    return self.get_min() <= other.get_min()
            else:
                return self.get_hour() <= other.get_hour()
        else:
            return "A ket objektum nem ooszehasonlithato!"

    def __ge__(self, other):
        if isinstance(other, Station):
            if self.get_hour() == other.get_hour():
                if self.get_min() == other.get_min():
                    return self.get_name() >= other.get_name()
                else:
                    return self.get_min() >= other.get_min()
            else:
                return self.get_hour() >= other.get_hour()
        else:
            return "A ket objektum nem ooszehasonlithato!"

class IC:

    def __init__(self, id, name, arrival, dest):
        self.__id = id
        self.__dest = dest
        self.__arrival = arrival
        self.__name = name
        self.__stops = self.input_stops("stops" + str(self.__id) + ".txt")

    def set_dest(self, dest):
        self.__dest = dest

    def set_arrival(self, arrival):
        self.__arrival = arrival

    def get_dest(self):
        return self.__dest

    def get_arrival(self):
        return  self.__arrival

    def get_name(self):
        return self.__name

    def get_id(self):
        return self.__id

    def get_stops(self):
        return self.__stops

    def input_stops(self, file_name):
        stops = []
        try:
            file = open(file_name, "r")
            for line in file:
                str = line.split(";")
                name = str[2]
                times = str[3].split(".")
                hour = times[0]
                min = times[1].rstrip()
                station = Station(name, hour, min)
                stops.append(station)
        except FileNotFoundError:
            return stops

        return stops

    def __str__(self):
        stops_str = ""
        self.__stops.sort()
        if len(self.__stops) != 0:
            for stops in self.__stops:
                stops_str += stops.__str__() + "\n"
        else:
            stops_str += "Ismeretlen informacio"
        return "{} ({}) from: {} to: {}\n".format(self.__name, self.__id, self.__arrival, self.__dest) \
        + stops_str


f = open("IC.txt","r")
f_out = open("output.txt","w")
ic_list = []
for line in f:
    string = line.split(";")
    ic1 = IC(string[0],string[1],string[2],string[3])
    ic_list.append(ic1)
    print(ic1,file=f_out)

f_out.close()
f.close()

menetrend = dict([])

for ic in ic_list:
    for i in ic.get_stops():
        if isinstance(i, Station):
            if i.get_name() not in menetrend:
                #menetrend[i.get_name()] = []
                menetrend[i.get_name()] = [str(i.get_hour()) + ":" + str(i.get_min()) + " - " + ic.get_name() + "(" + ic.get_id() + ")"]
            else:
                menetrend[i.get_name()].append(str(i.get_hour()) + ":" + str(i.get_min()) + " - " + ic.get_name() + "(" + ic.get_id() + ")")
                menetrend[i.get_name()].sort()

f_out = open("output2.txt","w")
for k in menetrend:
    print("{}:".format(k),file=f_out)
    for times in menetrend[k]:
        print(times,file=f_out)
f_out.close()

