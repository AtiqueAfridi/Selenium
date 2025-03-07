"""
This `__init__.py` file initializes the `src` package 
and provides convenient access to key functions and modules.
"""

# Import essential utilities
from .utilities import setup_driver, teardown_driver, pause

# Import test functions for different components
from .authentication_test import test_basic_auth
from .element_interactions_tests import test_add_remove_elements
from .page_interactions_tests import test_a_b_testing
from .form_auth_test import test_form_authentication  # Added new test
