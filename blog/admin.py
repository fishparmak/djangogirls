from django.contrib import admin
from .models import Post, Organization, Hackathon, User, Team, Project, UserTeam, OrgHack, UserTeamHack, UserTeamProject

admin.site.register(Post)
admin.site.register(Organization)
admin.site.register(Hackathon)
admin.site.register(User)
admin.site.register(Team)
admin.site.register(Project)
admin.site.register(UserTeam)
admin.site.register(OrgHack)
admin.site.register(UserTeamHack)
admin.site.register(UserTeamProject)
