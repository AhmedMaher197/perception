"""
Functions - Practice Exercises
===============================
Target: Pre-trained Image Classifier for Dog Breeds
Focus: Creating reusable helper functions for the classifier
"""

print("=" * 60)
print("EXERCISE 1: Basic Helper Functions")
print("=" * 60)
"""
Scenario:
You need helper functions to extract breed information from image filenames
and validate file types. These will be used throughout your classifier.

Tasks:
1. Write a function to extract breed name from filename
2. Write a function to check if file is valid image
3. Write a function to calculate accuracy from results
"""

# TODO: Write function to extract breed from filename
# Function should take filename like 'beagle_001.jpg' and return 'beagle'
def extract_breed(filename):
    """
    Extract breed name from image filename.
    
    Args:
        filename (str): Image filename (e.g., 'beagle_001.jpg')
    
    Returns:
        str: Breed name (e.g., 'beagle')
    """
    # TODO: Split filename by '_' and return first part
    pass


# TODO: Write function to validate image file
# Function should return True if filename ends with .jpg or .jpeg
def is_valid_image(filename):
    """
    Check if filename is a valid image file.
    
    Args:
        filename (str): Filename to check
    
    Returns:
        bool: True if valid image, False otherwise
    """
    # TODO: Check if filename ends with '.jpg' or '.jpeg'
    pass


# TODO: Write function to calculate accuracy
# accuracy = correct_predictions / total_predictions
def calculate_accuracy(correct, total):
    """
    Calculate prediction accuracy.
    
    Args:
        correct (int): Number of correct predictions
        total (int): Total number of predictions
    
    Returns:
        float: Accuracy as a decimal (0.0 to 1.0)
    """
    # TODO: Return correct / total
    pass


# Test your functions
print("\nTesting extract_breed:")
print(f"  extract_breed('beagle_001.jpg') = {extract_breed('beagle_001.jpg')}")
print(f"  extract_breed('golden_retriever_042.jpg') = {extract_breed('golden_retriever_042.jpg')}")

print("\nTesting is_valid_image:")
print(f"  is_valid_image('dog.jpg') = {is_valid_image('dog.jpg')}")
print(f"  is_valid_image('dog.png') = {is_valid_image('dog.png')}")
print(f"  is_valid_image('dog.jpeg') = {is_valid_image('dog.jpeg')}")

print("\nTesting calculate_accuracy:")
print(f"  calculate_accuracy(85, 100) = {calculate_accuracy(85, 100):.2%}")
print(f"  calculate_accuracy(92, 100) = {calculate_accuracy(92, 100):.2%}")


print("\n" + "=" * 60)
print("EXERCISE 2: Functions with Default Parameters")
print("=" * 60)
"""
Scenario:
Your classifier needs functions to filter predictions based on confidence
thresholds. Some parameters should have default values.

Tasks:
1. Create function with default confidence threshold
2. Create function with default breed filter
3. Use keyword arguments to call functions
"""

# TODO: Write function to filter predictions by confidence
# Default threshold should be 0.8
def filter_by_confidence(predictions, threshold=0.8):
    """
    Filter predictions by confidence threshold.
    
    Args:
        predictions (list): List of prediction dictionaries
        threshold (float): Minimum confidence (default: 0.8)
    
    Returns:
        list: Filtered predictions above threshold
    """
    # TODO: Return list comprehension filtering predictions
    # where prediction['confidence'] >= threshold
    pass


# TODO: Write function to get images for specific breed
# Default breed should be None (meaning all breeds)
def get_breed_images(predictions, breed=None):
    """
    Get images for a specific breed.
    
    Args:
        predictions (list): List of prediction dictionaries
        breed (str): Breed to filter (default: None for all)
    
    Returns:
        list: List of image filenames
    """
    # TODO: If breed is None, return all images
    # Otherwise, return images where prediction['breed'] == breed
    pass


# Test data
test_predictions = [
    {'image': 'beagle_001.jpg', 'breed': 'beagle', 'confidence': 0.95},
    {'image': 'poodle_001.jpg', 'breed': 'poodle', 'confidence': 0.75},
    {'image': 'beagle_002.jpg', 'breed': 'beagle', 'confidence': 0.88},
    {'image': 'husky_001.jpg', 'breed': 'husky', 'confidence': 0.65},
]

# Test your functions
print("\nTesting filter_by_confidence:")
print(f"  Default threshold (0.8): {len(filter_by_confidence(test_predictions))} predictions")
print(f"  Threshold 0.7: {len(filter_by_confidence(test_predictions, 0.7))} predictions")
print(f"  Threshold 0.9: {len(filter_by_confidence(test_predictions, threshold=0.9))} predictions")

print("\nTesting get_breed_images:")
print(f"  All breeds: {get_breed_images(test_predictions)}")
print(f"  Beagles only: {get_breed_images(test_predictions, 'beagle')}")
print(f"  Poodles only: {get_breed_images(test_predictions, breed='poodle')}")


print("\n" + "=" * 60)
print("EXERCISE 3: Processing Collections with Functions")
print("=" * 60)
"""
Scenario:
You need functions to process batches of images and calculate statistics
about your model's performance.

Tasks:
1. Count images per breed
2. Calculate average confidence per breed
3. Find top performing breed
"""

# TODO: Write function to count images per breed
def count_breeds(predictions):
    """
    Count number of images for each breed.
    
    Args:
        predictions (list): List of prediction dictionaries
    
    Returns:
        dict: Dictionary with breed:count pairs
    """
    # TODO: Create empty dictionary
    # Loop through predictions
    # Count occurrences of each breed
    # Return the dictionary
    pass


# TODO: Write function to calculate average confidence per breed
def average_confidence_by_breed(predictions):
    """
    Calculate average confidence for each breed.
    
    Args:
        predictions (list): List of prediction dictionaries
    
    Returns:
        dict: Dictionary with breed:avg_confidence pairs
    """
    # TODO: Create dictionaries to store total confidence and counts
    # Loop through predictions
    # Sum confidences and count per breed
    # Calculate averages
    # Return dictionary
    pass


# TODO: Write function to find breed with highest average confidence
def best_performing_breed(predictions):
    """
    Find breed with highest average confidence.
    
    Args:
        predictions (list): List of prediction dictionaries
    
    Returns:
        str: Breed name with highest average confidence
    """
    # TODO: Call average_confidence_by_breed to get averages
    # Use max() with key parameter to find breed with highest value
    pass


# Test data
test_predictions = [
    {'image': 'beagle_001.jpg', 'breed': 'beagle', 'confidence': 0.95},
    {'image': 'beagle_002.jpg', 'breed': 'beagle', 'confidence': 0.88},
    {'image': 'poodle_001.jpg', 'breed': 'poodle', 'confidence': 0.92},
    {'image': 'poodle_002.jpg', 'breed': 'poodle', 'confidence': 0.85},
    {'image': 'husky_001.jpg', 'breed': 'husky', 'confidence': 0.78},
]

# Test your functions
print("\nTesting count_breeds:")
breed_counts = count_breeds(test_predictions)
print(f"  Breed counts: {breed_counts}")

print("\nTesting average_confidence_by_breed:")
avg_confidences = average_confidence_by_breed(test_predictions)
print(f"  Average confidences: {avg_confidences}")

print("\nTesting best_performing_breed:")
best_breed = best_performing_breed(test_predictions)
print(f"  Best performing breed: {best_breed}")


print("\n" + "=" * 60)
print("EXERCISE 4: Lambda Functions for Data Processing")
print("=" * 60)
"""
Scenario:
Use lambda functions with map() and filter() to efficiently process
your image dataset.

Tasks:
1. Use map to extract breed names
2. Use filter to get high confidence predictions
3. Use filter to get incorrect predictions
4. Use map to format results for display
"""

# Test data
predictions = [
    {'image': 'beagle_001.jpg', 'breed': 'beagle', 'confidence': 0.95, 'correct': True},
    {'image': 'poodle_001.jpg', 'breed': 'poodle', 'confidence': 0.88, 'correct': True},
    {'image': 'husky_001.jpg', 'breed': 'husky', 'confidence': 0.65, 'correct': False},
    {'image': 'beagle_002.jpg', 'breed': 'beagle', 'confidence': 0.92, 'correct': True},
    {'image': 'bulldog_001.jpg', 'breed': 'bulldog', 'confidence': 0.78, 'correct': False},
]

# TODO: Use map with lambda to extract all breed names
breed_names = None  # list(map(lambda pred: ..., predictions))

# TODO: Use filter with lambda to get predictions with confidence > 0.85
high_confidence = None  # list(filter(lambda pred: ..., predictions))

# TODO: Use filter with lambda to get incorrect predictions
incorrect_predictions = None  # list(filter(lambda pred: ..., predictions))

# TODO: Use map with lambda to create formatted strings
# Format: "beagle_001.jpg: beagle (95%)"
formatted_results = None  # list(map(lambda pred: f"...", predictions))

# Print results
print("\nBreed names:")
print(f"  {breed_names}")

print("\nHigh confidence predictions:")
print(f"  Count: {len(high_confidence)}")
print(f"  Images: {[p['image'] for p in high_confidence]}")

print("\nIncorrect predictions:")
print(f"  Count: {len(incorrect_predictions)}")
print(f"  Images: {[p['image'] for p in incorrect_predictions]}")

print("\nFormatted results:")
for result in formatted_results:
    print(f"  {result}")


print("\n" + "=" * 60)
print("EXERCISE 5: Building a Complete Classifier Pipeline")
print("=" * 60)
"""
Scenario:
Combine everything into a complete classification pipeline with multiple
helper functions working together.

Tasks:
1. Validate and load images
2. Make predictions (simulated)
3. Evaluate results
4. Generate report
"""

# TODO: Write function to load and validate images
def load_images(filenames):
    """
    Load and validate image filenames.
    
    Args:
        filenames (list): List of image filenames
    
    Returns:
        list: List of valid image filenames
    """
    # TODO: Filter filenames using is_valid_image function
    pass


# TODO: Write function to simulate making predictions
def make_predictions(images):
    """
    Simulate making predictions for images.
    (In real project, this would call the actual model)
    
    Args:
        images (list): List of image filenames
    
    Returns:
        list: List of prediction dictionaries
    """
    # TODO: For each image in images:
    # - Extract breed using extract_breed
    # - Generate random confidence between 0.7 and 1.0
    # - Create prediction dict with image, breed, confidence
    # Return list of predictions
    import random
    pass


# TODO: Write function to evaluate predictions
def evaluate_predictions(predictions, confidence_threshold=0.8):
    """
    Evaluate model predictions and generate statistics.
    
    Args:
        predictions (list): List of prediction dictionaries
        confidence_threshold (float): Threshold for "high confidence"
    
    Returns:
        dict: Statistics dictionary
    """
    # TODO: Calculate:
    # - Total predictions
    # - High confidence count (>= threshold)
    # - Low confidence count (< threshold)
    # - Breed counts (use count_breeds function)
    # - Average confidence per breed (use average_confidence_by_breed)
    # Return dictionary with all statistics
    pass


# TODO: Write function to generate report
def generate_report(stats):
    """
    Generate formatted report from statistics.
    
    Args:
        stats (dict): Statistics dictionary
    
    Returns:
        str: Formatted report
    """
    # TODO: Create multi-line string with formatted statistics
    # Include: total predictions, high/low confidence counts,
    # breed counts, and average confidences
    pass


# Test the complete pipeline
print("\n=== RUNNING CLASSIFIER PIPELINE ===")

# Sample image files
image_files = [
    'beagle_001.jpg', 'beagle_002.jpg', 'beagle_003.jpg',
    'poodle_001.jpg', 'poodle_002.jpg',
    'husky_001.jpg', 'husky_002.jpg',
    'bulldog_001.txt',  # Invalid!
    'golden_retriever_001.jpg'
]

# Step 1: Load images
print("\nStep 1: Loading images...")
valid_images = load_images(image_files)
print(f"  Loaded {len(valid_images)} valid images")

# Step 2: Make predictions
print("\nStep 2: Making predictions...")
predictions = make_predictions(valid_images)
print(f"  Generated {len(predictions)} predictions")

# Step 3: Evaluate
print("\nStep 3: Evaluating results...")
stats = evaluate_predictions(predictions, confidence_threshold=0.85)

# Step 4: Generate report
print("\nStep 4: Generating report...")
report = generate_report(stats)
print(report)


print("\n" + "=" * 60)
print("All exercises completed!")
print("=" * 60)
print("\nFunction Skills for Dog Breed Classifier:")
print("• Helper functions - Extract breed, validate files, calculate metrics")
print("• Default parameters - Flexible threshold values")
print("• Processing collections - Count breeds, calculate averages")
print("• Lambda functions - Efficient filtering and mapping")
print("• Pipeline functions - Combine multiple steps into workflow")
print("\nThese functions will form the backbone of your classifier!")
