Feature: Wishlist

  Scenario: verify user is able to product add to wishlist and remove from wishlist
    Given I launch chrome browser
    When I Open Ajio homepage
    Then Click on Sign In button
    And Enter the mobile number
    And Click on continue button
    Then Click on start shopping button
    And search the product
    And click on that product
    And select the size a
    And product add to wishlist
    And click on wishlist to check wheather the product is added or not
    Then go to back page c
    And remove from wishlist
    And click on wishlist to check wheather the product is removed or not
    Then go to back page d
    And select the size b
    And product add to cart
    And click on cart
    And click on move to wishlist
    And remove from wishlist_b