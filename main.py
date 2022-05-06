from stack import get_pages, get_jobs
from save import save_csv

last_page = get_pages()

jobs = get_jobs(last_page)

save_csv(jobs)