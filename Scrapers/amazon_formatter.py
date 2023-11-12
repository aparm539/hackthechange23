import re


laptop_details = []

# Open the output file in write mode
with open('laptop_details_formatted.txt', 'w') as formatted_file:
    # Read the input file
    with open('laptop_details.txt', 'r') as file:
        for line in file:
            components = line.strip().split(',', 1)
            
            listing_name, remaining_details = components[0], components[1]
            remaining_details = re.sub(r'®|™', '', remaining_details)

            # Define patterns
            cpu_patterns = [
                r'Intel Core i[5-9]-\d{4,5}[H|U]',
                r'Intel Pentium(?: [A-Za-z0-9-]*)?'
                r'Apple M\d',
                r'AMD Ryzen [5937] \d{4}(U|HS|S|H)',
                r'Intel Celeron [A-Za-z0-9-]+',
                r'Intel Core i[3-7]-\d{4,5}[G|U]'
            ]
            refresh_rate_pattern = r'\b(\d{2,3}Hz)\b'
            ram_pattern = r'\b\d{1,2}GB\b'
            storage_patterns = [r'\b\d{1,3}GB\b', r'\b\d{1,2}TB\b']
            display_size_pattern = r'\d{1,2}\.?\d{0,2}[\"”]'
            resolution_pattern = r'\b(UHD|FHD|HD|WQHD|QHD|4K|1080p|1440p)\b'

            # Extract CPU
            cpu = "CPU not specified"
            for pattern in cpu_patterns:
                match = re.search(pattern, remaining_details)
                if match:
                    cpu = match.group(0)
                    remaining_details = remaining_details.replace(cpu, "")
                    break

            # Extract Refresh Rate
            refresh_rate_match = re.search(refresh_rate_pattern, remaining_details, re.IGNORECASE)
            refresh_rate = refresh_rate_match.group(1) if refresh_rate_match else "Refresh rate not specified"
            remaining_details = remaining_details.replace(refresh_rate, "")

            # Extract RAM
            ram_match = re.search(ram_pattern, remaining_details)
            ram = ram_match.group(0) if ram_match else "RAM not specified"
            remaining_details = remaining_details.replace(ram, "")

            # Extract Storage
            storage_type = "Storage type not specified"

            storage_type_patterns = [
                r'PCIE SSD Gen [2-5]',
                r'SSD',
                r'HDD',
                r'eMMC'
            ]

            for pattern in storage_type_patterns:
                match = re.search(pattern, remaining_details, re.IGNORECASE)
                if match:
                    storage_type = match.group(0)
                    break

            storage = "Storage not specified"
            for pattern in storage_patterns:
                match = re.search(pattern, remaining_details)
                if match:
                    storage = match.group(0)
                    remaining_details = remaining_details.replace(storage, "")
                    break



            # Extract Display
            display_size_match = re.search(display_size_pattern, remaining_details)
            display_size = display_size_match.group(0) if display_size_match else "Display not specified"
            remaining_details = remaining_details.replace(display_size, "")

            resolution_match = re.search(resolution_pattern, remaining_details, re.IGNORECASE)
            resolution = resolution_match.group(1) if resolution_match else "Resolution not specified"
            remaining_details = re.sub(resolution_pattern, '', remaining_details)

            display_type_patterns = [r'IPS', r'VA', r'OLED']
            display_type = "Display type not specified"
            for pattern in display_type_patterns:
                if re.search(pattern, line, re.IGNORECASE):
                    display_type = pattern
                    break

            os = "OS not specified"
            if "Apple" in listing_name:
                os = "macOS"
            elif "Chromebook" in listing_name:
                os = "Chrome OS"
            else:
                # Check for Windows as it's the most common OS apart from macOS and Chrome OS
                windows_match = re.search(r'Windows \d{1,2}(?: Home| Pro| in S Mode)?', remaining_details, re.IGNORECASE)
                if windows_match:
                    os = windows_match.group(0)
            
            price_pattern = r'\$\d{1,3}(?:,\d{3})*(?:\.\d{2})?'
            price_match = re.search(price_pattern, remaining_details)
            price = price_match.group(0) if price_match else "Price not specified"
            remaining_details = remaining_details.replace(price, "")

            laptop_dict = {
                "Name": listing_name,
                "CPU": cpu,
                "Display Size": display_size,
                "Resolution": resolution,
                "Display Type": display_type,
                "Refresh Rate": refresh_rate,
                "RAM": ram,
                "Storage": storage,
                "Storage Type": storage_type,
                "OS": os,
                "Price": price
            }

            # Add the dictionary to the list
            laptop_details.append(laptop_dict)

            # Write to the output file
            formatted_file.write(f"{laptop_dict}\n\n")




