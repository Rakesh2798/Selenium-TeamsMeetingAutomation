import sys
import os

# Add the project root to sys.path so we can import 'pages'
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pages.teams_page import TeamsSign

def test_teams_login_and_navigation():
    t = TeamsSign()
    try:
        t.sign_in_teams()
        t.send_email_id("starlocktemp@outlook.com")
        t.enter_email_password("rakesh@1234")
        t.click_chat_button()
        t.click_meet_button()
        t.click_people_button()
        t.click_copilot_button()
        t.click_communities_button()
        t.click_activity_button()
        t.click_calender_button()
    finally:
        t.driver.quit()

if __name__ == "__main__":
    test_teams_login_and_navigation()
