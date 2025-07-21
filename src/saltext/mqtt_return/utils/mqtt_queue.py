import concurrent.futures


class PersistentExecutor:
    def __init__(self, max_workers=4):
        self.executor = concurrent.futures.ThreadPoolExecutor(max_workers=max_workers)

    def submit_job(self, func, *args, **kwargs):
        """Submit a job and return the future"""
        future = self.executor.submit(func, *args, **kwargs)
        return future

    def shutdown(self, wait=True):
        """Shutdown the executor"""
        self.executor.shutdown(wait=wait)
