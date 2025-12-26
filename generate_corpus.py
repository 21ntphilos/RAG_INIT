import os
import wikipedia
import re 

"replace non-alphanumeric characters with underscores"
def sanitize_filename(name):
    return re.sub(r'[^a-zA-Z0-9]', '_', name)

def generate_corpus(search_term="Monetary policy", num_articles=1000, output_dir="output_dir"):
    # create the output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)


    articles = []
    # search wikipedia and pull out article lists
    search_result = wikipedia.search(search_term, results=num_articles)

    print(f"Found {len(search_result)} articles for search term '{search_term}'.")

    for i, title in enumerate(search_result):
        try:
            page = wikipedia.page(title)
            articles.append((title, page.content))

            # sanitize the filename and save the article content to a text file
            sanitized_filename = sanitize_filename(title)
            file_path = os.path.join(output_dir, f"{sanitized_filename}.txt")

            # write the file
            with open (file_path, "w", encoding="utf-8") as f:
                f.write(page.content)
            print(f"Saved article {i+1}/{len(search_result)}: {title}") 

        except Exception as e:
            print(f"Error retrieving article '{title}': {e}")
            continue
    
    print(f"\nCompleted!! \nSaved {len(articles)} articles to '{output_dir}' directory.")


if __name__ == "__main__":
    generate_corpus(search_term="Monetary policy", num_articles=1000, output_dir="output_dir")



