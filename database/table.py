
class Table:
    def __init__(self, *fields):
        self.data = {}
        self.cursor = 0
        self.fields = fields

    def insert(self, **params):
        # Requirements:
        #   - Add a record entry to the self.data dictionary

        #   - BUT ::::
        #   - Validate that params is a (1) dictionary (2) non-empty (3) Keys are in self.fields list
        #   - Ensure to generate a record id for the new record using the cursor attribute. Note: ids must always start from 1
        #   - Ensure to use generated id as key for insert and also inject into the actual record to be inserted with the key => _id
        #   - Manually or allow python to raise appropriate exceptions when there are errors
        #   - Return a dictionary representing the record that has just been successfully inserted

        # Remove the pass statement below and add your implementation there ...
        if not isinstance(params, dict):
            raise TypeError("This is not a dictionary")
        if len(params) == 0:
            raise ValueError("Length cannot be 0")
        for keys in params:
            if keys not in self.fields:
                raise ValueError("keys must be included in field dictionary")
        self.cursor += 1
        id_incre = self.cursor
        params['_id'] = id_incre
        self.data[id_incre] = params
        return self.data[id_incre]     

    def select(self, **conditions):
        # Requirements:
        #   - Filter and return records that has values matching those in the conditions argument
        #   - BUT ::::
        #   - Validate that conditions is a (1) dictionary (2) non-empty (3) Keys are in self.fields list
        #   - Manually or allow python to raise appropriate exceptions when there are errors
        #   - Return a list of dictionaries representing records that matched entires in the conditions argument

        # Remove the pass statement below and add your implementation there ...
        if not isinstance(conditions, dict):
            raise TypeError("This is not a dictionary")
        if len(conditions) == 0:
            raise ValueError("Length cannot be 0")
        for keys in conditions:
            if keys not in self.fields:
                raise ValueError("keys must be included in field dictionary")
        arr_list = []
        for words in self.data.values():
            for key, value in conditions.items():
                if words[key] == value:
                    arr_list.append(words)
        return arr_list
