from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from scrapping_spider import CarPricesSpider
import subprocess

def init_airflow_db():
    # Initialize Airflow database
    subprocess.run(["airflow", "db", "init"], check=True)

def start_airflow_webserver():
    # Start Airflow webserver on port 8080
    subprocess.run(["airflow", "webserver", "--port", "8080"], check=True)




if __name__ == "__main__":
    process = CarPricesSpider(get_project_settings())
    process.crawl(CarPricesSpider)  # Pass your Spider class
    process.start()

subprocess.run(["python", "scrapping_selenium.py"])
subprocess.run(["python", "scrapping_selenium.py"])
subprocess.run(["python", "airflowScheduling.py"])

if __name__ == "__main__":
    init_airflow_db()
    start_airflow_webserver()

