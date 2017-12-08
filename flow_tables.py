class FlowTables:
    def __init__(self, name, table_no, fl_md_tp):
        self.name = name
        self.table_no = table_no
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

