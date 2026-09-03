from behave import given, when, then

@given("I open the music app")
def open_app(context):
    # Initialize a playlist list for each scenario
    context.playlist = []
    print("Music app opened.")

@when('I add the song "{song}" to the playlist')
def add_song(context, song):
    context.playlist.append(song)
    print(f"Added song: {song}")

@then('the playlist should contain "{song}"')
def verify_song_added(context, song):
    assert song in context.playlist, f"{song} not found in playlist"
    print(f"Verified playlist contains: {song}")

@when('I remove the song "{song}" from the playlist')
def remove_song(context, song):
    if song in context.playlist:
        context.playlist.remove(song)
    print(f"Removed song: {song}")

@then('the playlist should not contain "{song}"')
def verify_song_removed(context, song):
    assert song not in context.playlist, f"{song} still present in playlist"
    print(f"Verified playlist does not contain: {song}")
