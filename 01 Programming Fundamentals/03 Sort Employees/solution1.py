def sort_employees(employees, sort_by):
    def get_key(item):
        if sort_by == 'name':
            return item[0]
        elif sort_by == 'age':
            return item[1]
        elif sort_by == 'salary':
            return item[2]
        
    return sorted(employees,key=get_key)