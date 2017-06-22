from django.shortcuts import render, redirect
from .models import League, Team, Player
from django.db.models import Count

from . import team_maker

def index(request):
	context = {
		#1. Find all teams in the Atlantic Soccer Conference
		#"leagues": League.objects.filter(teams__team_name = "Angels") ,
		#"teams": Team.objects.filter(league__name = "Atlantic Soccer Conference"),
		#2. Find all (current) players on the Boston Penguins
		#"players": Player.objects.filter(curr_team__team_name = "Penguins", curr_team__location = "Boston")
		#3. Find all (current) players in the International Collegiate Baseball Conference
		#"players" : Player.objects.filter(curr_team__league__name = "International Collegiate Baseball Conference"),
		#4. Find all (current) players in the American Conference of Amateur Football with last name "Lopez" | Levi Lopez, Isabella Lopez
		#"players" : Player.objects.filter(last_name = "Lopez", curr_team__league__name = "American Conference of Amateur Football"),
		#5. Find all football players 
		#"players" : Player.objects.filter(curr_team__league__sport = "Football"),
		#6. Find all teams with a (current) player named "Sophia"
		#"teams": Team.objects.filter(curr_players__first_name = "Sophia"),
		#7. Find all leagues with a (current) player named "Sophia"
		#"leagues": League.objects.filter(teams__curr_players__first_name = "Sophia"),
		#8. Find everyone with the last name "Flores" who DOESN'T (currently) play for the Washington Roughriders 
		#"players" : Player.objects.filter(last_name = "Flores").exclude(curr_team__team_name= "Roughriders"),
		#"teams": Team.objects.all(),
		#"players": Player.objects.all(),
		#"leagues": League.objects.all()
		
		#LEVEL-3
		#1. Find all teams, past and present, that Samuel Evans has played with 
		#"teams": Team.objects.filter(all_players__first_name = "Samuel"),
		#2. Find all players, past and present, with the Manitoba Tiger-Cats 
		#"players": Player.objects.filter(all_teams__team_name = "Tiger-Cats"),
		#3. Find all players who were formerly (but aren't currently) with the Wichita Vikings 
		#"players": Player.objects.filter(all_teams__team_name = "Vikings").exclude(curr_team__team_name = "Vikings"),
		#4. Find every team that Jacob Gray played for before he joined the Oregon Colts
		#"teams": Team.objects.filter(all_players__last_name = "Gray",all_players__first_name = "Jacob").exclude(curr_players__first_name = "Jacob",curr_players__last_name = "Gray"),
		#5. Find everyone named "Joshua" who has ever played in the Atlantic Federation of Amateur Baseball Players
		#"players": Player.objects.filter(first_name = "Joshua",all_teams__league__name = "Atlantic Federation of Amateur Baseball Players"),
		#6. Find all teams that have had 12 or more players, past and present.
		#"teams": Team.objects.annotate(total = Count('team_name'))
		#7. Show all players, sorted by the number of teams they've played for 
		#"players": Player.objects.values('curr_team__team_name').order_by('curr_team__team_name'),
	}
	
	team = Team.objects.annotate(total = Count('all_players')).__lt=12
	print team[2].total
	return render(request, "leagues/index.html", context)

def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("index")