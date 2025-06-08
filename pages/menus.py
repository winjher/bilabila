def display_content(item):
    content = {
        "Home": "Welcome to the Butterfly Management System!",
        "About": "This application is designed to help breeders effectively manage butterflies at various life stages.",
        "Contact": "Reach us at butterflycare@example.com for more information.",
        "Larval Diseases": "Information and management strategies for common larval diseases.",
        "Pupae Defects": "Details and preventive measures for pupae defects.",
        "Butterfly Life Cycle": "Learn about the fascinating stages of a butterfly's life: Egg, Larva, Pupa, and Adult.",
        "Breeders": "Guidelines for butterfly breeders to optimize care and maximize productivity.",
        "Breeders Income": "Reports and insights on the potential income from breeding butterflies.",
        "Butterfly": "General information about butterflies and their species.",
        "Butterfly Data": "Analyze and classify butterfly species using data-driven tools.",
        "Care Management": "Comprehensive care solutions for all butterfly life stages.",
        "Classification": "Methods to classify butterfly species based on unique features.",
        "Classifier": "Tools and algorithms for species and defect classification.",
        "Classify Diseases": "Techniques to identify and categorize diseases in larvae.",
        "CNN Classifier": "Using Convolutional Neural Networks for butterfly classification tasks.",
        "Countdown": "Track and schedule important care-related events.",
        "Defects": "Overview of defects observed in pupae and adult butterflies.",
        "Diseases": "Overview of diseases affecting larvae and butterflies.",
        "Example": "Example workflows for butterfly management tasks.",
        "Hostplants": "Guide to selecting and managing host plants for larvae.",
        "Larval Disease": "Detailed insights into specific larval diseases and treatments.",
        "Life Stages": "Detailed description of the life stages of butterflies.",
        "Menu": "Navigation menu for managing various functionalities.",
        "OpenCV": "Using OpenCV for image processing and classification.",
        "Pupae Defects": "Strategies for identifying and preventing pupae defects.",
        "Purchasers": "Insights into markets and potential purchasers of butterflies.",
        "Stages": "Information about butterfly growth and development stages.",
        "Tasks": "Manage and track butterfly care tasks.",
        "Transfer Learning": "Using transfer learning for advanced butterfly classification."
    }

    # Display corresponding content
    print(content.get(item, "No content available for this menu item."))
