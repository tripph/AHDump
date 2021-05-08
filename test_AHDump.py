from unittest import TestCase
from AHDump import get_realmsjson_and_slugs, validate_realm_id


class Test(TestCase):
    def test_get_realmsjson_and_slugs(self):
        (_, slugs) = get_realmsjson_and_slugs()
        # print(slugs)
    def test_validate_realm_id(self):
        (_, slugs) = get_realmsjson_and_slugs()
        validate_realm_id(slugs, "azuremyst")
    def test_validate_realm_id_BAD(self):
        (_, slugs) = get_realmsjson_and_slugs()
        with self.assertRaises(KeyError):
            validate_realm_id(slugs, "ajuremyzt")



