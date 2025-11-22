import os
from markdown_handler import markdown_to_html_node, extract_title
from node_handler import *


def generate_page(from_path, template_path, dest_path, base_path):
    print(
        f"Generating page from {from_path} to {dest_path} using template {template_path}..."
    )

    # read the markdown content from the source file (from_path):
    with open(from_path, "r") as f:
        markdown_content = f.read()

    # read the template content from the template file (template_path):
    with open(template_path, "r") as f:
        template_content = f.read()

    # use 'markdown_to_html_node' function and '.to_html()' method to convert the markdown file into an HTML string:
    html_content = markdown_to_html_node(markdown_content).to_html()

    # use the 'extract_title' function to grab the title from the markdown content:
    md_title = extract_title(markdown_content)

    # replace the {{ Title }} and {{ Content }} placeholders in the template with the extracted title and generated HTML content:
    final_html = template_content.replace("{{ Title }}", md_title).replace(
        "{{ Content }}", html_content
    )
    # replace 'href="/' with 'href="{base_path}' and 'src="/' with 'src="{base_path}' to handle base paths:
    final_html = final_html.replace('href="/', f'href="{base_path}').replace(
        'src="/', f'src="{base_path}'
    )

    # write the final HTML content to the destination file (dest_path) and be sure to create any necessary directories:
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    with open(dest_path, "w") as f:
        f.write(final_html)

    print(f"Generated page at {dest_path} using template {template_path}")


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, base_path):
    # crawl every entry in the content directory:
    all_entries = os.listdir(dir_path_content)
    # for each markdown file found, generate a new html file using the same template.html;
    # the generated pages should be written to the 'public' directory in teh same directory structure as the 'content' directory:
    for entry in all_entries:
        full_entry_path = os.path.join(dir_path_content, entry)
        if os.path.isfile(full_entry_path) and entry.endswith(".md"):
            relative_path = os.path.relpath(full_entry_path, dir_path_content)
            dest_path = os.path.join(
                dest_dir_path, relative_path[:-3] + ".html"
            )  # change .md to .html
            generate_page(full_entry_path, template_path, dest_path, base_path)
        elif os.path.isdir(full_entry_path):
            # recursively generate pages in subdirectories:
            generate_pages_recursive(
                full_entry_path,
                template_path,
                os.path.join(dest_dir_path, entry),
                base_path,
            )
