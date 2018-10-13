class Doctor:
    def set_first_name(self, first_name):
        self._first_name = first_name

    def set_last_name(self, last_name):
        self._last_name = last_name

    def set_id(self,id):
        self._id = id

    def set_specialization(self, specialization):
        self._specialization = specialization

    def set_availability(self, avail):
        self._availability = avail

    def get_first_name(self):
        return self._first_name

    def get_last_name(self):
        return self._last_name

    def get_id(self):
        return self._id

    def get_specialization(self):
        return self._specialization

    def get_availability(self):
        return self._availability
