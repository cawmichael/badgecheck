"""
INPUT Tasks:
Process user input
"""
DETECT_INPUT_TYPE = 'DETECT_INPUT_TYPE'


"""
GRAPH Tasks:
Fetch, store, and process nodes in the graph related to validation input.
"""
FETCH_HTTP_NODE = 'FETCH_HTTP_NODE'
JSONLD_COMPACT_DATA = 'JSONLD_COMPACT_DATA'


"""
VALIDATION Tasks:
Ensure data is in good shape for relevant Open Badges objects and links between
objects are sound.
"""
DETECT_AND_VALIDATE_NODE_CLASS = 'DETECT_AND_VALIDATE_NODE_CLASS'
VALIDATE_EXPECTED_NODE_CLASS = 'VALIDATE_EXPECTED_NODE_CLASS'
VALIDATE_RDF_TYPE_PROPERTY = 'VALIDATE_RDF_TYPE_PROPERTY'
VALIDATE_PROPERTY = 'VALIDATE_PROPERTY'

# Class Level Validation Tasks
ASSERTION_TIMESTAMP_CHECKS = 'ASSERTION_TIMESTAMP_CHECKS'
ASSERTION_VERIFICATION_DEPENDENCIES = 'ASSERTION_VERIFICATION_DEPENDENCIES'
CRITERIA_PROPERTY_DEPENDENCIES = 'CRITERIA_PROPERTY_DEPENDENCIES'
IDENTITY_OBJECT_PROPERTY_DEPENDENCIES = 'IDENTITY_OBJECT_PROPERTY_DEPENDENCIES'
ISSUER_PROPERTY_DEPENDENCIES = 'ISSUER_PROPERTY_DEPENDENCIES'

CLASS_VALIDATION_TASKS = (ASSERTION_TIMESTAMP_CHECKS, ASSERTION_VERIFICATION_DEPENDENCIES,
                          CRITERIA_PROPERTY_DEPENDENCIES, IDENTITY_OBJECT_PROPERTY_DEPENDENCIES,
                          ISSUER_PROPERTY_DEPENDENCIES,)


"""
VERIFICATION Tasks:
Ensure values are congruent with one another and that relevant verification
rules in the Open Badges Specification are met.
"""
HOSTED_ID_IN_VERIFICATION_SCOPE = 'HOSTED_ID_IN_VERIFICATION_SCOPE'
