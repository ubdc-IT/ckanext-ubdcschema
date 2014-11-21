import ckan.plugins as p
import ckan.plugins.toolkit as tk


class ExampleIDatasetFormPlugin(p.SingletonPlugin, tk.DefaultDatasetForm):
	p.implements(p.IDatasetForm)
	p.implements(p.IConfigurer)
	
	def _modify_package_schema(self, schema):
        schema.update({
            'identifier': []
            'title': []
            'contactPoint': []
            'description': []
            'landingPage': []
            'issued': []
            'modified': []
            'language': []
            'spatial': []
            'temporal': []
            'accrualPeriodicity': []
            'publisher': []
            'keyword': []
            'distribution': []
            'theme': []
            'definition': []
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
