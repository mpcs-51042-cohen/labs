# Convert this code into a class-oriented paradigm.

def clean_csv(input_path, output_path, delimiter=','):
    """Clean CSV by removing rows with empty fields"""
    processed_lines = 0
    removed_empty = 0
    
    with open(input_path, 'r') as f:
        lines = f.readlines()
    
    with open(output_path, 'w') as out:
        for line in lines:
            # Remove lines with empty fields
            fields = line.strip().split(delimiter)
            if any(field == '' for field in fields):
                removed_empty += 1
                continue  # Skip this line
            out.write(line)
            processed_lines += 1
    
    print(f"Processed {processed_lines} lines")
    print(f"Removed {removed_empty} rows with empty fields")


def redact_logs(input_path, output_path, sensitive_terms):
    """Redact sensitive information from log files"""
    processed_lines = 0
    redactions = 0
    
    with open(input_path, 'r') as f:
        lines = f.readlines()
    
    with open(output_path, 'w') as out:
        for line in lines:
            # Redact sensitive information
            redacted = line
            for term in sensitive_terms:
                if term in redacted:
                    redacted = redacted.replace(term, '[REDACTED]')
                    redactions += 1
            out.write(redacted)
            processed_lines += 1
    
    print(f"Processed {processed_lines} lines")
    print(f"Made {redactions} redactions")

  
clean_csv('data.csv', 'cleaned.csv')
redact_logs('data.log', 'cleaned.log', ['password=', 'api_key=', 'ssn:'])