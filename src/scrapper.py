import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from urllib.request import urlretrieve


def scrape_for_imgs(url, end, increment, img_counter, keyowrd):
    """Scrapes a website for images"""
    # Set up the webdriver to use Google Chrome
    driver = webdriver.Chrome()

    for start in range(0, end, increment):

        # Navigate to the website
        driver.get(f"{url}?{keyowrd}={start}")

        # Find all the image elements on the page using the "img" tag
        for image in driver.find_elements(By.TAG_NAME, "img"):
            try:
                src = image.get_attribute("src")
                if ".jpg" not in src:
                    continue
                if src.startswith("http"):
                    # download the image using requests
                    # ...
                    img_counter += 1
                    filename = f"image_{img_counter}.jpg"
                    filepath = os.path.join(
                        "../images/selenium_imgs", filename)
                    urlretrieve(src, filepath)
                    # print(f"Downloaded image {img_counter+1}: {src}")
            except Exception as e:
                # handle the exception (e.g. print an error message)
                # ...
                print(e)

    # Close the webdriver
    driver.quit()
    return img_counter


def scrape_single_page(url, img_counter):
    """Scrapes a single page for images"""
    # Set up the webdriver to use Google Chrome
    driver = webdriver.Chrome()

    # Navigate to the website
    driver.get(url)

    # Find all the image elements on the page using the "img" tag
    for image in driver.find_elements(By.TAG_NAME, "img"):
        try:
            src = image.get_attribute("src")
            if ".jpg" not in src:
                continue
            if src.startswith("http"):
                # download the image using requests
                # ...
                img_counter += 1
                filename = f"image_{img_counter}.jpg"
                filepath = os.path.join(
                    "../images/selenium_imgs", filename)
                urlretrieve(src, filepath)
                # print(f"Downloaded image {img_counter+1}: {src}")
        except Exception as e:
            # handle the exception (e.g. print an error message)
            # ...
            print(e)

    # Close the webdriver
    driver.quit()
    return img_counter


def main():
    count = scrape_for_imgs(
        "https://www.lowes.com/pl/Hardwood-flooring-Hardwood-Flooring/4294856493", 512, 24, 0, "offset")
    print(f"Downloaded {count} images")
    count = scrape_for_imgs(
        "https://www.floorsourceaz.com/all-hardwood-flooring", 120, 15, count, "start")
    print(f"Downloaded {count} images")
    count = scrape_for_imgs(
        "https://www.totalflooringinc.com/all-hardwood-flooring", 60, 15, count, "start")
    print(f"Downloaded {count} images")


if __name__ == "__main__":
    main()
