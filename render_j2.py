import argparse
import os
from jinja2 import Template


def render_template(template_file, context):
    """
    reads the mai.tf.j2 file and renders the inputs to the file and creates
    terraform configuration file
    """
    # Read the template file
    with open(template_file, 'r') as file:
        template_content = file.read()
    
    # Create a Template object
    template = Template(template_content)
    
    # Render the template with the given context (input values)
    rendered_output = template.render(context)
    
    return rendered_output


def create_main_tf_file(directory: str, content: str):
    """
    create the main.tf files in specific folder structure
    """
    # Ensure the directory exists
    os.makedirs(directory, exist_ok=True)

    # File path for main.tf
    file_path = os.path.join(directory, "main.tf")

    # Write content to the file
    with open(file_path, "w") as file:
        file.write(content)
    print(f"main.tf created at {file_path}")


def copy_file_to_structure(destination: str):
    """
    copy output.tf from root of repo to folder in which main.tf will be generated
    """
    # Defining the source file path in the root directory
    root_directory = "."
    source_file = os.path.join(root_directory, "output.tf")

    # Ensure the directory exists
    os.makedirs(destination, exist_ok=True)

    # Define the destination file path
    destination_file = os.path.join(destination, os.path.basename(source_file))

    try:
        # Open and copy the file content
        with open(source_file, "r") as src:
            content = src.read()
        with open(destination_file, "w") as dest:
            dest.write(content)
        print(f"Copied {source_file} to {destination_file}")
    except FileNotFoundError:
        print(f"Error: Source file {source_file} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")


def main():
    """
    Main function to parse arguments and run the rendering process
    """
    # Argument parser to receive input values
    parser = argparse.ArgumentParser(description="Render a Jinja2 template for Terraform configuration.")
    
    # Define the arguments to be passed
    parser.add_argument('--application_name', required=True, help="The application name.")
    parser.add_argument('--environment', required=True, help="The environment name.")
    parser.add_argument('--temporary', required=True, help="Temporary flag (true/false).")
    parser.add_argument('--location', required=True, help="The location for the VNet.")
    parser.add_argument('--resource_group_name', required=True, help="Resource group name.")
    parser.add_argument('--subnet_cidrs', required=True, help="List of subnet CIDRs (as a string).")
    parser.add_argument('--vnet_address_space', required=True, help="VNet address space (as a string).")
    parser.add_argument('--vnet_name', required=True, help="VNet name.")
    
    # Parse the arguments
    args = parser.parse_args()

    # Combine resource group name and vnet name to form directory
    directory_name = f"{args.resource_group_name}/{args.vnet_name}"

    # Convert the subnet_cidrs and vnet_address_space to lists using json.loads
    subnet_cidrs = [item.strip('"') for item in args.subnet_cidrs.split(',')]
    vnet_address_space = [args.vnet_address_space]

    # Create the context for the Jinja2 template
    context = {
        "application_name": args.application_name,
        "environment": args.environment,
        "temporary": args.temporary,
        "location": args.location,
        "resource_group_name": args.resource_group_name,
        "subnet_cidrs": subnet_cidrs,
        "vnet_address_space": vnet_address_space,
        "vnet_name": args.vnet_name
    }

    # Call the render_template function to generate the main.tf content
    main_tf_content = render_template('main.tf.j2', context)

    # Create the main.tf file
    create_main_tf_file(directory=directory_name, content=main_tf_content)

    # Copy output.tf into destination directory
    copy_file_to_structure(destination=directory_name)


# Run the script
if __name__ == "__main__":
    main()
