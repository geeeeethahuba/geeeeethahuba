import wikipedia

def get_treatment_from_wikipedia(disease):
    try:
        # Use Wikipedia API to search for the disease page
        search_results = wikipedia.search(disease)
        if search_results:
            # Get the summary of the first search result
            page_summary = wikipedia.summary(search_results[0], sentences=10)
            return page_summary
        else:
            return "Sorry, no information found for {} on Wikipedia.".format(disease)
    except wikipedia.exceptions.DisambiguationError as e:
        # If there are multiple results, provide some suggestions
        return "Multiple results found for {}. Try one of these: {}".format(disease, ", ".join(e.options))
    except wikipedia.exceptions.PageError:
        return "Sorry, no information found for {} on Wikipedia.".format(disease)

def main():
    disease = input("Enter the name of the disease: ")
    treatment_info = get_treatment_from_wikipedia(disease)
    print("Treatment information for {} from Wikipedia:".format(disease))
    print(treatment_info)

if __name__ == "__main__":
    main()
