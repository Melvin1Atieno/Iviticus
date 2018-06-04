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
    all_comments = []
    user = {}
    logged_in_user = login()

    if not logged_in_user:
        click.echo("You are no authorizes to comment on this post, please login")

    user_input = input("Enter your comment: ")
    try:
        all_comments.append(user_input)
    except Exception as e:
        click.echo(e)
    user.keys(logged_in_user)
    user.values(all_comments)

    return user


@cli.command()
def view_comments():
    pass


@cli.command()
@click.argument(comment_id)
def delete(comment_id):
    for a_comment in comments_list[:]:
        if a_comment['id'] == comment_id:
            comments_list.remove(a_comment)
            click.echo('Comment deleted successfully...')
            return
    else:
        click.echo('Comment not found!')
        return

if __name__ == '__main__':
    cli()
