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

    def modify_package_schema(self, schema):
        #set custom dataset schema
        schema.update({
            #dcat schema
            'identifier': [tk.get_validator('ignore_missing'),
				tk.get_converter('convert_to_extras')],
            'title': [tk.get_validator('ignore_missing')],
            'contactPoint': [tk.get_validator('ignore_missing'),
                tk.get_converter('convert_to_extras')],
            'description': [tk.get_validator('ignore_missing'),
                tk.get_converter('convert_to_extras')],
            'landingPage': [tk.get_validator('ignore_missing'),
                tk.get_converter('convert_to_extras')],
            'issued': [tk.get_validator('ignore_missing'),
				tk.get_converter('convert_to_extras')],
            'modified': [tk.get_validator('ignore_missing'),
				tk.get_converter('convert_to_extras')],
            'language': [tk.get_validator('ignore_missing'),
				tk.get_converter('convert_to_extras')],
            'spatial': [tk.get_validator('ignore_missing'),
				tk.get_converter('convert_to_extras')],
            'temporal': [tk.get_validator('ignore_missing'),
				tk.get_converter('convert_to_extras')],
            'accrualPeriodicity': [tk.get_validator('ignore_missing'),
				tk.get_converter('convert_to_extras')],
            #'publisher': publisher_schema(),
            'keyword': [tk.get_validator('ignore_missing'),
				tk.get_converter('convert_to_extras')],
            'distribution': [tk.get_validator('ignore_missing'),
				tk.get_converter('convert_to_extras')],
            'theme': [tk.get_validator('ignore_missing'),
				tk.get_converter('convert_to_extras')],
            'definition': [tk.get_validator('ignore_missing'),
				tk.get_converter('convert_to_extras')],
            # ignore default schema (not already ingored)
            'name': [tk.get_validator('ignore_missing')],
        })
        #set custom resource schema
        schema['resources'].update({
            'title': [tk.get_validator('ignore_missing')],
            'description': [tk.get_validator('ignore_missing')],
            'issued': [tk.get_validator('ignore_missing')],
            'modified': [tk.get_validator('ignore_missing')],
            'license': [tk.get_validator('ignore_missing')],
            'rights': [tk.get_validator('ignore_missing')],
            'accessURL': [tk.get_validator('ignore_missing')],
            'downloadURL': [tk.get_validator('ignore_missing')],
            'mediaType': [tk.get_validator('ignore_missing')],
            'format': [tk.get_validator('ignore_missing')],
            'byteSize': [tk.get_validator('ignore_missing')]
            })
        return schema

    def create_package_schema(self):
        schema = super(ExampleIDatasetFormPlugin, self).create_package_schema()
        #add files from modify_package_schema
        schema = self.modify_package_schema(schema)
        return schema

    def update_config(self, config):
        # Add this plugin's templates dir to CKAN's extra_template_paths, so
        # that CKAN will use this plugin's custom templates.
        tk.add_template_directory(config, 'templates')

    def update_package_schema(self):
        schema = super(ExampleIDatasetFormPlugin, self).update_package_schema()
        #add files from modify_package_schema
        schema = self.modify_package_schema(schema)
        return schema

    def show_package_schema(self):
        schema = super(ExampleIDatasetFormPlugin, self).show_package_schema()
        schema = self.modify_package_schema(schema)
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
