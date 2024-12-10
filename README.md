Proof of Concept (PoC) Python script to exploit SQL Injection in WordPress versions < 5.8.3 via WP_Query

Usage Instructions:

Replace the TARGET_URL with the target WordPress site’s AJAX handler.
Replace vulnerable_action with the actual action that calls WP_Query.
Adjust VULNERABLE_PARAM and SQL_PAYLOAD to match your target’s configuration.
Run the script: python WP_Query.py

Analyze the output for extracted credentials.
