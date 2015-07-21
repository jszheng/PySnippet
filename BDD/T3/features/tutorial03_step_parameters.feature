# file:features/tutorial03_step_parameters.feature
Feature: Step Parameters (tutorial03)

  As a 厨师
  I want 放入搅拌机 something
  So that a juice will comes out


  Scenario: 搅拌机
    Given I put "apples" in a blender
    When  I switch the blender on
    Then  it should transform into "apple juice"

  Scenario: 有毒物质
    Given I put "iPhone" in a blender
    When  I switch the blender on
    Then  it should transform into "toxic waste"
