"""
Functions - SOLUTIONS
======================
Use this file to check your answers after attempting the exercises!
"""

print("=" * 60)
print("EXERCISE 1: Basic Helper Functions")
print("=" * 60)

# SOLUTION: Extract breed from filename
def extract_breed(filename):
    """
    Extract breed name from image filename.
    
    Args:
        filename (str): Image filename (e.g., 'beagle_001.jpg')
    
    Returns:
        str: Breed name (e.g., 'beagle')
    """
    return filename.split('_')[0]


# SOLUTION: Validate image file
def is_valid_image(filename):
    """
    Check if filename is a valid image file.
    
    Args:
        filename (str): Filename to check
    
    Returns:
        bool: True if valid image, False otherwise
    """
    return filename.endswith('.jpg') or filename.endswith('.jpeg')
    # Alternative: return filename.endswith(('.jpg', '.jpeg'))


# SOLUTION: Calculate accuracy
def calculate_accuracy(correct, total):
    """
    Calculate prediction accuracy.
    
    Args:
        correct (int): Number of correct predictions
        total (int): Total number of predictions
    
    Returns:
        float: Accuracy as a decimal (0.0 to 1.0)
    """
    return correct / total


# Test the functions
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

# SOLUTION: Filter predictions by confidence
def filter_by_confidence(predictions, threshold=0.8):
    """
    Filter predictions by confidence threshold.
    
    Args:
        predictions (list): List of prediction dictionaries
        threshold (float): Minimum confidence (default: 0.8)
    
    Returns:
        list: Filtered predictions above threshold
    """
    return [pred for pred in predictions if pred['confidence'] >= threshold]


# SOLUTION: Get images for specific breed
def get_breed_images(predictions, breed=None):
    """
    Get images for a specific breed.
    
    Args:
        predictions (list): List of prediction dictionaries
        breed (str): Breed to filter (default: None for all)
    
    Returns:
        list: List of image filenames
    """
    if breed is None:
        return [pred['image'] for pred in predictions]
    else:
        return [pred['image'] for pred in predictions if pred['breed'] == breed]
    
    # Alternative one-liner:
    # return [pred['image'] for pred in predictions if breed is None or pred['breed'] == breed]


# Test data
test_predictions = [
    {'image': 'beagle_001.jpg', 'breed': 'beagle', 'confidence': 0.95},
    {'image': 'poodle_001.jpg', 'breed': 'poodle', 'confidence': 0.75},
    {'image': 'beagle_002.jpg', 'breed': 'beagle', 'confidence': 0.88},
    {'image': 'husky_001.jpg', 'breed': 'husky', 'confidence': 0.65},
]

# Test functions
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

# SOLUTION: Count images per breed
def count_breeds(predictions):
    """
    Count number of images for each breed.
    
    Args:
        predictions (list): List of prediction dictionaries
    
    Returns:
        dict: Dictionary with breed:count pairs
    """
    breed_counts = {}
    for pred in predictions:
        breed = pred['breed']
        breed_counts[breed] = breed_counts.get(breed, 0) + 1
    return breed_counts


# SOLUTION: Calculate average confidence per breed
def average_confidence_by_breed(predictions):
    """
    Calculate average confidence for each breed.
    
    Args:
        predictions (list): List of prediction dictionaries
    
    Returns:
        dict: Dictionary with breed:avg_confidence pairs
    """
    breed_totals = {}
    breed_counts = {}
    
    for pred in predictions:
        breed = pred['breed']
        confidence = pred['confidence']
        
        breed_totals[breed] = breed_totals.get(breed, 0) + confidence
        breed_counts[breed] = breed_counts.get(breed, 0) + 1
    
    # Calculate averages
    averages = {}
    for breed in breed_totals:
        averages[breed] = breed_totals[breed] / breed_counts[breed]
    
    return averages


# SOLUTION: Find breed with highest average confidence
def best_performing_breed(predictions):
    """
    Find breed with highest average confidence.
    
    Args:
        predictions (list): List of prediction dictionaries
    
    Returns:
        str: Breed name with highest average confidence
    """
    avg_confidences = average_confidence_by_breed(predictions)
    return max(avg_confidences, key=avg_confidences.get)


# Test data
test_predictions = [
    {'image': 'beagle_001.jpg', 'breed': 'beagle', 'confidence': 0.95},
    {'image': 'beagle_002.jpg', 'breed': 'beagle', 'confidence': 0.88},
    {'image': 'poodle_001.jpg', 'breed': 'poodle', 'confidence': 0.92},
    {'image': 'poodle_002.jpg', 'breed': 'poodle', 'confidence': 0.85},
    {'image': 'husky_001.jpg', 'breed': 'husky', 'confidence': 0.78},
]

# Test functions
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

# Test data
predictions = [
    {'image': 'beagle_001.jpg', 'breed': 'beagle', 'confidence': 0.95, 'correct': True},
    {'image': 'poodle_001.jpg', 'breed': 'poodle', 'confidence': 0.88, 'correct': True},
    {'image': 'husky_001.jpg', 'breed': 'husky', 'confidence': 0.65, 'correct': False},
    {'image': 'beagle_002.jpg', 'breed': 'beagle', 'confidence': 0.92, 'correct': True},
    {'image': 'bulldog_001.jpg', 'breed': 'bulldog', 'confidence': 0.78, 'correct': False},
]

# SOLUTION: Extract all breed names
breed_names = list(map(lambda pred: pred['breed'], predictions))

# SOLUTION: Get predictions with confidence > 0.85
high_confidence = list(filter(lambda pred: pred['confidence'] > 0.85, predictions))

# SOLUTION: Get incorrect predictions
incorrect_predictions = list(filter(lambda pred: not pred['correct'], predictions))
# Alternative: list(filter(lambda pred: pred['correct'] == False, predictions))

# SOLUTION: Create formatted strings
formatted_results = list(map(lambda pred: f"{pred['image']}: {pred['breed']} ({pred['confidence']*100:.0f}%)", predictions))

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

# SOLUTION: Load and validate images
def load_images(filenames):
    """
    Load and validate image filenames.
    
    Args:
        filenames (list): List of image filenames
    
    Returns:
        list: List of valid image filenames
    """
    return [f for f in filenames if is_valid_image(f)]
    # Alternative: return list(filter(is_valid_image, filenames))


# SOLUTION: Simulate making predictions
def make_predictions(images):
    """
    Simulate making predictions for images.
    
    Args:
        images (list): List of image filenames
    
    Returns:
        list: List of prediction dictionaries
    """
    import random
    predictions = []
    
    for image in images:
        breed = extract_breed(image)
        confidence = round(random.uniform(0.7, 1.0), 2)
        
        predictions.append({
            'image': image,
            'breed': breed,
            'confidence': confidence
        })
    
    return predictions


# SOLUTION: Evaluate predictions
def evaluate_predictions(predictions, confidence_threshold=0.8):
    """
    Evaluate model predictions and generate statistics.
    
    Args:
        predictions (list): List of prediction dictionaries
        confidence_threshold (float): Threshold for "high confidence"
    
    Returns:
        dict: Statistics dictionary
    """
    total = len(predictions)
    high_conf = len([p for p in predictions if p['confidence'] >= confidence_threshold])
    low_conf = total - high_conf
    
    breed_counts = count_breeds(predictions)
    avg_confidences = average_confidence_by_breed(predictions)
    
    return {
        'total': total,
        'high_confidence': high_conf,
        'low_confidence': low_conf,
        'breed_counts': breed_counts,
        'avg_confidences': avg_confidences
    }


# SOLUTION: Generate report
def generate_report(stats):
    """
    Generate formatted report from statistics.
    
    Args:
        stats (dict): Statistics dictionary
    
    Returns:
        str: Formatted report
    """
    report = []
    report.append("="*50)
    report.append("CLASSIFICATION REPORT")
    report.append("="*50)
    report.append(f"\nTotal Predictions: {stats['total']}")
    report.append(f"High Confidence: {stats['high_confidence']} ({stats['high_confidence']/stats['total']*100:.1f}%)")
    report.append(f"Low Confidence: {stats['low_confidence']} ({stats['low_confidence']/stats['total']*100:.1f}%)")
    
    report.append("\nBreed Distribution:")
    for breed, count in stats['breed_counts'].items():
        avg_conf = stats['avg_confidences'][breed]
        report.append(f"  {breed}: {count} images (avg confidence: {avg_conf:.2%})")
    
    report.append("="*50)
    
    return "\n".join(report)


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
print("KEY CONCEPTS REVIEW")
print("=" * 60)
print("""
1. FUNCTION BASICS:
   • def function_name(parameters):
   • return value - gives result back to caller
   • Docstrings - explain what function does

2. PARAMETERS AND ARGUMENTS:
   • Required parameters: def func(x, y)
   • Default parameters: def func(x, y=5)
   • Positional: func(10, 20)
   • Keyword: func(x=10, y=20)

3. FUNCTION SCOPE:
   • Local variables - only exist inside function
   • Global variables - exist outside function
   • Use return to get values out of functions

4. LAMBDA FUNCTIONS:
   • Anonymous one-line functions
   • Syntax: lambda x: expression
   • Use with map/filter: map(lambda x: x*2, list)

5. COMMON PATTERNS:
   • Helper functions - extract_breed, is_valid_image
   • Validation functions - return bool
   • Calculation functions - return computed value
   • Processing functions - take list, return processed list
   • Pipeline functions - call other functions in sequence

6. BEST PRACTICES:
   • Use descriptive function names
   • Add docstrings to explain purpose
   • Keep functions focused (do one thing well)
   • Use default parameters for common values
   • Return values instead of printing (more flexible)
""")

print("\n" + "=" * 60)
print("DOG BREED CLASSIFIER FUNCTION PATTERNS:")
print("=" * 60)
print("""
✓ extract_breed(filename) - Get breed from filename
✓ is_valid_image(filename) - Check if file is valid
✓ filter_by_confidence(predictions, threshold) - Filter results
✓ count_breeds(predictions) - Count images per breed
✓ calculate_accuracy(correct, total) - Compute metrics
✓ make_predictions(images) - Run classifier on images
✓ evaluate_predictions(predictions) - Analyze results
✓ generate_report(stats) - Format output

Real example from project:
```python
# You'll have a main function like this:
def classify_images(image_dir, model, threshold=0.8):
    images = load_images(image_dir)
    predictions = make_predictions(images, model)
    filtered = filter_by_confidence(predictions, threshold)
    stats = evaluate_predictions(filtered)
    report = generate_report(stats)
    return report
```

Functions make your code:
• Reusable - write once, use many times
• Testable - easy to verify each piece works
• Readable - clear what each part does
• Maintainable - easy to fix bugs or add features
""")
