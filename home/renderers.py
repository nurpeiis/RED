#render is there to get the JSON data in certain format
#Resource: https://medium.com/@jrmybrcf/how-to-build-a-project-with-django-vuejs-create-a-rest-api-endpoint-b57374a89661
import json
from rest_framework.renderers import JSONRenderer

class ProjectJSONRenderer (JSONRenderer):
    charset = 'utf-8'

    def render(self, data, media_type = None, render_context = None):
        errors = data.get('errors', None)

        if errors is not None:
            return super(ProjectJSONRenderer, self).render(data)
        return json.dumps({
                'projects': data    
            })  
    

