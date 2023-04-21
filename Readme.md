# ML3 Semester Project
#### Will Anderson & Samuel DeZube
# Floor Color Recognizer
### Setup & Installation
1. Run `pip install -r requirements.txt` to install the required packages.
2. Run `python3 make_csv.py` to create the data
    - This will take a little while, you should see progress in the terminal
    - Splits the data into training and testing sets
3. Run `python3 knn.py` to run the KNN algorithm
    - This will take a little while, you should see progress in the terminal
    - Outputs the accuracy of the algorithm


### Classifications

<div class="image-grid">
    <div>
        <img src="images/classes/alehouse.png" alt="Image 1">
        <div class="image-name">Alehouse</div>
    </div>
    <div>
        <img src="images/classes/alta_vista_hardwood.png" alt="Image 2">
        <div class="image-name">Alta Vista Hardwood</div>
    </div>
    <div>
        <img src="images/classes/british_isles.png" alt="Image 3">
        <div class="image-name">British Isles</div>
    </div>
    <div>
        <img src="images/classes/city_vouge.png" alt="Image 4">
        <div class="image-name">City Vouge</div>
    </div>
    <div>
        <img src="images/classes/designer_series.png" alt="Image 5">
        <div class="image-name">Designer Series</div>
    </div>
    <div>
        <img src="images/classes/english_pub.png" alt="Image 6">
        <div class="image-name">English Pub</div>
    </div>
    <div>
        <img src="images/classes/essex_maple.png" alt="Image 7">
        <div class="image-name">Essex Maple</div>
    </div>
    <div>
        <img src="images/classes/monterey_hardwood.png" alt="Image 8">
        <div class="image-name">Monterey Hardwood</div>
    </div>
    <div>
        <img src="images/classes/novella.png" alt="Image 9">
        <div class="image-name">Novella</div>
    </div>
    <div>
        <img src="images/classes/oak_plank.png" alt="Image 10">
        <div class="image-name">Oak Plank</div>
    </div>
    <div>
        <img src="images/classes/organic_567_engineered.png" alt="Image 11">
        <div class="image-name">Organic 567 Engineered</div>
    </div>
    <div>
        <img src="images/classes/organic_hardwood.png" alt="Image 12">
        <div class="image-name">Organic Hardwood</div>
    </div>
</div>

<style>
  .image-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    grid-gap: 10px;
  }
  
  .image-grid img {
    width: 250px;
    height: auto;
    display: block;
  }

  .image-name {
    text-align: left;
    font-size: 14px;
    font-weight: bold;
    margin-top: 5px;
  }
</style>

