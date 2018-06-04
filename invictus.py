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
@click.argument('username')
@click.argument('password')
def login(username, password):
    find_user = [user for user in users_list if user["username"] == username]
    if len(find_user) != 0:
        if find_user[0]['password'] == password:
            session["current_user"] = username
            return 'Hello {}, you can now add a comment'.format(username)
        return 'Password or username doesn't match'
    return '{}, don't have an account.format(username)


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
