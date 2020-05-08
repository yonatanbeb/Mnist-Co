# Mnist&Co


## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install modules in Project.

```bash
pip install -r requirements.txt
```

## Usage

Start session by typing:

```bash
. ./init.sh
```

Then browse catalog by typing:

```bash
browse
```

Create a profile:

```bash
create_profile Username Password clearance_level
```

Or sign into existing profile once a profile is created:

```bash
sign_in Username Password
```

To query the content of an image in catalog:

```bash
query catalog_item
```

To get a directory with all catalog items of certain label:

```grab
grab label [-a | --all] to_path
```

Or to get a directory with a specified amount of certain label:

```bash
grab label [-n | --num] amount to_path
```

When session finished:

```bash
sign_out
```

Or:

```bash
exit
```
