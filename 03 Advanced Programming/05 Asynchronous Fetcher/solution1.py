import asyncio

class BatchFetcher:
    # The `database` has an `async_fetch` method
    # that you should use in your code. This method
    # takes in a record id and returns a record.
    def __init__(self, database):
        self.database = database

    
    async def fetch_records(self, record_ids):
        new_list =[]
        for record_id in record_ids:
            new_list.append(self.database.async_fetch(record_id))
        
        return await asyncio.gather(*new_list)

        

    # Write your code here.
