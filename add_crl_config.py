#!/usr/bin/env python3
"""
Simple script to add CRL configuration to step-ca's ca.json.
This is copied into the step-ca container and executed there.
"""
import json
import sys

def add_crl_config(ca_json_path):
    """Add CRL configuration to ca.json"""
    try:
        with open(ca_json_path, 'r') as f:
            config = json.load(f)

        # Add CRL configuration
        config['crl'] = {
            'enabled': True,
            'generateOnRevoke': True,
            'cacheDuration': '24h'
        }

        # Write back with proper formatting
        with open(ca_json_path, 'w') as f:
            json.dump(config, f, indent=8)

        print("✓ CRL configuration added successfully")
        return 0
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1

if __name__ == '__main__':
    sys.exit(add_crl_config('/home/step/config/ca.json'))
