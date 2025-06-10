Feature: Login Page
 
    #Scenario: Successful Application Login
    #    Given User is on login page
    #    When User enter username "student" and password "Password123"
    #    Then User should be able to login successfully and new page open "Logged In Successfully"

    Scenario Outline: Invalid Application Login
        Given User is on login page
        When User enter username <username> and password <password>
        Then User should get the error "Your username is invalid!"

    Examples:
    | username | password |
    | "test1"    | "test@123" |
    | "test2"    | "test@234" |