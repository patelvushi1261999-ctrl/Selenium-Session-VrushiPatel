Feature: Playlist management in music app

  @smoke
  Scenario: Add song to playlist
    Given I open the music app
    When I add the song "Shape of You" to the playlist
    Then the playlist should contain "Shape of You"

  Scenario: Remove song from playlist
    Given I open the music app
    When I remove the song "Shape of You" from the playlist
    Then the playlist should not contain "Shape of You"
