import time

from selenium import webdriver
from utils.encoding import decode_base64
from utils.registers import execute_program


def scrape_longshot():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    options.set_capability("goog:loggingPrefs", {"browser": "INFO"})

    driver = webdriver.Chrome(options=options)

    driver.get("https://challenge.longshotsystems.co.uk/go")

    numbers = "".join(driver.execute_script("""
                let numbers = [];
                document.querySelectorAll('.number-box').forEach(element => {
                    numbers.push(element.textContent.trim());
                });
                return numbers;
            """))

    driver.execute_script(f"document.getElementById('answer').value = '{numbers}';")
    driver.execute_script(f"document.getElementById('name').value = 'Joween Flores';")
    driver.execute_script(f"submit()")

    driver.execute_script(f"window.location.href = 'https://challenge.longshotsystems.co.uk/ok'")

    time.sleep(1.5)

    logs = driver.get_log("browser")

    results = []
    for idx, log in enumerate(logs):
        if idx in (0, 1):  # skip first two elements
            pass
        else:
            results.append(decode_base64(log["message"]))

    encoded_answer = execute_program(results)

    ws_script = """
        ws.send("%s");
        
        ws.onmessage = function(event) {
            console.log(event.data);
        };
    """ % encoded_answer

    driver.execute_script(ws_script)

    time.sleep(1)

    last_log = driver.get_log("browser")

    driver.quit()

    return decode_base64(last_log[0]["message"])
