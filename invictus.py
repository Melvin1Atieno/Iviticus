import click

users_list = []
comments_list = []

# if the user is logged in, this is where
#  they will be stored for reference
session = dict(current_user=None)

@click.group()
def cli():
    pass

def create_user():
    pass

@cli.command()
def view_users():
    pass


@cli.command()
def register(username, password, role):
    pass

@cli.command()
def login():
    pass


@cli.command()
def comment():
    pass


@cli.command()
def view_comments():
    pass


@cli.command()
def delete():
    pass


if __name__ == '__main__':
    cli()
