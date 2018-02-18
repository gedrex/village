Configuration of the village
-----------------------------

This directory contains basic game setup. You can change the initial setup for everything, resources and human abilities etc. Just follow the format and instructions in comments in files. After every change you done in yaml file, run conf file of appropriate name. It consolidates yaml files.

Resources
---------
In this file you can add or edit resources or change products attributes. 

When adding some attribute, add it to global Attributes and then run resources.conf, this attribute is added to every resource.

Every resource has the same attributes. If there is some attribute with resource and not in global attributes, this attribute will be deleted from every resources when run resources.conf

When adding some resource, add the name and producer and then run resources.conf. All other attributes will be added automatically and set to 'Null'. Then set values as you want

