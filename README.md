# Password Generator

## Overview

This Python script generates secure passwords with customizable options. It creates two sets of passwords each time it's run:
1. Passwords using only ASCII characters.
2. Passwords incorporating characters from various languages and scripts.

## Features

- Generates 10 passwords per run.
- Allows specification of minimum and maximum password length.
- Ensures passwords contain a required number of symbols.
- Prevents consecutive use of the same symbol.
- Includes options for ASCII-only passwords and multi-language character passwords.

## Installation

1. Ensure you have Python 3.6 or later installed.
2. Clone or download this repository to your local machine.
3. Navigate to the project directory in your terminal.

## Usage

To generate passwords, run the script using the following command:

    python password_gen.py

This will print 10 passwords using ASCII characters and another 10 with multi-language characters.

### Customization

You can customize the script by modifying the following parameters:

- `count`: Number of passwords to generate (default is 10).
- `min_length`: Minimum length of each password (default is 12).
- `max_length`: Maximum length of each password (default is 24).

To adjust these parameters, update the `generate_passwords` function call at the bottom of the script:

    passwords = generate_passwords(count=10, min_length=12, max_length=24)

## Examples

Here are some sample outputs:

- **ASCII Passwords:**

    n$6Pc&bE4@W!Y

    Q^2rPz7*L.xw9

- **Multi-Language Passwords:**

    مちeo5bvöρiAtEןσ你

    нzWਸZEiTε녕ာßXgρत하eiürStχ

## Notes

- Passwords are generated with a minimum number of symbols and random non-repeating symbols.
- Ensure that the generated passwords meet your security requirements and policies.
![image](https://github.com/user-attachments/assets/e3a90422-1261-4172-a967-605d6811625a)

