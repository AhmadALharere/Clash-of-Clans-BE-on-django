profile:
    -links
    -village
    -dark-Village
    -resorses
    -attakarc
    -Lvl
    -name
    -clan
    -season-progress
    -event-progress
    -star-reward
    -league-cup
    -last-login
    -reagon
    -achivement



    -create_account
    -get_...
    -add_link
    -get_league
    -get_res
    -pay_res



settings:
    

    -link_with_google
    -link_with_facebook
    -link_with_supersall
    -swetch_between_supersall
    -swetch_reagon
    -log_out
    -log_in



AttackArchive:
    -account
    -attacks


    -get_archive
    -add_attack
    -replay


attack_info:

    -striker
    -attackarchive
    -army
    -date
    -type[normal,revange,frendly,clan_daul]
    -rivale_name
    -rivale_resorses
    -river_village
    -actions
    -star_gained
    -damage


actions:
    -type
    -date
    -unit
    -building



village:

    -account
    -buildings(file)


    -load_village
    -save_village



DarkVillage:

    -account
    -buildings_limit
    -buildings(file)


    -load_village
    -save_village
    


resorses:

    -account
    #(all of them is files contains total res then the amount of it in every building)
    -elxyre
    -dark_elxyre
    -gold
    -capital_gold
    -war_gold
    -crystale_gold
    -crystale_elxyre
    -daimond


    -get_resorses
    -get_river_resorses
    -chick_pyment
    -apply_pyment
    -apply_puying
    


league:

    -league_rewards
    -league_range


    -get_league_rewards_list
    -get_league_reward
    -get_league_icon
    -get_league
    -get_league_champions


achivement:

    -title
    -discription
    -reward

    -get_achivement_list


statues:

    -join_date
    -total_distroyed_buildings
    -total_distroyed_house
    -total_distroyed_clan_castle
    -total_distroyed_army_building
    -total_distroyed_elxyre_res
    -total_distroyed_gold_res
    -total_distroyed_dark_elxyre_res
    -total_distroyed_elxyre_con
    -total_distroyed_gold_con
    -total_distroyed_dark_elxyre_con
    -total_distroyed_wall
    -total_distroyed_defenseve_building
    -total_elxyre_gained
    -total_gold_gained
    -total_dark_elxyre_gained
    -total_elxyre_ocoubed
    -total_gold_ocoubed
    -total_dark_elxyre_ocoubed
    -total_diamond_ocoubed
    -total_star_gained
    -total_star_gained_in_war


    -get_list



Clan:

    -title
    -discription
    -combo_war_win
    -total_war_win
    -total_war_lose
    -total_war_drow
    -created_at
    -state[open,invite_only,close]
    -house_cond
    -cup_cond
    -icon_style
    -icon_color_1
    -icon_color_2
    -members
    -leader
    -leader_helper
    -unice_members
    -capitals
    -war
    -war_archive



ClansCapital:

    -account
    -buildings(file)


    -load_village
    -save_village




shop:

    -id
    -prize
    -discount
    -discount_date_start
    -discount_date_end


    git_prize_list


seasson:

    -point_gained
    -static_missions
    -daily_missions
    -reward_point
    -reward_state
    -is_buyed
    -elxyre_storage
    -dark_elxyre_storage
    -gold_storage



    -git_season_info
    -set_mission_complete
    -claim_riward
    -buy_season


event:

    -title
    -discription
    -village
    -reward
    -start_date
    -end_date


    get_list


ClansWar:

    
    -clan1
    -clan2
    -start_date
    -members[5,10,...]
    -clan1_members
    -clan2_members
    -actions[file]
    -RewardForClan1
    -RewardForClan2



?
buildings:

    -title
    -


unit:

