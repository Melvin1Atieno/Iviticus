import click

users_list = []
comments_list = []

roles = ['admin', 'regular', 'moderator']

# if the user is logged in, this is where
#  they will be stored for reference
session = dict(current_user=None)

@click.group()
def cli():
    pass

def create_user(username: str, password: str, role: str):
    user = dict(
        username=username,
        password=password,
        role=role
    )
    return user

@cli.command()
def view_users():
    pass


@cli.command()
@click.argument('username')
@click.argument('password')
@click.argument('role')
def register(username, password, role):
    if role not in roles:
        click.echo('error: Role specified does not exist')
        return

    user = create_user(username, password, role)
    click.echo(user['username']+' '+user['role'])
    return

@cli.command()
@click.argument('username')
@click.argument('password')
def login(username, password):
    find_user = [user for user in users_list if user["username"] == username]
    if len(find_user) != 0:
        if find_user[0]['password'] == password:
            session["current_user"] = username
            click.echo('Hello {}, you can now add a comment'.format(username))
            return
        click.echo('Password or username doesn\'t match')
        return
    click.echo('{}, don\'t have an account'.format(username))
    return


@cli.command()
def comment():
    pass


@cli.command()
def view_comments():
    click.echo(str(comments_list))

@cli.command()
def delete():
    pass


if __name__ == '__main__':
    cli()
