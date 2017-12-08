class FlowTables:
    def __init__(self, name, table_no, fl_md_tp):
        self.name = name
        self.table_no = table_no
        """
            flow_mod_type
                - flow_mod_name
                - match_set
                - instruction 
        """
        self.fl_md_tp = fl_md_tp

    def get_next_tables(self):
        try:
            for item in self.fl_md_tp['instruction']:
                if item['instruction'] == 'GOTO_TABLE':
                    return  item['table']
                    #re.append( item['table'])
            return 
        except KeyError:
            return

    def print_structures_per_table(self):
        values = list(self.fl_md_tp.values())
        print('Flow mod name:', values[0])

        for field in values[1]:
            print('MATCH FIELD', field['field'],'MATCH TYPE',field['match_type'])

        for instruction in values[2]:
            print('TABLE', instruction)
