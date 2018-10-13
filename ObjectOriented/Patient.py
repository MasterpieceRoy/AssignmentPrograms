class Patient:
    def set_first_name(self, first_name):
        self._firstname = first_name

    def set_last_name(self, last_name):
        self._lastname = last_name

    def set_id(self, id):
        self._id = id

    def set_mob_number(self, mob_number):
        self._mobnumber = mob_number

    def get_first_name(self):
        return self._firstname

    def get_last_name(self):
        return self._lastname

    def get_id(self):
        return self._id

    def get_mob_number(self):
        return self._mobnumber
