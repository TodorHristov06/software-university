def sort_games(*args, **kwargs):
    
    platform_games = {
        "console": set(),
        "pc": set()
    }
    
    for platform, title in args:
        platform_games[platform].add(title)
    
    title_to_release = {}
    for release_id, title in kwargs.items():
        title_to_release[title] = release_id
    
    con_games = []
    pc_games = []
    
    for title in platform_games["console"]:
        if title in title_to_release:
            con_games.append((title_to_release[title], title))
    for title in platform_games["pc"]:
        if title in title_to_release:
            pc_games.append((title_to_release[title], title))

    con_games.sort(key=lambda x: x[0])
    pc_games.sort(key=lambda x: x[0], reverse=True)
    
    result_lines = []
    
    if con_games:
        result_lines.append("Console Games:")
        for release_id, title in con_games:
            release_date = "_".join(release_id.split("_")[:-1])
            result_lines.append(f">>>{release_date}: {title}")
    
    if pc_games:
        if con_games:
            pass
        result_lines.append("PC Games:")
        for release_id, title in pc_games:
            release_date = "_".join(release_id.split("_")[:-1])
            result_lines.append(f"<<<{release_date}: {title}")
    
    return "\n".join(result_lines)
