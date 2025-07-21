Quick Start Guide
======================

Before You Start
----------------

Ensure Salt 3005 or above is installed and running on your machine.

If you haven't installed Salt yet, refer to the `Salt Installation Guide <https://docs.saltproject.io/salt/install-guide/en/latest>`_

Installing the Extension
------------------------

Several methods are available for installing the Prometheus Salt extension:

- **Method 1: Using pip**

.. code-block::

    salt-pip install saltext.mqtt_return

.. note::
    Depending on the Salt version, Salt may not be using the system Python. For those versions, ensure you're using the Python associated with Salt (typically found at **/opt/saltstack/salt/bin/python**).


- **Method 2: Using Salt**

Use an execution module like:

.. code-block::

    salt \* pip.install saltext.mqtt_return


Note: The extension can be installed and used on all minions or specific minions where reporting data is needed


Getting Started
---------------

To enable the extension add an entry to the Salt Master configuration

.. code-block::

    event_return: [mqtt_return]

    returner.mqtt_return.output: "awsiot"
    returner.mqtt_return.endpoint: https://at0m02rojb1ir-ats.iot.us-east-1.amazonaws.com
    returner.mqtt_return.aws_region: "us-east-1"
    returner.mqtt_return.topic_prefix: "salt/aws.sa-east-1.salt-master"
    returner.mqtt_return.topic_rewrite_regex: "salt/"
    returner.mqtt_return.topic_rewrite_replace: ""
