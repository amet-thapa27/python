#a package is a container for multiple modules
#in file system a package is a directory or folder

import ecommerce.shipping
ecommerce.shipping.calc_shipping()

from ecommerce.shipping import calc_shipping
calc_shipping()


from ecommerce import shipping
shipping.calc_shipping()
