import ckan.plugins as p
import ckan.plugins.toolkit as tk

#def publisher_schema():
#    schema = {
#        'name': [tk.get_validator('ignore_missing')],
#        'mbox': [tk.get_validator('ignore_missing')],
#        'homepage': [tk.get_validator('ignore_missing')],
#    }
#    return schema

class ExampleIDatasetFormPlugin(p.SingletonPlugin, tk.DefaultDatasetForm):
    p.implements(p.IDatasetForm)
    p.implements(p.IConfigurer)

    def _modify_package_schema(self, schema):
        #set custom dataset schema
        schema.update({
            #dcat schema
            'identifier': [tk.get_validator('ignore_missing')]
        })
        schema.update({
            'title': [tk.get_validator('ignore_missing')]
        })
        schema.update({
            'contactPoint': [tk.get_validator('ignore_missing')]
        })
        schema.update({
            'description': [tk.get_validator('ignore_missing')]
        })
        schema.update({
            'landingPage': [tk.get_validator('ignore_missing')]
        })
        schema.update({
            'issued': [tk.get_validator('ignore_missing')]
        })
        schema.update({
            'modified': [tk.get_validator('ignore_missing')]
        })
        schema.update({
            'language': [tk.get_validator('ignore_missing'), tk.get_converter('convert_to_extras')]
        })
        schema.update({
            'spatial': [tk.get_validator('ignore_missing')]
        })
        schema.update({
            'temporal': [tk.get_validator('ignore_missing')]
        })
        schema.update({
            'accrualPeriodicity': [tk.get_validator('ignore_missing')]
        })
            #'publisher': publisher_schema(),
        schema.update({
            'keyword': [tk.get_validator('ignore_missing')]
        })
        schema.update({
            'distribution': [tk.get_validator('ignore_missing')]
        })
        schema.update({
            'theme': [tk.get_validator('ignore_missing')]
        })
        schema.update({
            'definition': [tk.get_validator('ignore_missing')]
        })
            # ignore default schema (not already ingored)
        schema.update({
            'name': [tk.get_validator('ignore_missing')]
        })
        #set custom resource schema
        schema['resources'].update({
            'title': [tk.get_validator('ignore_missing')]
        })
        schema['resources'].update({
            'description': [tk.get_validator('ignore_missing')]
        })
        schema['resources'].update({
            'issued': [tk.get_validator('ignore_missing')]
        })
        schema['resources'].update({
            'modified': [tk.get_validator('ignore_missing')]
        })
        schema['resources'].update({
            'license': [tk.get_validator('ignore_missing')]
        })
        schema['resources'].update({
            'rights': [tk.get_validator('ignore_missing')]
        })
        schema['resources'].update({
            'accessURL': [tk.get_validator('ignore_missing')]
        })
        schema['resources'].update({
            'downloadURL': [tk.get_validator('ignore_missing')]
        })
        schema['resources'].update({
            'mediaType': [tk.get_validator('ignore_missing')]
        })
        schema['resources'].update({
            'format': [tk.get_validator('ignore_missing')]
        })
        schema['resources'].update({
            'byteSize': [tk.get_validator('ignore_missing')]
        })
        return schema

    def create_package_schema(self):
        schema = super(ExampleIDatasetFormPlugin, self).create_package_schema()
        #add files from modify_package_schema
        schema = self._modify_package_schema(schema)
        return schema

    def update_package_schema(self):
        schema = super(ExampleIDatasetFormPlugin, self).update_package_schema()
        #add files from modify_package_schema
        schema = self._modify_package_schema(schema)
        return schema

    def show_package_schema(self):
        schema = super(ExampleIDatasetFormPlugin, self).show_package_schema()
        schema.update({
            #dcat schema
            'identifier': [tk.get_validator('ignore_missing')]
        })
        schema.update({
            'title': [tk.get_validator('ignore_missing')]
        })
        schema.update({
            'contactPoint': [tk.get_validator('ignore_missing')]
        })
        schema.update({
            'description': [tk.get_validator('ignore_missing')]
        })
        schema.update({
            'landingPage': [tk.get_validator('ignore_missing')]
        })
        schema.update({
            'issued': [tk.get_validator('ignore_missing')]
        })
        schema.update({
            'modified': [tk.get_validator('ignore_missing')]
        })
        schema.update({
            'language': [tk.get_validator('ignore_missing'), tk.get_converter('convert_from_extras')]
        })
        schema.update({
            'spatial': [tk.get_validator('ignore_missing')]
        })
        schema.update({
            'temporal': [tk.get_validator('ignore_missing')]
        })
        schema.update({
            'accrualPeriodicity': [tk.get_validator('ignore_missing')]
        })
            #'publisher': publisher_schema(),
        schema.update({
            'keyword': [tk.get_validator('ignore_missing')]
        })
        schema.update({
            'distribution': [tk.get_validator('ignore_missing')]
        })
        schema.update({
            'theme': [tk.get_validator('ignore_missing')]
        })
        schema.update({
            'definition': [tk.get_validator('ignore_missing')]
        })
            # ignore default schema (not already ingored)
        schema.update({
            'name': [tk.get_validator('ignore_missing')]
        })
        #set custom resource schema
        schema['resources'].update({
            'title': [tk.get_validator('ignore_missing')]
        })
        schema['resources'].update({
            'description': [tk.get_validator('ignore_missing')]
        })
        schema['resources'].update({
            'issued': [tk.get_validator('ignore_missing')]
        })
        schema['resources'].update({
            'modified': [tk.get_validator('ignore_missing')]
        })
        schema['resources'].update({
            'license': [tk.get_validator('ignore_missing')]
        })
        schema['resources'].update({
            'rights': [tk.get_validator('ignore_missing')]
        })
        schema['resources'].update({
            'accessURL': [tk.get_validator('ignore_missing')]
        })
        schema['resources'].update({
            'downloadURL': [tk.get_validator('ignore_missing')]
        })
        schema['resources'].update({
            'mediaType': [tk.get_validator('ignore_missing')]
        })
        schema['resources'].update({
            'format': [tk.get_validator('ignore_missing')]
        })
        schema['resources'].update({
            'byteSize': [tk.get_validator('ignore_missing')]
        })
        return schema

    def is_fallback(self):
        # Return True to register this plugin as the default handler for
        # package types not handled by any other IDatasetForm plugin.
        return True

    def package_types(self):
        # This plugin doesn't handle any special package types, it just
        # registers itself as the default (above).
        return []

    def update_config(self, config):
# Add this plugin's templates dir to CKAN's extra_template_paths, so
# that CKAN will use this plugin's custom templates.
        tk.add_template_directory(config, 'templates')
